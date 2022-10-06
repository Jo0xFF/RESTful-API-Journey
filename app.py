from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
	{
		"name": "3D Portrait Store",
		"items": [
			{
				"name": "Johnny Depp Portrait",
				"price": 19.99
			}
		]
	}
]

# Create a new store
@app.route("/store", methods=["POST"])
def create_store():
	request_data = request.get_json()
	new_store = {
			"name": request_data["name"],
			"items": [] 
	}
	stores.append(new_store)
	return jsonify(new_store)

# Get a certain Store /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
	for store in stores:
		if store["name"] == name:
			return jsonify(store)
	return jsonify({"Error": "we didn't find it"})

# Get a list of stores
@app.route("/store")
def get_stores():
	return jsonify({"stores": stores})

# Create an item in a specific store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
	requested_item = request.get_json()
	for store in stores:
		if store["name"] == name:
			new_item = {
					"name": requested_item["name"],
					"price": requested_item["price"]
			}

			return jsonify(new_item)
	return jsonify({"Error": "we didn't find the store!"})

# Get items from a store
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
	items_list = []
	for store in name:
		if store["name"] == name:
			items_list.append(store["items"])
	return jsonify({"items": items_list)



app.run(port=5000)