# Day 5: Authentication & Permissions in Django REST Framework

## Overview
Today, I explored how Django REST Framework (DRF) handles **access control** using **authentication** and **permission classes**.

## What I Learned

### Authentication
- **Basic Authentication**: Sends credentials with each request.
  - Simple and easy for testing.
  - Not recommended for production environments.

### Permissions
- DRF provides built-in permission classes to control access:
  - `AllowAny`: Grants unrestricted access (useful for public endpoints).
  - `IsAuthenticated`: Only allows access to authenticated users.
  - `IsAdminUser`: Restricts access to admin users only.

## Takeaways
- Authentication and permissions are **essential for building secure APIs**.
- These tools allow scalable control over **who can access what** in your application.

## Next Steps
- Day 6: Dive deeper into **Session Authentication** and how Django manages user sessions.

### Hashtags
#100DaysOfCode #DRF #DjangoRESTFramework #Python #WebDevelopment
