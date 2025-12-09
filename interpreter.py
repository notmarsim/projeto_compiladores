from antlr4 import *
from FootprinterLexer import FootprinterLexer
from FootprinterParser import FootprinterParser

from modules import *

mem = {}

def eval_node(t):
    match t:

        case FootprinterParser.ProgramContext():
            for s in t.statement():
                eval_node(s)
            return

        case FootprinterParser.StatementContext():
            if t.getChildCount() > 0:
                eval_node(t.getChild(0))
            return

        case FootprinterParser.AssignStmtContext():

            name = t.NAME(0).getText()
            if t.IP():
                value = t.IP().getText()
            elif t.WORDLIST():
                value = t.WORDLIST().getText()
            elif t.functionCall():
                value = eval_node(t.functionCall())
            else:
                value = t.getChild(2).getText()
            mem[name] = value
            return value

        case FootprinterParser.FuncCallStmtContext():
            return eval_node(t.functionCall())

        case FootprinterParser.FunctionCallContext():
            func = t.NAME().getText()
            args = [eval_node(a) for a in t.funcArgs().expr()]
            if func not in globals():
                raise Exception(f"função '{func}' não encontrada")
            return globals()[func](*args)

        case FootprinterParser.ForStmtContext():
            itVar = t.NAME(0).getText()
            listVar = t.NAME(1).getText()
            if listVar not in mem:
                raise Exception(f"variável '{listVar}' não definida")
            for value in mem[listVar]:
                mem[itVar] = value
                eval_node(t.block())
            return

        case FootprinterParser.CaseStmtContext():
            if eval_node(t.condition()):
                eval_node(t.block())
            return

        case FootprinterParser.ConditionContext():
            left = eval_node(t.expr(0))
            right = eval_node(t.expr(1))
            op = t.cmpOp().getText()
            return (left == right) if op == "==" else \
                   (left != right) if op == "!=" else \
                   (left in right) if op == "in" else False

        case FootprinterParser.ExprContext():
            if t.NAME():   return mem.get(t.NAME().getText(), t.NAME().getText())
            if t.IP():     return t.IP().getText()
            if t.NUMBER(): return int(t.NUMBER().getText())

        case FootprinterParser.BlockContext():
            for s in t.statement():
                eval_node(s)
            return

    raise Exception(f"[ERRO] interpretando -> {t.getText()}")


def run(code):
    lexer = FootprinterLexer(InputStream(code))
    parser = FootprinterParser(CommonTokenStream(lexer))
    eval_node(parser.program())
