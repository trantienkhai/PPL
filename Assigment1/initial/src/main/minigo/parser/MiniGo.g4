//2211560
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
lastTokenType = None

def emit(self):
    tk = self.type

    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        emitted_token = super().emit()
        self.lastTokenType = emitted_token.type  # Update lastTokenType here
        return emitted_token
}
options{
	language=Python3;
}

//3.3.2 Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//3.3.3 Operators
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN_DECL: ':=';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
LESS: '<';
GREATER: '>';
DOT: '.';

//3.3.4 Separators
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI:';';

// 3.3.5 Literals
fragment DECIMAL: '0' | [1-9][0-9]*;
fragment BINARY: '0b' [01]+ | '0B' [01]+;
fragment OCTAL: '0o' [0-7]+ | '0O' [0-7]+;
fragment HEX: '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+;
fragment ESC: '\\' [tnr"\\]; 
INTLIT: DECIMAL | BINARY | OCTAL | HEX;
FLOATLIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;
STRINGLIT: '"' ( ~["\\\r\n] | ESC )* '"';

//3.2 Comment
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

//3.3.1 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;


program : (declare)* EOF ;
main_function : FUNC 'main' LPAREN RPAREN block SEMI ;
declare : variable_declaration | constant_declaration | type_declaration | function_declaration| method_declare | quick_decl;
variable_declaration : VAR ID (type_specifier ASSIGN expression1 | type_specifier | ASSIGN expression1) SEMI;
constant_declaration : CONST ID ASSIGN (expression1|arrayLiteral|structLiteral) SEMI;
type_declaration : TYPE ID struct_declaration SEMI | TYPE ID interface_declaration SEMI;
struct_declaration : STRUCT LBRACE struct_field+ RBRACE ;
struct_field : ID type_specifier SEMI;
interface_declaration : INTERFACE LBRACE interface_method+ RBRACE ;
interface_method : ID LPAREN parameter_list? RPAREN  type_specifier? SEMI;
parameter_list : parameter (COMMA parameter)* ;
parameter : ID (COMMA ID)* type_specifier ; 
function_declaration : main_function | (FUNC ID LPAREN parameter_list? RPAREN type_specifier? block SEMI);
type_specifier : INT
               | FLOAT
               | BOOLEAN
               | STRING
               | ID               
               | LBRACK (INTLIT|ID) RBRACK type_specifier ;  
method_declare: FUNC LPAREN ID ID RPAREN ID LPAREN parameter_list? RPAREN type_specifier? block SEMI;
quick_decl: ID ASSIGN_DECL (arrayLiteral | structLiteral) SEMI;
arrayLiteral: LBRACK (INTLIT | ID) RBRACK type_specifier LBRACE expressionlist RBRACE;
structLiteral: ID LBRACE structField (COMMA structField)* RBRACE | ID LBRACE RBRACE;  
structField: ID ':' expression1;


//Statement
statement : assignment_statement SEMI
          | if_statement SEMI
          | for_statement SEMI
          | break_statement SEMI 
          | continue_statement SEMI
          | call_statement SEMI
          | return_statement SEMI;
        
assignment_statement : (ID | array_access | struct_access) assignment_operator expression1 ;
assignment_operator : ASSIGN_DECL 
                    | ADD_ASSIGN 
                    | SUB_ASSIGN 
                    | MUL_ASSIGN 
                    | DIV_ASSIGN 
                    | MOD_ASSIGN ;
if_statement : IF LPAREN expression1 RPAREN block else_clause? ;
else_clause : ELSE (if_statement | block) ;
for_statement : FOR for_condition block ;
for_condition : expression1
              | (variable_declaration | assignment_statement SEMI) expression1 SEMI assignment_statement
              | ID COMMA ID ASSIGN_DECL RANGE ID ;
break_statement : BREAK ;
continue_statement : CONTINUE ;
call_statement : function_call | method_call | builtin_function_call ;
builtin_function_call : builtin_function_name LPAREN expressionlist? RPAREN ;
builtin_function_name : 'getInt'
                      | 'putInt'
                      | 'putIntLn'
                      | 'getFloat'
                      | 'putFloat'
                      | 'putFloatLn'
                      | 'getBool'
                      | 'putBool'
                      | 'putBoolLn'
                      | 'getString'
                      | 'putString'
                      | 'putStringLn'
                      | 'putLn' ;
return_statement : RETURN expression1? ;
block : LBRACE (statement|declare)* RBRACE;


//Expressions
expressionlist: expression1 (COMMA expression1)*;
expression1: expression1 OR expression2 | expression2;
expression2: expression2 AND expression3 | expression3;
expression3: expression3 (EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) expression4 | expression4;
expression4: expression4 (PLUS | MINUS) expression5 | expression5;
expression5: expression5 (MULT | DIV | MOD) expression6 | expression6;
expression6: (NOT | MINUS) expression6 | expression7;
expression7: operand | array_access | struct_access | method_call | function_call | LPAREN expression1 RPAREN;
array_access: ID (LBRACK expression1 RBRACK)+;
struct_access : primary1 struct_tail ;
struct_tail : DOT ID struct_tail
            | LBRACK expression1 RBRACK struct_tail
            | ;
primary1 : ID | function_call ;
method_call : primary DOT ID LPAREN expressionlist? RPAREN ;
primary : ID
        | function_call
        | struct_access ;
function_call: ID LPAREN expressionlist? RPAREN;
operand: literal | ID;
literal: INTLIT | FLOATLIT | STRINGLIT | TRUE | FALSE | NIL;


WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING: '"' (~["\\\r\n] | ESC)* ('\r'?'\n' | EOF)
{
    text_without_newline = self.text[:-1] if self.text[-1] in ['\n', '\r'] else self.text;
    raise UncloseString(text_without_newline.strip("\n\r"));
};

NEWLINE:'\n' {
            if self.lastTokenType in { 
                self.ID, self.INTLIT, self.FLOATLIT, self.BOOLEAN, self.STRINGLIT, 
                self.INT, self.FLOAT, self.STRING, 
                self.RETURN, self.CONTINUE, self.BREAK, 
                self.RPAREN, self.RBRACK, self.RBRACE,
                self.TRUE, self.FALSE
            }:
                self.lastTokenType = self.SEMI;
                self.text = ";";
                self.type = self.SEMI;
            else:
                self.skip();  
        };


// UNCLOSE_STRING: '"' (~["\\\r\n] | ESC)* ('\r'?'\n' | EOF)
// {
//     raise UncloseString(self.text[1:])
// };
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESC)* '\\' ~[tnr"\\]
{
    raise IllegalEscape(self.text)
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
