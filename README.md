# Learning Django REST Framework (DRF) – Journey 🚀 

Welcome to my  learning journey of Django REST Framework (DRF) 
This repository documents the key concepts, projects, and hands-on practice I completed each day while learning to build robust APIs with Django.

---

## Day 1: Serializers and Serialization
- Explored **serializers** to convert Django models into JSON for APIs.
- Built a basic API with **GET** and **POST** endpoints.
- Learned the foundations of modern web API development.

**Key Files:** `models.py`, `serializers.py`, `views.py`, `urls.py`  

---

## Day 2: CRUD Operations with Function-Based Views
- Implemented full **CRUD** operations in Function-Based Views.
- Tested APIs thoroughly with **Postman**:
  - GET, POST, PUT, DELETE
- Learned how to structure FBV APIs efficiently.

**Key Files:** `models.py`, `serializers.py`, `views.py`, `urls.py`  

---

## Day 3: Class-Based Views (APIView)
- Built CRUD endpoints using **APIView** for better control.
- Utilized **ModelSerializers** to reduce boilerplate code.
- Handled status codes and errors cleanly for better API communication.

**Tech Stack:** Django, DRF, APIView, ModelSerializer  

---

## Day 4: Concrete Generic Views
- Leveraged DRF’s **Concrete Generic Views** for simplified CRUD:
  - `CreateAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`, `ListAPIView`
  - Combined views like `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`
- Built mini projects like an **Expense API** using these views.

---

## Day 5: Authentication & Permissions
- Explored **Basic Authentication** and DRF **permission classes**:
  - `AllowAny`, `IsAuthenticated`, `IsAdminUser`
- Learned how authentication and permissions secure APIs.

---

## Day 6: Session Authentication & Built-in Permissions
- Implemented **Session Authentication** using Django login/logout.
- Learned built-in permission classes:
  - `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`, `AllowAny`, `DjangoModelPermissions`
- Created secure and scalable APIs with proper access control.

---

## Day 7: Custom Permissions
- Learned to create **custom permissions** for more flexible, role-based API access.
- Enhanced control over who can perform specific actions in the API.

---

## Day 8: Authentication & Permissions in Function-Based Views
- Applied **authentication** and **permission classes** to Function-Based Views:
  - Authentication types: Basic, Session, JWT
  - Permissions: `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`
- Protected endpoints to ensure only authorized users can access or modify data.

---

## Day 9: Nested Serializers
- Used **nested serializers** to serialize related models (One-to-Many, Many-to-Many).
- Made APIs **clean, organized, and scalable** for complex data structures.

---

## Day 10: Filtering
- Implemented **basic filtering** using query parameters.
- Allowed users to fetch specific data without creating multiple endpoints.
- Enhanced API usability by providing **targeted data retrieval**.

---

## Day 11: Search Filters
- Explored **SearchFilter** in DRF.
- Enabled users to search across one or more fields efficiently.
- Made APIs more **interactive and user-friendly**.

---

## Day 12: CRUD with ViewSets and ModelViewSet
- Built CRUD operations using **ViewSets** and **ModelViewSet** for efficiency.
- Combined with routers to automatically generate endpoints.
- Reduced boilerplate and created **maintainable, scalable APIs**.

---

## Day 13: Pagination
- Explored **Pagination** to efficiently manage large datasets in APIs.
- DRF pagination styles:
  - `PageNumberPagination` – Splits data by page number.
  - `LimitOffsetPagination` – Uses limit and offset parameters.
  - `CursorPagination` – Provides stable ordering for large datasets.
- Improved **performance** and **user experience** by delivering data in manageable chunks.

---


## Day 14: LimitOffsetPagination with Hostel Model
- Created a Hostel model with fields such as name, owner_name, and location.
- Implemented LimitOffsetPagination globally in settings.py:
- limit → Specifies how many records to return.
- offset → Specifies the starting point in the dataset.
- Tested the API by fetching hostel records with different limits and offsets.
- Learned how LimitOffsetPagination provides more flexibility for client-side data navigation.
---

## Day 15: Serializer Relationships
- Explored serializer relationships to handle related models in DRF.
- Implemented nested serializers for one-to-many and many-to-many relationships:
- Built APIs to fetch related data cleanly:
- Tested CRUD operations with Postman including related data:
- GET, POST, PUT, PATCH, DELETE
- Learned how serializer relationships make APIs clean, organized, and scalable.
- Key Files: models.py, serializers.py, views.py, urls.py

## Day 16: Token Authentication
- Implemented Token Authentication to secure APIs.
- Used DRF's built-in token authentication system:
- Endpoint to obtain token: /api-token-auth/
- Token is required in Authorization header as Bearer <token> to access protected APIs.
- Tested all CRUD operations with Postman using the token:
- GET, POST, PUT, PATCH, DELETE
- Learned how token authentication provides stateless, secure access to APIs.
- Key Files: urls.py, views.py, settings.py


## Day 17: JWT Authentication
- CRUD API for Employee using ModelViewSet
- JWT Authentication (access & refresh tokens)
- Global IsAuthenticated permission
- Fully testable in Postman

---

## Summary
 I progressed from **basic serializers** to **secure, scalable, and professional APIs** with Django REST Framework.  
I gained hands-on experience with:

- Function-Based and Class-Based Views
- Generic Views and ModelViewSet
- Authentication, Permissions, and Custom Permissions
- Nested Serializers, Filtering, Search, and Pagination
- Token Authentication To Authenticate Api
- Serializers Relationship
- JWT Authentication

- API testing with Postman and practical mini-projects  

This journey strengthened my understanding of **modern web API development with Django** and prepared me to build production-ready applications.

---

## Connect with Me
- **GitHub:** [susanacharya12](https://github.com/susanacharya12)  
- **LinkedIn:** [Susan Acharya](https://www.linkedin.com/in/susan-acharya1618/)
