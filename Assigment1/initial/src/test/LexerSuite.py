import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self): 
        input = """if(x + 1){
                }
                """ 
        expect = "if,(,x,+,1,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    def test2(self):
        input = "var_ Nil True False"
        expect = "var_,Nil,True,False,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test3(self):
        input = "_xinchao xin_chao ___"
        expect = "_xinchao,xin_chao,___,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test4(self):
        input = ".abc .0xyz"
        expect = ".,abc,.,0,xyz,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test5(self):
        input = "_0123 .1.23___2_345"
        expect = "_0123,.,1.23,___2_345,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test6(self):
        input = "intege boolene typer fore fo"
        expect = "intege,boolene,typer,fore,fo,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test7(self):
        input = "EOF Const Bool Nil"
        expect = "EOF,Const,Bool,Nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test8(self):
        input = "printf()"
        expect = "printf,(,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test9(self):
        input = "trueValue ranger break_up"
        expect = "trueValue,ranger,break_up,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test10(self):
        input = "12()abcba"
        expect = "12,(,),abcba,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    # test keywords
    def test11(self):
        input = """if else for return func type struct interface string int float boolean const var continue break range nil true false"""
        expect = """if,else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    #test integer literals, float literals
    def test12(self):
        input = "0 0123 456789"
        expect = "0,0,123,456789,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test13(self):
        input = "0b101 0B1100 0b0 0b 0B123 0b234"
        expect = "0b101,0B1100,0b0,0,b,0B1,23,0,b234,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test14(self):
        input = "0o7 0O12 0o777 0O 0o28"
        expect = "0o7,0O12,0o777,0,O,0o2,8,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test15(self):
        input = "0xA 0X1F 0xaBCdEF 0X"
        expect = "0xA,0X1F,0xaBCdEF,0,X,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test16(self):
        input = "123_456 0xA_B_C 0b1_0_1 0o7_2"
        expect = "123,_456,0xA,_B_C,0b1,_0_1,0o7,_2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test17(self):
        input = "3.14 0. 2.0e10"
        expect = "3.14,0.,2.0e10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test18(self):
        input = "1.2345e-4 5.678E+9"
        expect = "1.2345e-4,5.678E+9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test19(self):
        input = "42. .123 7.89E"
        expect = "42.,.,123,7.89,E,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test20(self):
        input = "9e3 6E-2 4.e5"
        expect = "9,e3,6,E,-,2,4.e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    #test string literals
    def test21(self):
        input = """ "Hello, my name is \\"Khai\\" and I love coding." """
        expect = """"Hello, my name is \\"Khai\\" and I love coding.",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test22(self):
        input = """ "First line\\nSecond line" """
        expect = """"First line\\nSecond line",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test23(self):
        input = """ "Hello\\tWorld" """
        expect = """"Hello\\tWorld",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test24(self):
        input = """ "This is a backslash: \\\\" """
        expect = """"This is a backslash: \\\\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test25(self):
        input = """ "Special characters: !@#$%^&*()_+-={}|[]:;" """
        expect = """"Special characters: !@#$%^&*()_+-={}|[]:;",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test26(self):
        input = """ "Price: $10.99" """
        expect = """"Price: $10.99",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test27(self):
        input = """ "It's a beautiful day!" """
        expect = """"It's a beautiful day!",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test28(self):
        input = """ "Path: C:\\\\Users\\\\Admin" """
        expect = """"Path: C:\\\\Users\\\\Admin",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test29(self):
        input = """ "Newline\\nTab\\tBackslash\\\\quote\\"" """
        expect = """"Newline\\nTab\\tBackslash\\\\quote\\"",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test30(self):
        input = """ "Code: if (x > 10) { return x; }" """
        expect = """"Code: if (x > 10) { return x; }",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    #test unclose string
    def test31(self):
        input = """ "Hello world """
        expect = """Unclosed string: "Hello world """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test32(self):
        input = """ "This string never ends """
        expect = """Unclosed string: "This string never ends """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test33(self):
        input = """ "C:Users " "Documents """
        expect = """"C:Users ",Unclosed string: "Documents """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test34(self):
        input = """ "abc"def"xinchao"_21a"234 """
        expect = """"abc",def,"xinchao",_21a,Unclosed string: "234 """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test35(self):
        input = """ "Testing escape sequence \\" """
        expect = """Unclosed string: "Testing escape sequence \\" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))
    def test36(self):
        input = """ "abc\\t\\r\\t\\r """
        expect = """Unclosed string: "abc\\t\\r\\t\\r """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    #test escape illigal
    def test37(self):
        input = """ "abcdefgh\\v" """
        expect = """Illegal escape in string: "abcdefgh\\v"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))
    def test38(self):
        input = """ "abcdefgh\\t \\r ikl\\m" """
        expect = """Illegal escape in string: "abcdefgh\\t \\r ikl\\m"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))
    def test39(self):
        input = """ "test\\n\\\\a\\a" """
        expect = """Illegal escape in string: "test\\n\\\\a\\a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))
    
    def test40(self):
        input = """ "abcde\\"\\r\\n\\abc" """
        expect = """Illegal escape in string: "abcde\\"\\r\\n\\a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))
    def test41(self):
        input = """ "\\\\\\\\\\.'"" """
        expect = """Illegal escape in string: "\\\\\\\\\\."""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))
    def test42(self):
        input = """ "\\\\\\." """
        expect = 'Illegal escape in string: "\\\\\\.'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))
    
    #test operators
    def test43(self):
        input = """+ - * / % == != <= < >= > && || ! := += /= -= *= %= = ."""
        expect = "+,-,*,/,%,==,!=,<=,<,>=,>,&&,||,!,:=,+=,/=,-=,*=,%=,=,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test44(self):
        input = """10589-1755 && 15-1264 > 11-167-19378 && -17-105-62"""
        expect = "10589,-,1755,&&,15,-,1264,>,11,-,167,-,19378,&&,-,17,-,105,-,62,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test45(self):
        input = """++--===/*=="""
        expect = "+,+,-,-=,==,/,*=,=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test46(self):
        input = """***==*=*=//*/%%"""
        expect = "*,*,*=,=,*=,*=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test47(self):
        input = """7%2325_11*4"""
        expect = "7,%,2325,_11,*,4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test48(self):
        input = """100 || 32 ->= -67 && 199 !!= 5"""
        expect = "100,||,32,-,>=,-,67,&&,199,!,!=,5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test49(self):
        input = """abcabc % 123 * 0 / 12 / 123 ijk"""
        expect = "abcabc,%,123,*,0,/,12,/,123,ijk,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test50(self):
        input = """a + 9 === 20 -> a = 11"""
        expect = "a,+,9,==,=,20,-,>,a,=,11,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test51(self):
        input = """a - 123 || 1675 + _+abc78 * 23 < 16_78 - 1 > 34 || 79"""
        expect = "a,-,123,||,1675,+,_,+,abc78,*,23,<,16,_78,-,1,>,34,||,79,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test52(self):
        input = """12312453 && -56756 - 435643 :=== 56"""
        expect = "12312453,&&,-,56756,-,435643,:=,==,56,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))
    def test53(self):
        input = """ ++a = 34 --> a = 35 """
        expect = """+,+,a,=,34,-,-,>,a,=,35,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))
    
    #test bool literals
    def test54(self):
        input = """ a = true || false """
        expect = """a,=,true,||,false,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))     
    def test55(self):
        input = """ b = true && c = true || d = false """
        expect = """b,=,true,&&,c,=,true,||,d,=,false,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))  

    #test  nil literals
    def test56(self):
        input = "nil"
        expect = "nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test57(self):
        input = "x = nil; y = 10; z = nil"
        expect = "x,=,nil,;,y,=,10,;,z,=,nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    #test separators
    def test58(self):
        input = "( ) [ ] { } , ;"
        expect = "(,),[,],{,},,,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test59(self):
        input = "array[3] = {1, 2, 3};"
        expect = "array,[,3,],=,{,1,,,2,,,3,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test60(self):
        input = "(a + b) * {x, y} / z;"
        expect = "(,a,+,b,),*,{,x,,,y,},/,z,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    #test comments
    def test61(self):
        input = "// This is a single-line comment bla bla..."
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test62(self):
        input = "x == 50; // This is a comment"
        expect = "x,==,50,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test63(self):
        input = """
        // Comment 1
        // Comment 2
        x = 10;
        """
        expect = "x,=,10,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test64(self):
        input = "/* This is a block comment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test65(self):
        input = "/* int x1 = 10.56; */ float y = 5;"
        expect = "float,y,=,5,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test66(self):
        input = """ 
        /* 
        This is a 
        multi-line comment 
        /*another comment*/
        */
        float x = 20.;
        """
        expect = "float,x,=,20.,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test67(self):
        input = "z = /* ignored */ 15 + 3;"
        expect = "z,=,15,+,3,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test68(self):
        input = """ 
        /* Outer comment
        /* Nested comment */
        End of outer */
        var x = 30;
        """
        expect = "var,x,=,30,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test69(self):
        input = "/* Special characters: @#$%^&*()! */ const hang_so = 42;"
        expect = "const,hang_so,=,42,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test70(self):
        input = """ 
        /* This is a block comment
        // This is a single-line comment inside a block comment
        Still inside */
        return 100;
        """
        expect = "return,100,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    #test error_char
    def test71(self):
        input = "@"
        expect = "ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test72(self):
        input = "int tam = 3 + 5; #"
        expect = "int,tam,=,3,+,5,;,ErrorToken #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test73(self):
        input = "a = 5 @ 10"
        expect = "a,=,5,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test74(self):
        input = """
                //@#$%#$%$#
                ~"""
        expect = "ErrorToken ~"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test75(self):
        input = "int x = 10 $ y = 20"
        expect = "int,x,=,10,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test76(self):
        input = """ "sontung\\t\"\\n + "mtp" """
        expect =""""sontung\\t",ErrorToken \\"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test77(self):
        input = """ Hello  \\ \\\\world """
        expect = "Hello,ErrorToken \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test78(self):
        input = """x\\"y"""
        expect = "x,ErrorToken \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test79(self):
        input = "$^bffsfffsf^&"
        expect = "ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test80(self):
        input = "@ $ # ^ &"
        expect = "ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))
    
    #random
    def test81(self):
        self.assertTrue(TestLexer.checkLexeme("ab_sdfsd_sdfc_", "ab_sdfsd_sdfc_,<EOF>", 181))

    def test82(self):
        input = """ a:=array [5] of integer;
        /*
                    a = {1,2,3,4,5};*/"""
        expect = """a,:=,array,[,5,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))
    
    def test83(self):
        input = "cbad_"
        expect = "cbad_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))
    
    def test84(self):
        input = """ -3.4 7. 2.0e """
        expect = """-,3.4,7.,2.0,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test85(self):
        input = """ "Hello" 123 4.56 true """
        expect = """"Hello",123,4.56,true,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test86(self):
        input = """ + - * / % ////345kksmo56 """
        expect = """+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test87(self):
        input = "abvf?svn"
        expect = "abvf,ErrorToken ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test88(self):
        input = """ "     khaitran     " """
        expect = """"     khaitran     ",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test89(self):
        input = """ "\\r\\l " """
        expect = """Illegal escape in string: "\\r\\l"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test90(self):
        input = """ nil """
        expect = """nil,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test91(self):
        input = """ if else for while function return """
        expect = """if,else,for,while,function,return,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test92(self):
        input = """ function foo() { return 42; } """
        expect = """function,foo,(,),{,return,42,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test93(self):
        input = """ // """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test94(self):
        input = """ /* This is a 
        multi-line comment */ """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test95(self):
        input = """ int x for 
                xpskd"""
        expect = """int,x,for,xpskd,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test96(self):
        input = """ computer x int
                    science """
        expect = """computer,x,int,;,science,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test97(self):
        input = """ "abc_sdf\\q" """
        expect = """Illegal escape in string: "abc_sdf\\q"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test98(self):
        input = """ int a 56
                float b """
        expect = """int,a,56,;,float,b,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test99(self):
        input = """ =n-'i{3S"m-:Y;5?8<tb^"i91*?7GDZ^,12_91-192_716302:=flaoy;"""
        expect = """=,n,-,ErrorToken '"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test100(self):
        input = """ return break
                test 
                """
        expect = """return,break,;,test,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
    
    