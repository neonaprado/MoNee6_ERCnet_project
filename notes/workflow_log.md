# Workflow Log

## Tree polytomy fix

The original OrthoFinder/ERCnet species tree had a polytomy at node N179 with 3 children.

Checked with:

python check_bifurcating.py SpeciesTree_rooted_node_labels.txt

Output:
Tree is NOT bifurcating.
Non-bifurcating nodes:
node=N179, children=3

Resolved with:
python resolve_polytomy.py


