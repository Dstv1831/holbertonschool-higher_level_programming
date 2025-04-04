from flask import Flask, request, render_template
import json, csv
import sqlite3

app = Flask(__name__)

def load_from_csv():
    with open("products.csv") as csv_products:
        data = list(csv.DictReader(csv_products))
        print(data)
    return data
            
def load_from_json():
    with open("products.json") as json_products:
        data = json.load(json_products)
        print(data)
    return data

def load_from_db():
    conn = sqlite3.connect('products.db')
    # Set the rows to be returned as dictionaries instead of tuples (default)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    # Creating a list of dictionaries for each row
    data = [dict(row) for row in rows]
    print(data)
    conn.close()
    return data


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

@app.route('/products')
def products():

    query = request.args.get('source')
    id = request.args.get('id', type=int)

    if not query :
        data = []
    elif query == "json":
        data = load_from_json()
    elif query == "csv":
        data = load_from_csv()
    elif query == "sql":
        data = load_from_db()
    else:
        data = "error 1"

    if id:
        data =[item for item in data if int(item['id']) == id ]
    
    return render_template('product_display.html', products = data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)