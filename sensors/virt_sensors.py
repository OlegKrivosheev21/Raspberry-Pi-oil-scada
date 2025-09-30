import random

def get_sensor_data():
    """Возвращает случайные значения виртуальных датчиков"""
    return {
        "temperature": round(random.uniform(20, 90), 1),
        "pressure": round(random.uniform(1, 5), 2),
        "oil_level": round(random.uniform(0, 100), 1)
    }
