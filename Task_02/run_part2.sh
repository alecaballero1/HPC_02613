#!/bin/bash
#BSUB -J part2
#BSUB -q hpc
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 5
#BSUB -n 10
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "span[hosts=1]"
#BSUB -o part2/part2_%J.out
#BSUB -e part2/part2_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python part2.py 10