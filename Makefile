build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

lint:
	uv run flake8 task_manager

migrate:
	python manage.py makemigrations | python manage.py migrate

test:
	uv run manage.py test

