from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Bakery Website</h1><p>Fresh cakes and pastries, baked with love!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

