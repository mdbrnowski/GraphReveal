// $antlr-format alignTrailingComments true, columnLimit 120, minEmptyLines 1, maxEmptyLinesToKeep 1
// $antlr-format reflowComments false, useTab false, allowShortRulesOnASingleLine false
// $antlr-format allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar QueryParser;

options {
    tokenVocab = QueryLexer;
}

query
    : expr (SEPERATOR expr)* EOF
    ;

expr
    : entityProperty     # simpleExpr
    | boolProperty       # simpleExpr
    | NOT entityProperty # notExpr
    | NOT boolProperty   # notExpr
    ;

entityProperty
    : INTEGER entity                        # numEntityProperty
    | op = LESS INTEGER entity              # halfOpenRange
    | op = GREATER INTEGER entity           # halfOpenRange
    | op = LESS_OR_EQUAL INTEGER entity     # halfOpenRange
    | op = GREATER_OR_EQUAL INTEGER entity  # halfOpenRange
    | INTEGER RANGE_OPERATOR INTEGER entity # closedRange
    ;

entity
    : VERTEX
    | EDGE
    | BLOCK
    | COMPONENT
    ;

boolProperty
    : ACYCLIC
    | BIPARTITE
    | COMPLETE
    | CONNECTED
    | CUBIC
    | EULERIAN
    | HAMILTONIAN
    | NO_ISOLATED_V
    | PLANAR
    | REGULAR
    | TREE
    ;