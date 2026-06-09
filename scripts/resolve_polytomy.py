from Bio import Phylo
from Bio.Phylo.Newick import Clade

input_tree = "SpeciesTree_rooted_node_labels.txt"
output_tree = "SpeciesTree_rooted_node_labels_bifurcating.txt"

tree = Phylo.read(input_tree, "newick")

def resolve_clade(clade):
    for child in clade.clades:
        resolve_clade(child)

    while len(clade.clades) > 2:
        child1 = clade.clades.pop()
        child2 = clade.clades.pop()

        new_internal = Clade(
            branch_length=0.0,
            clades=[child1, child2]
        )

        clade.clades.append(new_internal)

resolve_clade(tree.root)

Phylo.write(tree, output_tree, "newick")

print("Wrote:", output_tree)
