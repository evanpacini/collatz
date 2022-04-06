import networkx as nx
import os
from networkx.drawing.nx_agraph import write_dot

N = input("N: ")
n = int(N)


def c1(n) -> int:  # Make a single step in the collatz sequence.
    return int((n & 1) * ((n << 1) + 1 + n) + (not n & 1) * (n >> 1))


g = nx.DiGraph()
seen = [1]

for i in range(1, n+1):
    while i != 1:
        if i not in seen:
            seen.append(i)
            j = c1(i)
            g.add_edge(i, j)
            i = j
        else:
            i = 1

write_dot(g, 'dot\Collatz_digraph_('+N+').dot')
# os.system("dot -Tpng dot\Collatz_digraph_("+N +
#           ").dot -o Figs\Collatz_digraph_("+N+").png")
