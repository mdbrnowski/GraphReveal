import networkx as nx


def _find_closure(G: nx.Graph) -> nx.Graph:
    """Returns a graph cl(G) defined as in Bondy-Chvátal Theorem."""
    G = G.copy()
    n = G.number_of_nodes()
    edges_to_add = []
    for v in G.nodes:
        for u in G.nodes - G.neighbors(v) - {v}:
            if G.degree[v] + G.degree[u] >= n:
                edges_to_add.append((v, u))

    while edges_to_add:
        v, u = edges_to_add.pop()
        G.add_edge(v, u)
        for w in G.nodes - G.neighbors(v) - {v}:
            if G.degree[w] + G.degree[v] >= n:
                edges_to_add.append((w, v))
        for w in G.nodes - G.neighbors(u) - {u}:
            if G.degree[w] + G.degree[u] >= n:
                edges_to_add.append((w, u))

    return G


def is_hamiltonian(G: nx.Graph) -> bool:
    """Checks whether a graph G is hamiltonian or not."""
    n = G.number_of_nodes()
    if n == 1:
        return True
    if n == 2:
        return False
    if not nx.is_connected(G) or nx.is_tree(G):
        return False
    if not nx.is_biconnected(G):
        return False

    cl_G = _find_closure(G)
    if (
        cl_G.number_of_edges()
        == cl_G.number_of_nodes() * (cl_G.number_of_nodes() - 1) / 2
    ):
        return True

    return nx.isomorphism.GraphMatcher(G, nx.cycle_graph(n)).subgraph_is_monomorphic()


def max_degree(graph: nx.Graph) -> int:
    return max(d for _, d in graph.degree())


def min_degree(graph: nx.Graph) -> int:
    return min(d for _, d in graph.degree())
