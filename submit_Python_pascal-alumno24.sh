#!/bin/bash
#SBATCH -p hpc-bio-pascal
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 00:10:00
#SBATCH -J reduc-numba
#SBATCH -o salida_%j.txt
#SBATCH -e error_%j.err

module load anaconda/2023.03

# Uso el valor pasado como argumento, por defecto 10000000 si no se pasa ninguno
value=${1:-10000000}

# Ejecuto el script con IPython para asegurar compatibilidad con Jupyter notebooks
python reduc-operation-alumno24-2.py $value

