import sys
from collections import defaultdict
from itertools import combinations
import networkx as nx

f = sys.argv[1] if len(sys.argv) > 1 else "input"
adj = defaultdict(set)
for line in open(f).read().split():
    a, b = line.split("-")
    adj[a].add(b); adj[b].add(a)

tri = set()
for a in adj:
    for b, c in combinations(adj[a], 2):
        if c in adj[b]:
            tri.add(tuple(sorted((a, b, c))))
print("part1:", sum(any(x[0] == "t" for x in t) for t in tri))

G = nx.Graph((a, b) for a in adj for b in adj[a])
best = max(nx.find_cliques(G), key=len)
print("part2:", ",".join(sorted(best)))
