# 🛒 Flask Marketplace App

This is a simple Flask-based marketplace web application where users can register, log in, purchase items from a market, and manage their owned items. The app uses SQLite as the database and implements user authentication and password security with Flask-Login and bcrypt.

---

## 🔧 Features

- User registration and login/logout
- Secure password hashing
- Flash message notifications
- Marketplace to view and purchase items
- Sell owned items back to the market
- Profile page with password update option
- Bootstrap-based responsive UI

---

## 🖥️ Tech Stack

- Python 3.x
- Flask
- Flask-WTF
- Flask-Login
- SQLAlchemy (with SQLite)
- Bootstrap 4
- HTML / Jinja2 templates

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lalitaditya04/FlaskProj.git
   cd FlaskProj
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python run.py
   ```

5. Open the app in your browser at `http://127.0.0.1:5000`.

---

## 📁 Project Structure

```
FlaskProj/
│
├── market/
│   ├── templates/
│   │   ├── includes/
│   │   │   ├── items_modals.html
│   │   │   └── owned_items_modals.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── market.html
│   │   ├── profile.html
│   │   └── register.html
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
├── README.md
├── requirements.txt
└── run.py
```

---

## 🔒 Security

- Passwords are securely hashed using `bcrypt`.
- Only authenticated users can access the market or profile pages.

---

## ✍️ Author

**Lalit Aditya M**

Feel free to reach out or fork the project and build on it!

---
