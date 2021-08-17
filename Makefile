.PHONY: check

check:
	flake8
	mypy
	pytest
