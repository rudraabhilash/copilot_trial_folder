# Starter Flask web app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Web Development!'

if __name__ == '__main__':
    app.run(debug=True)
