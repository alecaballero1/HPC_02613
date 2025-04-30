#!/bin/bash
#BSUB -J part1
#BSUB -q hpc
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 5
#BSUB -n 10
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "span[hosts=1]"
#BSUB -o part1/part1_%J.out
#BSUB -e part1/part1_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python part1.py