from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'First Service! v1'


if __name__ == '__main__':
    app.run(debug=True)