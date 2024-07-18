#!/usr/bin/env python3

import sqlite3
import networkx as nx
from . import util


def create_db():
    con = sqlite3.connect('../../graphs.db')
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS graphs")

    cur.execute(
        """ CREATE TABLE graphs (
                id VARCHAR(20) PRIMARY KEY,
                vertices INT NOT NULL,
                edges INT NOT NULL,
                acyclic BOOLEAN NOT NULL,
                bipartite BOOLEAN NOT NULL,
                eulerian BOOLEAN NOT NULL,
                hamiltonian BOOLEAN NOT NULL,
                planar BOOLEAN NOT NULL,
                blocks INT NOT NULL,
                components INT NOT NULL,
                degree_max INT NOT NULL,
                degree_min INT NOT NULL
            )"""
    )

    for n in range(1, 8):
        with open(f'data/graph{n}.g6', encoding='utf-8') as f:
            graphs_g6 = f.read().strip().split("\n")
        for graph_g6 in graphs_g6:
            graph = nx.from_graph6_bytes(str.encode(graph_g6))
            cur.execute(
                "INSERT INTO graphs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [
                    graph_g6,
                    graph.number_of_nodes(),
                    graph.number_of_edges(),
                    nx.is_forest(graph),
                    nx.is_bipartite(graph),
                    nx.is_eulerian(graph),
                    util.is_hamiltonian(graph),
                    nx.is_planar(graph),
                    len(list(nx.biconnected_components(graph))),
                    nx.number_connected_components(graph),
                    max(d for _, d in graph.degree()),
                    min(d for _, d in graph.degree()),
                ],
            )

    con.commit()
    con.close()


if __name__ == '__main__':
    create_db()
