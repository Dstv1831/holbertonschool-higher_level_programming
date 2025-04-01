from flask import Flask, render_template
import json

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

    with open("items.json") as json_file:
        data = json.load(json_file)

    return render_template('items.html', json_data = data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    # // "experiment_1": [],
    # // "experiment_2": ["",""],
    # // "experiment_3": [123, 30.5, true]