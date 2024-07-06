import networkx as nx


def is_hamiltonian(G: nx.Graph):
    n = G.number_of_nodes()
    if n == 1:
        return True
    if n == 2:
        return False
    if not nx.is_connected(G) or nx.is_tree(G):
        return False
    if min(d for _, d in G.degree()) == 1:
        return False

    ore_assumption = True
    for v in G.nodes:
        for u in G.nodes - G.neighbors(v) - {v}:
            if G.degree[v] + G.degree[u] < n:
                ore_assumption = False
    if ore_assumption:
        return True

    return nx.isomorphism.GraphMatcher(G, nx.cycle_graph(n)).subgraph_is_monomorphic()
