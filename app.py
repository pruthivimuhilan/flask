from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Deploying on Heroku - FPV'


if __name__ == '__main__':
    app.run(debug=True)