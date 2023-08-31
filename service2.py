from flask import Flask

app = Flask(__name__)

@app.route('/service2', methods=['GET'])
def service2():
    return 'Hello from Service 2!'

if __name__ == '__main__':
    app.run(port=5002)