from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>VERSION 2: The Update Worked! 🚀</h1>"

if __name__ == "__main__":
    # 0.0.0.0 means "listen to requests from outside the container"
    app.run(host='0.0.0.0', port=5000)