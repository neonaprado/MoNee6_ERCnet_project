# MoNee6 ERCnet Project

This repository tracks scripts, job files, and notes for testing whether MoNee6 coevolves with other fungal proteins using ERCnet.

## Project Question

Does MoNee6 coevolve with other fungal proteins across fungal pathogen species?

Sub-questions:
- If MoNee6 has ERC hits, what proteins are they?
- What are their molecular functions?
- Do ERC hit proteins have plastid-targeting motifs?
- Does MoNee6 show accelerated evolution?
- Are there genes specifically absent in hemibiotrophs or necrotrophs?

## Workflow

1. Fix OrthoFinder species tree polytomy.
2. Rerun/continue OrthoFinder using the bifurcating species tree.
3. Use OrthoFinder output as input for ERCnet.
4. Run ERCnet test workflow on sample data.
5. Run ERCnet on fungal dataset.

### Interactive MoNEE gene tree viewing

Cleaned Newick tree files are included in the `viewer_trees/` folder. These files can be opened in iTOL to inspect the full OrthoFinder gene trees interactively. In each tree, the MoNEE target accession is labeled with `TARGET`, for example `TARGET_MoNEE3_EHA47798.1`.

To view a tree:
1. Open iTOL in a web browser.
2. Upload one `.tree` file from `viewer_trees/`.
3. Use the node search tool and search `TARGET`.
4. The highlighted node marks the MoNEE gene in that orthogroup tree.

These tree views are used as visual confirmation that the MoNEE accessions were recovered in the OrthoFinder gene-tree output. They are not used as direct evidence of ERC-based coevolution.

## Important HPC Paths

Original shared project data:

/shared/Forsythe_lab_shared/Fungal_effectors_project/

Fixed bifurcating tree:
/scratch/pradon/MoNee6_ERC_project/tree_fix/SpeciesTree_rooted_node_labels_bifurcating.txt

Completed OrthoFinder output to use for ERCnet:
/scratch/pradon/MoNee6_ERC_project/orthofinder_runs/orthofinder_fixed_tree/Results_Jun04/

ERCnet repo:
/scratch/pradon/MoNee6_ERC_project/ERCnet/



