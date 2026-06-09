#!/bin/bash
#SBATCH --job-name=orthofinder_fixed_tree
#SBATCH --output=/scratch/pradon/MoNee6_ERC_project/logs/orthofinder_fixed_tree_%j.out
#SBATCH --error=/scratch/pradon/MoNee6_ERC_project/logs/orthofinder_fixed_tree_%j.err
#SBATCH --partition=forsythe.q
#SBATCH --account=forsythe
#SBATCH --ntasks=96
#SBATCH --time=200:00:00

module load python/anaconda/3.12
source /opt/ohpc/pub/apps/anaconda/3.12/etc/profile.d/conda.sh
conda activate orthofinder_py39
export PATH=/home/pradon/.conda/envs/orthofinder_py39/bin:$PATH
hash -r

which python
python --version
which orthofinder

orthofinder \
-f /shared/Forsythe_lab_shared/Fungal_effectors_project/renamed_proteomes \
-s /scratch/pradon/MoNee6_ERC_project/tree_fix/SpeciesTree_rooted_node_labels_bifurcating.txt \
-y \
-X \
-M msa \
-t 96 \
-o /scratch/pradon/MoNee6_ERC_project/orthofinder_runs/orthofinder_fixed_tree \