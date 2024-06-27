# GraphReveal

The beginnings of what may one day be a graph database search system.

## Generate parser and lexer yourself

Your should have [ANTLR 4](https://www.antlr.org/) installed.

```shell
cd parser
antlr4 -o generated -Dlanguage=Python3 QueryLexer.g4
antlr4 -o generated -Dlanguage=Python3 QueryParser.g4
```