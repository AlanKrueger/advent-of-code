import sys
import networkx as nx

f = sys.argv[1] if len(sys.argv) > 1 else "input"
G = nx.Graph()
for line in open(f):
    if ":" in line:
        a, rest = line.split(":")
        for b in rest.split():
            G.add_edge(a.strip(), b)
cut = nx.minimum_edge_cut(G)
assert len(cut) == 3, cut
G.remove_edges_from(cut)
p = 1
for c in nx.connected_components(G):
    p *= len(c)
print(f"part1: {p}")
