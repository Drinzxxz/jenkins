from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Welcome to your first web app."

if __name__ == '__main__':
    app.run(debug=True)