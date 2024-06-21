#!/usr/bin/env python3

import sqlite3
import networkx as nx

con = sqlite3.connect("graphs.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS graphs")

cur.execute(
    """ CREATE TABLE graphs (
            id VARCHAR(20) PRIMARY KEY,
            vertices INT NOT NULL,
            edges INT NOT NULL,
            connected BOOLEAN NOT NULL,
            acyclic BOOLEAN NOT NULL
        )"""
)

for n in range(2, 8):
    with open(f"data/graph{n}.g6", encoding="utf-8") as f:
        graphs_g6 = f.read().strip().split("\n")
    for graph_g6 in graphs_g6:
        graph = nx.from_graph6_bytes(str.encode(graph_g6))
        cur.execute(
            "INSERT INTO graphs VALUES (?, ?, ?, ?, ?)",
            [
                graph_g6,
                graph.number_of_nodes(),
                graph.number_of_edges(),
                nx.is_connected(graph),
                nx.is_forest(graph),
            ],
        )

con.commit()

con.close()
