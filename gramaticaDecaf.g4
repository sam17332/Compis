// Gramatica Decaf
grammar gramaticaDecaf;

fragment LETTER: ('a'..'z' | 'A' .. 'Z');
fragment DIGIT: '0' .. '9';
ID: LETTER (LETTER|DIGIT)*;
NUM: DIGIT (DIGIT)*;
CHAR: LETTER;
WS : [ \t\r\n]+ -> skip;

program: 'class' 'Program' '{' (declaration)* '}'
;
declaration: structDeclaration
    | varDeclaration
    | methodDeclaration
;
varDeclaration: varType ID ';'
    | varType ID '[' NUM ']' ';'
;
structDeclaration: 'struct' ID '{' (varDeclaration)* '}' ';'
;
varType: 'int'
    |'char'
    | 'boolean'
    | 'struct' ID
    | structDeclaration
    | 'void'
;
methodDeclaration: methodType ID '(' (parameter (',')? )* ')' block
;
methodType: 'int'
    | 'char'
    | 'boolean'
    | 'void'
;
parameter: parameterType (ID)?
    | parameterType ID '[' ']'
;
parameterType: 'int'
    | 'char'
    | 'boolean'
    | 'void'
;
block: '{' (varDeclaration)* (statement)* '}';
statement: 'if' '(' expression ')' block ('else' block)?
    | 'while' '(' expression ')' block
    | 'return' (expression)? ';'
    | methodCall ';'
    | block
    | location '=' expression
    | (expression)? ';'
;
location: (ID | ID '[' expression ']') ('.' location)?;
expression: location
    | methodCall
    | literal
    | expression op expression
    | '-' expression
    | '!' expression
    | '(' expression ')'
;
methodCall: ID '(' (arg (',')?)* ')'
;
arg: expression
;
op: arith_op
    | rel_op
    | eq_op
    | cond_op
;
arith_op: '*'
    | '/'
    | '+'
    | '-'
    | '%'
;
rel_op: '<'
    | '>'
    | '<='
    | '>='
;
eq_op: '=='
    | '!='
;
cond_op: '&&'
    | '||'
;
literal: int_literal
    | char_literal
    | bool_literal
;
int_literal: NUM
;
char_literal: '"' CHAR '"'
;
bool_literal: 'true'
    | 'false'
;