lint:
	poetry run flake8 gendiff
install:
	poetry install
test:
	poetry run pytest
selfcheck:
	poetry check
check: selfcheck test lint

build: check
	poetry build
.PHONY: install test lint selfcheck check build

test-coverage:
	poetry run pytest --cov
