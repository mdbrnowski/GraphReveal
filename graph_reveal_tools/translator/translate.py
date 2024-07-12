from antlr4 import *
from graph_reveal_tools.translator import QueryLexer, QueryParser, QueryEmitter


def translate(input_text, print_parse_tree=False):
    lexer = QueryLexer(InputStream(input_text))
    parser = QueryParser(CommonTokenStream(lexer))
    tree = parser.query()

    if print_parse_tree:
        print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()
    translator = QueryEmitter()
    walker.walk(translator, tree)

    return translator.get_result()
