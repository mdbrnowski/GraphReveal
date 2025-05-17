# GraphReveal

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/graphreveal)](https://pypi.org/project/graphreveal/)
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

This process should take less than two seconds and will create a database of graphs with an order no greater than 7. To use a larger database, add the `--n 8` or `--n 9` flag to this command (it should take no more than half an hour).

### Some examples

```shell
graphreveal search "10 edges, bipartite, no isolated vertices, 2 components"
```

```shell
graphreveal search --count "5..6 vertices, connected"
```

Without `--count`, this command will print a list of graphs in [graph6](https://users.cecs.anu.edu.au/~bdm/data/formats.html) format. You can use [houseofgraphs.org](https://houseofgraphs.org/draw_graph) to visualize them.

### List of available properties

* [N] `vertices` (alternatives: `verts`,`V`, `nodes`)
* [N] `edges` (alternative: `E`)
* [N] `blocks` (alternative: `biconnected components`)
* [N] `components` (alternative: `C`)
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

As [N], you can use a simple number or range (e.g., `3-4`, `3..4`, `< 5`, `>= 2`).
You can also negate any property using `!` or `not`.
