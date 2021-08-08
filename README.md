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
- [python-string-utils](https://github.com/daveoncode/python-string-utils) package.

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
  - Go to matching parentheses: `%`.
  - Go to start/end of line: `0`/`$`.
  - Find word under cursor:
    - `*`: next occurrence.
    - `#`: previous occurrence.
  - Go to beginning/end of file: `gg`/`G`. `G` can be combined with a number too.
  - Search:
    - `/<text>`.
    - `n`: next occurrence.
    - `N`: previous occurrence.
  - Insert new line:
    - `o`: below the current line.
    - `O`: above the current line.
    - The editor is set to `insert` mode.
  - Remove a character:
    - `x`: under the cursor.
    - `X`: to the left of the cursor.
  - Replace a character:
    - `r`.
    - Under the cursor, without switching to `insert` mode.
  - Delete:
    - `d`.
    - It can be combined with numbers and movement keys (`dw` and `d2e`, for example).
    - It copies the content. Content can be pasted with `p`.
  - Repeat the previous command: `.`.
  - Visual mode:
    - `v`.
    - To select text with the movement keys first and then apply a command.
  - Exiting:
    - `:w`: save.
    - `:q`: quit.
    - `:q!`: quit without saving.
  - Editing:
    - `u`: undo.
    - `Ctrl` + `r`: redo.
  - [`Vim.gitignore` file](https://github.com/github/gitignore/blob/master/Global/Vim.gitignore).

### VIM and Python – A Match Made in Heaven

[Source](https://realpython.com/vim-and-python-a-match-made-in-heaven/).

- [`.vimrc` file](https://github.com/j1z0/vim-config/blob/master/vimrc).
- `vim --version`.
- _\*nix_ or _Unix-like_ [systems](https://en.wikipedia.org/wiki/Unix-like).
- Check the Python version used in Vim: `:python import sys; print(sys.version)`.
- Extensions or bundles or plugins.
- [Vundle](https://github.com/VundleVim/Vundle.vim):
  - `pip` for Vim/Vim plugin manager.
  - `git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim`.
  - Extensions can be managed from the `.vimrc` file (`touch ~/.vimrc`) + `:PluginInstall`.
- Split layouts:
  - `:sp <filename>`: vertical split.
  - `:vs <filename>`: horizontal split.
- [vscode-viml-syntax](https://marketplace.visualstudio.com/items?itemName=dunstontc.viml) (VS Code extension).
- Buffers:
  - Think of a buffer as a recently opened file.
  - `:b <buffer name or number>`: switch to an open buffer.
  - `:ls`: list all buffers.
- Extensions:
  - [SimpylFold](https://github.com/tmhedberg/SimpylFold) (code folding).
  - [indentpython.vim](https://github.com/vim-scripts/indentpython.vim).
  - [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe) (auto-complete). [Installation instructions](https://github.com/ycm-core/YouCompleteMe#macos).
  - [syntastic](https://github.com/vim-syntastic/syntastic) (syntax checking).
  - [vim-flake8](https://github.com/nvie/vim-flake8).
  - [NERDTree](https://github.com/preservim/nerdtree) (file browsing).
  - [CtrlP](https://github.com/ctrlpvim/ctrlp.vim) (searching).
  - [fugitive.vim](https://github.com/tpope/vim-fugitive) (Git integration).
  - [Powerline](https://github.com/powerline/powerline) (status bar).

### Effective Python Testing With Pytest

[Source](https://realpython.com/pytest-python-testing/).

- Arrange (set up)-Act-Assert model.
- pytest allows you to use Python's `assert` directly.
- [Test double](https://en.wikipedia.org/wiki/Test_double): an object that stands in for another object during a test ([source](https://doubles.readthedocs.io/en/latest/terminology.html)), such as mocks, for example.
- In pytest, fixtures are functions that create data/test doubles or initialize some system state for the test suite. They are used as arguments (explicit dependency declarations).
