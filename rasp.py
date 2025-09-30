from flask import Flask, jsonify, render_template_string
from sensors.virt_sensors import get_sensor_data
from control.pump import turn_on, turn_off, pump_state

rasp = Flask(__name__)

# Главная страница
@rasp.route("/")
def dashboard():
    html = """
    <html>
      <head>
        <title>Oil SCADA</title>
      </head>
      <body>
        <h1>Raspberry Pi Oil SCADA</h1>
        <p>Температура: <span id="temp">-</span> °C</p>
        <p>Давление: <span id="pressure">-</span> бар</p>
        <p>Уровень нефти: <span id="oil_level">-</span> %</p>
        <p>Состояние насоса: <span id="pump_status">OFF</span></p>

        <button onclick="fetch('/pump/on').then(updatePump)">Включить насос</button>
        <button onclick="fetch('/pump/off').then(updatePump)">Выключить насос</button>

        <script>
        // Обновление данных датчиков через AJAX
        function updateData() {
            fetch('/sensors')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('temp').innerText = data.temperature;
                    document.getElementById('pressure').innerText = data.pressure;
                    document.getElementById('oil_level').innerText = data.oil_level;
                });
        }

        // Обновление состояния насоса
        function updatePump(response) {
            response.json().then(data => {
                document.getElementById('pump_status').innerText = data.pump;
            });
        }

        // Автообновление каждые 2 секунды
        setInterval(updateData, 2000);
        updateData(); // сразу при загрузке
        </script>
      </body>
    </html>
    """
    return render_template_string(html)

# Маршрут для данных датчиков
@rasp.route("/sensors")
def sensors_route():
    return jsonify(get_sensor_data())

# Маршруты для управления насосом
@rasp.route("/pump/on")
def pump_on_route():
    turn_on()
    return jsonify({"pump": pump_state["status"]})

@rasp.route("/pump/off")
def pump_off_route():
    turn_off()
    return jsonify({"pump": pump_state["status"]})

if __name__ == "__main__":
    rasp.run(host="0.0.0.0", port=5000)
