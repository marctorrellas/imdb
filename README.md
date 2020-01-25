IMDB classifier
==============================

A classifier for IMDB movie reviews, but in general would work for many binary text 
classification problems. See reports folder for:

- Classical NLP proof-of-concept notebook
- Deep learning based notebook, actually hosted in Google
Colab, see https://colab.research.google.com/drive/1YUewI5gALb78zVKD0FHtbI7KI3nEwT5y
- Future / Missing work


User guide
---------------

### Install

To distribute, just provide the whl file in the dist folder. 

To install run `pip install dist/feedstock-{version}-py3-none-any.whl`


### Train

There are several options here. To see the help page:

```
imdb_train -h 
```

Run without arguments to use sample data


### Predict

There are several options here. To see the help page:

```
imdb_predict -h 
```

Run without arguments to use sample data


### Evaluate

There are several options here. To see the help page:

```
imdb_evaluate -h 
```

Run without arguments to use sample data


Contributors guidelines
---------------------

### Set-up the conda environment

1. Navigate to the project folder.
1. Deactivate your conda environment, if any.
1. Create the environment with `. create_conda_env.sh`.
1. Bonus: run `. after_poetry_install.sh` to add some nice extensions to Jupyter :)


### Run tests

`pytest imdb`

### Build updated package

Run `poetry build`


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
│                           environment, and allowing to build the wheel
│
└── imdb                          <- Source code for use in this project.
    ├── __init__.py              
    ├── config.py                <- A config to define file paths, and other constants
    │
    ├── configs                  <- The definition of hyper-parameters for ML models (not used for now)
    │   └── __init__.py
    │
    ├── core                     <- Groups core functions (probably can be split into many if it grows)
    │   ├── __init__.py
    │   ├── data_loaders.py      <- Utility functions to load data
    │   ├── analysis.py          <- Utility functions to analyse models
    │   ├── visualize.py         <- Utility functions to visualise data or results
    │   └── metrics.py           <- Utility functions to load data
    │
    ├── models                    <- Classes defining the available ML models 
    │   ├── __init__.py
    │   ├── base_model.py        <- Define the class all other models inherit from
    │   └─- models.py            <- Defines the ML models
    │   
    ├── scripts                  <- A store of scripts to run from CLI
    │   ├── __init__.py
    │   ├── train.py   
    │   ├── predict.py 
    │   └── evaluate.py
    │
    └── tests
        ├── __init__.py
        ├── benchmark            
        ├── feature              
        ├── fixtures             
        └── unit                 
```

--------


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
