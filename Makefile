.PHONY: install
install:
	pipenv sync --dev

.PHONY: fmt
fmt:
	PYTHONPATH=$$(pwd) python chinese_calendar/scripts/__init__.py
	pipenv run isort .
	pipenv run black .

.PHONY: test
test:
	pipenv run flake8
	pipenv run isort --check .
	pipenv run black --check -l 120 .
	$(Make) pytest

.PHONY: pytest
pytest:
	pipenv run pytest


.PHONY: release
release:
	pipenv run pip install twine wheel
	rm -rf dist
	pipenv run python setup.py release
	sed -i 's/chinesecalendar/chinese_calendar/g' setup.py
	pipenv run python setup.py release
	pipenv run twine upload -r pypi dist/*
