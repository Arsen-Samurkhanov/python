from flask import Flask, Response
import prometheus_client

REQUEST = prometheus_client.Counter(
    'request', 'Aplication request count', ['endpoint']
)

app = Flask('__name__')

@app.route('/metrics/')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype='text/plain; version=0.0.4; charset=utf-8'
    )

@app.route('/')
def index():
    REQUEST.labels(endpoint = '/').inc()
    return '<h1>Development Prometheus-backed App</h1>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)