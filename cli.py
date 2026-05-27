import requests

BASE_URL = "http://127.0.0.1:5000"

while True:

    print("\n=== Inventory Menu ===")
    print("1. View All Items")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Product Barcode")
    print("6. Exit")

    choice = input("Choose an option: ")

    # -----------------------------
    # VIEW ITEMS
    # -----------------------------
    if choice == "1":

        response = requests.get(f"{BASE_URL}/items")

        print(response.json())

    # -----------------------------
    # ADD ITEM
    # -----------------------------
    elif choice == "2":

        name = input("Enter item name: ")
        quantity = input("Enter quantity: ")

        item = {
            "name": name,
            "quantity": quantity
        }

        response = requests.post(
            f"{BASE_URL}/items",
            json=item
        )

        print(response.json())

    # -----------------------------
    # UPDATE ITEM
    # -----------------------------
    elif choice == "3":

        item_id = input("Enter item ID: ")

        new_quantity = input("Enter new quantity: ")

        updated_item = {
            "quantity": new_quantity
        }

        response = requests.patch(
            f"{BASE_URL}/items/{item_id}",
            json=updated_item
        )

        print(response.json())

    # -----------------------------
    # DELETE ITEM
    # -----------------------------
    elif choice == "4":

        item_id = input("Enter item ID: ")

        response = requests.delete(
            f"{BASE_URL}/items/{item_id}"
        )

        print(response.json())

    # -----------------------------
    # SEARCH BARCODE
    # -----------------------------
    elif choice == "5":

        barcode = input("Enter barcode: ")

        response = requests.get(
            f"{BASE_URL}/product/{barcode}"
        )

        print(response.json())

    # -----------------------------
    # EXIT
    # -----------------------------
    elif choice == "6":

        print("Goodbye!")
        break

    else:
        print("Invalid choice")