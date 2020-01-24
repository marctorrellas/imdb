#!/usr/bin/env bash

# An extension to maintain all conda environments as notebook kernels
# https://github.com/fcollonval/jupyter_conda
echo "Installing jupyterlab_conda (this takes a while)"
jupyter labextension install jupyterlab_toastify jupyterlab_conda

# An extension to add a Table of Contents to Jupyterlab
# https://github.com/jupyterlab/jupyterlab-toc
echo "Installing jupyterlab/toc (and this too)"
jupyter labextension install @jupyterlab/toc