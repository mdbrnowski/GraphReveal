// $antlr-format alignTrailingComments true, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0, alignSemicolons ownLine
// $antlr-format alignColons trailing, singleLineOverrulesHangingColon true, alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar QueryLexer;

WHITESPACE: [ \t\r\n]+ -> skip;

INTEGER: [0-9]+;

SCOLON: ';';

NOT: 'not' | '!';

VERTEX : 'vertex' | 'vertices' | 'vertexes' | 'verts' | 'V';
EDGE   : 'edge' | 'edges' | 'E';

ACYCLIC   : 'acyclic';
BIPARTITE : 'bipartite';
COMPLETE  : 'complete';
CONNECTED : 'connected';
EULERIAN  : 'eulerian' | 'euler';
PLANAR    : 'planar';