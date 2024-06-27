// $antlr-format alignTrailingComments true, columnLimit 120, maxEmptyLinesToKeep 1, reflowComments false
// $antlr-format useTab false, allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0
// $antlr-format alignSemicolons ownLine, alignColons trailing, singleLineOverrulesHangingColon true
// $antlr-format alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar QueryLexer;

WHITESPACE: [ \t\r\n]+ -> skip;

INTEGER: [0-9]+;

SEPERATOR: ',' | ';';

NOT: 'not' | '!';

VERTEX    : 'vertex' | 'vertices' | 'vertexes' | 'verts' | 'V';
EDGE      : 'edge' | 'edges' | 'E';
COMPONENT : 'component' | 'components' | 'C';

ACYCLIC     : 'acyclic';
BIPARTITE   : 'bipartite';
COMPLETE    : 'complete';
CONNECTED   : 'connected';
EULERIAN    : 'eulerian' | 'euler';
HAMILTONIAN : 'hamiltonian' | 'hamilton';
PLANAR      : 'planar';