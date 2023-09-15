
from flask import render_template
from salesapp import app
import utils

@app.route("/")
def home():
    cates = utils.load_categories()

    return render_template('index.html', categories = cates)

@app.route("/products")
def product_list():
    products = utils.load_products()
    return render_template('products.html', products = products)

if __name__ == '__main__':
    app.run(debug=True)