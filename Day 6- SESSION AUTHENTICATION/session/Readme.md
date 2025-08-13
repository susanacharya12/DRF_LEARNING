# Day 6: Session Authentication & Built-in Permissions in Django REST Framework

## Overview
Today, I explored **Session Authentication** and various built-in **permission classes** in Django REST Framework (DRF) to secure APIs and control access.

## What I Learned

### Session Authentication
- Enabled Django’s login/logout system for API testing using the **browsable API interface**.
- Useful for managing user sessions in a web application context.

### Built-in Permissions in DRF
- `IsAuthenticated` – Only logged-in users can access.
- `IsAdminUser` – Only admin users can access.
- `IsAuthenticatedOrReadOnly` – Anyone can read; only authenticated users can write.
- `AllowAny` – No restrictions; public access.
- `DjangoModelPermissions` – Uses Django's model-level **add, change, delete, and view** permissions.

## Takeaways
- Session Authentication and permission classes provide a **layer of security** for APIs.
- These tools make it easier to create **secure and scalable APIs** for real-world applications.

## Next Steps
- Day 7: Learn **Custom Permissions** in DRF for more flexible, role-based access control.

### Hashtags
#Django #DjangoRESTFramework #DRF #SessionAuthentication #Permissions #Python #WebDevelopment #100DaysOfCode #BackendDevelopment #APISecurity
