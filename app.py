from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask Welcome API!'

if __name__ == '__main__':
    app.run(host='100.27.21.113')
