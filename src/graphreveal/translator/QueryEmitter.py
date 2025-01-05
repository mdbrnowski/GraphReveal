from antlr4.tree.Tree import TerminalNodeImpl

from graphreveal.translator import QueryParser, QueryParserListener

BOOL_PROPERTY_MAP = {
    QueryParser.ACYCLIC: "acyclic = TRUE",
    QueryParser.BIPARTITE: "bipartite = TRUE",
    QueryParser.COMPLETE: "vertices * (vertices - 1) / 2 = edges",
    QueryParser.CONNECTED: "components = 1",
    QueryParser.EULERIAN: "eulerian = TRUE",
    QueryParser.HAMILTONIAN: "hamiltonian = TRUE",
    QueryParser.NO_ISOLATED_V: "degree_min > 0",
    QueryParser.PLANAR: "planar = TRUE",
    QueryParser.TREE: "acyclic = TRUE AND components = 1",
}


class QueryEmitter(QueryParserListener):
    def __init__(self):
        self.conditions: list[str] = []

    def get_result(self) -> str:
        return "SELECT * FROM graphs WHERE " + " AND ".join(self.conditions)

    def enterQuery(self, ctx: QueryParser.QueryContext):
        self.conditions.clear()

    def enterExpr(self, ctx: QueryParser.ExprContext):
        if (
            isinstance(ctx.children[0], TerminalNodeImpl)
            and ctx.children[0].symbol.type == QueryParser.NOT
        ):
            self.conditions.append("NOT ")
        else:
            self.conditions.append("")

    def enterBoolProperty(self, ctx: QueryParser.BoolPropertyContext):
        child = ctx.children[0]
        self.conditions[-1] += BOOL_PROPERTY_MAP[child.symbol.type]

    def enterNumEntityExpr(self, ctx: QueryParser.NumEntityExprContext):
        num = ctx.children[0].symbol.text
        entity = ctx.children[1].children[0]
        if entity.symbol.type == QueryParser.VERTEX:
            self.conditions[-1] += f"vertices = {num}"
        if entity.symbol.type == QueryParser.EDGE:
            self.conditions[-1] += f"edges = {num}"
        if entity.symbol.type == QueryParser.BLOCK:
            self.conditions[-1] += f"blocks = {num}"
        if entity.symbol.type == QueryParser.COMPONENT:
            self.conditions[-1] += f"components = {num}"
