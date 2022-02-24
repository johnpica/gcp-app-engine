from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello, World! v1'


if __name__ == '__main__':
    app.run(debug=True)