from prometheus_client import start_http_server, Summary, make_asgi_app, Counter

metricApp = make_asgi_app()
api_call_counter = Counter('api_calls', 'Api Calls', ['method', 'endpoint'])


def api_called(method, endpoint):
    api_call_counter.labels(method, endpoint).inc()
