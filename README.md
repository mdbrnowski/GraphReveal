# GraphReveal

The beginnings of what may one day be a graph database search system.

## Installation

Clone the repository and run `pip install -e .` (with a dot at the end).

## Basic usage

```shell
graph-reveal search --count "6 vertices, connected"
```

Run `graph-reveal --help` for the full description. You can also use it in your Python script:

```python
from graph_reveal_tools.translator import translate

translate('6 vertices, connected, bipartite')
```

## Generate parser and lexer yourself

Your should have [ANTLR 4](https://www.antlr.org/) installed.

```shell
cd graph_reveal_tools/translator
antlr4 -o generated -Dlanguage=Python3 QueryLexer.g4
antlr4 -o generated -Dlanguage=Python3 QueryParser.g4
```