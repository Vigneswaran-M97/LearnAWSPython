from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask Welcome API Test!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
