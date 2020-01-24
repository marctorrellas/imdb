feedstock
==============================

A classifier for IMDB movie reviews. See reports folder for PoC notebooks:

- Classical NLP notebook
- Deep learning based notebook is actually hosted in Google
Colab, see https://colab.research.google.com/drive/1YUewI5gALb78zVKD0FHtbI7KI3nEwT5y


# User guide


### Install

To distribute, just provide the whl file in the dist folder. 

To install run `pip install dist/feedstock-{version}-py3-none-any.whl`


### Train

There are several options here. To see the help page:

```
fs_train -h 
```

Typical use cases:

```
xxx
```

### Predict

There are several options here. To see the help page:

```
fs_predict -h 
```

Typical use cases:

```
xxx
```



# Contributors guidelines

### Set-up the environment
1. Navigate to the project folder.
1. Deactivate your conda environment, if any.
1. Create the environment with `. create_conda_env.sh`.
1. Bonus: run `. after_poetry_install.sh` to add some nice extensions to Jupyter :)

## Development packages
If you need to use locally modified versions of the packages,
1. Uninstall the necessary package by commenting it in pyproject and running `poetry update`.
1. Add the local version using conda-develop, `conda install conda-build; conda-develop path/to/repo`.
1. Make note in the pyproject.toml and README.md of the commit of the local library used for reproducibility.

Note: using local library versions is discouraged because it circumvents the packaging locking provided in this template.

## Run tests

XXXXX

Project Organization
------------

```
├── README.md            <- The top-level README for developers using this project.
├── data
│   ├── external         <- Use this to symlink to some other place.
│   ├── interim          <- Intermediate data that has been transformed.
│   ├── processed        <- Data after applying some processing pipeline.
│   └── raw              <- The original, immutable data dump.
│
├── models               <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks            <- Jupyter notebooks.
│
├── references           <- Papers, manuals, and all other explanatory materials.
│
├── reports              <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures          <- Generated graphics and figures to be used in reporting
│
├── conda_setup.yml      <- The conda requirements file for installation of conda env
├── build-linux.yml      <- The linux specific conda requirements file for installation
├── build-mac.yml        <- The mac specific conda requirements file for installation
├── create_conda_env.sh  <- The script to create the conda env using all other files
├── pyproject.toml       <- The poetry requirements file for reproducing the dev virtual 
│                           environment
│
└── src                          <- Source code for use in this project.
    ├── __init__.py              <- Makes src a Python module
    ├── config.py                <- A config to define file paths, datasets and pipelines
    │
    ├── data                     <- Scripts to generate data_pods and run pipelines
    │   ├── __init__.py
    │   └── load_data.py         <- utility functions to load the data pods generated in make_dataset.py
    │
    ├── scripts                  <- A store of scripts to run the analysis.
    │   ├── __init__.py
    │   ├── make_dataset.py      <- make datasets from data/raw
    │   ├── run_pipelines.py     <- A script to run the pipelines defined in config.py over the preprocessed
    │   │                           data_pods.
    │   └── run_preprocessing.py <- A script to run the preprocessing pipeline defined in config.py over the
    │                               loaded data_pods.
    │
    ├── pipes                    <- A store of prototype pipes specific to the poject
    │   └── __init__.py
    │
    ├── configs                  <- The definition of the pipelines to be used in the experiments.
    │   ├── __init__.py
    │   └── example.py           <- An example (empty) pipeline configuration file.
    │
    └── visualization            <- Scripts to create exploratory and results oriented visualizations
        ├── __init__.py
        └── visualize.py
```

--------


Build updated package
---------------------

Run `poetry build`


Missing pieces for future work
------------------------------

* Set up a web framework to enable API requests, using e.g. Flask
* Implement a deep learning solution (see Google Colab notebook)
*  


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
