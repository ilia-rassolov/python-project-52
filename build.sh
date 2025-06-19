#!/usr/bin/env bash
# скачиваем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# здесь добавьте все необходимые команды для установки вашего проекта
# python manage.py runserver
# команду установки зависимостей, сборки статики, применения миграций и другие
# psql -U user_52 -d db_52 -h 127.0.0.1 подключиться к db_52 от user_52
make install
make migrate