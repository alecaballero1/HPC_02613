
#!/bin/bash
#BSUB -J gpu_optimization
#BSUB -q c02613
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=6GB]"
#BSUB -W 60
#BSUB -n 4
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -R "span[hosts=1]"
#BSUB -oo gpu_optimization%J.out
#BSUB -eo gpu_optimization%J.err
#BSUB -N
#BSUB -u s231912@dtu.dk

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613
module load cuda/11.8

nsys profile --force-overwrite true -o final_prof python final.py 10