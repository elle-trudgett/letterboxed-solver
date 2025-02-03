# Silence all commands by default
.SILENT:

.PHONY: venv install run lint format test all clean

venv:
	python -m venv .venv 2>/dev/null || $(MAKE) --no-silent venv
	.venv/bin/pip install uv >/dev/null 2>&1 || $(MAKE) --no-silent venv
	.venv/bin/uv pip install --upgrade pip 2>/dev/null || $(MAKE) --no-silent venv

install: venv
	.venv/bin/uv sync --inexact 2>/dev/null || $(MAKE) --no-silent install

install-dev: venv
	.venv/bin/uv sync --all-extras 2>/dev/null || $(MAKE) --no-silent install-dev

run: install
	.venv/bin/uv run main.py || $(MAKE) --no-silent run

lint: install-dev
	.venv/bin/uv run ruff check --fix src tests || $(MAKE) --no-silent lint

format: install-dev
	.venv/bin/uv run ruff format src tests || $(MAKE) --no-silent format

test: install-dev
	.venv/bin/uv run pytest || $(MAKE) --no-silent test

clean:
	rm -rf .venv || $(MAKE) --no-silent clean

# Run format, lint, and test
all: format lint test