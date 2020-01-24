#!/usr/bin/env bash

env_name=feedstock
conda_setup_file=conda_setup.yml

if [[ -z ${operating_system} ]]; then
    operating_system=`uname`
    echo Setting operating_system variable to $operating_system
fi

if [[ ${operating_system} == "Darwin" ]]; then
    extra_conda_file="build-mac.yml"
elif [[ ${operating_system} == "Linux" ]]; then
    extra_conda_file="build-linux.yml"
else
    echo "Please define operating_system variable as in operating_system=Darwin or operating_system=Linux"
    return
fi

# Create the environment if we're not in update mode or the environment doesn't exist

conda env create -f ${extra_conda_file} --force
conda activate ${env_name}
conda env update -f ${conda_setup_file}
poetry install