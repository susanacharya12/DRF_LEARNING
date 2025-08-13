# Day 1: Serializers and Serialization in Django REST Framework

## Overview
Today, I explored **Serializers** and **Serialization** in Django REST Framework (DRF), taking my first step toward building APIs.

## What I Learned
- **Serialization**: Converting Django model instances into JSON for APIs.
- **Serializer Class**: Created for a simple model with fields:
  - `name`
  - `roll`
  - `city`
- **API Implementation**:
  - Built basic API endpoints to **fetch** and **post** personal details.
  - Tested successfully using **Postman** with `GET` and `POST` requests.

## Key Files
- `models.py` – Defines the Student model.
- `serializers.py` – Serializer class for the Student model.
- `views.py` – Function-based API views for GET and POST requests.
- `urls.py` – URL routing for the API endpoints.

## Takeaways
- Understanding serializers is **crucial** for building APIs with DRF.
- Data flows cleanly from the database to JSON responses, forming the foundation of web APIs.

## Next Steps
- Explore **Class-Based Views** and **Generic Views**.
- Learn about **authentication** and **permissions** to secure APIs.

### Hashtags
#Django #DjangoRESTFramework #DRF #Python #WebDevelopment #API
