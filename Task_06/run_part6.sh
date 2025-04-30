#!/bin/bash
#BSUB -J part6[1-24]
#BSUB -q hpc
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 30
#BSUB -n 24
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "span[hosts=1]"
#BSUB -o part6/part6_%J_%I.out
#BSUB -e part6/part6_%J_%I.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python part6.py 100  $LSB_JOBINDEX