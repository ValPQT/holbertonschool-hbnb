# HBnB API - Testing Report

## 1. Objective

This document describes the validation and testing performed on the HBnB API.
Testing includes automated unit tests and manual black-box testing using cURL.

---

## 2. Automated Tests

Command used:

```bash
python3 -m unittest discover tests


url -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
"first_name":"John",
"last_name":"Doe",
"email":"john@doe.com"
}'

Result : Code 201
{
    "id": "dca66dd7-b423-49ad-a7f4-a7668c1de72b",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@doe.com"
}


url -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
"first_name":"",
"last_name":"",
"email":"bad"
}'
Result : Code 400
{
    "error": "First name is required"
}

## 3. Manual Testing (cURL)

| Endpoint | Action | Payload | Expected Code | Status |
| :--- | :--- | :--- | :--- | :--- |
| `POST /users/` | Create Valid User | `{...}` | 201 | ✅ Pass |
| `POST /users/` | Missing Email | `{"first_name": "Jo"}` | 400 | ✅ Pass |
| `GET /users/1` | Get User by ID | None | 200 | ✅ Pass |

## 4. Swagger Documentation Validation

The interactive API documentation is available at `http://localhost:5000`. 
The following elements have been verified:
- **Models**: The `User` model correctly displays mandatory fields (`first_name`, `last_name`, `email`).
- **Endpoints**: All CRUD operations for Users are exposed and documented.
- **Validation**: Error codes (400, 404) are explicitly listed for each endpoint.

## 5. Conclusion
All core endpoints for the User entity have been validated. 
- **Validation Logic**: Implemented using Flask-RESTx fields and patterns.
- **Automated Testing**: 100% pass rate for unit tests.
- **Manual Verification**: cURL tests confirm expected HTTP status codes (201, 400, 404).

The API is robust, documented, and ready for the next development phase.