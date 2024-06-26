# Generated from QueryParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete listener for a parse tree produced by QueryParser.
class QueryParserListener(ParseTreeListener):

    # Enter a parse tree produced by QueryParser#query.
    def enterQuery(self, ctx:QueryParser.QueryContext):
        pass

    # Exit a parse tree produced by QueryParser#query.
    def exitQuery(self, ctx:QueryParser.QueryContext):
        pass


    # Enter a parse tree produced by QueryParser#expr.
    def enterExpr(self, ctx:QueryParser.ExprContext):
        pass

    # Exit a parse tree produced by QueryParser#expr.
    def exitExpr(self, ctx:QueryParser.ExprContext):
        pass


    # Enter a parse tree produced by QueryParser#fundamental.
    def enterFundamental(self, ctx:QueryParser.FundamentalContext):
        pass

    # Exit a parse tree produced by QueryParser#fundamental.
    def exitFundamental(self, ctx:QueryParser.FundamentalContext):
        pass


    # Enter a parse tree produced by QueryParser#boolProperty.
    def enterBoolProperty(self, ctx:QueryParser.BoolPropertyContext):
        pass

    # Exit a parse tree produced by QueryParser#boolProperty.
    def exitBoolProperty(self, ctx:QueryParser.BoolPropertyContext):
        pass



del QueryParser