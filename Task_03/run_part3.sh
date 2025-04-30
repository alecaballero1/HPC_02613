#!/bin/bash
#BSUB -J part3
#BSUB -q hpc
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 5
#BSUB -n 4
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "span[hosts=1]"
#BSUB -o part3/part3_%J.out
#BSUB -e part3/part3_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python part3.py 4