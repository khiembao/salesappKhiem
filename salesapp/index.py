
from flask import render_template
from salesapp import app
import utils

@app.route("/")
def home():
    cates = utils.load_categories()

    return render_template('index.html', categories = cates)

if __name__ == '__main__':
    app.run(debug=True)