PYTEST_ARGS := --cov
PYTEST_REPORT_ARGS :=  --cov-report=xml:coverage.xml

.PHONY: install
install:
	@uv init
	@uv run pre-commit install

.PHONY: align_code
align_code:
	poetry run ruff format .

.PHONY: lint.mypy
lint.mypy:
	@poetry run mypy

.PHONY: lint.ruff
lint.ruff:
	@poetry run ruff check . --fix

.PHONY: pre-commit-all
pre-commit-all:
	@poetry run pre-commit run --all-files

.PHONY: test.pytest
test.pytest:
	@poetry run pytest $(PYTEST_ARGS) -- tests

.PHONY: test.coverage
test.coverage:
	@poetry run pytest $(PYTEST_ARGS) $(PYTEST_REPORT_ARGS) -- tests
