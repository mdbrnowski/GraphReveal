from antlr4.tree.Tree import ParseTree, TerminalNodeImpl, ErrorNodeImpl, TerminalNode, INVALID_INTERVAL
from graph_reveal_tools.translator import QueryParser, QueryParserListener


class QueryEmitter(QueryParserListener):
    result = ""

    def get_result(self):
        return self.result

    def enterQuery(self, ctx: QueryParser.QueryContext):
        self.result += "SELECT * FROM graphs WHERE TRUE"

    def enterExpr(self, ctx: QueryParser.ExprContext):
        self.result += " AND "
        if isinstance(ctx.children[0], TerminalNodeImpl) and ctx.children[0].symbol.type == QueryParser.NOT:
            self.result += "NOT "

    def enterBoolProperty(self, ctx: QueryParser.BoolPropertyContext):
        child = ctx.children[0]
        if child.symbol.type == QueryParser.ACYCLIC:
            self.result += "acyclic = TRUE"
        if child.symbol.type == QueryParser.BIPARTITE:
            self.result += "bipartite = TRUE"
        if child.symbol.type == QueryParser.COMPLETE:
            self.result += "vertices * (vertices - 1) / 2 = edges"
        if child.symbol.type == QueryParser.CONNECTED:
            self.result += "components = 1"
        if child.symbol.type == QueryParser.EULERIAN:
            self.result += "eulerian = TRUE"
        if child.symbol.type == QueryParser.HAMILTONIAN:
            self.result += "hamiltonian = TRUE"
        if child.symbol.type == QueryParser.NO_ISOLATED_V:
            self.result += "degree_min > 0"
        if child.symbol.type == QueryParser.PLANAR:
            self.result += "planar = TRUE"
        if child.symbol.type == QueryParser.TREE:
            self.result += "acyclic = TRUE AND components = 1"

    def enterNumEntityExpr(self, ctx: QueryParser.NumEntityExprContext):
        num = ctx.children[0].symbol.text
        entity = ctx.children[1].children[0]
        if entity.symbol.type == QueryParser.VERTEX:
            self.result += f"vertices = {num}"
        if entity.symbol.type == QueryParser.EDGE:
            self.result += f"edges = {num}"
        if entity.symbol.type == QueryParser.COMPONENT:
            self.result += f"components = {num}"
