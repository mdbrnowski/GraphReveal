from antlr4.tree.Tree import ParseTree, TerminalNodeImpl, ErrorNodeImpl, TerminalNode, INVALID_INTERVAL
from graph_reveal_tools.translator import QueryParser, QueryParserListener


class QueryEmitter(QueryParserListener):
    def __init__(self):
        self.conditions: list[str] = []

    def get_result(self):
        return "SELECT * FROM graphs WHERE " + " AND ".join(self.conditions)

    def enterQuery(self, ctx: QueryParser.QueryContext):
        self.conditions.clear()

    def enterExpr(self, ctx: QueryParser.ExprContext):
        if isinstance(ctx.children[0], TerminalNodeImpl) and ctx.children[0].symbol.type == QueryParser.NOT:
            self.conditions.append("NOT ")
        else:
            self.conditions.append("")

    def enterBoolProperty(self, ctx: QueryParser.BoolPropertyContext):
        child = ctx.children[0]
        if child.symbol.type == QueryParser.ACYCLIC:
            self.conditions[-1] += "acyclic = TRUE"
        if child.symbol.type == QueryParser.BIPARTITE:
            self.conditions[-1] += "bipartite = TRUE"
        if child.symbol.type == QueryParser.COMPLETE:
            self.conditions[-1] += "vertices * (vertices - 1) / 2 = edges"
        if child.symbol.type == QueryParser.CONNECTED:
            self.conditions[-1] += "components = 1"
        if child.symbol.type == QueryParser.EULERIAN:
            self.conditions[-1] += "eulerian = TRUE"
        if child.symbol.type == QueryParser.HAMILTONIAN:
            self.conditions[-1] += "hamiltonian = TRUE"
        if child.symbol.type == QueryParser.NO_ISOLATED_V:
            self.conditions[-1] += "degree_min > 0"
        if child.symbol.type == QueryParser.PLANAR:
            self.conditions[-1] += "planar = TRUE"
        if child.symbol.type == QueryParser.TREE:
            self.conditions[-1] += "acyclic = TRUE AND components = 1"

    def enterNumEntityExpr(self, ctx: QueryParser.NumEntityExprContext):
        num = ctx.children[0].symbol.text
        entity = ctx.children[1].children[0]
        if entity.symbol.type == QueryParser.VERTEX:
            self.conditions[-1] += f"vertices = {num}"
        if entity.symbol.type == QueryParser.EDGE:
            self.conditions[-1] += f"edges = {num}"
        if entity.symbol.type == QueryParser.COMPONENT:
            self.conditions[-1] += f"components = {num}"
