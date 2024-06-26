from antlr4.tree.Tree import ParseTree, TerminalNodeImpl, ErrorNodeImpl, TerminalNode, INVALID_INTERVAL
from generated.QueryParser import QueryParser
from generated.QueryParserListener import QueryParserListener


class QueryTranslator(QueryParserListener):
    result = ""

    def enterQuery(self, ctx: QueryParser.QueryContext):
        self.result += "SELECT * FROM graphs WHERE TRUE"

    def enterExpr(self, ctx: QueryParser.ExprContext):
        self.result += " AND "
        if isinstance(ctx.children[0], TerminalNodeImpl) and ctx.children[0].symbol.type == QueryParser.NOT:
            self.result += "NOT "

    def enterBoolProperty(self, ctx: QueryParser.BoolPropertyContext):
        for child in ctx.children:
            if child.symbol.type == QueryParser.ACYCLIC:
                self.result += "acyclic = TRUE"
            if child.symbol.type == QueryParser.BIPARTITE:
                self.result += "bipartite = TRUE"
            if child.symbol.type == QueryParser.CONNECTED:
                self.result += "components = 1"
            if child.symbol.type == QueryParser.EULERIAN:
                self.result += "eulerian = TRUE"
            if child.symbol.type == QueryParser.PLANAR:
                self.result += "planar = TRUE"
