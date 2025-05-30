from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.0")

@app.route("/")
def homepage():
    return render_template("main.html")

@app.route('/trigger-error')
def trigger_error():
    raise Exception("Intentional 500 error for testing")

if __name__ == "__main__":
    app.run()
