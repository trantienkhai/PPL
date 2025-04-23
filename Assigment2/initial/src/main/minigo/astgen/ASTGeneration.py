from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
         return Program(self.visit(ctx.declares()))
     
    # declares: declare declares | declare;
    def visitDeclares(self, ctx: MiniGoParser.DeclaresContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        else:
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.declares()) 
    
    # main_function : FUNC 'main' LPAREN RPAREN block SEMI ;
    def visitMain_function(self, ctx: MiniGoParser.Main_functionContext):
        return FuncDecl("main", [], VoidType(), self.visit(ctx.block()))
    
    # declare : variable_declaration | constant_declaration | type_declaration | function_declaration| method_declare | quick_decl;
    def visitDeclare(self, ctx: MiniGoParser.DeclareContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        if ctx.constant_declaration():
            return self.visit(ctx.constant_declaration())
        if ctx.type_declaration():
            return self.visit(ctx.type_declaration())
        if ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        if ctx.method_declare():
            return self.visit(ctx.method_declare())
        # if ctx.quick_decl():
        #     return self.visit(ctx.quick_decl())
        
    #variable_declaration: VAR ID (type_specifier ASSIGN expression1 | type_specifier | ASSIGN expression1 ) SEMI;
    def visitVariable_declaration(self, ctx: MiniGoParser.Variable_declarationContext):
        varName = ctx.ID().getText()  
        if ctx.type_specifier() and ctx.ASSIGN():  
            varType = self.visit(ctx.type_specifier())
            varInit = self.visit(ctx.expression1())
        
        elif ctx.type_specifier():  
            varType = self.visit(ctx.type_specifier())
            varInit = None
        
        elif ctx.ASSIGN() and ctx.expression1():  
            varType = None  
            varInit = self.visit(ctx.expression1())
        return VarDecl(varName, varType, varInit)
   
    # constant_declaration : CONST ID ASSIGN expression1  SEMI;
    def visitConstant_declaration(self, ctx: MiniGoParser.Constant_declarationContext):
        conName = ctx.ID().getText()
        iniExpr = self.visit(ctx.expression1())  
        conType = None
        return ConstDecl(conName, conType, iniExpr)        
    
    # type_declaration : TYPE ID struct_declaration SEMI | TYPE ID interface_declaration SEMI;
    def visitType_declaration(self, ctx: MiniGoParser.Type_declarationContext):
        typeName = ctx.ID().getText()
        if ctx.struct_declaration():
            struct_body = self.visit(ctx.struct_declaration())
            return StructType(typeName, struct_body, [])  # Không có method

        elif ctx.interface_declaration():
            interface_methods = self.visit(ctx.interface_declaration())
            return InterfaceType(typeName, interface_methods)
        
    # struct_declaration : STRUCT LBRACE struct_field_dec RBRACE ;
    def visitStruct_declaration(self, ctx: MiniGoParser.Struct_declarationContext):
        return self.visit(ctx.struct_field_dec()) if ctx.struct_field_dec() else []

    # struct_field_dec : ID type_specifier SEMI struct_field_dec | ID type_specifier SEMI ;
    def visitStruct_field_dec(self, ctx: MiniGoParser.Struct_field_decContext):
        fieldName = ctx.ID().getText()
        fieldType = self.visit(ctx.type_specifier())

        if ctx.struct_field_dec():
            return [(fieldName, fieldType)] + self.visit(ctx.struct_field_dec())
        else:
            return [(fieldName, fieldType)]



    # interface_declaration : INTERFACE LBRACE interface_method_dec RBRACE ;
    def visitInterface_declaration(self, ctx: MiniGoParser.Interface_declarationContext):
        return self.visit(ctx.interface_method_dec()) if ctx.interface_method_dec() else []

     # interface_method_dec : ID LPAREN parameter_list RPAREN  return_type SEMI interface_method_dec | ID LPAREN parameter_list RPAREN  return_type SEMI;
    def visitInterface_method_dec(self, ctx: MiniGoParser.Interface_method_decContext):
        methodName = ctx.ID().getText()
        paramDecls = self.visit(ctx.parameter_list())
        params = [p.parType for p in paramDecls]
        retType = self.visit(ctx.return_type())

        method = Prototype(methodName, params, retType)

        if ctx.interface_method_dec():
            return [method] + self.visit(ctx.interface_method_dec())
        else:
            return [method]
        
    # parameter_list : param | ;
    def visitParameter_list(self, ctx: MiniGoParser.Parameter_listContext):
        if ctx.param():
            return self.visit(ctx.param())
        else:
            return []
    # param: parameter COMMA param | parameter;
    def visitParam(self, ctx: MiniGoParser.ParamContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.parameter())
        else:
            return self.visit(ctx.parameter()) + self.visit(ctx.param())
    # parameter : ids  type_specifier ; 
    def visitParameter(self, ctx: MiniGoParser.ParameterContext):
        ids = self.visit(ctx.ids())
        type = self.visit(ctx.type_specifier())
        return [ParamDecl(x.name, type) for x in ids]
    # ids: ID COMMA ids | ID;
    def visitIds(self, ctx: MiniGoParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
    
    # function_declaration : main_function | (FUNC ID LPAREN parameter_list RPAREN return_type block SEMI);
    def visitFunction_declaration(self, ctx: MiniGoParser.Function_declarationContext):
        if ctx.main_function():
            return self.visit(ctx.main_function())
        else:
            return FuncDecl(ctx.ID().getText(), self.visit(ctx.parameter_list()), self.visit(ctx.return_type()), self.visit(ctx.block()))

    # type_specifier: primitive_type | array_type;
    def visitType_specifier(self, ctx: MiniGoParser.Type_specifierContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        
    # primitive_type: INT | FLOAT | BOOLEAN | STRING | ID;
    def visitPrimitive_type(self, ctx: MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return Id(ctx.ID().getText())
        
    # array_type: array_type_cell primitive_type;
    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        dimensions = self.visit(ctx.array_type_cell())
        eleType = self.visit(ctx.primitive_type())
        return ArrayType(dimensions, eleType)

    # array_type_cell: LBRACK (INTLIT | ID) RBRACK array_type_cell | LBRACK (INTLIT | ID) RBRACK;
    ############fix them literal
    def visitArray_type_cell(self, ctx: MiniGoParser.Array_type_cellContext):
        if ctx.array_type_cell():
            if ctx.INTLIT():
                return [IntLiteral(ctx.INTLIT().getText())] + self.visit(ctx.array_type_cell())
            else:
                return [Id(ctx.ID().getText())] + self.visit(ctx.array_type_cell())
        else:
            if ctx.INTLIT():
                return [IntLiteral(ctx.INTLIT().getText())]
            else:
                return [Id(ctx.ID().getText())]    
    # return_type: type_specifier | ;
    def visitReturn_type(self, ctx: MiniGoParser.Return_typeContext):
        if ctx.type_specifier():
            return self.visit(ctx.type_specifier())
        else:
            return VoidType()
    # method_declare: FUNC LPAREN ID ID RPAREN ID LPAREN parameter_list RPAREN return_type block SEMI;
    def visitMethod_declare(self, ctx: MiniGoParser.Method_declareContext):
        return MethodDecl(ctx.ID(0).getText(), Id(ctx.ID(1).getText()), FuncDecl(ctx.ID(2).getText(), self.visit(ctx.parameter_list()), self.visit(ctx.return_type()), self.visit(ctx.block())))
    # # quick_decl: ID ASSIGN_DECL  expression1  SEMI;
    # def visitQuick_decl(self, ctx: MiniGoParser.Quick_declContext):
    #     return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression1()))

    
    # arrayliteral: array_type_cell primitive_type LBRACE nestedarray RBRACE;    
    def visitArrayliteral(self, ctx: MiniGoParser.ArrayliteralContext):
        dimens = self.visit(ctx.array_type_cell())  # Kích thước của mảng
        eleType = self.visit(ctx.primitive_type()) # Kiểu phần tử trong mảng
        value = self.visit(ctx.nestedarray())  # Giá trị của mảng
        return ArrayLiteral(dimens, eleType, value)
    
    #nestedarray: array_element nestedarray_tail | ;
    def visitNestedarray(self, ctx: MiniGoParser.NestedarrayContext):
        if ctx.getChildCount() == 0:  # Không có phần tử tiếp theo
            return []
        return [self.visit(ctx.array_element())] + self.visit(ctx.nestedarray_tail())
    
    #nestedarray_tail: COMMA array_element nestedarray_tail | ;
    def visitNestedarray_tail(self, ctx: MiniGoParser.Nestedarray_tailContext):
        if ctx.getChildCount() == 0:  # Không có phần tử tiếp theo
            return []
        return [self.visit(ctx.array_element())] + self.visit(ctx.nestedarray_tail())

    #array_element: expression1 | LBRACE nestedarray RBRACE;
    def visitArray_element(self, ctx: MiniGoParser.Array_elementContext):
        if ctx.expression1():
            return self.visit(ctx.expression1())  # Phần tử là một biểu thức
        return self.visit(ctx.nestedarray())  # Phần tử là một mảng con



    
    # # arrays: LBRACE expressionlist RBRACE COMMA arrays | LBRACE expressionlist RBRACE ; 
    # def visitArrays(self, ctx: MiniGoParser.ArraysContext):
    #     if ctx.getChildCount() == 3:
    #         return [self.visit(ctx.expressionlist())]
    #     else:
    #         return [self.visit(ctx.expressionlist())] + self.visit(ctx.arrays())
    
    # structliteral: ID LBRACE structfieldlist RBRACE | ID LBRACE RBRACE;
    def visitStructliteral(self, ctx: MiniGoParser.StructliteralContext):
        if ctx.getChildCount() == 3:
            return StructLiteral(ctx.ID().getText(), [])
        else:
            return StructLiteral(ctx.ID().getText(), self.visit(ctx.structfieldlist()))
      
    # structfieldlist: structfield COMMA structfieldlist | structfield ;
    def visitStructfieldlist(self, ctx: MiniGoParser.StructfieldlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.structfield())]
        else:
            return [self.visit(ctx.structfield())] + self.visit(ctx.structfieldlist())
        
    # structfield: ID ':' expression1; 
    def visitStructfield(self, ctx: MiniGoParser.StructfieldContext):
        return (ctx.ID().getText(), self.visit(ctx.expression1()))
    
        
        


    # statement : assignment_statement SEMI
    #           | if_statement SEMI
    #           | for_statement SEMI
    #           | break_statement SEMI 
    #           | continue_statement SEMI
    #           | call_statement SEMI
    #           | return_statement SEMI;
    def visitStatement(self, ctx: MiniGoParser.StatementContext):
        if ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.for_statement(): 
            return self.visit(ctx.for_statement())
        if ctx.break_statement():
            return self.visit(ctx.break_statement())
        if ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        if ctx.call_statement():
            return self.visit(ctx.call_statement())
        if ctx.return_statement():
            return self.visit(ctx.return_statement())
    
    # assignment_statement : (ID | array_access | struct_access) assignment_operator expression1 ;
    def visitAssignment_statement(self, ctx: MiniGoParser.Assignment_statementContext):
        lhs = None
        if ctx.struct_access():
            lhs = self.visit(ctx.struct_access())
        elif ctx.array_access():
            lhs = self.visit(ctx.array_access())
        elif ctx.ID():
            lhs = Id(ctx.ID().getText())
        op = self.visit(ctx.assignment_operator())
        rhs = self.visit(ctx.expression1())
        if op != ":=":
            rhs = BinaryOp(op[:-1], lhs, rhs)  # Tạo BinaryOp cho các toán tử gán như +=, -=, *=, /=, %=
        return Assign(lhs, rhs)
    
    # assignment_operator : ASSIGN_DECL 
    #                     | ADD_ASSIGN 
    #                     | SUB_ASSIGN 
    #                     | MUL_ASSIGN 
    #                     | DIV_ASSIGN 
    #                     | MOD_ASSIGN ;
    def visitAssignment_operator(self, ctx: MiniGoParser.Assignment_operatorContext):
        return ctx.getText()
    
    # if_statement : IF LPAREN expression1 RPAREN block else_clause;
    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        exp = self.visit(ctx.expression1())
        thenStmt = self.visit(ctx.block())
        elseStmt = self.visit(ctx.else_clause())
        return If(exp, thenStmt, elseStmt)
    
    # else_clause : ELSE (if_statement | block) |  ;
    def visitElse_clause(self, ctx: MiniGoParser.Else_clauseContext):
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.block():
            return self.visit(ctx.block())
        if ctx.getChildCount() == 0:
            return None
        
    # for_statement : FOR for_condition block ;
    def visitFor_statement(self, ctx: MiniGoParser.For_statementContext):
        cond = self.visit(ctx.for_condition())
        loop = self.visit(ctx.block())
        if isinstance(cond, tuple) and cond[0] == "step":
            return ForStep(cond[1], cond[2], cond[3], loop)
        elif isinstance(cond, tuple) and cond[0] == "foreach":
            return ForEach(cond[1], cond[2], cond[3], loop)
        elif isinstance(cond, Expr):
            return ForBasic(cond, loop)
            
    # for_condition : expression1
    #               | (variable_declaration | assignment_statement SEMI) expression1 SEMI assignment_statement
    #               | ID COMMA ID ASSIGN_DECL RANGE (ID|struct_access) ;
    def visitFor_condition(self, ctx: MiniGoParser.For_conditionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        elif ctx.assignment_statement(0):
            init = None
            if ctx.variable_declaration():
                init = self.visit(ctx.variable_declaration())
            else:
                init = self.visit(ctx.assignment_statement(0))

            condition = self.visit(ctx.expression1())
            if ctx.variable_declaration():
                update = self.visit(ctx.assignment_statement(0))
            else:
                update = self.visit(ctx.assignment_statement(1))
            return ("step", init, condition, update)
        else: 
            idx = Id(ctx.ID(0).getText())
            value = Id(ctx.ID(1).getText())
            if ctx.struct_access():
                arr = self.visit(ctx.struct_access())
            else: 
                arr = Id(ctx.ID(2).getText())
            return ("foreach", idx, value, arr)
    
    # break_statement : BREAK ;
    def visitBreak_statement(self, ctx: MiniGoParser.Break_statementContext):
        return Break()
    
    # continue_statement : CONTINUE ;
    def visitContinue_statement(self, ctx: MiniGoParser.Continue_statementContext):
        return Continue()
    
    # call_statement : function_call | method_call  ;
    def visitCall_statement(self, ctx: MiniGoParser.Call_statementContext):
        if ctx.function_call():
            return self.visit(ctx.function_call())
        if ctx.method_call():
            return self.visit(ctx.method_call())

    # return_statement : RETURN value ;
    def visitReturn_statement(self, ctx: MiniGoParser.Return_statementContext):
        return Return(self.visit(ctx.value()))
    
    # value: expression1 | ;
    def visitValue(self, ctx: MiniGoParser.ValueContext):
        if ctx.expression1():
            return self.visit(ctx.expression1())
        else:
            return None

    # block : LBRACE stmt_dec RBRACE;
    def visitBlock(self, ctx: MiniGoParser.BlockContext):
        return Block(self.visit(ctx.stmt_dec()))
    
    # stmt_dec: stmts_decs | ;
    def visitStmt_dec(self, ctx: MiniGoParser.Stmt_decContext):
        if ctx.stmts_decs():
            return self.visit(ctx.stmts_decs())
        else:
            return []
        
    # stmts_decs: (statement|declare) stmts_decs | (statement|declare);
    def visitStmts_decs(self, ctx: MiniGoParser.Stmts_decsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        else:
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.stmts_decs())  


    # expressionlist: expression1 COMMA expressionlist | expression1;
    def visitExpressionlist(self, ctx: MiniGoParser.ExpressionlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression1())]
        else:
            return [self.visit(ctx.expression1())] + self.visit(ctx.expressionlist())

    # expression1: expression1 OR expression2 | expression2;
    def visitExpression1(self, ctx: MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        else:
            left = self.visit(ctx.expression1())
            right = self.visit(ctx.expression2())
            return BinaryOp(ctx.OR().getText(), left, right)
    
    # expression2: expression2 AND expression3 | expression3;
    def visitExpression2(self, ctx: MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        else:
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(ctx.AND().getText(), left, right)
        
    # expression3: expression3 (EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) expression4 | expression4;
    def visitExpression3(self, ctx: MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        else:
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        
    # expression4: expression4 (PLUS | MINUS) expression5 | expression5;
    def visitExpression4(self, ctx: MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        else:
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
    
    # expression5: expression5 (MULT | DIV | MOD) expression6 | expression6;
    def visitExpression5(self, ctx: MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        else:
            left = self.visit(ctx.expression5())
            right = self.visit(ctx.expression6())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    # expression6: (NOT | MINUS) expression6 | expression7;
    def visitExpression6(self, ctx: MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expression6())
            return UnaryOp(op, body)
    
    # expression7: operand | array_access | struct_access | method_call | function_call | LPAREN expression1 RPAREN;
    def visitExpression7(self, ctx: MiniGoParser.Expression7Context):
        if ctx.operand():
            return self.visit(ctx.operand())
        if ctx.array_access():
            return self.visit(ctx.array_access())
        if ctx.struct_access():
            return self.visit(ctx.struct_access())
        if ctx.method_call():
            return self.visit(ctx.method_call())
        if ctx.function_call():
            return self.visit(ctx.function_call())
        if ctx.LPAREN():
            return self.visit(ctx.expression1())
    
    # array_access: ID arrayindex;
    def visitArray_access(self, ctx: MiniGoParser.Array_accessContext):
        arr = Id(ctx.ID().getText())
        idx = self.visit(ctx.arrayindex())
        return ArrayCell(arr, idx)
    
    # arrayindex: LBRACK expression1 RBRACK arrayindex | LBRACK expression1 RBRACK  ;
    def visitArrayindex(self, ctx: MiniGoParser.ArrayindexContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression1())]
        else:
            return [self.visit(ctx.expression1())] + self.visit(ctx.arrayindex())
        
      # struct_access : (ID | function_call)  struct_tail;
    def visitStruct_access(self, ctx: MiniGoParser.Struct_accessContext):
        if ctx.ID():
            receiver = Id(ctx.ID().getText())
        else:
            receiver = self.visit(ctx.function_call())
        return self.visitStruct_tail(ctx.struct_tail(), receiver)

    # struct_tail : DOT ID struct_tail
    #             | LBRACK expression1 RBRACK struct_tail
    #             | ;
    def visitStruct_tail(self, ctx: MiniGoParser.Struct_tailContext, receiver):
        if ctx.getChildCount() == 0:
            return receiver
        elif ctx.DOT():
            field = ctx.ID().getText()
            new_receiver = FieldAccess(receiver, field)
            return self.visitStruct_tail(ctx.struct_tail(), new_receiver)
        else:
            indices = []
            while ctx.LBRACK():
                indices.append(self.visit(ctx.expression1()))  # Lấy giá trị index
                ctx = ctx.struct_tail()  # Di chuyển đến phần tiếp theo của tail
            new_receiver = ArrayCell(receiver, indices)
            return self.visitStruct_tail(ctx, new_receiver)

    
    # function_call: ID LPAREN argumentlist RPAREN;
    def visitFunction_call(self, ctx: MiniGoParser.Function_callContext):
        funName = ctx.ID().getText()
        args = self.visit(ctx.argumentlist())
        return FuncCall(funName, args)
    
    # method_call: (ID | function_call | struct_access) DOT ID LPAREN argumentlist RPAREN;
    def visitMethod_call(self, ctx: MiniGoParser.Method_callContext):
        if ctx.struct_access():
            receiver = self.visit(ctx.struct_access())  
        elif ctx.function_call():
            receiver = self.visit(ctx.function_call())  
        elif ctx.ID(0):
            receiver = Id(ctx.ID(0).getText())  
        metName = ctx.getChild(2).getText()
        args = self.visit(ctx.argumentlist())
        return MethCall(receiver, metName, args)

        
    # argumentlist: expressionlist |  ;
    def visitArgumentlist(self, ctx: MiniGoParser.ArgumentlistContext):
        if ctx.expressionlist():
            return self.visit(ctx.expressionlist())
        else:
            return []

    # operand: literal | ID | arrayliteral | structliteral;
    def visitOperand(self,ctx:MiniGoParser.OperandContext): 
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrayliteral():
            return self.visit(ctx.arrayliteral())
        elif ctx.structliteral():
            return self.visit(ctx.structliteral())
 
         
    # literal: INTLIT | FLOATLIT | STRINGLIT | TRUE | FALSE | NIL;
    # def visitLiteral(self,ctx:MiniGoParser.LiteralContext):
    #     if ctx.INTLIT():
    #         return IntLiteral(int(ctx.INTLIT().getText()))
    #     if ctx.FLOATLIT():
    #         return FloatLiteral(float(ctx.FLOATLIT().getText()))
    #     if ctx.STRINGLIT():
    #         return StringLiteral(ctx.STRINGLIT().getText())
    #     if ctx.TRUE():
    #         return BooleanLiteral(True)
    #     if ctx.FALSE():                
    #         return BooleanLiteral(False)
    #     if ctx.NIL():
    #         return NilLiteral()
    def visitLiteral(self,ctx:MiniGoParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        if ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        if ctx.FALSE():                
            return BooleanLiteral(ctx.FALSE().getText())
        if ctx.NIL():
            return NilLiteral()   
   
        



    

