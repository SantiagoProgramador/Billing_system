# Billing System Demo

This is a small demo of a billing system created with Django. The project includes basic features such as client management and billing creation. The purpose of this demo is to showcase a simple implementation using Django, Bootstrap, and templates.

## Features
- Create and manage clients
- Create invoices (basic setup)
- Simple and responsive UI with Bootstrap

## Prerequisites
Before you begin, make sure you have the following installed:
- Python (version 3.9 or later)
- pip (Python package manager)

## Installation (Local Setup)
Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SantiagoProgramador/Billing_system
   cd Billing_system

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Set up environment variables**:
    Create a .env file in the project directory with the following content:
  
    ```bash
    SECRET_KEY=your-secret-key
    DEBUG=True
    
  - Apply migrations:

  ```bash
    python manage.py makemigrations
    python manage.py migrate
    Run the server:

  ```bash
    python manage.py runserver

5. Access the application:
  Open your browser and go to http://127.0.0.1:8000/.