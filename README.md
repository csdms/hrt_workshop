# Landlab Tutorials for the HRT Workshop
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/gantian127/overlandflow_usecase/blob/master/LICENSE.txt)

This repository includes the Jupyter Notebooks used as the [Landlab](https://landlab.github.io/) tutorials for the
[EarthCube Advancing the Analysis of HRT Workshop](https://opentopography.org/workshops/earthcube-advancing-analysis-hrt-workshop-2).
You can run the tutorial notebooks either on the CSDMS JupyterHub or on your local PC.

### Method 1: Use the CSDMS JupyterHub
- All the HRT workshop participants have a user account on the CSDMS JupyterHub.
- Click on **[this link](https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2F%2Fcsdms%2Fhrt_workshop&urlpath=lab%2Ftree%2Fhrt_workshop%3Fautodecode&branch=master)**.
It will lead you to the login page (see figure below). After you provide the account info, the tutorial notebooks will be loaded on the CSDMS JupyterHub.
- Select the **"CSDMS" kernel** before running the notebooks.

![login_plot](login.png)

### Method 2: Use Local PC
- Clone the workshop repository to the local PC.
```
$ git clone https://github.com/csdms/hrt_workshop
$ cd hrt_workshop
```

- Create and activate a virtual environment named as "landlab_tutorials".
The environment.yml file is in the "hrt_workshop" folder.
```
$ conda env create --file=environment.yml
$ conda activate landlab_tutorials
```

- Launch the tutorial notebooks on the local PC.
```
$ jupyter notebook
```
