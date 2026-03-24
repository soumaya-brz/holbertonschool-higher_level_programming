from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:

                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '')
    prod_id = request.args.get('id', type=int)
    error = None
    products_list = []

    if source == 'json':
        products_list = read_json('products.json')
    elif source == 'csv':
        products_list = read_csv('products.csv')
    else:
        error = "Wrong source"
        products_list = []

    if not error and prod_id is not None:

        filtered = [p for p in products_list if p['id'] == prod_id]
        if filtered:
            products_list = filtered
        else:
            products_list = []
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
