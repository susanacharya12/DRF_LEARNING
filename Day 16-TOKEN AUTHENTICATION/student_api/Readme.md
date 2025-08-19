# Django REST Framework Token Authentication

This project demonstrates how to implement **Token Authentication** in Django REST Framework (DRF) and perform CRUD operations (**POST, GET, PUT, PATCH, DELETE**) using Postman.




---

## Features

- User authentication using DRF **Token Authentication**  
- CRUD operations for a simple `Student` model  
- Protected API endpoints  
- Example usage with Postman  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/drf-token-auth.git
cd drf-token-auth
Create a virtual environment and activate it:
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
Install dependencies:
pip install django djangorestframework djangorestframework-simplejwt
Run migrations:
python manage.py migrate
Create a superuser:
python manage.py createsuperuser
