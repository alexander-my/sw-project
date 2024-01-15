#!/bin/bash

sleep 10

# Выполнение скрипта create_db.py
echo "creating database..."
python create_db.py
echo "done"
echo "Starting app.."

# Запуск Flask приложения
flask run --host=0.0.0.0
