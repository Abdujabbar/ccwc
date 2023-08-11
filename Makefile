install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 .

test:
	poetry run pytest -vv

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
