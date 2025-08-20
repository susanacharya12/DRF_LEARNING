# Django REST Framework Serializer Relationships & CRUD

This project demonstrates how to use **serializer relationships** in Django REST Framework (DRF) and perform CRUD operations on related models. You can test all endpoints using Postman.

## 1. Setup Project

### Create virtual environment

### Install dependencies

### Start Django project & app

## 2. Configure settings.py

* Add rest\_framework and apiapp to INSTALLED\_APPS
* Configure REST Framework settings as needed

## 3. Models with Relationships

* Create models with relationships (OneToOne, ForeignKey, ManyToMany)
* Example: Employee and Department, where Employee has ForeignKey to Department
* Make migrations and migrate

## 4. Serializers

* Create serializers for related models
* Use `PrimaryKeyRelatedField`, `StringRelatedField`, or nested serializers to define relationships

## 5. Views

* Create ModelViewSets for each model
* Global permissions can be set if using JWT or other authentication

## 6. URLs

### App URLs

* Register ModelViewSets with DefaultRouter

### Project URLs

* Include app URLs
* Add authentication endpoints if needed

## 7. Apply Migrations & Create Superuser

## 8. Testing with Postman

### CRUD Operations

* GET, POST, PUT/PATCH, DELETE endpoints for related models
* Include related fields in payloads when creating or updating

### Authentication (optional)

* If JWT or token authentication is used, add Authorization header

## Features

* Demonstrates serializer relationships in DRF
* CRUD operations for related models
* Nested or related serializers for proper API responses
* Testable using Postman
