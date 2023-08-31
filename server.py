from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Define mapping of routes to backend services
backend_services = {
    '/service1': 'http://127.0.0.1:5001/service1',
    '/service2': 'http://127.0.0.1:5002/service2',
    '/service3': 'http://127.0.0.1:5003/service3'
}

# Route to handle incoming requests and forward to backend services
@app.route('/<path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_gateway(path):
    if path in backend_services:
        backend_url = backend_services[path]
        response = requests.request(
            method=request.method,
            url=backend_url + '/' + request.path,
            headers=request.headers,
            data=request.data
        )
        return Response(response.content, status=response.status_code, content_type=response.headers['content-type'])
    else:
        return Response('Route not found' + path, status=404)

if __name__ == '__main__':
    app.run(port=5000)