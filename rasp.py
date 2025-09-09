from flask import Flask

rasp = Flask(__name__)

@app.route("/")
def index():
    return "Запуск flask"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
