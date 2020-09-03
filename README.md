# Microeconometrics Replication Project: González (2013)


Madhurima Chandra

This project seeks to replicate the core results of:

> González, Libertad. 2013. "The Effect of a Universal Child Benefit on Conceptions, Abortions, and Early Maternal Labor Supply." American Economic Journal: Economic Policy, 5 (3): 160-88.


[![Build Status](https://travis-ci.org/HumanCapitalAnalysis/microeconometrics-course-project-mchandra12.svg)](https://travis-ci.org/HumanCapitalAnalysis/microeconometrics-course-project-mchandra12)
[![Continuous Integration](https://github.com/mchandra12/replication_gonzalez_2013/workflows/Continuous%20Integration/badge.svg)](https://github.com/mchandra12/replication_gonzalez_2013/actions)


## Viewing the notebook:

-   _Recommended_: Clone this repository to your local machine, run `conda env create -f environment.yml` in your shell to create the environment, and access the notebook by launching `jupyter lab` or `jupyter notebook`.

-   Note that `mybinder` or `nbviewer` may run into errors with displaying images and the like.

<a href="https://nbviewer.jupyter.org/github/mchandra12/replication_gonzalez_2013/blob/master/Replication.ipynb"
   target="_parent">
   <img align="center"
  src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png"
      width="109" height="20">
</a>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mchandra12/replication_gonzalez_2013/master?filepath=Replication.ipynb)

## Project Structure

-   auxiliary: hosts the code behind all functions called in the notebook

    -   pre_process_datasets.py
    -   run_regressions.py
    -   generate_tables.py
    -   generate_figures.py

-   causal_graphs: figures created with [Dagitty](dagitty.net) can be found here

-   data: datasets accessed to recreate paper results

-   Replication.ipynb


## References

-   **González, Libertad (2013)**. The Effect of a Universal Child Benefit on Conceptions, Abortions, and Early Maternal Labor Supply. _American Economic Journal: Economic Policy_, 5 (3): 160-88.

-   **Eisenhauer, P. (2020)**. Course project template, _HumanCapitalAnalysis_, <https://github.com/HumanCapitalAnalysis/template-course-project>.

* * *

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/HumanCapitalAnalysis/template-course-project/blob/master/LICENSE)
