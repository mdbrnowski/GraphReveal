from antlr4 import *

from graph_reveal_tools.main import ParsingError
from graph_reveal_tools.translator import QueryLexer, QueryParser, QueryEmitter


def translate(input_text: str, print_parse_tree: bool = False) -> str:
    """ Translates natural language query to SQL beginning with `SELECT * ` """
    lexer = QueryLexer(InputStream(input_text))
    parser = QueryParser(CommonTokenStream(lexer))
    tree = parser.query()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise ParsingError('Your query is invalid')

    if print_parse_tree:
        print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()
    translator = QueryEmitter()
    walker.walk(translator, tree)

    return translator.get_result()
