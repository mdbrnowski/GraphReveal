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
    : INTEGER fundamental
    | NOT? boolProperty
    ;

fundamental
    : VERTEX
    | EDGE
    ;

boolProperty
    : ACYCLIC
    | BIPARTITE
    | COMPLETE
    | CONNECTED
    | EULERIAN
    | HAMILTONIAN
    | PLANAR
    ;