from flask import Flask
import logging
from prometheus_flask_exporter import PrometheusMetrics
import logging_loki


handler = logging_loki.LokiHandler(
    url="http://loki:3100/loki/api/v1/push", 
    tags={"application": "my-app"},
    version="1",
)
app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

@app.route('/')
def home():
    logger.info('Received request on home page')
    return 'Hello, Monitoring!'

@app.route('/error')
def error():
    logger.error('Simulated error occurred')
    return 'Error simulated', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
