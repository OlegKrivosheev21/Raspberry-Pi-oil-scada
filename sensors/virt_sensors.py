import random
from control.pump import pump_state  # импортируем состояние насоса

# Хранимые значения для виртуальных датчиков
sensor_state = {
    "temperature": 25.0,  # Начальная температура
    "pressure": 0.009,      # Начальное давление в МПа 
    "oil_level": 50.0     # Начальный уровень нефти
}

def get_sensor_data():
    """
    Возвращает обновленные значения виртуальных датчиков:
    - Температура (изменяется с небольшими колебаниями)
    - Давление (колеблется вокруг среднего значения)
    - Уровень нефти зависит от состояния насоса
    """

    # Колебания температуры и давления
    sensor_state["temperature"] += random.uniform(-0.5, 0.5)
    sensor_state["pressure"] += random.uniform(-0.002, 0.003)

    # Изменение уровня нефти с учетом состояния насоса
    if pump_state["status"] == "ON":
        sensor_state["oil_level"] += random.uniform(0.6, 0.9)  # растет
    else:
        sensor_state["oil_level"] -= random.uniform(0.1, 0.3)  # падает

    # Ограничения значений
    sensor_state["temperature"] = max(20, min(sensor_state["temperature"], 90))
    sensor_state["pressure"] = max(0.01, min(sensor_state["pressure"], 0.07))
    sensor_state["oil_level"] = max(0, min(sensor_state["oil_level"], 100))

    # Возвращаем округленные значения
    return {
        "temperature": round(sensor_state["temperature"], 1),
        "pressure": round(sensor_state["pressure"], 2),
        "oil_level": round(sensor_state["oil_level"], 1)
    }
