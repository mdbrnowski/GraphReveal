# GraphReveal

[![PyPI - Version](https://img.shields.io/pypi/v/graphreveal)](https://pypi.org/project/graphreveal/)
[![Test](https://github.com/mdbrnowski/GraphReveal/actions/workflows/test.yml/badge.svg)](https://github.com/mdbrnowski/GraphReveal/actions/workflows/test.yml)

Have you ever needed an example of a graph that, e.g., is Hamiltonian, has exactly 8 vertices, and can be drawn on a plane without intersecting edges? Or wondered how many graphs of size 10 are bipartite, have no isolated vertices, and have exactly two components?

This package aims to answer some of your questions. You can search through all graphs with some reasonable order (currently 9 is the maximum) using a very simple DSL (*domain-specific language*).

## Installation

Make sure that you have Python in a sufficiently recent version. To install the package using `pip`, you can use the following command:

```shell
pip install graphreveal
```

## Basic usage

Firstly, you should create the database:

```shell
graphreveal create-database
```

This process should take less than two seconds and will create a database of graphs with an order no larger than 7. To use a larger database, add `--n 8` or `--n 9` flag to this command.

### Some examples

```shell
graphreveal search "10 edges, bipartite, no isolated vertices, 2 components"
```

```shell
graphreveal search --count "6 vertices, connected"
```

Without `--count`, this command will print a list of graphs in [graph6](https://users.cecs.anu.edu.au/~bdm/data/formats.html) format. You can use [houseofgraphs.org](https://houseofgraphs.org/draw_graph) to visualize them.

### List of available properties

* [int] `vertices` (alternatives: `verts`,`V`, `nodes`)
* [int] `edges` (alternative: `E`)
* [int] `blocks` (alternative: `biconnected components`)
* [int] `components` (alternative: `C`)
* `acyclic` (alternative: `forest`)
* `bipartite`
* `complete`
* `connected`
* `cubic` (alternative: `trivalent`)
* `eulerian` (alternative: `euler`)
* `hamiltonian` (alternative: `hamilton`)
* `no isolated vertices` (alternatives: `no isolated v`, `niv`)
* `planar`
* `regular`
* `tree`

You can also negate these properties using `!` or `not`.
