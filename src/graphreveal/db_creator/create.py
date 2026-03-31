import importlib.resources
import os
import sqlite3

import igraph as ig
import networkx as nx
from rich.progress import track

from graphreveal import DATABASE_PATH
from . import util


def create_db(max_n):
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
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
        with (
            importlib.resources.files("graphreveal")
            / "db_creator"
            / "data"
            / f"graph{n}.g6"
        ).open(encoding="utf-8") as f:
            all_graphs += f.read().strip().split("\n")

    for graph_g6 in track(all_graphs, description="Creating the database"):
        graph_nx = nx.from_graph6_bytes(str.encode(graph_g6))
        graph = ig.Graph.from_networkx(graph_nx)
        cur.execute(
            "INSERT INTO graphs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                graph_g6,
                graph.vcount(),
                graph.ecount(),
                graph.is_acyclic(),
                graph.is_bipartite(),
                util.is_eulerian(graph),
                util.is_hamiltonian(graph),
                nx.is_planar(graph_nx),
                len(graph.biconnected_components()),
                len(graph.connected_components()),
                util.max_degree(graph),
                util.min_degree(graph),
            ],
        )

    con.commit()
    con.close()
