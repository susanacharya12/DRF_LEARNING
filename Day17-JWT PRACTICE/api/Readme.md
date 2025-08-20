# Django REST Framework JWT Authentication & Employee CRUD (ModelViewSet)

This project demonstrates JWT Authentication in DRF and a CRUD API for Employee model using ModelViewSet, fully protected using JWT tokens. You can test all endpoints using Postman.

## 1. Setup Project

### Create virtual environment

### Install dependencies

### Start Django project & app

## 2. Configure settings.py

* Add rest\_framework and apiapp to INSTALLED\_APPS
* Configure DEFAULT\_AUTHENTICATION\_CLASSES to JWTAuthentication
* Configure DEFAULT\_PERMISSION\_CLASSES to IsAuthenticated
* Optional: Configure token lifetime using SIMPLE\_JWT

## 3. Employee Model

* Create Employee model with fields: name, email, position, salary
* Make migrations and migrate

## 4. Serializer

* Create EmployeeSerializer with all fields

## 5. Views

* Create EmployeeViewSet using ModelViewSet
* Global JWT authentication applies, no need to set permission\_classes

## 6. URLs

### App URLs

* Register EmployeeViewSet with DefaultRouter

### Project URLs

* Include app URLs
* Add JWT endpoints: token obtain, refresh, verify

## 7. Apply Migrations & Create Superuser

## 8. Testing with Postman

### Obtain JWT Token

### Access Employee CRUD API

* GET, POST, PUT/PATCH, DELETE
* Use Authorization header with Bearer token

### Refresh Token

### Verify Token

## Features

* CRUD API for Employee using ModelViewSet
* JWT Authentication (access & refresh tokens)
* Global IsAuthenticated permission
* Fully testable in Postman
