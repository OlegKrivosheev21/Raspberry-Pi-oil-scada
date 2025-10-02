
from sensors.virt_sensors import get_sensor_data
from control.pump import turn_on, turn_off, pump_state
from flask import Flask, jsonify, render_template
rasp = Flask(__name__)

# Главная страница
@rasp.route("/")
def dashboard():
    return render_template("HMI.html")

# Получение данных с сенсоров
@rasp.route("/sensors")
def sensors_route():
    # Сначала получаем текущие показания
    data = get_sensor_data() 

    # Автоматическое управление насосом
    if data["oil_level"] < 20:
        turn_on()   # если уровень ниже 20 процентов то вкл насос
    elif data["oil_level"] > 80:
        turn_off()  # если выше 80 то выкл насос
    data["pump_status"] = pump_state["status"]  # добавляем состояние насоса
    return jsonify(data)
# Маршруты для управления насосом
@rasp.route("/pump/on") #вкл насос
def pump_on_route():
    turn_on()
    return jsonify({"pump": pump_state["status"]})

@rasp.route("/pump/off") #выкл насос
def pump_off_route():
    turn_off()
    return jsonify({"pump": pump_state["status"]})

if __name__ == "__main__":
    rasp.run(host="0.0.0.0", port=5000)
