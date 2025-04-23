import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """var x int = true ;"""
        expect = str(Program([VarDecl("x",IntType(),BooleanLiteral("True"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test2(self):
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test3(self):
        input = """var x int = 10;"""
        expect = str(Program([VarDecl("x",IntType(),IntLiteral("10"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test4(self):
        input = """var y float = 5.6e1;"""
        expect = str(Program([VarDecl("y",FloatType(),FloatLiteral("5.6e1"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test5(self):
        input = """var flag boolean = true;"""
        expect = str(Program([VarDecl("flag",BoolType(),BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test6(self):
        input = """var message string = "Hello, World!";"""
        expect = str(Program([VarDecl("message",StringType(),StringLiteral('"Hello, World!"'))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test7(self):
        input = """var matrix [3][4][5][6]float;"""
        expect = str(Program([VarDecl("matrix",ArrayType([IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)],FloatType()),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test8(self):
        input = """var arr[1]int = [2][3]int{1,2,3};"""
        expect = str(Program([VarDecl("arr",ArrayType([IntLiteral(1)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test9(self):
        input = """var arr[2][3]int =  [2][3]int{{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test10(self):
        input = """var arr[3][4][5]int =  [2][3][3]int{ {{1, 2, 3}}, {{4}, {5, 6}}, {{}} };"""
        expect = str(Program([VarDecl("arr",ArrayType([IntLiteral(3),IntLiteral(4),IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(3)],IntType(),[[[IntLiteral(1),IntLiteral(2),IntLiteral(3)]],[[IntLiteral(4)],[IntLiteral(5),IntLiteral(6)]],[[]]]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test11(self):
        input = "var b = a.b.c;"
        expect = str(Program([VarDecl("b",None,FieldAccess(FieldAccess(Id("a"),"b"),"c"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test12(self):
        input = "var p Person = Person{name: \"Alice\", age: 25};"
        expect = str(Program([VarDecl("p",Id("Person"),StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(25))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test13(self):
        input = "var p Person = foo().a[2];"
        expect = str(Program([VarDecl("p", Id("Person"),ArrayCell(FieldAccess(FuncCall("foo", []), "a"),[IntLiteral(2)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test14(self):
        input = " var p = Person{name: \"Alice\", age: 25};"
        expect = str(Program([VarDecl("p",None,StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(25))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test15(self):
        input = """
            var b = false;
            var i = 10;
            var f = 5.6;
            var s = "Hello, World!";
        """
        expect = str(Program([
            VarDecl("b", None, BooleanLiteral(False)),
            VarDecl("i", None, IntLiteral(10)),
            VarDecl("f", None, FloatLiteral(5.6)),
            VarDecl("s", None, StringLiteral('"Hello, World!"'))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test16(self):
        input = """
            var P person = person{name: "Alice", age: 25};
            var c = person{};
        """
        expect = str(Program([
            VarDecl("P", Id("person"), StructLiteral("person", [("name", StringLiteral('"Alice"')), ("age", IntLiteral(25))])),
            VarDecl("c", None, StructLiteral("person", []))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    
    def test17(self):
        input = """
            var p Person = Person{name: "Alice", age: 25};
            var p2 Person = Person{name: "Bob", age: 30};
        """
        expect = str(Program([
            VarDecl("p", Id("Person"), StructLiteral("Person", [("name", StringLiteral('"Alice"')), ("age", IntLiteral(25))])),
            VarDecl("p2", Id("Person"), StructLiteral("Person", [("name", StringLiteral('"Bob"')), ("age", IntLiteral(30))]))

            
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    
    def test18(self):
        input = """
            var test = walk{Person : Person{name: "Alice", age: 25}, Address : Address{street: "123 Main St", city: "HCMC"}};
        """
        expect = str(Program([
            VarDecl("test", None, StructLiteral("walk", [
                ("Person", StructLiteral("Person", [("name", StringLiteral('"Alice"')), ("age", IntLiteral(25))])),
                ("Address", StructLiteral("Address", [("street", StringLiteral('"123 Main St"')), ("city", StringLiteral('"HCMC"'))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test19(self):
        input = """
            var arr[b]float = [c]int{name{a: 1, b: 2}, name{a: 3, b: 4}};
        """
        expect = str(Program([
            VarDecl("arr", ArrayType([Id("b")], FloatType()), ArrayLiteral([Id("c")], IntType(), [
                StructLiteral("name", [("a", IntLiteral(1)), ("b", IntLiteral(2))]),
                StructLiteral("name", [("a", IntLiteral(3)), ("b", IntLiteral(4))])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))


    def test20(self):
        input = """
            var arr[2][3][4]boolean = [2][3][4]Person{ 2 + 3 - 4, b, 5. };
        """
        expect = str(Program([
            VarDecl("arr", ArrayType([IntLiteral(2), IntLiteral(3), IntLiteral(4)], BoolType()), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)], Id("Person"), [
                BinaryOp("-", BinaryOp("+", IntLiteral(2), IntLiteral(3)), IntLiteral(4)),
                Id("b"),
                FloatLiteral("5.")
            ])
        )]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test21(self):
        input = " const a = 234; "
        expect = str(Program([ConstDecl("a",None, IntLiteral(234))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test22(self):
        input = " const b = 3.14; "
        expect = str(Program([ConstDecl("b",None, FloatLiteral(3.14))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test23(self):
        input = " const c = true; "
        expect = str(Program([ConstDecl("c",None, BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test24(self):
        input = " const d = \"Hello, World!\"; "
        expect = str(Program([ConstDecl("d",None, StringLiteral('"Hello, World!"'))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test25(self):
        input = " const e = a.b[1].c(); "
        expect = str(Program([ConstDecl("e", None,MethCall(ArrayCell(FieldAccess(Id("a"), "b"),[IntLiteral(1)]),"c",[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        input = " const f = person{name: \"Alice\", age: 25}; "
        expect = str(Program([ConstDecl("f",None, StructLiteral("person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(25))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test27(self):
        input = """ const g = walk{Person : Person{name: \"Alice\", age: 25}, Address : Address{street: \"123 Main St\", city: \"HCMC"}}; """
        expect = str(Program([ConstDecl("g",None, StructLiteral("walk",[
            ("Person",StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(25))])),
            ("Address",StructLiteral("Address",[("street",StringLiteral('"123 Main St"')),("city",StringLiteral('"HCMC"'))]))
        ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test28(self):
        input = """ const h = [2][3][4]Person{ 2+3-4, b, 5. }; """
        expect = str(Program([ConstDecl("h",None, ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)],Id("Person"),[
            BinaryOp("-",BinaryOp("+",IntLiteral(2),IntLiteral(3)),IntLiteral(4)),
            Id("b"),
            FloatLiteral("5.")
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test29(self):
        input = " const a = 234 + b - \"Hello, World!\"; "
        expect = str(Program([ConstDecl("a",None,BinaryOp("-",BinaryOp("+",IntLiteral(234),Id("b")),StringLiteral('"Hello, World!"')))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test30(self):
        input = "const _tienkhai = a.test.foo();"
        expect = str(Program([ConstDecl("_tienkhai",None,MethCall(FieldAccess(Id("a"),"test"),"foo",[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test31(self):
        input = "func main() {};"
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    

    def test32(self):
        input = "func add(a int, b int) int {};"
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], IntType(), Block([]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test33(self):
        input = "func add(a , b int) int { return a + b; };"
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test34(self):
        input = "func add(a , b int) [2]int { return a + b; };"
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], ArrayType([IntLiteral(2)], IntType()), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test35(self):
        input = "func greet(name string) { print(\"Hello, \" + name); };"
        expect = str(Program([
            FuncDecl("greet", [
                ParamDecl("name", StringType())
            ], VoidType(), 
            Block([
                FuncCall("print", [BinaryOp("+", StringLiteral('"Hello, "'), Id("name"))])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
        
    def test36(self):
        input = "func isEven(n int) boolean { return n % 2 == 0; };"
        expect = str(Program([
            FuncDecl("isEven", [
                ParamDecl("n", IntType())
            ], BoolType(), 
            Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test37(self):
        input = "func isEven(n, m int, a , b float) boolean { return n % 2 == 0; break; };"
        expect = str(Program([
            FuncDecl("isEven", [  
                ParamDecl("n", IntType()),
                ParamDecl("m", IntType()),
                ParamDecl("a", FloatType()),
                ParamDecl("b", FloatType())
            ], BoolType(), 
            Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0))),
                Break()
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test38(self):
        input = "func add(a int, c Person) walk {continue;};"
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("c", Id("Person"))
            ], Id("walk"), Block([Continue()]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
        

    def test39(self):
        input = "func power(base float, exp int) float { var result float = 1.0; return; };"
        expect = str(Program([
            FuncDecl("power", [
                ParamDecl("base", FloatType()),
                ParamDecl("exp", IntType())
            ], FloatType(), 
            Block([
                VarDecl("result", FloatType(), FloatLiteral(1.0)),
                Return(None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test40(self):
        input = "func factorial(n int) int { return n * factorial(n-1); };"
        expect = str(Program([
            FuncDecl("factorial", [
                ParamDecl("n", IntType())
            ], IntType(), 
            Block([
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test41(self):
        input = "type Point struct { x int; y int; };"
        expect = str(Program([
            StructType("Point", [
                ("x", IntType()), 
                ("y", IntType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test42(self):
        input = "type Rectangle struct { width float; height float; };"
        expect = str(Program([
            StructType("Rectangle", [
                ("width", FloatType()), 
                ("height", FloatType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test43(self):
        input = "type Person struct { name string; age int; isEmployed boolean; };"
        expect = str(Program([
            StructType("Person", [
                ("name", StringType()), 
                ("age", IntType()), 
                ("isEmployed", BoolType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test44(self):
        input = "type Employee struct { id Person; name string; salary float; };"
        expect = str(Program([
            StructType("Employee", [
                ("id", Id("Person")), 
                ("name", StringType()), 
                ("salary", FloatType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test45(self):
        input = "type Student struct { id int; name string; marks [3][4]int; };"
        expect = str(Program([
            StructType("Student", [
                ("id", IntType()), 
                ("name", StringType()), 
                ("marks", ArrayType([IntLiteral(3), IntLiteral(4)], IntType()))
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test46(self):
        input = "type Vector3D struct { x float; y float; z float; };"
        expect = str(Program([
            StructType("Vector3D", [
                ("x", FloatType()), 
                ("y", FloatType()), 
                ("z", FloatType())
            ], 
            []
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test47(self):
        input = "type Car struct { brand string; speed int;  };"
        expect = str(Program([
            StructType("Car", [
                ("brand", StringType()), 
                ("speed", IntType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test48(self):
        input = "type Account struct { balance float; };"
        expect = str(Program([
            StructType("Account", [
                ("balance", FloatType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test49(self):
        input = "type Camera struct { resolution int;  };"
        expect = str(Program([
            StructType("Camera", [
                ("resolution", IntType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test50(self):
        input = "type Animal struct { species string; age int; };"
        expect = str(Program([
            StructType("Animal", [
                ("species", StringType()), 
                ("age", IntType())
            ], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test51(self):
        input = "type Drawable interface { draw(); };"
        expect = str(Program([
            InterfaceType("Drawable", [
                Prototype("draw", [], VoidType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test52(self):
        input = "type Shape interface { area() float; perimeter() float; };"
        expect = str(Program([
            InterfaceType("Shape", [
                Prototype("area", [], FloatType()),
                Prototype("perimeter", [], FloatType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test53(self):
        input = "type Logger interface { log(message string); };"
        expect = str(Program([
            InterfaceType("Logger", [
                Prototype("log", [StringType()], VoidType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test54(self):
        input = "type Calculator interface { add(a int, b int) int; subtract(a int, b int) int; };"
        expect = str(Program([
            InterfaceType("Calculator", [
                Prototype("add", [IntType(), IntType()], IntType()),
                Prototype("subtract", [IntType(), IntType()], IntType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test55(self):
        input = "type Database interface { connect(); disconnect(); query(sql student) Person; };"
        expect = str(Program([
            InterfaceType("Database", [
                Prototype("connect", [], VoidType()),
                Prototype("disconnect", [], VoidType()),
                Prototype("query", [Id("student")], Id("Person"))
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test56(self):
        input = "type Vehicle interface { start(); stop(); accelerate(speed [2][a]int); };"
        expect = str(Program([
            InterfaceType("Vehicle", [
                Prototype("start", [], VoidType()),
                Prototype("stop", [], VoidType()),
                Prototype("accelerate", [ArrayType([IntLiteral(2),Id("a")],IntType())], VoidType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test57(self):
        input = "type Vehicle interface { start(); stop(); accelerate(speed [2][a]int)[2][3]Person; };"
        expect = str(Program([
            InterfaceType("Vehicle", [
                Prototype("start", [], VoidType()),
                Prototype("stop", [], VoidType()),
                Prototype("accelerate", [ArrayType([IntLiteral(2),Id("a")],IntType())], ArrayType([IntLiteral(2),IntLiteral(3)],Id("Person")))
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test58(self):
        input = "type Vehicle interface { start(a , b , c int); stop(); accelerate(speed [2][a]int)[2][3]Person; };"
        expect = str(Program([
            InterfaceType("Vehicle", [
                Prototype("start", [IntType(), IntType(), IntType()], VoidType()),
                Prototype("stop", [], VoidType()),
                Prototype("accelerate", [ArrayType([IntLiteral(2),Id("a")],IntType())], ArrayType([IntLiteral(2),IntLiteral(3)],Id("Person")))
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))    

    def test59(self):
        input = "type  FileHandler interface { open(file string); close(); write(data string); read() string; };"
        expect = str(Program([
            InterfaceType("FileHandler", [
                Prototype("open", [StringType()], VoidType()),
                Prototype("close", [], VoidType()),
                Prototype("write", [StringType()], VoidType()),
                Prototype("read", [], StringType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test60(self):
        input = "type PaymentGateway interface  { processPayment(amount float) boolean; refund(transactionId string) boolean; };"
        expect = str(Program([
            InterfaceType("PaymentGateway", [
                Prototype("processPayment", [FloatType()], BoolType()),
                Prototype("refund", [StringType()], BoolType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test61(self):
        input = """func (c Calculator) Add(x int) int {
                    c.value += x;
                    return c.value;
                    }
                """
        expect = str(Program([
            MethodDecl("c", Id("Calculator"), 
                FuncDecl("Add", [
                    ParamDecl("x", IntType())  
                ], IntType(), 
                Block([
                    Assign(FieldAccess(Id("c"), "value"),  
                        BinaryOp("+", FieldAccess(Id("c"), "value"), Id("x"))),  
                    Return(FieldAccess(Id("c"), "value"))  
                ]))
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test62(self):
        input = """func (p Person) Greet() string {
                        return "Hello, " + p.name;
                    }
                    """
        expect = str(Program([
            MethodDecl("p", Id("Person"), 
                FuncDecl("Greet", [], StringType(), 
                    Block([
                        Return(BinaryOp("+", StringLiteral('"Hello, "'), FieldAccess(Id("p"), "name")))
                    ])
                )
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test63(self):
        input = """func (r Rectangle) Area(a, b int) float {
                        return r.width * r.height;
                    }
                    """
        expect = str(Program([
            MethodDecl("r", Id("Rectangle"), 
                FuncDecl("Area", [ParamDecl("a", IntType()),ParamDecl("b", IntType()) ], FloatType(), 
                    Block([
                        Return(BinaryOp("*", FieldAccess(Id("r"), "width"), FieldAccess(Id("r"), "height")))
                    ])
                )
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test64(self):
        input = """func (b BankAccount) Withdraw(amount float) boolean {
                        if (b.balance >= amount) {
                            b.balance -= amount;
                            return true;
                        } else {
                            return false;
                        }
                    }
                    """
        expect = str(Program([
            MethodDecl("b", Id("BankAccount"), 
                FuncDecl("Withdraw", [
                    ParamDecl("amount", FloatType())
                ], BoolType(), 
                Block([
                    If(
                        BinaryOp(">=", FieldAccess(Id("b"), "balance"), Id("amount")),
                        Block([
                            Assign(FieldAccess(Id("b"), "balance"), 
                                BinaryOp("-", FieldAccess(Id("b"), "balance"), Id("amount"))),
                            Return(BooleanLiteral(True))
                        ]),
                        Block([Return(BooleanLiteral(False))])
                    )
                ])
            ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test65(self):
        input = """func (c Car) Accelerate(delta int) {
                        c.speed += delta;
                    }
                    """
        expect = str(Program([
            MethodDecl("c", Id("Car"), 
                FuncDecl("Accelerate", [
                    ParamDecl("delta", IntType())
                ], VoidType(), 
                Block([
                    Assign(FieldAccess(Id("c"), "speed"), 
                        BinaryOp("+", FieldAccess(Id("c"), "speed"), Id("delta")))
                ])
            ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test66(self):
        input = """
                func main() {
                     x := a[2][3];
                     b += 2 * foo();
                }
    """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("x"), 
                    ArrayCell(Id("a"), [IntLiteral(2),IntLiteral(3)])
                ),
                Assign(Id("b"), 
                    BinaryOp("+", Id("b"), 
                        BinaryOp("*", IntLiteral(2), FuncCall("foo", []))
                    )
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test67(self):
        input = """
                func main() {
                    for i := 0; i < 10; i += 1 {
                        print(i);
                    }
                }
                """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),  # Khởi tạo i := 0
                    BinaryOp("<", Id("i"), IntLiteral(10)),  # Điều kiện i < 10
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),  # Cập nhật i += 1
                    Block([
                        FuncCall("print", [Id("i")])  # print(i);
                    ])
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test68(self):
        input = """
                func main() {
                   a := "helo";
                   b := a.b() + a.b;
                }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), 
                Block([
                    Assign(Id("a"), StringLiteral('"helo"')),  # Gán giá trị chuỗi cho a
                    Assign(Id("b"), 
                        BinaryOp("+", 
                            MethCall(Id("a"), "b", []),  # a.b() (gọi phương thức trên a)
                            FieldAccess(Id("a"), "b")  # a.b (truy cập thuộc tính b của a)
                        )
                    )
                ])
            )
        ]))
        
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))


    def test69(self):
        input = """
                func main() {
                  a[5].b := 10;
                }
                """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(
                    FieldAccess(  # a[5].b (truy cập vào thuộc tính b của phần tử mảng)
                        ArrayCell(Id("a"), [IntLiteral(5)]),  
                        "b"
                    ),
                    IntLiteral(10)  # Gán giá trị 10
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
        
    def test70(self):
        input = """
                var b[1][2] int;
                func main() {
                  a().b[2] := 10;
                }
                """
        expect = str(Program([
        VarDecl("b", ArrayType([IntLiteral(1), IntLiteral(2)], IntType()), None),  # Khai báo mảng b[1][2] kiểu int
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(
                    ArrayCell(  # a().b[2] (truy cập phần tử thứ 2 của a().b)
                        FieldAccess(FuncCall("a", []), "b"),  
                        [IntLiteral(2)]
                    ),
                    IntLiteral(10)  # Gán giá trị 10
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test71(self):
        input ="""
        func main() {
            for var i = 0; i < 10; i += 1 {
                print(i);
                for var j = 0; j < 10; j += 1 {
                    print(j);
                }
            }
            }
        """

        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForStep(
                    VarDecl("i", None, IntLiteral(0)),  # Khởi tạo i = 0
                    BinaryOp("<", Id("i"), IntLiteral(10)),  # Điều kiện i < 10
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),  # Cập nhật i += 1
                    Block([
                        FuncCall("print", [Id("i")]),  # print(i);
                        ForStep(
                            VarDecl("j", None, IntLiteral(0)),  # Khởi tạo j = 0
                            BinaryOp("<", Id("j"), IntLiteral(10)),  # Điều kiện j < 10
                            Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),  # Cập nhật j += 1
                            Block([
                                FuncCall("print", [Id("j")])  # print(j);
                            ])
                        )
                    ])
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test72(self):
        input = """
        func main() {      
            for i > 10 {
                var x[1][2]int = [1][2]int{1, 2}; 
            }
        }
            """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForBasic(
                    BinaryOp(">", Id("i"), IntLiteral(10)),  # Điều kiện i > 10
                    Block([
                        VarDecl(
                            "x",  
                            ArrayType([IntLiteral(1), IntLiteral(2)], IntType()),  # Kiểu mảng x[1][2] int
                            ArrayLiteral([IntLiteral(1), IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])  # Giá trị khởi tạo {1,2}
                        )
                    ])
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test73(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                for var j = 10; j < 10; j += 1 {
                    print(j);
                }
            }
        }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),  # Khởi tạo i = 0
                    BinaryOp("<", Id("i"), IntLiteral(10)),  # Điều kiện i < 10
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),  # Cập nhật i += 1
                    Block([
                        ForStep(
                            VarDecl("j", None, IntLiteral(10)),  # Khởi tạo j = 10
                            BinaryOp("<", Id("j"), IntLiteral(10)),  # Điều kiện j < 10
                            Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),  # Cập nhật j += 1
                            Block([
                                FuncCall("print", [Id("j")])  # print(j);
                            ])
                        )
                    ])
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
       
    def test74(self):
        input = """
        func main() {
            for index, value := range array {
                print(index, value);
            }
        }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForEach(
                    Id("index"),  # Biến index (chỉ số)
                    Id("value"),  # Biến value (giá trị)
                    Id("array"),  # Mảng cần duyệt
                    Block([
                        FuncCall("print", [Id("index"), Id("value")])  # print(index, value);
                    ])
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test75(self):
        input = """
        func main() {
            for _, value := range array {
                print(index, value);
            }
        }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                ForEach(
                    Id("_"),  # Bỏ qua index (dùng `_`)
                    Id("value"),  # Biến value (giá trị)
                    Id("array"),  # Mảng cần duyệt
                    Block([
                        FuncCall("print", [Id("index"), Id("value")])  # print(index, value);
                    ])
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test76(self):
        input = """
                func main() {
                if(a > b) {return 1;};    
            }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                If(
                    BinaryOp(">", Id("a"), Id("b")),  # Điều kiện a > b
                    Block([
                        Return(IntLiteral(1))  # return 1;
                    ]),
                    None  # Không có else
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))



    def test77(self):
        input = """
                func main() {
                if(a > b){
                    return a + b;
                } else {
                    return;
                }     
            }
        """

        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                If(
                    BinaryOp(">", Id("a"), Id("b")),  # Điều kiện a > b
                    Block([
                        Return(BinaryOp("+", Id("a"), Id("b")))  # return a + b;
                    ]),
                    Block([
                        Return(None)  # return;
                    ])
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test78(self):
        input = """
                func main() {
                if(a > b){
                    return a + b;
                } else if(a < b) {
                    return a - b;
                } else { return 0;}    
            }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                If(
                    BinaryOp(">", Id("a"), Id("b")),  # Điều kiện a > b
                    Block([
                        Return(BinaryOp("+", Id("a"), Id("b")))  # return a + b;
                    ]),
                    If(
                        BinaryOp("<", Id("a"), Id("b")),  # Điều kiện a < b
                        Block([
                            Return(BinaryOp("-", Id("a"), Id("b")))  # return a - b;
                        ]),
                        Block([
                            Return(IntLiteral(0))  # return 0;
                        ])
                    )
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test79(self):
        input = """ 
            func main(){
                a := b + c;
                arr := [3]int{10, 20, 30};
            }
    """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a"), BinaryOp("+", Id("b"), Id("c"))),  # Gán a = b + c
                Assign(
                    Id("arr"), 
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)])  # Gán mảng arr
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
        
    def test80(self):
        input = """
                func main(){
                a := Person();
                }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a"), FuncCall("Person", []))  
            ])
        )
    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test81(self):
        input = """
                func main(){
                a := Person{name: "TienKhai"};
                }
        """
        expect = str(Program([
        FuncDecl("main", [], VoidType(), 
            Block([
                Assign(
                    Id("a"), 
                    StructLiteral(
                        "Person",  # Tên struct
                        [("name", StringLiteral('"TienKhai"'))]  
                    )
                )
            ])
        )
    ]))
    
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test82(self):
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test83(self):
        input = """const x = 5; func main() {};"""
        expect = str(Program([
            ConstDecl("x", None, IntLiteral(5)),
            FuncDecl("main", [], VoidType(), Block([]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test84(self):
        input = """var y int; func main() {};"""
        expect = str(Program([
            VarDecl("y",IntType(), None),
            FuncDecl("main", [], VoidType(), Block([]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test85(self):
        input = """func main() { a := 10; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), 
            Block([Assign(Id("a"), IntLiteral(10))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test86(self):
        input = """func main() { b:= 5.9; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("b"), FloatLiteral(5.9))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test87(self):
        input = """func add(a int, b int) int { return a + b; };"""
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], IntType(),
            Block([Return(BinaryOp("+", Id("a"), Id("b")))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test88(self):
        input = """func main() { print("Hello, world!"); };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([FuncCall("print", [StringLiteral('"Hello, world!"')])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test89(self):
        input = "func isEven(n int) boolean { return n % 2 == 0; };"
        expect = str(Program([
            FuncDecl("isEven", [
                ParamDecl("n", IntType())
            ], BoolType(), 
            Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test90(self):
        input = """
                func main() { 
                for i := 0; i < 10; i += 1 { 
                    print(i); 
                    } 
                };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                ForStep(Assign(Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([FuncCall("print", [Id("i")])]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test91(self):
        input = """func main() { return; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([Return(None)]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test92(self):
        input = """func main() { break; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([Break()]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test93(self):
        input = """func main() { continue; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([Continue()]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test94(self):
        input = """func main() { arr := [5]int{1, 2, 3, 4, 5}; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(Id("arr"),
                    ArrayLiteral([IntLiteral(5)], IntType(), 
                                    [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    
    def test95(self):
        input = """func main() { x := y * z + 10; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(Id("x"), BinaryOp("+", BinaryOp("*", Id("y"), Id("z")), IntLiteral(10)))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test96(self):
        input = """func main() { a := Person{name: "John", age: 30}; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(Id("a"),
                    StructLiteral("Person", [("name", StringLiteral('"John"')), ("age", IntLiteral(30))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test97(self):
        input = """func main() { a := Person{name: "John", age: 30}; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(Id("a"),
                    StructLiteral("Person", [("name", StringLiteral('"John"')), ("age", IntLiteral(30))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test98(self):
        input = """func main() { a.b.c := 5; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(FieldAccess(FieldAccess(Id("a"), "b"), "c"), IntLiteral(5))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test99(self):
        input = """func main() { a.b[2] := 3; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(ArrayCell(FieldAccess(Id("a"), "b"), [IntLiteral(2)]), IntLiteral(3))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test100(self):
        input = """func main() { a.b[1] := 3; };"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(),
            Block([
                Assign(ArrayCell(FieldAccess(Id("a"), "b"), [IntLiteral(1)]), IntLiteral(3))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

 