
# Хранимое состояние насоса (по умолчанию вкл)
pump_state = {"status": "ON"}

# Функция для включения насоса
def turn_on():
    pump_state["status"] = "ON"
    return pump_state

# Функция для выключения насоса
def turn_off():
    pump_state["status"] = "OFF"
    return pump_state
