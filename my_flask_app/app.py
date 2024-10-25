from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    products = [
        {'name': 'Product 1', 'image': 'product1.png'},
        {'name': 'Product 2', 'image': 'product2.png'},    
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

