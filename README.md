# Inventory Management System

A simple Flask REST API project for managing inventory items.

This project allows users to:

- Add inventory items
- View inventory items
- Update items
- Delete items
- Search products using the OpenFoodFacts API
- Interact with the API using a CLI program
- Run basic unit tests

---

# Technologies Used

- Python
- Flask
- Requests
- Pytest

---

# Project Structure

```plaintext
inventory_project/
│
├── app.py
├── cli.py
├── test_app.py
├── requirements.txt
├── README.md
└── venv/
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
```

Enter project folder:

```bash
cd inventory_project
```

---

## 2. Create Virtual Environment

### Linux / Mac

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\Activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Start Flask Server

```bash
python app.py
```

The server will run on:

```plaintext
http://127.0.0.1:5000
```

---

# Running the CLI Program

Open a second terminal and activate the virtual environment again.

Run:

```bash
python cli.py
```

---

# API Endpoints

## Home Route

```http
GET /
```

---

## Get All Items

```http
GET /items
```

---

## Add Item

```http
POST /items
```

Example JSON body:

```json
{
  "name": "Laptop",
  "quantity": 5
}
```

---

## Get One Item

```http
GET /items/<item_id>
```

---

## Update Item

```http
PATCH /items/<item_id>
```

Example JSON body:

```json
{
  "quantity": 10
}
```

---

## Delete Item

```http
DELETE /items/<item_id>
```

---

## Search Product by Barcode

```http
GET /product/<barcode>
```

Example:

```http
GET /product/3274080005003
```

---

# Running Tests

Run:

```bash
pytest
```

---

# Example Barcode

Use this barcode to test the external API:

```plaintext
3274080005003
```

---

# Features Implemented

- Flask REST API
- CRUD Operations
- External API Integration
- CLI Interface
- Unit Testing
- Virtual Environment Setup

---

# Author

Greg