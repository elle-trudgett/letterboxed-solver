.PHONY: venv install run lint format test all clean

venv:
	python -m venv .venv
	.venv/bin/pip install uv
	.venv/bin/uv pip install --upgrade pip

install: venv
	.venv/bin/uv sync

run:
	.venv/bin/uv run main.py

lint:
	.venv/bin/uv run ruff check --fix src tests

format:
	.venv/bin/uv run ruff format src tests

test:
	.venv/bin/uv run pytest

clean:
	rm -rf .venv

# Run format, lint, and test
all: format lint test