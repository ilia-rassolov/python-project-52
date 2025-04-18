build:
	./build.sh

render-start:
	.venv/bin/python -m gunicorn --chdir hexlet-code task_manager.wsgi

install:
	uv sync

