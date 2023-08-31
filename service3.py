from flask import Flask

app = Flask(__name__)

@app.route('/service3', methods=['GET'])
def service3():
    return 'Hello from Service 3!'

if __name__ == '__main__':
    app.run(port=5003)