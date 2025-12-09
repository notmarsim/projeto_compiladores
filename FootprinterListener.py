# Generated from Footprinter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FootprinterParser import FootprinterParser
else:
    from FootprinterParser import FootprinterParser

# This class defines a complete listener for a parse tree produced by FootprinterParser.
class FootprinterListener(ParseTreeListener):

    # Enter a parse tree produced by FootprinterParser#program.
    def enterProgram(self, ctx:FootprinterParser.ProgramContext):
        pass

    # Exit a parse tree produced by FootprinterParser#program.
    def exitProgram(self, ctx:FootprinterParser.ProgramContext):
        pass


    # Enter a parse tree produced by FootprinterParser#statement.
    def enterStatement(self, ctx:FootprinterParser.StatementContext):
        pass

    # Exit a parse tree produced by FootprinterParser#statement.
    def exitStatement(self, ctx:FootprinterParser.StatementContext):
        pass


    # Enter a parse tree produced by FootprinterParser#condition.
    def enterCondition(self, ctx:FootprinterParser.ConditionContext):
        pass

    # Exit a parse tree produced by FootprinterParser#condition.
    def exitCondition(self, ctx:FootprinterParser.ConditionContext):
        pass


    # Enter a parse tree produced by FootprinterParser#expr.
    def enterExpr(self, ctx:FootprinterParser.ExprContext):
        pass

    # Exit a parse tree produced by FootprinterParser#expr.
    def exitExpr(self, ctx:FootprinterParser.ExprContext):
        pass


    # Enter a parse tree produced by FootprinterParser#cmpOp.
    def enterCmpOp(self, ctx:FootprinterParser.CmpOpContext):
        pass

    # Exit a parse tree produced by FootprinterParser#cmpOp.
    def exitCmpOp(self, ctx:FootprinterParser.CmpOpContext):
        pass


    # Enter a parse tree produced by FootprinterParser#assignStmt.
    def enterAssignStmt(self, ctx:FootprinterParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by FootprinterParser#assignStmt.
    def exitAssignStmt(self, ctx:FootprinterParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by FootprinterParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:FootprinterParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by FootprinterParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:FootprinterParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by FootprinterParser#functionCall.
    def enterFunctionCall(self, ctx:FootprinterParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by FootprinterParser#functionCall.
    def exitFunctionCall(self, ctx:FootprinterParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by FootprinterParser#funcArgs.
    def enterFuncArgs(self, ctx:FootprinterParser.FuncArgsContext):
        pass

    # Exit a parse tree produced by FootprinterParser#funcArgs.
    def exitFuncArgs(self, ctx:FootprinterParser.FuncArgsContext):
        pass


    # Enter a parse tree produced by FootprinterParser#forStmt.
    def enterForStmt(self, ctx:FootprinterParser.ForStmtContext):
        pass

    # Exit a parse tree produced by FootprinterParser#forStmt.
    def exitForStmt(self, ctx:FootprinterParser.ForStmtContext):
        pass


    # Enter a parse tree produced by FootprinterParser#caseStmt.
    def enterCaseStmt(self, ctx:FootprinterParser.CaseStmtContext):
        pass

    # Exit a parse tree produced by FootprinterParser#caseStmt.
    def exitCaseStmt(self, ctx:FootprinterParser.CaseStmtContext):
        pass


    # Enter a parse tree produced by FootprinterParser#block.
    def enterBlock(self, ctx:FootprinterParser.BlockContext):
        pass

    # Exit a parse tree produced by FootprinterParser#block.
    def exitBlock(self, ctx:FootprinterParser.BlockContext):
        pass



del FootprinterParser