# Используем официальный образ Python
FROM python:3.10-slim
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем зависимости
COPY requirements.txt .
# Устанавливаем зависимости
RUN pip install -r requirements.txt
# Копируем все файлы приложения в контейнер
COPY . .
# Открываем порт 5000 для Flask приложения
EXPOSE 5000
# Запускаем приложение
CMD ["python", "temperature_service.py"]