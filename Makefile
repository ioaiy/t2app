.PHONY: all

project := t2test

help::
	@echo "Available commands:"
	@grep --color=never --extended-regexp --only '^\w[^: ]+:' Makefile | sed -E -e 's/^([^: ]+):/ - \1/'

fmt:: isort black

isort::
	isort $(project) tests

black::
	black $(project) tests

fmt-check::
	isort --check --diff $(project)
	black --check --diff $(project)

lint:: flake8

flake8::
	flake8 $(project)

test:: djtest

djtest::
	docker-compose exec web python manage.py test t2test.apps.ledgers
