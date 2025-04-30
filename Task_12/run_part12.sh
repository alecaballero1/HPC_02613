#!/bin/bash
#BSUB -J part12
#BSUB -q hpc
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 10:00
#BSUB -n 24
#BSUB -R "select[model == XeonE5_2650v4]"
#BSUB -R "span[hosts=1]"
#BSUB -o part12_%J.out
#BSUB -e part12_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python part6_with_csv.py 4571 24

python part12_stats.py