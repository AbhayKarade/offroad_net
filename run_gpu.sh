#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=mmseg
#SBATCH -t 20:00:00
#SBATCH -C P100
#SBATCH --mem 80G
#SBATCH --gres=gpu:1
#SBATCH -p whitehill


module load cuda11.1/toolkit/11.1.1
module load cudnn/8.1.1.33-11.2/3k5bbs63

source /home/sskodate/py39_dl/bin/activate

echo "Starting to run mmsegmentation_architecture.py"
python mmsegmentation_architecture.py
