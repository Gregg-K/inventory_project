from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# -----------------------------
# FAKE DATABASE
# -----------------------------
inventory = []


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API"
    })


# -----------------------------
# CREATE ITEM
# -----------------------------
@app.route("/items", methods=["POST"])
def add_item():

    data = request.get_json()

    item = {
        "name": data["name"],
        "quantity": data["quantity"]
    }

    inventory.append(item)

    return jsonify({
        "message": "Item added successfully",
        "item": item
    }), 201


# -----------------------------
# GET ALL ITEMS
# -----------------------------
@app.route("/items", methods=["GET"])
def get_items():

    return jsonify(inventory)


# -----------------------------
# GET ONE ITEM
# -----------------------------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):

    if item_id >= len(inventory):
        return jsonify({
            "error": "Item not found"
        }), 404

    return jsonify(inventory[item_id])


# -----------------------------
# UPDATE ITEM
# -----------------------------
@app.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    if item_id >= len(inventory):
        return jsonify({
            "error": "Item not found"
        }), 404

    data = request.get_json()

    inventory[item_id].update(data)

    return jsonify({
        "message": "Item updated",
        "item": inventory[item_id]
    })


# -----------------------------
# DELETE ITEM
# -----------------------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    if item_id >= len(inventory):
        return jsonify({
            "error": "Item not found"
        }), 404

    deleted_item = inventory.pop(item_id)

    return jsonify({
        "message": "Item deleted",
        "item": deleted_item
    })


# -----------------------------
# EXTERNAL API ROUTE
# -----------------------------
@app.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):

    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}.json"

    response = requests.get(
        url,
        auth=("off", "off")
    )

    data = response.json()

    # Product found
    if data["status"] == 1:

        product = data["product"]

        return jsonify({
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "quantity": product.get("quantity")
        })

    # Product not found
    return jsonify({
        "error": "Product not found"
    }), 404


# -----------------------------
# RUN FLASK APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)