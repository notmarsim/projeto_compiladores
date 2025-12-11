grammar Footprinter;


COLON : ':' ;
NAME   : [a-zA-Z_][a-zA-Z0-9_]* ;
WORDLIST: ('/'NAME('-'NAME)?)+ '.txt';
IP     : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ ;
NUMBER : [0-9]+ ;
SPACE   : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;

program
    : statement* EOF
    ;

statement
    : assignStmt ';'
    | funcCallStmt ';'
    | forStmt
    | caseStmt
    | block
    ;

condition
    : expr cmpOp expr
    ;

expr
    : NAME
    | IP
    | NUMBER
    ;

cmpOp
    : '==' | '!=' | 'in'
    ;

// host: 127.0.0.1;
assignStmt
    : NAME COLON (IP | functionCall | NAME | NUMBER | WORDLIST | list)
    ;

// scan_tcp(host);
funcCallStmt
    : functionCall 
    ;

functionCall
    : NAME '(' funcArgs ')'
    ;

funcArgs
    : expr (',' expr)*
    ;

// for port in openports { ... }
forStmt
    : 'for' NAME 'in' NAME block
    ;

// case (port == dns) { ... }
caseStmt
    : 'case' '(' condition ')' block
    ;

block
    : '{' statement* '}'
    ;

list
    : '[' val+=NUMBER (','val+=NUMBER)* ']'
    | '[' val+=NAME (','val+=NAME)* ']'
    | '[' val+=WORDLIST (','val+=WORDLIST)* ']'
    | '[' val+=IP (','val+=IP)* ']'
    ;