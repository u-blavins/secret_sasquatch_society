from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# Test JSON dictionary collection
items = [
    {
        "product_code": "PENB",
        "product_name": "Pen",
        "description": "Blue Pen",
        "stock-level": 57,
        "price": 0.99
    },
    {
        "product_code": "PENR",
        "product_name": "Pen",
        "description": "Red Pen",
        "stock-level": 60,
        "price": 0.99
    },
    {
        "product_code": "PENG",
        "product_name": "Pen",
        "description": "Green Pen",
        "stock-level": 59,
        "price": 0.99
    }
]

@app.route('/', methods=['GET'])
def home():
    return("<h1>This is a test</h1>"+
        "<p>This site is a prototype API for distant reading of science fiction novels.</p>")

@app.route('/api/v1/resources/items/all', methods=['GET'])
def item_all():
    return jsonify(items)

@app.route('/api/v1/resources/items', methods=['GET'])
def item_id():

    if "product_code" in request.args:
        product_code = str(request.args['product_code'])
    else:
        return jsonify(
            {
                "Info": "Error",
                "Message": "No 'product_code' field provided. Please specify a product code."
            }
        )
    for item in items:
        if product_code == item['product_code']:
            return jsonify(item)


app.run()