from flask import Flask, request, render_template
import json, csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():

    with open("items.json") as json_items:
        data = json.load(json_items)

    return render_template('items.html', json_data = data)

@app.route('/product')
def products():

    source = request.args.get('source')
    id = request.args.get('id')

    if source == "json":
        with open("products.json") as json_products:
            data = json.load(json_products)
            
    elif source == "csv":
        with open("products.csv") as csv_products:
            data = csv.reader(csv_products)
    
    print(data)
    # if id:

    # else:
    # data = "No Products where found"
    return render_template('product_display.html', products = data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)