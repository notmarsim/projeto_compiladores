from antlr4 import *
from FootprinterLexer import FootprinterLexer
from FootprinterParser import FootprinterParser

from modules import *

mem = {}
code = []
indent = 0
def generate(t):
    global indent
    match t:

        case FootprinterParser.ProgramContext():
            code.append('from modules import *')
            for s in t.statement():
                generate(s)
  
            return code

        case FootprinterParser.StatementContext():
            generate(t.getChild(0))
            return

        case FootprinterParser.AssignStmtContext():
            
            name = t.NAME(0).getText()
            value = t.getChild(2).getText()
            
            if t.IP() or t.WORDLIST():
                value = '"'+t.getChild(2).getText()+'"'
            elif t.list_():
                value = [
                    int(v.text) if v.text.isnumeric()
                    else v.text
                    for v in t.list_().val
                ]
            else:
                value = t.getChild(2).getText()
       
            code.append(f'{name} = {value}')
            for _ in range(indent):
                code[-1] ='    ' + code[-1]
            return

        case FootprinterParser.FuncCallStmtContext():
            code.append(f'{t.getText()}')
            for _ in range(indent):
                code[-1] ='    ' + code[-1]
            return 

        case FootprinterParser.ForStmtContext():
            itVar = t.NAME(0).getText()
            listVar = t.NAME(1).getText()
            code.append(f'for {itVar} in {listVar}:')
            for _ in range(indent):
                code[-1] ='    ' + code[-1]
            generate(t.block()) 
            return

        case FootprinterParser.CaseStmtContext():
            generate(t.condition())
            generate(t.block())
            return

        case FootprinterParser.ConditionContext():
            
            left = t.expr(0).getText()
            right = t.expr(1).getText()
            op = t.cmpOp().getText()

            code.append(f'if {left} {op} {right} or {left}[1] {op} {right}:')
            for _ in range(indent):
                code[-1] ='    ' + code[-1]

            return 

        case FootprinterParser.BlockContext():
            indent+=1
            for s in t.statement():
                generate(s)
            indent-=1
            return
        
    return 



def run(code):
    lexer = FootprinterLexer(InputStream(code))
    parser = FootprinterParser(CommonTokenStream(lexer))
    print('--CODIGO GERADO--')
    [print(l) for l in generate(parser.program())]
    print('-----------------')
    print('\n')