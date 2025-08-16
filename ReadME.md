# 📦 Inventory Logistics

An Inventory Management System built with Django 5, designed to help businesses efficiently track their products, stock levels, suppliers, and transactions (stock in & stock out).

# ✨ Features

✅ Manage categories and organize products

✅ Add and update products with stock quantity, price, and reorder levels

✅ Record stock in (purchases/supplies received)

✅ Record stock out (sales, damages, or company use)

✅ Track suppliers and their contact details

✅ Simple dashboard with KPIs and inventory insights

✅ Secure authentication with Django's built-in auth system

✅ Styled using Bootstrap 5 & Crispy Forms for clean UI

# 🛠 Tech Stack

Backend: Django 5.1.1

Database: SQLite (default) – easily switchable to PostgreSQL/MySQL

Frontend: HTML, CSS, Bootstrap 5, Django Templates

Forms: Django Crispy Forms with Bootstrap 5

# 📂 Project Structure
Inventory_Logistics/
│── authsys/           # Authentication system
│── inventory/         # Core inventory app
│   ├── models.py      # Category, Product, StockIn, StockOut, Supplier
│   ├── views.py       # Class-based views for home, dashboard, reports
│   ├── urls.py        # Inventory endpoints
│── manage.py
│── requirements.txt
│── db.sqlite3         # Default database (development)

# ⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/inventory.git
cd inventory


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create a superuser (for admin access)

python manage.py createsuperuser


Run the server

python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

# 📊 Models Overview

Category → Groups products by type

Product → Stores details of each item (price, stock, reorder level)

StockIn → Tracks incoming stock from suppliers

StockOut → Tracks outgoing stock (sales, damages, company use)

Supplier → Stores supplier info & linked products

# 🔑 Default Routes
Route	Description
/	Index page
/home/	Home page (after login)
/dashboard/	Dashboard with KPIs
/add-item/	Add a new product
/reports/	View reports & analytics
/admin/	Django admin panel

🤝 Contributing

# Fork the project

Create your feature branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add feature')

Push to the branch (git push origin feature-name)

Open a Pull Request

# 📜 License

This project is licensed under the MIT License.