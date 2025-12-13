from antlr4 import *
from FootprinterLexer import FootprinterLexer
from FootprinterParser import FootprinterParser

from modules import *


dec = []
def analyze(t):
    global dec
    match t:

        case FootprinterParser.ProgramContext():
            for s in t.statement():
                analyze(s)
            return

        case FootprinterParser.StatementContext():
            analyze(t.getChild(0))
            return

        case FootprinterParser.FuncCallStmtContext():
            return analyze(t.functionCall())

        case FootprinterParser.BlockContext():
            for s in t.statement():
                analyze(s)
            return
        
        case FootprinterParser.CaseStmtContext():
            if analyze(t.condition()):
                analyze(t.block())
            return

        case FootprinterParser.ConditionContext():
            analyze(t.expr(0))
            analyze(t.expr(1))
            return 
        
        case FootprinterParser.AssignStmtContext():
            name = t.NAME(0).getText()
            if name in dec:
                raise Exception(f'Variável {name} já foi declarada')
            if t.functionCall():
                analyze(t.functionCall())
            dec += [name]
            return
        
        case FootprinterParser.FunctionCallContext():
            func = t.NAME().getText()
            [analyze(a) for a in t.funcArgs().expr()]
            if func not in globals():
                raise Exception(f"função '{func}' não encontrada")
            return

        case FootprinterParser.ForStmtContext():
            listVar = t.NAME(1).getText()
            if listVar not in dec:
                raise Exception(f"variável '{listVar}' não definida")
            return

        case FootprinterParser.ExprContext():
            if t.NAME() and not t.NAME().getText() in dec:
                raise Exception(f'Variável {t.NAME().getText()} não foi declarada')
            return

    raise Exception(f"[ERRO] interpretando -> {t.getText()}")


def run(code):
    lexer = FootprinterLexer(InputStream(code))
    parser = FootprinterParser(CommonTokenStream(lexer))
    analyze(parser.program())
