build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

lint:
	uv run flake8 task_manager

