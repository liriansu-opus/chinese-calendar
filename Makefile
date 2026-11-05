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

# The package is published to PyPI under two names: chinesecalendar and chinese_calendar.
# Both are built from a clean export of HEAD, so local changes never leak into a release
# and pyproject.toml is never edited in place.
.PHONY: build
build:
	@test -z "$$(git status --porcelain)" || { echo "error: working tree is not clean" >&2; exit 1; }
	rm -rf dist
	set -e; \
	src=$$(mktemp -d); trap 'rm -rf "$$src"' EXIT; \
	git archive HEAD | tar -x -C "$$src"; \
	uv build --quiet --out-dir dist "$$src"; \
	sed -i.bak 's/^name = "chinesecalendar"$$/name = "chinese_calendar"/' "$$src/pyproject.toml"; \
	grep -q '^name = "chinese_calendar"$$' "$$src/pyproject.toml"; \
	uv build --quiet --out-dir dist "$$src"
	uvx twine check --strict dist/*
	ls dist

.PHONY: release
release: build
	@version=$$(sed -n 's/^__version__ = "\(.*\)"$$/\1/p' chinese_calendar/__init__.py); \
	git tag --points-at HEAD | grep -qx "$$version" || { echo "error: HEAD is not tagged $$version" >&2; exit 1; }
	uvx twine upload -r pypi dist/*

.PHONY: clean
clean:
	rm -rf dist build *.egg-info .coverage .pytest_cache
	find . -name __pycache__ -type d -not -path './.venv/*' -prune -exec rm -rf {} +
