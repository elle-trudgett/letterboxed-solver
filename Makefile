.PHONY: install run lint format test all

install:
	uv sync

run:
	uv run main.py

lint:
	uv run ruff check --fix src tests

format:
	uv run ruff format src tests

test:
	uv run pytest

# Run format, lint, and test
all: format lint test