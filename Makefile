.PHONY: install
install:
	uv sync --locked

.PHONY: fmt
fmt:
	uv run python chinese_calendar/scripts/__init__.py
	uv run isort .
	uv run black .

.PHONY: lint
lint:
	uv run flake8
	uv run isort --check .
	uv run black --check .

.PHONY: pytest
pytest:
	uv run pytest

.PHONY: test
test: lint pytest

.PHONY: release
release:
	pipenv run pip install twine wheel
	rm -rf dist
	pipenv run python setup.py release
	sed -i 's/chinesecalendar/chinese_calendar/g' setup.py
	pipenv run python setup.py release
	pipenv run twine upload -r pypi dist/*
