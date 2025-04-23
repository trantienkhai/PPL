import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test400(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test401(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test402(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test403(self):
        input = Program([
        FuncDecl("foo", [], IntType(), Block([])),
        FuncDecl("foo", [], FloatType(), Block([]))
        ])
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test404(self):
        input = Program([
        FuncDecl("getInt", [], IntType(), Block([])),
        FuncDecl("foo", [], VoidType(), Block([]))
        ])
        expect = "Redeclared Function: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test405(self):
        input = Program([
            FuncDecl("foo", [
                ParamDecl("x", IntType()),
                ParamDecl("x", FloatType()) 
            ], IntType(), Block([]))
        ])
        expect = "Redeclared Parameter: x\n"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test406(self):
        input = Program([
            StructType("Point", [
                ("x", IntType()),
                ("x", FloatType())
            ], [])
        ])
        expect = "Redeclared Field: x\n"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test407(self):
        input = Program([
            InterfaceType("I", [
                Prototype("foo", [], IntType()),
                Prototype("foo", [], FloatType())
            ])
        ])
        expect = "Redeclared Prototype: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test408(self):
        input = Program([
            StructType("Point", [("x", IntType())], []),
            StructType("Point", [("y", FloatType())], [])
        ])
        expect = "Redeclared Type: Point\n"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test409(self):
        input = Program([
            InterfaceType("Printable", [
                Prototype("print", [], VoidType())
            ]),
            InterfaceType("Printable", [
                Prototype("display", [], VoidType())
            ]) 
        ])
        expect = "Redeclared Type: Printable\n"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test410(self):
        input = Program([
            StructType("Entity", [("id", IntType())], []),
            InterfaceType("Entity", [
                Prototype("getId", [], IntType())
            ])  
        ])
        expect = "Redeclared Type: Entity\n"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test411(self):
        input = Program([
            ConstDecl("x", IntType(), BinaryOp("+", Id("y"), IntLiteral(1)))
        ])
        expect = "Undeclared Identifier: y\n"
        self.assertTrue(TestChecker.test(input, expect, 411))


    # def test411(self):
    #     input = Program([
    #         ConstDecl("y", None, BinaryOp("+", BinaryOp("/", FloatLiteral(3.5), IntLiteral(1)), BooleanLiteral(True))),
    #         ConstDecl("x", None, BinaryOp("+", Id("y"), IntLiteral(9)))
    #         # ConstDecl("y", None, IntLiteral(123)),

    #     ])
    #     expect = "Undeclared Identifier: y\n"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    def test412(self):
        input = Program([
            StructType("Entity", [("id", IntType())], []),
            ConstDecl("y", None, StructLiteral("Entity", [('id',IntLiteral(1))])),
            # ConstDecl("x", None, BinaryOp("+", Id(""), IntLiteral(9)))
            # ConstDecl("y", None, IntLiteral(123)),

        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test413(self):
        input = Program([VarDecl("arr",ArrayType([IntLiteral(1)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(1)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 413))
    


    def test414(self):
        input = Program([
            VarDecl("arr",
            ArrayType([IntLiteral(2), IntLiteral(2)], IntType()),
            ArrayLiteral([IntLiteral(2), IntLiteral(3)], IntType(), [
            [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
            [IntLiteral(4), IntLiteral(5), IntLiteral(6)]
        ])
                    )
                ])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2),IntLiteral(2)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType,[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test415(self):
        input = Program([
            VarDecl("arr",
                ArrayType([IntLiteral(2), IntLiteral(2)], IntType()),
                ArrayLiteral([IntLiteral(2)], IntType(), [
                    [IntLiteral(1), IntLiteral(2)],
                    [IntLiteral(3), IntLiteral(4)]
                ])
            )
        ])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2),IntLiteral(2)]),ArrayLiteral([IntLiteral(2)],IntType,[[IntLiteral(1),IntLiteral(2)],[IntLiteral(3),IntLiteral(4)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test416(self):
        input = Program([
            VarDecl("arr",
                ArrayType([IntLiteral(1)], IntType()),
                ArrayLiteral([IntLiteral(1)], FloatType(), [
                   [IntLiteral(1)],
                ])
            )
        ])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(1)]),ArrayLiteral([IntLiteral(1)],FloatType,[[IntLiteral(1)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test417(self):
        input = Program([
            ConstDecl("n", None, IntLiteral(3)),
            VarDecl("arr",
                ArrayType([Id("n")], IntType()),
                ArrayLiteral([IntLiteral(2)], IntType(), [
                    [IntLiteral(1), IntLiteral(2)]
                ])
            ),
            ConstDecl("x", None, BinaryOp("+", Id("y"), IntLiteral(1)))
        ])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[Id(n)]),ArrayLiteral([IntLiteral(2)],IntType,[[IntLiteral(1),IntLiteral(2)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test418(self):
        input = Program([
            ConstDecl("n", None, IntLiteral(2)),
            VarDecl("arr",
                ArrayType([Id("n")], IntType()),
                ArrayLiteral([IntLiteral(2)], IntType(), [
                    [IntLiteral(1), IntLiteral(2)]
                ])
            ),
            ConstDecl("x", None, BinaryOp("+", Id("y"), IntLiteral(1)))
        ])
        expect = "Undeclared Identifier: y\n"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test418(self):
        input = Program([
            ConstDecl("n", None, IntLiteral(2)),
            VarDecl("arr",
                ArrayType([Id("n")], IntType()),
                ArrayLiteral([IntLiteral(2)], IntType(), [
                    [IntLiteral(1), IntLiteral(2)]
                ])
            ),
            VarDecl("a",IntType(),Id("arr")),
            
        ])
        expect = "Type Mismatch: VarDecl(a,IntType,Id(arr))\n"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test419(self):
        input = Program([
            ConstDecl("n", None, IntLiteral(2)),
            VarDecl("arr",
                ArrayType([Id("n")], IntType()),
                ArrayLiteral([IntLiteral(2)], IntType(), [
                    [IntLiteral(1), IntLiteral(2)]
                ])
            ),
            VarDecl("a",IntType(),Id("arr")),
            
        ])
        expect = "Type Mismatch: VarDecl(a,IntType,Id(arr))\n"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test420(self):
        input = Program([
            FuncDecl("foo", [ParamDecl("x", IntType()), ParamDecl("x", FloatType())], VoidType(), Block([]))
        ])
        expect = "Redeclared Parameter: x\n"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test421(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                ConstDecl("x", None, IntLiteral(10)),
                VarDecl("y", BoolType() , Id("x"))
            ]))
        ])
        expect = "Type Mismatch: VarDecl(y,BoolType,Id(x))\n"  
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test422(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                VarDecl("x", IntType(), IntLiteral(20))  
            ]))
        ])
        expect = "Redeclared Variable: x\n"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test423(self):
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                ConstDecl("x", IntType(), IntLiteral(10)),
                Return(StringLiteral("abc"))
            ]))
        ])
        expect = "Type Mismatch: Return(StringLiteral(abc))\n"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test424(self):
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                Return(IntLiteral(123))  
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test425(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                Return(IntLiteral(10))  
            ]))
        ])
        expect = "Type Mismatch: Return(IntLiteral(10))\n"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test426(self):
        input = Program([
            StructType("S", [], []),
            MethodDecl("s", Id("S"),
                FuncDecl("m", [], IntType(),
                    Block([]))),
            MethodDecl("s", Id("S"),
                FuncDecl("m", [], IntType(),
                    Block([])))
        ])
        expect = "Redeclared Method: m\n"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test427(self):
        input = Program([
            StructType("A", [], []),
            MethodDecl("a", Id("A"),
                FuncDecl("foo", [
                    ParamDecl("x", IntType()),
                    ParamDecl("x", FloatType())
                ], VoidType(), Block([])))
        ])
        expect = "Redeclared Parameter: x\n"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test428(self):
        input = Program([
            StructType("Point", [("x", IntType())], []),
            MethodDecl("p", Id("Point"),
                FuncDecl("x", [], IntType(),
                    Block([
                        Return(FieldAccess(Id("p"), "x"))
                    ])))
        ])
        expect = "Redeclared Method: x\n"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test429(self):
        input = Program([
            StructType("Calc", [("val", IntType())], []),
            MethodDecl("c", Id("Calc"),
                FuncDecl("add", [ParamDecl("c", IntType())], IntType(),
                    Block([
                        Return(BinaryOp("+", FieldAccess(Id("c"), "val"), Id("x")))
                    ])))
        ])
        expect = "Type Mismatch: FieldAccess(Id(c),val)\n"
        self.assertTrue(TestChecker.test(input, expect, 429))


    def test430(self):
        input = Program([
            StructType("Thing", [], []),
            MethodDecl("t", Id("Thing"),
                FuncDecl("check", [], VoidType(),
                    Block([
                        VarDecl("a", IntType(), Id("b"))  
                    ])))
        ])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test431(self):
        input = Program([
            FuncDecl("foo", [], IntType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("foo", [])
            ]))
        ])
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test432(self):
        input = Program([
            FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("foo", []) 
            ]))
        ])
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test433(self):
        input = Program([
            FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("foo", [FloatLiteral(3.5)])
            ]))
        ])
        expect = "Type Mismatch: FuncCall(foo,[FloatLiteral(3.5)])\n"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test434(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("bar", []) 
            ]))
        ])
        expect = "Undeclared Function: bar\n"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test435(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([])),
            VarDecl("foo", IntType(), None),
            FuncDecl("main", [], VoidType(), Block([]))
        ])
        expect = "Redeclared Variable: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test436(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"),
                FuncDecl("getX", [ParamDecl("a", IntType())], IntType(), 
                    Block([Return(FieldAccess(Id("self"), "x"))]))
            ),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", Id("A"), None),
                    MethCall(Id("a"), "getX", [])  
                ])
            )
        ])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test437(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"),
                FuncDecl("setX", [ParamDecl("val", IntType())], VoidType(), 
                    Block([]))
            ),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", Id("A"), None),
                    MethCall(Id("a"), "setX", [StringLiteral("abc")])  
                ])
            )
        ])
        expect = "Type Mismatch: MethodCall(Id(a),setX,[StringLiteral(abc)])\n"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test438(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"),
                FuncDecl("getX", [], IntType(), 
                    Block([Return(FieldAccess(Id("self"), "x"))]))
            ),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", Id("A"), None),
                    MethCall(Id("a"), "getX", []) 
                ])
            )
        ])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test439(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"),
                FuncDecl("getX", [], IntType(), 
                    Block([Return(FieldAccess(Id("self"), "x"))]))
            ),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", IntType(), IntLiteral(5)),
                    MethCall(Id("a"), "getX", [])
                ])
            )
        ])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test440(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"),
                FuncDecl("setX", [ParamDecl("val", IntType())], VoidType(), 
                    Block([]))
            ),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", Id("A"),None),
                    MethCall(Id("a"), "unknown", [])
                ])
            )
        ])
        expect = "Undeclared Method: unknown\n"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test441(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            FuncDecl("main", [], VoidType(), 
                Block([
                    VarDecl("a", Id("A"), None),
                    MethCall(Id("a"), "getX", [])
                ])
            ),
            MethodDecl("self", Id("A"),
                FuncDecl("getX", [], VoidType(), 
                    Block([Return(FieldAccess(Id("self"), "x"))]))
            )
        ])
        expect = "Undeclared Method: getX\n"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test442(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            StructType("B", [("x", Id("A") )], []),
             MethodDecl("self", Id("A"),
                FuncDecl("getX", [], VoidType(), 
                    Block([]))
            ),
            FuncDecl("main", [], VoidType(),
                Block([
                    VarDecl("a", Id("A"), None),
                    VarDecl("b", Id("B"), None),
                    MethCall(Id("a"), "getX", []),
                    MethCall(Id("b"), "getX", []),
                    
                ])
            )
        ])
        expect = "Undeclared Method: getX\n"
        self.assertTrue(TestChecker.test(input, expect, 442))


    def test443(self):
        input = Program([
            Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))
        ])
        expect = "Undeclared Identifier: x\n"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test444(self):
        input = Program([
            VarDecl("f", FloatType(), None),
            Assign(Id("f"), StringLiteral("hello"))
        ])
        expect = "Type Mismatch: Assign(Id(f),StringLiteral(hello))\n"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test445(self):
        input = Program([
            VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), None),
            Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), StringLiteral('"hi"'))
        ])
        expect = """Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(0)]),StringLiteral("hi"))\n"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test446(self):
        input = Program([
            VarDecl("x", FloatType(), None),
            Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test447(self):
        input = Program([
            VarDecl("x", FloatType(), None),
            Assign(Id("x"), BinaryOp("+", Id("y"), IntLiteral(1)))
        ])
        expect = "Undeclared Identifier: y\n"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test448(self):
        input = Program([
            StructType("S", [("x", IntType())], []),
            VarDecl("s", Id("S"), None),
            Assign(FieldAccess(Id("s"), "y"), IntLiteral(5))
        ])
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test449(self):
        input = Program([
            StructType("S", [("x", IntType())], []),
            VarDecl("s", Id("S"), None),
            Assign(FieldAccess(Id("s"), "x"), FloatLiteral(3.14))
        ])
        expect = "Type Mismatch: Assign(FieldAccess(Id(s),x),FloatLiteral(3.14))\n"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test450(self):
        input = Program([
            VarDecl("a", IntType(), None),
            Assign(FieldAccess(Id("a"), "x"), IntLiteral(10))
        ])
        expect = "Type Mismatch: FieldAccess(Id(a),x)\n"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test451(self):
        input = Program([
            StructType("A", [("val", IntType())], []),
            MethodDecl("self", Id("A"), FuncDecl("get", [], IntType(), Block([
                Return(FieldAccess(Id("self"), "val"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", Id("A"), None),
                VarDecl("x", IntType(), None),
                Assign(Id("x"), MethCall(Id("a"), "get", []))
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test452(self):
        input = Program([
            FuncDecl("getValue", [], IntType(), Block([Return(IntLiteral(9))])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), FuncCall("getValue", []))
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test453(self):
        input = Program([
            StructType("A", [("val", BoolType())], []),
            MethodDecl("self", Id("A"), FuncDecl("get", [], BoolType(), Block([
                Return(FieldAccess(Id("self"), "val"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", Id("A"), None),
                VarDecl("x", IntType(), None),
                Assign(Id("x"), MethCall(Id("a"), "get", []))
            ]))
        ])
        expect = "Type Mismatch: Assign(Id(x),MethodCall(Id(a),get,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test454(self):
        input = Program([
            StructType("S", [("val", StringType())], []),
            MethodDecl("self", Id("S"), FuncDecl("getStr", [], StringType(), Block([
                Return(FieldAccess(Id("self"), "val"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("s", Id("S"), None),
                VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0), IntLiteral(2)]), MethCall(Id("s"), "getStr", []))
            ]))
        ])
        expect = "Type Mismatch: ArrayCell(Id(arr),[IntLiteral(0),IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test455(self):
        input = Program([
            StructType("S", [("val", StringType())], []),
            MethodDecl("self", Id("S"), FuncDecl("getStr", [], StringType(), Block([
                Return(FieldAccess(Id("self"), "val"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("s", Id("S"), None),
                VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), MethCall(Id("s"), "getStr", []))
            ]))
        ])
        expect = "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(0)]),MethodCall(Id(s),getStr,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test456(self):
        input = Program([
            FuncDecl("f", [], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), None),
                Assign(Id("a"), FuncCall("f", []))
            ]))
        ])
        expect = "Type Mismatch: Assign(Id(a),FuncCall(f,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test457(self):
        input = Program([
            FuncDecl("f", [], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), FuncCall("f", []))
            ]))
        ])
        expect = "Type Mismatch: Assign(Id(a),FuncCall(f,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test458(self):
        input = Program([
            FuncDecl("f", [], VoidType(), Block([])),
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), BinaryOp('+',IntLiteral(1) ,FuncCall("f", [])))
            ]))
        ])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),+,FuncCall(f,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test459(self):
        input = Program([
            FuncDecl("getValue", [], IntType(), Block([Return(IntLiteral(9))])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2),IntLiteral(2)]), FuncCall("getValue", []))
            ]))
        ])
        expect = "Type Mismatch: ArrayCell(Id(arr),[IntLiteral(2),IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test460(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                If(IntLiteral(1), Block([
                    VarDecl("x", IntType(), IntLiteral(5),)
                ]), None)
            ]))
        ])
        expect = "Type Mismatch: If(IntLiteral(1),Block([VarDecl(x,IntType,IntLiteral(5))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test461(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BooleanLiteral(True), Block([
                    VarDecl("x", IntType(), IntLiteral(5))
                ]), Block([
                    VarDecl("y", IntType(), IntLiteral(10))
                ]))
            ]))
        ])
        expect = ""  # Không có lỗi
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test462(self):
        input = Program([
            FuncDecl("main", [], VoidType(),
                Block([
                    If(BooleanLiteral(True),
                    Block([
                        VarDecl("x", IntType(), IntLiteral(1)),
                        VarDecl("x", IntType(), IntLiteral(2))
                    ]),
                    None)
                ])
            )
        ])
        expect = "Redeclared Variable: x\n"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test463(self):
        input = Program([
            FuncDecl("getValue", [], VoidType(), Block([Return(None)])),
            FuncDecl("main", [], VoidType(), Block([
                If(FuncCall("getValue",[]), Block([
                    VarDecl("x", IntType(), IntLiteral(5))
                ]), Block([
                    VarDecl("y", IntType(), IntLiteral(10))
                ]))
            ]))
        ])
        expect = "Type Mismatch: If(FuncCall(getValue,[]),Block([VarDecl(x,IntType,IntLiteral(5))]),Block([VarDecl(y,IntType,IntLiteral(10))]))\n"  # Không có lỗi
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test464(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                ForBasic(IntLiteral(1), Block([]))
            ]))
        ])
        expect = "Type Mismatch: For(IntLiteral(1),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test465(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                ForBasic(BinaryOp("<", IntLiteral(1), IntLiteral(2)), Block([
                    VarDecl("x", IntType(), IntLiteral(5))
                ]))
            ]))
        ])
        expect = ""  # Không có lỗi
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test466(self):
        input = Program([
            FuncDecl("f", [], IntType(), Block([
                Return(IntLiteral(1))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                ForBasic(BooleanLiteral(True), Block([
                    FuncCall("f", [])
                ]))
            ]))
        ])
        expect = "Type Mismatch: FuncCall(f,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test467(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("self", Id("A"), FuncDecl("getX", [], IntType(), Block([
                Return(FieldAccess(Id("self"), "x"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", Id("A"),None),
                ForBasic(BooleanLiteral(True), Block([
                    MethCall(Id("a"), "getX", [])
                ]))
            ]))
        ])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test468(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    IntLiteral(1),  
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([])
                )
            ]))
        ])
        expect = "Type Mismatch: For(Assign(Id(i),IntLiteral(0)),IntLiteral(1),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test469(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(5)),
                    Assign(Id("i"), StringLiteral('"hi"')), 
                    Block([])
                )
            ]))
        ])
        expect = "Type Mismatch: Assign(Id(i),StringLiteral(\"hi\"))\n"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test470(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                ForStep(
                    VarDecl("i", IntType(), IntLiteral(1)),  # lỗi: trùng tên trong cùng scope
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([])
                )
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test471(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                ForStep(
                    VarDecl("i", IntType(), IntLiteral(1)),  # lỗi: trùng tên trong cùng scope
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([VarDecl("i", IntType(), IntLiteral(0))])
                )
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    
    def test471(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                ForStep(
                    VarDecl("i", IntType(), IntLiteral(1)), 
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([VarDecl("i", IntType(), IntLiteral(0))])
                )
            ]))
        ])
        expect = "Redeclared Variable: i\n"
        self.assertTrue(TestChecker.test(input, expect, 471))
    

    def test472(self):
        input = Program([
            StructType("S", [("x", IntType())], []),
            VarDecl("s", Id("S"), None),
            Assign(FieldAccess(Id("s"), "x"), FloatLiteral(3.14))
        ])
        expect = "Type Mismatch: Assign(FieldAccess(Id(s),x),FloatLiteral(3.14))\n"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test473(self):
        input = Program([
            VarDecl("a", IntType(), None),
            Assign(FieldAccess(Id("a"), "x"), IntLiteral(10))
        ])
        expect = "Type Mismatch: FieldAccess(Id(a),x)\n"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test474(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("s", StringType(), StringLiteral('"hello"')),
                ForEach(
                    Id("i"),
                    Id("c"),
                    Id("s"),  # lỗi: s không phải array
                    Block([])
                )
            ]))
        ])
        expect = "Type Mismatch: ForEach(Id(i),Id(c),Id(s),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test475(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), ArrayLiteral([IntLiteral(2)], IntType(), [[IntLiteral(1), IntLiteral(2)]])),
                ForEach(
                    Id("i"),
                    Id("val"),
                    Id("arr"),  # arr có phần tử kiểu int
                    Block([
                        VarDecl("val", StringType(), StringLiteral('"oops"'))  # lỗi: val trùng tên và sai kiểu
                    ])
                )
            ]))
        ])
        expect = "Redeclared Variable: val\n"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test476(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), ArrayLiteral([IntLiteral(2)], IntType(), [[IntLiteral(1), IntLiteral(2)]])),
                ForEach(
                    Id("idx"),
                    Id("val"),
                    Id("arr"),
                    Block([
                        VarDecl("idx", IntType(), IntLiteral(0))  # lỗi: redeclared
                    ])
                )
            ]))
        ])
        expect = "Redeclared Variable: idx\n"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test477(self):
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("matrix", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
                ForEach(
                    Id("i"),
                    Id("row"),
                    Id("matrix"),  # OK: row sẽ có kiểu ArrayType([IntLiteral(3)], IntType())
                    Block([
                        VarDecl("x", IntType(), IntLiteral(0))
                    ])
                )
            ]))
        ])
        expect = ""  # Không lỗi
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_090(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 90))

    def test_091(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien\n"
        self.assertTrue(TestChecker.test(input, expect, 91))

    def test_092(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 92))

    def test_093(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 93))

    def test_094(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 94))

    def test_095(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 95))
        
    def test_096(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 96))

    def test_097(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 97))
        
    def test_098(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 98))

    def test_099(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 99))
    def test_100(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 100))


    def test_080(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 80))

    def test_081(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 81))

    def test_082(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 82))

    def test_083(self):
        input = Program([
            InterfaceType("VoTien", [
                Prototype("VoTien", [], VoidType()),
                Prototype("VoTien", [IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: VoTien\n"
        self.assertTrue(TestChecker.test(input, expect, 83))

    def test_084(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 84))

    def test_085(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                VarDecl("b", None, IntLiteral(1)),
                VarDecl("a", None, IntLiteral(1)),
                ConstDecl("a", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 85))

    def test_086(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                    Block([ConstDecl("a", None, IntLiteral(2))])
                )
            ]))
        ])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 86))

    def test_087(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 87))

    def test_088(self):
        input = Program([
            FuncDecl("Votien", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("Votien", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        expect = "Undeclared Function: foo_votine\n"
        self.assertTrue(TestChecker.test(input, expect, 88))

    def test_089(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien\n"
        self.assertTrue(TestChecker.test(input, expect, 89))


    def test_037(self):
        input = Program([
            MethodDecl("v", Id("TIEN"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            StructType("TIEN", [("Votien", IntType())], [])
        ])
        expect = "Redeclared Method: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 37))

    def test602(self):
        input = Program([
            InterfaceType("ICalc", [
                Prototype("calc", [IntType()], IntType())
            ]),
            StructType("BrokenCalc", [], [
                MethodDecl("self", Id("BrokenCalc"),
                    FuncDecl("calc", [], IntType(), Block([]))  # Sai: thiếu param
                )
            ]),
            VarDecl("a", Id("ICalc"), None),
            VarDecl("b", Id("BrokenCalc"),None),         
            Assign(Id("a"), Id("b"))                 

        ])
        expect = "Type Mismatch: VarDecl(a,Id(ICalc),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 602))













    








