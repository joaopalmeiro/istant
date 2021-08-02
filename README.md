# istant

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python package to check if an object is of a certain type in an instant.

## Development

- `poetry install`
- `poetry shell`

## Tech Stack

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-pkg`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## References

- [How to check if a string is upper, lower, or mixed case in Python](kite.com/python/answers/how-to-check-if-a-string-is-upper,-lower,-or-mixed-case-in-python).

## Notes

- [pyenv](https://github.com/pyenv/pyenv):
  - `pyenv local 3.6.13`. It generates a `.python-version` file. It is similar to the `.nvmrc` file ([nvm](https://github.com/nvm-sh/nvm)).
  - [Should we gitignore the .python-version file?](https://stackoverflow.com/questions/54315206/should-we-gitignore-the-python-version-file).
