# Project name

Brief description of project, including

- Sentence describing the molecule(s).
- Sentence describing the models (example keywords: in vitro, human, mouse, cyno, PK, RO, cell expansion, tumor growth inhibition, PD)

## Project directory structure

Notebooks to be run are stored in the root directory. Other files are stored in the following locations:

| Directory      | Contents                                                   |
| -------------  | ---------------------------------------------------------- |
| `/data`        | Data .csv files                                            |
| `/data/outputs`| Designer .csv simulation outputs                           |
| `/models`      | Designer model exports                                     |
| `/parameters`  | Parameter .csv files                                       |
| `/utilities`   | Utility .py files to be loaded as modules                  |
| `/workspaces`  | QSP Designer workspace files                               |

## Installing the project

This repo uses Poetry to define its dependencies.
After checking out a new commit, run `poetry install` to update the local dependencies.
When opening an existing notebook make sure that the kernel is set to "Poetry".
When creating a new notebook, be sure to use the "Poetry" kernel.

New dependencies can be added to the `pyproject.toml` file either manually or with the `poetry add` command.
When the TOML file is updated, use `poetry lock` followed by `poetry install` again to update the environment.

More information about poetry can be found [here](https://python-poetry.org/docs/).

## Description of run files

- `example_notebook.ipynb`: Notebook file that imports the `abm` module (simulation framework). Useful as a starting point for other notebooks.
