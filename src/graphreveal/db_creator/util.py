import igraph as ig


def _find_closure(G: ig.Graph) -> ig.Graph:
    """Returns a graph cl(G) defined as in Bondy-Chvátal Theorem."""
    G = G.copy()
    n = G.vcount()
    edges_to_add = []
    for v in range(n):
        for u in range(v + 1, n):
            if not G.are_adjacent(u, v):
                if G.degree(v) + G.degree(u) >= n:
                    edges_to_add.append((v, u))

    while edges_to_add:
        v, u = edges_to_add.pop()
        if not G.are_adjacent(v, u):  # check if edge already exists
            G.add_edges([(v, u)])
            for w in range(n):
                if w != v and not G.are_adjacent(w, v):
                    if G.degree(w) + G.degree(v) >= n:
                        edges_to_add.append((w, v))
            for w in range(n):
                if w != u and not G.are_adjacent(w, u):
                    if G.degree(w) + G.degree(u) >= n:
                        edges_to_add.append((w, u))

    return G


def is_hamiltonian(G: ig.Graph) -> bool:
    """Checks whether a graph G is hamiltonian or not."""
    n = G.vcount()
    if n == 1:
        return True
    if n == 2:
        return False
    if not G.is_connected():
        return False
    if G.ecount() == n - 1:  # is a tree
        return False
    if len(G.articulation_points()) > 0:  # is not biconnected
        return False

    cl_G = _find_closure(G)
    if cl_G.ecount() == n * (n - 1) / 2:  # is a complete graph
        return True

    cycle = ig.Graph.Ring(n)
    return G.subisomorphic_vf2(cycle)


def is_eulerian(graph: ig.Graph) -> bool:
    """Checks whether a graph has an Eulerian circuit."""
    if not graph.is_connected():
        return False
    return all(degree % 2 == 0 for degree in graph.degree())


def max_degree(graph: ig.Graph) -> int:
    return max(graph.degree())


def min_degree(graph: ig.Graph) -> int:
    return min(graph.degree())
