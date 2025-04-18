build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

