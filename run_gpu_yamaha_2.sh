#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=mm_yama
#SBATCH -t 23:00:00
#SBATCH -C P100
#SBATCH --mem 80G
#SBATCH --gres=gpu:1
#SBATCH -p short


module load cuda11.1/toolkit/11.1.1
module load cudnn/8.1.1.33-11.2/3k5bbs63

source /home/sskodate/py39_dl/bin/activate

echo "Starting to run python src/offroad_path_detection.py --yaml_path=src/run_configs/yamaha/encnet_res101_yamaha.yaml"
python src/offroad_path_detection.py --yaml_path=src/run_configs/yamaha/encnet_res101_yamaha.yaml
