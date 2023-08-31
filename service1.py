from flask import Flask

app = Flask(__name__)

@app.route('/service1', methods=['GET'])
def service1():
    return 'Hello from Service 1!'

if __name__ == '__main__':
    app.run(port=5001)