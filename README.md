# Inventory Management API

A Django REST Framework-based API for managing inventory, including items, categories, suppliers, customers, purchases, and sales.

## Features

- CRUD for categories, items, customers, suppliers
- Purchase orders (increase stock)
- Sales (record sales – stock update not yet implemented)
- RESTful endpoints with JSON responses

## Tech Stack

- Django 6.0
- Django REST Framework
- SQLite (development)
- WhiteNoise for static files

## Setup

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies:
pip install django djangorestframework whitenoise
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## API Endpoints

All endpoints are prefixed with `/api/`.

### Categories
- `GET /api/categories/` – list all categories
- `POST /api/categories/` – create a category (fields: `name`, `description`)
- `GET /api/categories/<id>/` – retrieve a category
- `PUT /api/categories/<id>/` – update a category
- `DELETE /api/categories/<id>/` – delete a category

### Items
- `GET /api/items/` – list all items
- `POST /api/items/` – create an item (fields: `name`, `category_id`, `stock_quantity`)
- `GET /api/items/<id>/` – retrieve an item
- `PUT /api/items/<id>/` – update an item
- `DELETE /api/items/<id>/` – delete an item

### Customers
- `GET /api/customers/` – list all customers
- `POST /api/customers/` – create a customer (fields: `name`, `email`, `phone`, `city`, `gender`)

### Suppliers
- `GET /api/suppliers/` – list all suppliers
- `POST /api/suppliers/` – create a supplier (fields: `name`, `email`, `phone`)

### Purchases
- `GET /api/purchases/` – list all purchases
- `POST /api/purchases/` – create a purchase (fields: `supplier_id`, `items` array)

### Sales
- `POST /api/sales/` – create a sale (fields: `customer_id`, `items` array)

## Deployment

This API is deployed on Render. Live URL: [https://nexus-inventory-kmn8.onrender.com](https://nexus-inventory-kmn8.onrender.com)

## Author

Mohammed Abdulmalik