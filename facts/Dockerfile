FROM python:3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8000

# Запускаем сервер на 0.0.0.0 чтобы он был доступен извне контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
