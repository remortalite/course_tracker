install:
	poetry install --no-dev


# Dev
install-dev:
	poetry install --with=dev

dev: install-dev
	poetry run python course_tracker/manage.py runserver

test:
	poetry run python course_tracker/manage.py test course_tracker

lint:
	poetry run flake8 course_tracker

.PHONY: install dev test lint