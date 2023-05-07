# Landlab Tutorials for the HRT Workshop
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/gantian127/overlandflow_usecase/blob/master/LICENSE.txt)

# Model-Data Integration with Landlab

May 10, 2023  
Arizona State University, Tempe, AZ

This workshop will be divided into two parts. In the first half we will provide a
brief tutorial introduction to the theory and implementation of *Landlab* for landscape
evolution modeling. We will cover grid representation, working with data fields,
and using *Landlab* components to create new integrated models.

In the second half we will turn our focus to how we can incorporate high-resolution
topography data into the *Landlab* environment. In both parts participants will
be able to run hands-on examples and be free to write and run their own *Landlab*
code. This clinic is intended both for beginners, who may have little to no
experience using the *Landlab* library, as well as for more advanced *Landlab* users.
Prior experience with Python programming will be helpful.

This repository includes the Jupyter Notebooks used as the [Landlab][landlab-docs]
tutorials for the [EarthCube Advancing the Analysis of HRT Workshop #2][hrt-workshop].
You can run the tutorial notebooks either on the CSDMS JupyterHub or on your local PC.

## 🚀 Run the lessons

All lessons are available to run on [EarthscapeHub][jhub].

👉 [![Run on EarthscapeHub][badge]][jhub-link] 👈

> ⚠️ Select the **"CSDMS" kernel** before running the notebooks.


> **Note:** The EarthscapeHub *lab* instance is password-protected.
  Please contact your instructor about obtaining a login,
  or visit [the CSDMS wiki][jhub-info] page for more information.

### Local installation

If you would like to run these notebooks on your personal computer, you can do
that too. You will need to have a Python installation (we recommend the
[Anaconda distribution][anaconda-download], but others should work as well).

If you have `git` installed on your computer, you can get the lessons by cloning
this repository,

    git clone git@github.com:csdms/hrt_workshop

You can, alternatively, [download a zip file][hrt-workshop-zip] of the repository.

Install the necessary dependencies to run the notebooks into your current
environment (either *pip* or *conda*/*mamba* should work),

    cd hrt_workshop
    pip install -r requirements.in


![login_plot](login.png)


[anaconda-download]: https://www.anaconda.com/download
[badge]: https://img.shields.io/badge/Run%20on-EarthscapeHub-green
[hrt-workshop]: https://opentopography.org/workshops/earthcube-advancing-analysis-hrt-workshop-2
[hrt-workshop-zip]: https://github.com/csdms/hrt_workshop/archive/refs/heads/master.zip
[jhub-info]: https://csdms.colorado.edu/wiki/JupyterHub
[jhub-link]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2F%2Fcsdms%2Fhrt_workshop&urlpath=lab%2Ftree%2Fhrt_workshop%3Fautodecode&branch=master
[landlab-dev]: https://github.com/landlab/landlab/
[landlab-docs]: https://landlab.readthedocs.io/
