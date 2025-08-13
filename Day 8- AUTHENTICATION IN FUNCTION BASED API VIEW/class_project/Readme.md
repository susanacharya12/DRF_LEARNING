# Day 8: Authentication & Permissions in Function-Based Views

## Overview
Today, I learned how to secure APIs in **Function-Based Views (FBVs)** by combining **authentication** and **permissions** in Django REST Framework (DRF).

- **Authentication** answers: Who are you?  
- **Permissions** answer: Are you allowed to do this?

DRF makes it simple to apply these security layers using built-in decorators, allowing only the right users to access or modify data.

## What I Learned
- DRF supports multiple authentication types:
  - **Basic Authentication**
  - **Session Authentication**
  - **JWT Authentication**
- Permissions control access to endpoints:
  - `AllowAny` – Open to all users.
  - `IsAuthenticated` – Only logged-in users can access.
  - `IsAdminUser` – Only admin users can access.
  - `IsAuthenticatedOrReadOnly` – Anyone can read; only authenticated users can write.
- Combining **authentication** and **permissions** ensures sensitive data stays safe.

## Takeaways
- Security is **essential** for professional API development.
- Function-Based Views can be secured effectively with DRF decorators and permission classes.

### Hashtags
#Django #DjangoRESTFramework #DRF #Authentication #Permissions #Python #WebDevelopment #APISecurity
