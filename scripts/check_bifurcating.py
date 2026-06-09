from Bio import Phylo
import sys

tree_file = sys.argv[1]
tree = Phylo.read(tree_file, "newick")

bad_nodes = []

for clade in tree.find_clades():
    n_children = len(clade.clades)

    if n_children not in (0, 2):
        bad_nodes.append((clade.name, n_children))

if bad_nodes:
    print("Tree is NOT bifurcating.")
    print("Non-bifurcating nodes:")
    for name, n in bad_nodes:
        print(f"node={name}, children={n}")
else:
    print("Tree is bifurcating.")
    