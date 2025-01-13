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
    : numEntityProperty     # simpleExpr
    | boolProperty          # simpleExpr
    | NOT numEntityProperty # notExpr
    | NOT boolProperty      # notExpr
    ;

numEntityProperty
    : INTEGER entity
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