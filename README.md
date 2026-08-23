# Building Portfolio Project Using Django 6.1 - Real World Project: A Master For Beginners

This project is a comprehensive guide to building a professional portfolio application from scratch using **Django 6.1**. 

## 🚀 Project Overview
* **Built from Scratch:** Developed entirely from the ground up utilizing a raw HTML template downloaded from ThemeWagon, heavily modified to suit production-ready project requirements.
* **Structured Learning:** The entire curriculum is divided into three progressive tiers: **Beginner**, **Intermediate**, and **Advanced**. 
* **Current Phase:** This repository represents the **Beginner Level** foundation.

## 📖 Localization & Documentation
* **Indonesian Textbook:** Every micro-step of the development process is fully documented in an Indonesian-language book, specifically crafted to empower the younger generation of Indonesian developers.
* **Global Access:** While the textbook is in Indonesian, all project configurations, codebase documentations, and repository details are written in English. This ensures the project remains universally accessible and easy to follow for global learners.

## 📄 Beginner Level Details
For a step-by-step breakdown, progress tracking, and specific implementation notes for this beginner phase, please refer directly to the [jurnal.md](./jurnal.md) file.

## Project structure

```bash
.
|-- README.md
|-- apps
|   `-- portfolio
|       |-- __init__.py
|       |-- admin.py
|       |-- apps.py
|       |-- migrations
|       |-- models.py
|       |-- tests.py
|       |-- urls.py
|       `-- views.py
|-- config
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- db.sqlite3
|-- journal.md
|-- manage.py
|-- requirements.txt
|-- static
|   `-- assets
|-- templates
|   `-- portfolio
|       |-- about.html
|       |-- contact.html
|       |-- home.html
|       |-- portfolio.html
|       |-- services.html
|       |-- skills.html
|       `-- testimoni.html
`-- venv31361
    |-- Include
    |-- Lib
    |   `-- site-packages
    |-- Scripts
    `-- pyvenv.cfg
```

## 🚀 Key Features
* **Full CRUD Operations:** Seamless data management (Create, Read, Update, Delete).
* **Responsive Design:** Optimized layout for all screen sizes and mobile devices.

## 🛠️ Prerequisites & Technologies
* Python 3.13
* Django 6.1
* Database (SQLite)

## 📦 Installation & Setup Guide

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/ingskillsetstraining/iportfolio-beginner
cd iportfolio-beginner
```

### 2. Create & Activate a Virtual Environment
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries using the existing `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
*(Note: If there are any schema modifications, run `python manage.py makemigrations` first).*
```bash
python manage.py migrate
```

### 5. Start the Local Development Server
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0`

## 👥 Contributors
* **INGSkillSetsTraining** - [@ingskillsetstraining](https://github.com/ingskillsetstraining)


