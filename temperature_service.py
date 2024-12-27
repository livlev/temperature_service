import time
import logging
import numpy as np
from flask import Flask, jsonify
from datetime import datetime
from threading import Thread

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(filename="temperature_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')


# Функция генерации температуры
def generate_temperature():
    # Основной процесс генерации температуры, которая имеет заданные квантильные ограничения
    while True:
        # Генерируем температуру с нормальным распределением
        temperature = np.random.normal(loc=20.0, scale=1.0)

        # Применяем квантильные ограничения
        temperature = max(16.0, min(temperature, 24.0))

        # Логируем значение температуры
        logging.info(f"Generated temperature: {temperature}")

        # Пауза 5 секунд
        time.sleep(5)


# Эндпоинт для получения последнего значения температуры
@app.route('/temperature', methods=['GET'])
def get_temperature():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature = np.random.normal(loc=20.0, scale=1.0)
    temperature = max(16.0, min(temperature, 24.0))

    return jsonify({"temperature": temperature, "time": current_time})


if __name__ == "__main__":
    # Запускаем генерацию температуры в отдельном потоке
    generator_thread = Thread(target=generate_temperature)
    generator_thread.daemon = True
    generator_thread.start()

    # Запускаем Flask приложение
    app.run(host='0.0.0.0', port=5000)