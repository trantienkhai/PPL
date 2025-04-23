from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *
#from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class GetEnv(BaseVisitor):
    def visitProgram(self, ast, o):
        o = []
        env = self.builtins()
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                env = self.visit(decl, env)
            elif type(decl) is StructType or type(decl) is InterfaceType:
                env = self.visit(decl, env)
        for e in env:
            if e.name not in [s.name for s in self.builtins()]:
                o.append(e)
        return o
    
    def builtins(self):
        return [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType()))
        ]

    def visitFuncDecl(self, ast, o):
        if self.lookup(ast.name, o):
            raise Redeclared(Function(), ast.name)

        param_names = []
        for param in ast.params:
            if param.parName in param_names:
                raise Redeclared(Parameter(), param.parName)
            param_names.append(param.parName)

        param_types = [param.parType for param in ast.params]
        return o + [Symbol(ast.name, MType(param_types, ast.retType))]


    def visitStructType(self, ast, o):
        if self.lookup(ast.name, o):
            raise Redeclared(Type(), ast.name)
        
        field_names = []
        for field_name, _ in ast.elements:
            if field_name in field_names:
                raise Redeclared(Field(), field_name)
            field_names.append(field_name)

        return o + [Symbol(ast.name, MType(None, ast))]

    def visitInterfaceType(self, ast, o):
        if self.lookup(ast.name, o):
            raise Redeclared(Type(), ast.name)
        
        prototype_names = []
        for proto in ast.methods:
            if proto.name in prototype_names:
                raise Redeclared(Prototype(), proto.name)
            prototype_names.append(proto.name)

        return o + [Symbol(ast.name, MType(None, ast))]

    def lookup(self, name, lst):
        for sym in lst:
            if sym.name == name:
                return sym
        return None


class StaticChecker(BaseVisitor):
        
    def __init__(self,ast):
        self.ast = ast
        self.env = []
    
    def check(self):
        self.env = GetEnv().visit(self.ast, [])
        return self.visit(self.ast, [[]])

    def lookup_all(self, name, env):
        for scope in env:
            for sym in scope:
                if sym.name == name:
                    return sym
        return None
    
    def lookup_in_scope(self, name, scope):
        for sym in scope:
            if sym.name == name:
                return sym
        return None

    def eval_const_expr(self, expr, o):
        if type(expr) is IntLiteral:
            return expr.value
        elif type(expr) is FloatLiteral:
            return expr.value
        elif type(expr) is BooleanLiteral:
            return expr.value
        elif type(expr) is StringLiteral:
            return expr.value

        elif type(expr) is Id:
            sym = self.lookup_all(expr.name, o)
            return sym.value if sym else None

        elif type(expr) is UnaryOp:
            val = self.eval_const_expr(expr.body, o)
            return -val if expr.op == '-' else not val

        elif type(expr) is BinaryOp:
            left = self.eval_const_expr(expr.left, o)
            right = self.eval_const_expr(expr.right, o)
            op = expr.op

            ops = {
                '+': lambda l, r: l + r,
                '-': lambda l, r: l - r,
                '*': lambda l, r: l * r,
                '/': lambda l, r: l / r,
                '%': lambda l, r: l % r,
                '&&': lambda l, r: l and r,
                '||': lambda l, r: l or r,
                '==': lambda l, r: l == r,
                '!=': lambda l, r: l != r,
                '>': lambda l, r: l > r,
                '>=': lambda l, r: l >= r,
                '<': lambda l, r: l < r,
                '<=': lambda l, r: l <= r,
            }

            return ops[op](left, right)

        return None


    def eval_dim_expr(self, expr, o):
        if type(expr) is IntLiteral:
            return expr.value
        elif type(expr) is Id:
            sym = self.lookup_all(expr.name, o)
            return sym.value  
        
    def implements_interface(self, struct_type, interface_type):
        for proto in interface_type.methods:
            method_found = False

            for method in struct_type.methods:
                if method.fun.name == proto.name:
                    method_found = True

                    # Kiểm tra số lượng tham số
                    if len(method.fun.params) != len(proto.params):
                        return False

                    # Kiểm tra từng kiểu tham số
                    for i in range(len(proto.params)):
                        if type(method.fun.params[i].parType) is not type(proto.params[i].parType):
                            return False

                    # Kiểm tra kiểu trả về
                    if type(method.fun.retType) is not type(proto.retType):
                        return False

                    break  # dừng vì đã kiểm tra xong method trùng tên

            if not method_found:
                return False  # không tìm thấy method tương ứng trong struct

        return True



    def visitProgram(self,ast, o):
        o[0] = [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType()))
        ]
        for decl in ast.decl:
            o = self.visit(decl, o)

    def visitVarDecl(self, ast, o):
        if self.lookup_in_scope(ast.varName, o[0]):
            raise Redeclared(Variable(), ast.varName)

        var_type = ast.varType
        init_type = None

        if ast.varInit:
            init_type = self.visit(ast.varInit, o)

        if var_type is None and init_type is None:
            raise TypeMismatch(ast)

        if var_type is None:
            var_type = init_type

        elif init_type is not None:
            if type(var_type) == type(init_type):
                if type(var_type) is ArrayType:
                    if len(var_type.dimens) != len(init_type.dimens):
                        raise TypeMismatch(ast)
                    
                    for l_dim, r_dim in zip(var_type.dimens, init_type.dimens):
                        l_val = self.eval_dim_expr(l_dim, o)
                        r_val = self.eval_dim_expr(r_dim, o)
                        if l_val != r_val:
                            raise TypeMismatch(ast)

                    ele_type = var_type.eleType
                    rhs_ele_type = init_type.eleType
                    if type(ele_type) != type(rhs_ele_type):
                        if type(ele_type) is FloatType and type(rhs_ele_type) is IntType:
                            pass
                        else:
                            raise TypeMismatch(ast)

            # Cho phép Int → Float
            elif type(var_type) is FloatType and type(init_type) is IntType:
                pass

            # Interface nhận Struct implement nó (chưa xử lý implement, TODO)
            elif type(var_type) is InterfaceType and type(init_type) is StructType:
                if not self.implements_interface(init_type, var_type):
                    raise TypeMismatch(ast)
            else:
                raise TypeMismatch(ast)

        o[0] += [Symbol(ast.varName, MType(None, var_type))]
        return o

                

    def visitConstDecl(self, ast, o):
        if self.lookup_in_scope(ast.conName, o[0]):
            raise Redeclared(Constant(), ast.conName)
        
        expr_type = self.visit(ast.iniExpr, o)
        const_type = expr_type

        value = None
        if type(ast.iniExpr) in [IntLiteral, FloatLiteral, BooleanLiteral, StringLiteral]:
            value = ast.iniExpr.value            
        elif type(ast.iniExpr) in [Id, BinaryOp, UnaryOp]:
            value = self.eval_const_expr(ast.iniExpr, o)

        o[0] += [Symbol(ast.conName, MType(None, const_type), value)]
        return o
    
    def visitFuncDecl(self, ast, o):
        if self.lookup_in_scope(ast.name, o[0]):
            raise Redeclared(Function(), ast.name)


        param_scope = []
        for param in ast.params:
            if self.lookup_in_scope(param.parName, param_scope):
                raise Redeclared(Parameter(), param.parName)
            param_scope.append(Symbol(param.parName, MType(None, param.parType)))

        

        self.return_type = ast.retType

        env = [param_scope] + o
        self.visit(ast.body, env)
        o[0] += [Symbol(ast.name, MType([p.parType for p in ast.params], ast.retType))]
        return o

    def visitMethodDecl(self, ast, o):
        method_name = ast.fun.name
        struct_name = ast.recType.name  # ast.recType là Id("Calculator")

        struct_sym = None
        for sym in self.env:
            if sym.name == struct_name and type(sym.mtype.rettype) is StructType:
                struct_sym = sym
                break

        struct_type = struct_sym.mtype.rettype
        for m in struct_type.methods:
            if m.fun.name == method_name:
                raise Redeclared(Method(), method_name)
            
        for field_name, _ in struct_type.elements:
            if field_name == method_name:
                raise Redeclared(Method(), method_name)


        #Thêm method vào danh sách method của struct trong env 
        struct_type.methods.append(ast)

        receiver_sym = Symbol(ast.receiver, MType(None, ast.recType))
        receiver_scope = [receiver_sym]

        param_scope = []
        for param in ast.fun.params:
            if self.lookup_in_scope(param.parName, param_scope):
                raise Redeclared(Parameter(), param.parName)
            param_scope.append(Symbol(param.parName, MType(None, param.parType)))

        self.return_type = ast.fun.retType

        env = [param_scope, receiver_scope] + o
        self.visit(ast.fun.body, env)

        o[0] += [Symbol(method_name, MType([p.parType for p in ast.fun.params], ast.fun.retType))]

        return o

    def visitPrototype(self, param):pass
    
    def visitIntType(self, ast, o):pass
    
    def visitFloatType(self, ast, o):pass
    
    def visitBoolType(self, ast, o):pass
    
    def visitStringType(self, ast, o):pass
    
    def visitVoidType(self, ast, o):pass
    
    def visitArrayType(self, ast, o):pass
     
    def visitStructType(self, ast, o):
        if self.lookup_in_scope(ast.name, o[0]):
            raise Redeclared(Type(), ast.name)

        field_names = []
        for field_name, field_type in ast.elements:
            if field_name in field_names:
                raise Redeclared(Field(), field_name)
            field_names.append(field_name)

        o[0] += [Symbol(ast.name, MType(None, ast),)]  
        return o

    def visitInterfaceType(self, ast, o):
        if self.lookup_in_scope(ast.name, o[0]):
            raise Redeclared(Type(), ast.name)

        prototype_names = []
        for proto in ast.methods:
            if proto.name in prototype_names:
                raise Redeclared(Prototype(), proto.name)
            prototype_names.append(proto.name)
        o[0] += [Symbol(ast.name, MType(None, ast),)]  
        return o
    
    def visitBlock(self, ast, o, new_scope=True):
        env = [[]] + o  if new_scope else o

        for stmt in ast.member:
            if type(stmt) is FuncCall:
                ret_type = self.visit(stmt, env)
                if type(ret_type) is not VoidType:
                    raise TypeMismatch(stmt)
            elif type(stmt) is MethCall:
                ret_type = self.visit(stmt, env)
                if type(ret_type) is not VoidType:
                    raise TypeMismatch(stmt)
            else:
                env = self.visit(stmt, env)

        return o  
 
    def visitAssign(self, ast, o):
        lhs = ast.lhs
        rhs = ast.rhs
        rhs_type = self.visit(rhs, o)

        if isinstance(rhs, (FuncCall, MethCall)) and type(rhs_type) is VoidType:
            raise TypeMismatch(ast)

        if type(lhs) is Id:
            sym = self.lookup_in_scope(lhs.name, o[0])
            if sym is None:
                o[0] += [Symbol(lhs.name, MType(None, rhs_type))]
                return
        lhs_type = self.visit(lhs, o)

        if type(lhs_type) is VoidType:
            raise TypeMismatch(ast)

        if type(lhs_type) == type(rhs_type):
            if type(lhs_type) is ArrayType:
                if len(lhs_type.dimens) != len(rhs_type.dimens):
                    raise TypeMismatch(ast)

                for l_dim, r_dim in zip(lhs_type.dimens, rhs_type.dimens):
                    l_val = self.eval_dim_expr(l_dim, o)
                    r_val = self.eval_dim_expr(r_dim, o)
                    if l_val != r_val:
                        raise TypeMismatch(ast)

                ele_type = lhs_type.eleType
                rhs_ele_type = rhs_type.eleType
                if type(ele_type) != type(rhs_ele_type):
                    if type(ele_type) is FloatType and type(rhs_ele_type) is IntType:
                        pass
                    else:
                        raise TypeMismatch(ast)
        elif type(lhs_type) is FloatType and type(rhs_type) is IntType:
            pass
        elif type(lhs_type) is InterfaceType and type(rhs_type) is StructType:
            if not self.implements_interface(rhs_type, lhs_type, self.env):
                raise TypeMismatch(ast)
        else:
            raise TypeMismatch(ast)

        return

    def visitIf(self, ast, o):
        cond_type = self.visit(ast.expr, o)
    
        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)

        self.visit(ast.thenStmt, o)

        if ast.elseStmt:
            self.visit(ast.elseStmt, o)

  
    
    def visitForBasic(self, ast, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.loop, o)
  
 
    def visitForStep(self, ast, o):
        env = [[]] + o

        updated_env = self.visit(ast.init, env)
        if updated_env is not None:
            env = updated_env

        cond_type = self.visit(ast.cond, env)
        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)

        updated_env = self.visit(ast.upda, env)
        if updated_env is not None:
            env = updated_env

        self.visitBlock(ast.loop, env, False)

    def visitForEach(self, ast,o):
        arr_type = self.visit(ast.arr, o)
        if type(arr_type) is not ArrayType:
            raise TypeMismatch(ast)

        ele_type = arr_type.eleType

        idx_sym = Symbol(ast.idx.name, MType(None, IntType()))
        val_sym = Symbol(ast.value.name, MType(None, ele_type))
        env = [[idx_sym, val_sym]] + o

        self.visitBlock(ast.loop, env, False)

    def visitContinue(self, ast, o):pass
    
    def visitBreak(self, ast, o):pass
    
    def visitReturn(self, ast, o):
        if ast.expr is None:
            if type(self.return_type) is not VoidType:
                raise TypeMismatch(ast)
        else:
            expr_type = self.visit(ast.expr, o)
            if type(self.return_type) != type(expr_type):
                if type(self.return_type) is FloatType and type(expr_type) is IntType:
                    return
                raise TypeMismatch(ast)

    def visitBinaryOp(self, ast, o):
        left_type = self.visit(ast.left, o)
        right_type = self.visit(ast.right, o)
        op = ast.op
        
        if op == '+':
            if type(left_type) is StringType and type(right_type) is StringType:
                return StringType()
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType()
            if (type(left_type) is IntType and type(right_type) is FloatType) or (type(left_type) is FloatType and type(right_type) is IntType) or (type(left_type) is FloatType and type(right_type) is FloatType):
                return FloatType()
            raise TypeMismatch(ast)
        
        if op in ['-', '*', '/']:
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType()
            if (type(left_type) is IntType and type(right_type) is FloatType) or (type(left_type) is FloatType and type(right_type) is IntType) or (type(left_type) is FloatType and type(right_type) is FloatType):
                return FloatType()
            raise TypeMismatch(ast)
        
        if op == '%':
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType()
            raise TypeMismatch(ast)
        
        if op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(left_type) is not type(right_type):
                raise TypeMismatch(ast)
            if type(left_type) in [IntType, FloatType, StringType]:
                return BoolType()
            raise TypeMismatch(ast)
        
        if op in ['&&', '||']:
            if type(left_type) is BoolType and type(right_type) is BoolType:
                return BoolType()
            raise TypeMismatch(ast)
            
    
    def visitUnaryOp(self, ast, o):
        operand_type = self.visit(ast.body, o)
        op = ast.op

        if op == '-':
            if type(operand_type) is IntType:
                return IntType()
            if type(operand_type) is FloatType:
                return FloatType()
            raise TypeMismatch(ast)

        if op == '!':
            if type(operand_type) is BoolType:
                return BoolType()
            raise TypeMismatch(ast)
        
    def visitFuncCall(self, ast, o):
        sym = self.lookup_in_scope(ast.funName, self.env)
        if sym is None:
            raise Undeclared(Function(), ast.funName)

        if len(sym.mtype.partype) != len(ast.args):
            raise TypeMismatch(ast)

        for arg, expected_type in zip(ast.args, sym.mtype.partype):
            arg_type = self.visit(arg, o)
            if type(arg_type) != type(expected_type):
                raise TypeMismatch(ast)

        return sym.mtype.rettype
    
    def visitMethCall(self, ast, o):
        recv_type = self.visit(ast.receiver, o)

        if type(recv_type) is not Id:
            raise TypeMismatch(ast)

        recv_sym = None
        for sym in self.env:
            if sym.name == recv_type.name and type(sym.mtype.rettype) in [StructType, InterfaceType]:
                recv_sym = sym
                break

        recv_decl = recv_sym.mtype.rettype

        method_decl = None
        for method in recv_decl.methods:
            if method.fun.name == ast.metName:
                method_decl = method
                break

        if method_decl is None:
            raise Undeclared(Method(), ast.metName)

        if len(ast.args) != len(method_decl.fun.params):
            raise TypeMismatch(ast)

        for arg, param in zip(ast.args, method_decl.fun.params):
            arg_type = self.visit(arg, o)
            param_type = param.parType
            if type(arg_type) != type(param_type):
                raise TypeMismatch(ast)

        return method_decl.fun.retType
    
    def visitId(self, ast, o):
        name = ast.name
        for scope in o:
            for sym in scope:
                if sym.name == name:
                    if sym.mtype.partype is None and type (sym.mtype.rettype) not in  [StructType, InterfaceType]:
                        return sym.mtype.rettype
        raise Undeclared(Identifier(), name)
        
    def visitArrayCell(self, ast, o):
        arr_type = self.visit(ast.arr, o)

        if type(arr_type) is not ArrayType:
            raise TypeMismatch(ast)

        if len(ast.idx) != len(arr_type.dimens):
            raise TypeMismatch(ast)
        
        for index_expr in ast.idx:
            index_type = self.visit(index_expr, o)
            if type(index_type) is not IntType:
                raise TypeMismatch(ast)
            
        return arr_type.eleType
    
    def visitFieldAccess(self, ast, o):
        recv_type = self.visit(ast.receiver, o)

        if type(recv_type) is Id:
            struct_name = recv_type.name
            struct_sym = None
            for sym in self.env:
                if sym.name == struct_name and type(sym.mtype.rettype) is StructType:
                    struct_sym = sym
                    break

            for fname, ftype in struct_sym.mtype.rettype.elements:
                if fname == ast.field:
                    return ftype

            raise Undeclared(Field(), ast.field)

        raise TypeMismatch(ast)


    
    def visitIntLiteral(self, ast, o):
        return IntType()
    
    def visitFloatLiteral(self, ast, o):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, o):
        return BoolType()
    
    def visitStringLiteral(self, ast, o):
        return StringType()

    def visitArrayLiteral(self, ast, o):
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast, o):
        name = ast.name
        return Id(name)

    def visitNilLiteral(self, ast, o):pass

    
