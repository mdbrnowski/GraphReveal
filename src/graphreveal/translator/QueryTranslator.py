from graphreveal.translator import QueryParser, QueryParserVisitor

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

NUM_ENTITY_PROPERTY_MAP = {
    QueryParser.VERTEX: "vertices",
    QueryParser.EDGE: "edges",
    QueryParser.BLOCK: "blocks",
    QueryParser.COMPONENT: "components",
}


class QueryTranslator(QueryParserVisitor):
    def visitQuery(self, ctx: QueryParser.QueryContext) -> str:
        return " AND ".join(
            [self.visit(ctx.expr(i)) for i in range(ctx.getChildCount() // 2)]
        )

    def visitSimpleExpr(self, ctx: QueryParser.SimpleExprContext):
        return self.visitChildren(ctx)

    def visitNotExpr(self, ctx: QueryParser.NotExprContext):
        return "NOT " + self.visitChildren(ctx)

    def visitNumEntityProperty(self, ctx: QueryParser.NumEntityPropertyContext):
        num = ctx.INTEGER().getText()
        entity = self.visit(ctx.entity())
        return NUM_ENTITY_PROPERTY_MAP[entity] + " = " + num

    def visitEntity(self, ctx: QueryParser.EntityContext):
        return ctx.getChild(0).symbol.type

    def visitBoolProperty(self, ctx: QueryParser.BoolPropertyContext):
        return BOOL_PROPERTY_MAP[ctx.getChild(0).symbol.type]