from app import app

client = app.test_client()


# -----------------------------
# TEST HOME ROUTE
# -----------------------------
def test_home():

    response = client.get("/")

    assert response.status_code == 200


# -----------------------------
# TEST GET ITEMS
# -----------------------------
def test_get_items():

    response = client.get("/items")

    assert response.status_code == 200


# -----------------------------
# TEST ADD ITEM
# -----------------------------
def test_add_item():

    response = client.post(
        "/items",
        json={
            "name": "Laptop",
            "quantity": 5
        }
    )

    assert response.status_code == 201


# -----------------------------
# TEST PRODUCT API
# -----------------------------
def test_product_api():

    response = client.get(
        "/product/3274080005003"
    )

    assert response.status_code == 200