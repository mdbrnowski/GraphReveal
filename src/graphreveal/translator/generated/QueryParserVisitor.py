# Generated from QueryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryParser#query.
    def visitQuery(self, ctx:QueryParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#simpleExpr.
    def visitSimpleExpr(self, ctx:QueryParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#notExpr.
    def visitNotExpr(self, ctx:QueryParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#numEntityProperty.
    def visitNumEntityProperty(self, ctx:QueryParser.NumEntityPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#halfOpenRange.
    def visitHalfOpenRange(self, ctx:QueryParser.HalfOpenRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#closedRange.
    def visitClosedRange(self, ctx:QueryParser.ClosedRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#entity.
    def visitEntity(self, ctx:QueryParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#boolProperty.
    def visitBoolProperty(self, ctx:QueryParser.BoolPropertyContext):
        return self.visitChildren(ctx)



del QueryParser