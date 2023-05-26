# TDD PYTHON BOILERPLATE

Quick implementation (and not finished) of the [Bowling Game Kata](https://kata-log.rocks/bowling-game-kata)
we did at HolaLuz as a TDD practice.

## Install
To run the project you'll need python 3.11. You can install it using [Pyenv](https://github.com/pyenv/pyenv)
or any other Python version management tool.

You'll need to create a virtualenv and install pytest. Easiest way to do that is to
install [pipenv](https://pypi.org/project/pipenv/) and run the following commands:

Create the environment and install dependencies
```
pipenv sync --dev
```
Activate the environment
```
pipenv shell
```

## Tests
With the virtual environment activated just run:
```
pytest
```