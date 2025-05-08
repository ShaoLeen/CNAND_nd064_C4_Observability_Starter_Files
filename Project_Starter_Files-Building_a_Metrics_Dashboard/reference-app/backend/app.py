import time
from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

import pymongo
from flask_pymongo import PyMongo

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({"service.name": "backend-service"}))
)
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    collector_endpoint="http://hotrod-collector.default.svc.cluster.local:14268/api/traces"
)

span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.0")

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)


@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(response=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal Server Error"), 500

@app.route('/error')
def cause_error():
    raise Exception("Simulated server error")

def do_db_query():
    time.sleep(0.1)
    return {"db": "fake-result"}

def transform_data(data):
    time.sleep(0.2)
    return {"transformed": True, "input": data}

# The traced route
@app.route("/span")
def my_process():
    with tracer.start_as_current_span("step_1_db_query"):
        result = do_db_query()

    with tracer.start_as_current_span("step_2_data_transform"):
        final = transform_data(result)

    return jsonify({"status": "done", "output": final})

if __name__ == "__main__":
    app.run()
