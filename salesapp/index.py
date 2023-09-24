import math

from flask import render_template, request
from salesapp import app
import utils

@app.route("/")
def home():
    cates = utils.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    page = request.args.get('page', 1)

    counter = utils.count_products()
    products = utils.load_products(cate_id=cate_id, kw=kw, page=int(page))

    return render_template('index.html', categories=cates, products=products,
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))

@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    products = utils.load_products(cate_id=cate_id, kw=kw, from_price=from_price, to_price=to_price)

    return render_template('products.html', products=products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)

    return render_template('product_detail.html',product=product)

if __name__ == '__main__':
    from salesapp.admin import *
    app.run(debug=True)