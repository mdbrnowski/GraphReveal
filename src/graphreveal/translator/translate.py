from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from graphreveal import ParsingError
from graphreveal.translator import QueryLexer, QueryParser, QueryTranslator


class QueryErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol:
            length = offendingSymbol.stop - offendingSymbol.start + 1
        elif isinstance(recognizer, QueryLexer):
            length = len(msg.split("recognition error at: ")[1]) - 2
        else:  # this should not happen
            raise AssertionError("length of this error cannot be determined")
        length = max(1, length)
        self.errors.append((line, column, length))


def translate(input_text: str, print_parse_tree: bool = False) -> str:
    """Translates natural language query to SQL beginning with `SELECT * `"""
    lexer = QueryLexer(InputStream(input_text))
    parser = QueryParser(CommonTokenStream(lexer))

    lexer.removeErrorListeners()
    lexer_error_listener = QueryErrorListener()
    lexer.addErrorListener(lexer_error_listener)

    parser.removeErrorListeners()
    parser_error_listener = QueryErrorListener()
    parser.addErrorListener(parser_error_listener)

    tree = parser.query()
    if print_parse_tree:
        print(tree.toStringTree(recog=parser))

    if lexer_error_listener.errors:
        raise ParsingError("Your query is invalid", lexer_error_listener.errors)

    if parser_error_listener.errors:
        raise ParsingError("Your query is invalid", parser_error_listener.errors)

    translator = QueryTranslator()
    return "SELECT * FROM graphs WHERE " + translator.visit(tree)
