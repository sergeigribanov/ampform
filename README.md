# AmpForm

[![10.5281/zenodo.5526648](https://zenodo.org/badge/doi/10.5281/zenodo.5526648.svg)](https://doi.org/10.5281/zenodo.5526648)
[![GPLv3+ license](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

[![PyPI package](https://badge.fury.io/py/ampform.svg)](https://pypi.org/project/ampform)
[![Conda package](https://anaconda.org/conda-forge/ampform/badges/version.svg)](https://anaconda.org/conda-forge/ampform)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/ampform)](https://pypi.org/project/ampform)

[![Binder](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ComPWA/ampform/stable?filepath=docs/usage)
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ComPWA/ampform/blob/stable)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-open-blue?logo=visualstudiocode)](https://open.vscode.dev/ComPWA/ampform)
[![GitPod](https://img.shields.io/badge/gitpod-open-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ComPWA/ampform)

[![Documentation build status](https://readthedocs.org/projects/ampform/badge/?version=latest)](https://ampform.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ComPWA/ampform/main.svg)](https://results.pre-commit.ci/latest/github/ComPWA/ampform/main)
[![pytest](https://github.com/ComPWA/ampform/workflows/pytest/badge.svg)](https://github.com/ComPWA/ampform/actions?query=branch%3Amain+workflow%3Apytest)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy.readthedocs.io)
[![Test coverage](https://codecov.io/gh/ComPWA/ampform/branch/main/graph/badge.svg)](https://codecov.io/gh/ComPWA/ampform)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/70fc5fb0f3954a9d82d142efeff4df31)](https://www.codacy.com/gh/ComPWA/ampform)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/master/packages/cspell)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

AmpForm is a Python library of spin formalisms and dynamics with which you can
automatically formulate symbolic amplitude models for Partial Wave Analysis. The
resulting amplitude models are formulated with
[SymPy](https://www.sympy.org/en/index.html) (a Computer Algebra System). This not only
makes it easy to inspect and visualize the resulting amplitude models, but also means
the amplitude models can be used as templates for faster computational back-ends (see
[TensorWaves](https://github.com/ComPWA/tensorwaves))!

Visit [ampform.rtfd.io](https://ampform.readthedocs.io) for several usage examples. For
an overview of **upcoming releases and planned functionality**, see
[here](https://github.com/ComPWA/ampform/milestones?direction=asc&sort=title&state=open).

## Available features

- **Automatic amplitude model building**<br /> Convert state transition graphs from
  [QRules](https://github.com/ComPWA/qrules) to an amplitude model that is
  _mathematically expressed_ with [SymPy](https://docs.sympy.org) and can be _converted
  to any backend_ (see [TensorWaves](https://tensorwaves.rtfd.io)).
- **Spin formalisms**
  - [Helicity formalism](https://ampform.readthedocs.io/en/stable/usage/helicity/formalism.html)
  - Canonical formalism
  - [Spin alignment](https://ampform.readthedocs.io/en/stable/usage/helicity/spin-alignment.html)
    for generic, multi-body decays that feature different decay topologies
- **Dynamics**
  - [Relativistic Breit-Wigner](https://ampform.readthedocs.io/en/stable/api/ampform.dynamics.html#ampform.dynamics.relativistic_breit_wigner_with_ff),
    optionally with form factors and/or
    [energy-dependent width](https://ampform.readthedocs.io/en/stable/api/ampform.dynamics.html#ampform.dynamics.EnergyDependentWidth)
  - [Symbolic _K_-matrix](https://ampform.readthedocs.io/en/stable/usage/dynamics/k-matrix.html#non-relativistic-k-matrix)
    for an arbitrary number of poles and channels
  - [Symbolic _P_-vector](https://ampform.readthedocs.io/en/stable/usage/dynamics/k-matrix.html#p-vector)
    for an arbitrary number of poles and channels

## Contribute

See [`CONTRIBUTING.md`](./CONTRIBUTING.md)
