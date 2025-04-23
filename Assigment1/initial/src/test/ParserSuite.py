import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test201(self):
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test202(self):
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test203(self):
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test204(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test205(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test206(self):
        self.assertTrue(TestParser.checkParser("const tam = 1;","successful", 206))
    def test207(self):
        self.assertTrue(TestParser.checkParser("const _123 = true;","successful",207 ))
    def test208(self):
        self.assertTrue(TestParser.checkParser("const khai = [5][0]string{1, \"string\"};","successful", 208))
    def test209(self):
        self.assertTrue(TestParser.checkParser("const tam = [0.]ID{1, 3};","Error on line 1 col 14: 0.", 209))
    def test210(self):
        self.assertTrue(TestParser.checkParser("const tam2 = People{name: \"Nam\", age: 30};","successful", 210))
    def test211(self):
        self.assertTrue(TestParser.checkParser("const _23kh = 1 || 2 && c - 3 / 2 - -1;","successful", 211))
    def test212(self):
        self.assertTrue(TestParser.checkParser("const tienkhai =  foo2()[5] + ID[7].name.age;","successful", 212))
    def test213(self):
        self.assertTrue(TestParser.checkParser("const _khai = t.foo(12,45) + b.c[7].age;","successful", 213))
    def test214(self):
        self.assertTrue(TestParser.checkParser("const _tienkhai = a.test.foo();","successful", 214))
    def test215(self):
        self.assertTrue(TestParser.checkParser("""
            var x1 float = foo() + 3 / 4;
            var y = "Hello" / 4
            var z People;
        ""","successful", 215))
    def test216(self):
        self.assertTrue(TestParser.checkParser("""
            const _sdfjceioe = a.arr[2].b(23,45,test) + 2;
        ""","successful", 216))
    def test217(self):
        self.assertTrue(TestParser.checkParser("""
            func walk(x int, y int) int {}
            func gow() [2][3] ID {}
            func wack() {}
        ""","successful", 217))
    def test218(self):
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) people(x int) int {}
            func (c Calculator) _(c walk) ID {}
            func (c Calculator) test(x int, y [2]VoTien) {}
        ""","successful", 218))
    def test219(self):
        self.assertTrue(TestParser.checkParser("""
            type people struct {
                name string ;
                age [1][3]people ;
            }
        ""","successful", 219))
    def test220(self):
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {           
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()                 
                SayHello(name string);                 
            }
            type _ interface {
                test();
            }
            ""","successful", 220))
    def test221(self):
        self.assertTrue(TestParser.checkParser("""
            func wake() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;
                var z str;                   
                const tam = a.b() + 2;
            }
        ""","successful", 221))
    def test222(self):
        self.assertTrue(TestParser.checkParser("""
            func quack(x int) {
                x  := a.name + 3 / 4;
                x.c[2][0] := 1 + 2;
            }
        ""","successful", 222))
    def test223(self):
        self.assertTrue(TestParser.checkParser("""
            func If() {
                if (x > 1) {}
                if (x == 10) {
                } else if (x >= 10) {
                    var tam = 23.;
                } else {
                    var z ID;
                }
            }
        ""","successful", 223))
    def test224(self):
        self.assertTrue(TestParser.checkParser("""
            func tam() {
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
            }
        ""","successful", 224))
    def test225(self):
        self.assertTrue(TestParser.checkParser("""
            func test() {
                for i < 10 {break;}
                break;
                continue;
                return a;
                return                
                foo(2 + x, 4 / y); m.goo();
             }                            
        ""","successful", 225))
    def test226(self):
        self.assertTrue(TestParser.checkParser("""
            const b = 0B10;
        ""","successful", 226))
    def test227(self):
        self.assertTrue(TestParser.checkParser("""    
            var z people 1;                         
        ""","Error on line 2 col 26: 1", 227))
    def test228(self):
        self.assertTrue(TestParser.checkParser("""
            var y _1234 = ID {a 4};
        ""","Error on line 2 col 30: {", 228))
    def test229(self):
        self.assertTrue(TestParser.checkParser("""    
            var m tam = float{1};                         
        ""","Error on line 2 col 25: float", 229))
    def test230(self):
        self.assertTrue(TestParser.checkParser("""
            var z test = ID.name;
        ""","successful", 230))
    def test231(self):
        self.assertTrue(TestParser.checkParser("""
            var z khanh = [2]int{};
        ""","Error on line 2 col 27: [", 231))
    def test232(self):
        self.assertTrue(TestParser.checkParser("""
            func Add(x int, y int) int {} ;
        """, "successful", 232))
    def test234(self):
        self.assertTrue(TestParser.checkParser("""
            var z khanh = ID {a: };
        ""","Error on line 2 col 30: {", 234))
    def test235(self):
        self.assertTrue(TestParser.checkParser("""
            var z _1van = a >= 2 <= "string" > a[2][3];
        ""","successful",235 ))
    def test236(self):
        self.assertTrue(TestParser.checkParser("""
            var z People = a[2][3][a + 2];
        """, "successful",236 ))
    def test237(self):
        self.assertTrue(TestParser.checkParser("""
            var z Walky = a[2, 3];
        ""","Error on line 2 col 30: ,", 237))
    def test238(self):
        self.assertTrue(TestParser.checkParser("""
            var z testi = a.b.a[2].foo();
        ""","successful",238))
    def test239(self):
        self.assertTrue(TestParser.checkParser("""
            var c [2][3]ID
        ""","successful",   239 ))
    def test240(self):
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {}
        """, "Error on line 2 col 21: int",  240))
    def test241(self):
        """Tests a function declaration"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {}
        """, "successful", 241))
    def test242(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                const a = a[2].b;
                var a = a[2].b; var a = "s";
            }
        """, "successful", 242))
    
    def test243(self):
        self.assertTrue(TestParser.checkParser("""
            type metquaroi struct {
                test string ;
                metghe [1][3]VoTien ;                     
            }
            var temp = 12                                                                      
        ""","successful", 243))

    def test244(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type khai struct {
                tien string ;       
            }                                                                       
        ""","successful", 244))

    def test245(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                
                Subtract(a, b float, c int) [3]ID;
                Reset()         
                SayHello(name string);
                                        
            }
        ""","successful", 245))

    def test246(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", 246))


    def test247(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", 247))

    def test248(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func van() {
                if (x > 10) {} 
                if (x > 10) {
                  
                } else if (x == 10) {
                    var z str;
                } 
            }
        ""","successful", 248))

    def test249(self):
        self.assertTrue(TestParser.checkParser("""    
            func khai() {
                for _, value := range array {}
            }
        ""","successful", 249))


    def test250(self):
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;                     
             }
                                        
        ""","successful", 250))
    def test251(self):
        self.assertTrue(TestParser.checkParser("""    
            func example() {
                return;
                return 1;
                return "Hello";
            }
        ""","successful", 251))
    def test252(self):
        self.assertTrue(TestParser.checkParser("""
            func compute() {
                var x = foo(bar(3, test()), 5);
            }
        ""","successful", 252))
    def test253(self):
        self.assertTrue(TestParser.checkParser("""
            func compute() {
                var x = foo(,);
            }
        ""","Error on line 3 col 29: ,", 253))
    def test254(self):
        self.assertTrue(TestParser.checkParser("""
            var arr [2][3]ID{}
        ""","Error on line 2 col 29: {", 254))
    def test255(self):
        self.assertTrue(TestParser.checkParser("""
            type Data struct {
                name string;
                scores [5]float;
                metadata [2][3]int;
            }
        ""","successful", 255))
    def test256(self):
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string
                age int
            }
        ""","successful", 256))
    def test257(self):
        self.assertTrue(TestParser.checkParser("""
            type EmptyInterface interface {
                diachi string;                   
            }
        ""","Error on line 3 col 24: string", 257))
    def test258(self):
        self.assertTrue(TestParser.checkParser("""
            type Logger interface {
                Log(message string);
            }
        ""","successful", 258))
    def test259(self):
        self.assertTrue(TestParser.checkParser("""
            type WrongType struct {
                data unknownType;
            }
        ""","successful", 259))
    def test260(self):
        self.assertTrue(TestParser.checkParser("""
            func empty() {}
        ""","successful", 260))
    def test261(self):
        """Test missing closing brace"""
        self.assertTrue(TestParser.checkParser("""
            func broken() {
                var x int = 10;
        ""","Error on line 4 col 9: <EOF>", 261))

    def test262(self):
        """Test for loop with missing range"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for _, value := range {}
            }
        ""","Error on line 3 col 39: {", 262))

    def test263(self):
        """Test while-like for loop"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for x < 100 {
                    x = x + 1;
                }
            }
        ""","Error on line 4 col 23: =", 263))

    def test264(self):
        self.assertTrue(TestParser.checkParser("""
            func checkValue() {
                switch x {
                    case 1: return;
                    case 2: return;
                    default: return;
                }
            }
        ""","Error on line 3 col 24: x", 264))

    def test265(self):
        self.assertTrue(TestParser.checkParser("""
            var person = Person{name: "John", age: 25};
        ""","Error on line 2 col 32: {", 265))

    def test266(self):
        self.assertTrue(TestParser.checkParser("""
            var person = Person{name: "Alice"};
        ""","Error on line 2 col 32: {", 266))

    def test267(self):
        self.assertTrue(TestParser.checkParser("""
            var person = Person{"Alice", 30};
        ""","Error on line 2 col 32: {", 267))

    def test268(self):
        """Test logical operators"""
        self.assertTrue(TestParser.checkParser("""
            const result = true && false || !flag;
        ""","successful", 268))

    def test269(self):
        self.assertTrue(TestParser.checkParser("""
            const x 10;
        ""","Error on line 2 col 21: 10", 269))

    def test270(self):
        """Test array initialization"""
        self.assertTrue(TestParser.checkParser("""
            var arr = [3]int{1, 2, 3};
        ""","Error on line 2 col 23: [", 270))

    def test271(self):
        """Test 2D array initialization"""
        self.assertTrue(TestParser.checkParser("""
            var matrix = [2][3]int{{1, 2, 3}, {4, 5, 6}};
        ""","Error on line 2 col 26: [", 271))

    def test272(self):
        """Test invalid array index"""
        self.assertTrue(TestParser.checkParser("""
            var x = arr[1.5];
        ""","successful", 272))

    def test273(self):
        """Test function returning struct"""
        self.assertTrue(TestParser.checkParser("""
            func getPerson() Person {
                return Person{name: "Alice", age: 30};
            }
        ""","Error on line 3 col 30: {", 273))

    def test274(self):
        self.assertTrue(TestParser.checkParser("""
            func getNumbers() [5]int {
                return [5]int{1, 2, 3, 4, 5};
            }
        ""","Error on line 3 col 24: [", 274))

    def test275(self):
        """Test nested function calls"""
        self.assertTrue(TestParser.checkParser("""
            func compute() {
                var result = f1(f2(3, f3(4, 5)));
            }
        ""","successful", 275))

    def test276(self):
        """Test binary operations"""
        self.assertTrue(TestParser.checkParser("""
            var x = 10 + 20 * 3 - 5 / 2;
        ""","successful", 276))

    def test277(self):
        """Test function without parameters"""
        self.assertTrue(TestParser.checkParser("""
            func hello() {
                print("Hello, world!");
            }
        ""","successful", 277))

    def test278(self):
        """Test function with multiple parameters"""
        self.assertTrue(TestParser.checkParser("""
            func add(a int, b int) int {
                return a + b;
            }
        ""","successful", 278))

    def test279(self):
        """Test variable shadowing"""
        self.assertTrue(TestParser.checkParser("""
            func shadow() {
                var x = 10;
                {
                    var x = 20;
                }
            }
        ""","Error on line 4 col 17: {", 279))

    def test280(self):
        """Test complex nested structures"""
        self.assertTrue(TestParser.checkParser("""
            type Company struct {
                name string;
                employees [10]Person;
            }
        ""","successful", 280))
    def test281(self):
        input = """func bar () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test282(self):
        input = """func start({};"""
        expect = "Error on line 1 col 12: {"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test283(self):
        input = """var float;"""
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test284(self):
        input = """var x ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test285(self):
        self.assertTrue(TestParser.checkParser("const data = 10;", "successful", 285))

    def test286(self):
        self.assertTrue(TestParser.checkParser("const _test = false;", "successful", 286))

    def test287(self):
        self.assertTrue(TestParser.checkParser("const arr = [3][1]string{5, \"hello\"};", "successful", 287))

    def test288(self):
        self.assertTrue(TestParser.checkParser("const x = [1.]ID{2, 3};", "Error on line 1 col 12: 1.", 288))

    def test289(self):
        self.assertTrue(TestParser.checkParser("const person = User{name: \"Alice\", age: 25};", "successful", 289))

    def test290(self):
        self.assertTrue(TestParser.checkParser("const val = 3 && 5 || y - 2 / 1 - -4;", "successful", 290))

    def test291(self):
        self.assertTrue(TestParser.checkParser("const result = compute()[8] + Node[3].value.id;", "successful", 291))

    def test292(self):
        self.assertTrue(TestParser.checkParser("const expr = funcCall(10,20) + x.y[6].attr;", "successful", 292))

    def test293(self):
        self.assertTrue(TestParser.checkParser("const sample = b.process.run();", "successful", 293))
    def test294(self):
        input = """var myVar string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test295(self):
        input = """var array [5]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test296(self):
        input = """const check = [2][2]float{1.5, 2.5, 3.5, 4.5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test297(self):
        input = """const matrix = [0.][1]int{10};"""
        expect = "Error on line 1 col 17: 0."
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test298(self):
        input = """func calculate(x int, y int) int { return x + y; };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test299(self):
        input = """func processData() { var x = getValue() + 4 / 2; };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test300(self):
        input = """type Data struct { name string; values [3]int; };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test301(self):
        input = """type Shape interface { Area() float; Perimeter() float }"""
        expect = "Error on line 1 col 56: }"
        self.assertTrue(TestParser.checkParser(input, expect, 301))



   