#!/bin/bash
#BSUB -J katpa_miniproject7/fulldataset
#BSUB -q hpc
#BSUB -W 10:00
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model==XeonGold6126]" 
#BSUB -n 20
#BSUB -o python_%J.out
#BSUB -e python_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python HPC_miniproject_7.py 4571
