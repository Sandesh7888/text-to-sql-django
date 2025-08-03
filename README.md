# 🧠 Text-to-SQL Django Web App

Convert natural language queries into SQL statements and execute them on a database using a simple and interactive web interface.

![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=flat&logo=django&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 Features

- 🔍 Convert English sentences to SQL queries
- 🗃️ Execute queries on a connected database (`db.sqlite3`)
- 🧾 View results directly in the browser
- 🔐 Admin panel with Django’s built-in interface
- 🧰 Uses `django-widget-tweaks` for form customization

---

## 🏗️ Tech Stack

- Python 3.x
- Django 3.0.5
- SQLite
- HTML/CSS (Django templates)
- django-widget-tweaks

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sandesh7888/text-to-sql-django.git
cd text-to-sql-django

# 2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
