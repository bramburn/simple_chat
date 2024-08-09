# User API Endpoints
======================

## Overview
------------

The User API provides endpoints for managing user accounts.

## Endpoints
------------

### GET /users/

* **Description**: Retrieve a list of all users.
* **Permissions**: `IsAuthenticated`
* **Response**: A list of user objects in JSON format.

### GET /users/{user_id}/

* **Description**: Retrieve a user's profile information.
* **Permissions**: `IsAuthenticated`
* **Response**: A user object in JSON format.
* **Error**: `404 Not Found` if the user does not exist.

### POST /users/

* **Description**: Create a new user account.
* **Permissions**: `IsAuthenticated` todo: to add additional permission
* **Request Body**: A user object in JSON format.
* **Response**: A user object in JSON format.
* **Error**: `400 Bad Request` if the request is invalid.

### PUT /users/{user_id}/

* **Description**: Update a user's profile information.
* **Permissions**: `IsAuthenticated` todo: to add additional permission
* **Request Body**: A user object in JSON format.
* **Response**: A user object in JSON format.
* **Error**: `404 Not Found` if the user does not exist, `400 Bad Request` if the request is invalid.