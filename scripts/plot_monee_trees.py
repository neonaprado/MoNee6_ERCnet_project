# Plot gene trees for the six MoNEE genes.
# This script reads a table that connects each MoNEE gene to its tree file,
# then saves one tree figure for each gene.

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from Bio import Phylo


# Folder where the six MoNEE tree files are saved on the HPC
tree_folder = Path("/scratch/pradon/MoNee6_ERC_project/ERCnet/MoNEE_gene_trees")

# Mapping table in this GitHub repo
mapping_file = Path("data/MoNEE_tree_mapping.tsv")

# Folder for output figures
figure_folder = Path("figures")
figure_folder.mkdir(exist_ok=True)


# Read the table
mapping = pd.read_csv(mapping_file, sep="\t")


# Plot one tree for each MoNEE gene
for index, row in mapping.iterrows():
    monee_gene = row["MoNEE_gene"]
    og_id = row["OG_ID"]
    accession = row["Protein_accession"]
    tree_file = tree_folder / row["Tree_file"]

    print("Plotting", monee_gene, "from", tree_file)

    # Read tree file in Newick format
    tree = Phylo.read(tree_file, "newick")

    # Large figure because the trees have many labels
    plt.figure(figsize=(14, 18))

    Phylo.draw(tree, do_show=False)

    plt.title(f"{monee_gene} gene tree ({og_id}, {accession})")

    output_file = figure_folder / f"{monee_gene}_{og_id}_tree.pdf"
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()

    print("Saved", output_file)

    