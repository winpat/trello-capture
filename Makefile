.PHONY: run install

install:
	pip install -r requirements.txt

test:
	pytest --black --isort --flake8 --mypy --cov=wiki
