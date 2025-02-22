#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=mmrugd
#SBATCH -t 20:00:00
#SBATCH -C P100
#SBATCH --mem 80G
#SBATCH --gres=gpu:1
#SBATCH -p short

module load cuda11.1/toolkit/11.1.1
module load cudnn/8.1.1.33-11.2/3k5bbs63

source /home/sskodate/py39_dl/bin/activate

echo "Starting to run src/offroad_path_detection.py"
python src/offroad_path_detection.py --yaml_path=src/run_configs/r002_psp_res50_rugd_full.yaml
