import sys

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else "input"
    g = [l for l in open(fn).read().split("\n") if l]
    H, W = len(g), len(g[0])
    seen = set()
    p1 = p2 = 0
    for sr in range(H):
        for sc in range(W):
            if (sr, sc) in seen:
                continue
            ch = g[sr][sc]
            reg = {(sr, sc)}
            st = [(sr, sc)]
            while st:
                r, c = st.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and g[nr][nc] == ch and (nr, nc) not in reg:
                        reg.add((nr, nc))
                        st.append((nr, nc))
            seen |= reg
            edges = set()
            for r, c in reg:
                for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (r + d[0], c + d[1]) not in reg:
                        edges.add((r, c, d))
            sides = 0
            for r, c, d in edges:
                # count edge if its "previous" neighbour along the side isn't also an edge
                pr, pc = (r, c - 1) if d[0] else (r - 1, c)
                if (pr, pc, d) not in edges:
                    sides += 1
            p1 += len(reg) * len(edges)
            p2 += len(reg) * sides
    print(f"part1: {p1}")
    print(f"part2: {p2}")

main()
