from antlr4 import *
from generated.QueryLexer import QueryLexer
from generated.QueryParser import QueryParser
from QueryEmitter import QueryEmitter


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


if __name__ == '__main__':
    text = input("> ")
    print(translate(text, print_parse_tree=True))
