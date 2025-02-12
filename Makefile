.PHONY: venv install install-dev run lint format test all clean
.DEFAULT_GOAL := run

venv:
	@python -m venv .venv
	@.venv/bin/pip install -q uv
	@.venv/bin/uv pip install -q --upgrade pip

install: venv
	@.venv/bin/uv sync -q --inexact

install-dev: venv
	@.venv/bin/uv sync -q --all-extras

run: install
	@.venv/bin/uv run main.py

lint: install-dev
	@.venv/bin/uv run ruff check --fix src tests

format: install-dev
	@.venv/bin/uv run ruff format src tests

test: install-dev
	@.venv/bin/uv run pytest

clean:
	@rm -rf .venv

# Run format, lint, and test
all: format lint test