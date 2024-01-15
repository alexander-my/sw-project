# Используем официальный образ Python
FROM python:3.8

# Устанавливаем переменную окружения для предотвращения вывода сообщений о попытке ввода данных
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта (requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога (где находится Dockerfile) в контейнер в /app
COPY . /app/

# Определяем переменные окружения для Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Делаем entrypoint.sh исполняемым
RUN chmod +x /app/entrypoint.sh

# Открываем порт 5000
EXPOSE 5000

# Определяем скрипт entrypoint.sh как точку входа
ENTRYPOINT ["/app/entrypoint.sh"]