# letterboxed-solver

[![Tests](https://github.com/elle-trudgett/letterboxed-solver/actions/workflows/tests.yml/badge.svg)](https://github.com/elle-trudgett/letterboxed-solver/actions/workflows/tests.yml)

solver for nyt letterboxed puzzle

### install

```shell
uv sync
```

### run solver
```shell
uv run main.py
```

## development

### lint

```shell
uv run ruff check --fix src tests
```

### format

```shell
uv run ruff format src tests
```

### test

```shell
uv run pytest
```
