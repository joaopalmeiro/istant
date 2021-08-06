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
- Vim:
  - Learning tools:
    - [VIM-ADVENTURES](https://vim-adventures.com/).
    - [OpenVim](https://www.openvim.com/).
    - [Vim Cheat Sheet](https://vim.rtorr.com/).
  - Two basic modes:
    - `insert` mode (`i`): to write text (like in a text editor).
    - `normal` mode (`Esc`): to navigate and manipulate text.
  - Basic movement: `h` (←), `j` (↓), `k` (↑), and `l` (→).
  - Word movement:
    - `w`: start of the next word.
    - `e`: end of the word.
    - `b`: beginning of the word.
    - These keys can be combined with a number (number powered movement). `3w` is the same as pressing `w` 3x, for example.
  - Insert text repeatedly: `30` + `i` + `-` + `Esc` to insert `-` 30x, for example.
  - Find a character:
    - `f`: next occurrence of a character.
    - `F`: previous occurrence of a character.
    - `fo` to find the next `o`, for example.
    - These keys can also be combined with numbers.
