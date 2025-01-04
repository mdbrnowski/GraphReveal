import os.path
import sqlite3

import networkx as nx
from rich.progress import track

from graphreveal_tools import PKG_PATH, DATABASE_PATH
from . import util


def create_db(max_n):
    con = sqlite3.connect(DATABASE_PATH)
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

    all_graphs = []

    for n in range(1, max_n + 1):
        file_path = os.path.join(
            PKG_PATH, "graphreveal_tools", "db_creator", "data", f"graph{n}.g6"
        )
        with open(file_path, encoding="utf-8") as f:
            all_graphs += f.read().strip().split("\n")

    for graph_g6 in track(all_graphs, description="Creating the database"):
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
                util.max_degree(graph),
                util.min_degree(graph),
            ],
        )

    con.commit()
    con.close()
