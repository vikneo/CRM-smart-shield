test_flake8:
	flake8 src/

test_mypy:
	mypy --check-untyped-defs src/

test_isort:
	isort --check-only --diff --profile black src/

test_black:
	black --diff --check src/
	