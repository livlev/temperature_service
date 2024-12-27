# Temperature Service

Сервис для генерации температурных значений с определенными квантильными ограничениями. Данные о температуре генерируются каждые 5 секунд и сохраняются в лог. Также предоставляется API для получения текущей температуры.

## Как запустить локально

1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Запустите сервис: `python temperature_service.py`.
4. Приложение будет доступно на `http://localhost:5000/temperature`.

## Как использовать CI/CD

- Пайплайн CI/CD автоматически запускается при пуше в основную ветку.
- При каждом изменении в репозитории Docker-образ собирается и публикуется в Docker Hub.
# temperature_service
# temperature_service
