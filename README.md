# Backend Capstone Project

A backend API built with **Node.js**, **Express**, and **MongoDB**, following clean architectural principles.

##  Project Purpose
This API is designed as part of a backend capstone, following a structured 5-week plan:
- Week 1: Planning & Setup  
- Week 2: Core API Development  
- Week 3: Authentication & Advanced Features  
- Week 4: Testing, Optimization & Documentation  
- Week 5: Deployment & Final Polish  

---

##  Tech Stack
- Python 3.13
- Django 5.2
- Django REST Framework
- Django REST Framework Simple JWT
- SQLite (default) / other DB supported

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-project-folder>

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run Development Server
python manage.py runserver


Server runs at http://127.0.0.1:8000/.

Authentication (JWT)
Obtain Token
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'


Response:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

Use Token

Include the access token in all API requests:

curl -H "Authorization: Bearer <access_token>" \
http://127.0.0.1:8000/api/properties/

API Endpoints
1. User Registration
POST /api/register/


Request Body:

{
  "username": "del",
  "email": "del@example.com",
  "password": "woakil123"
}


Response:

{
  "id": 1,
  "username": "del",
  "email": "del@example.com"
}

2. Properties CRUD
Create Property
curl -X POST http://127.0.0.1:8000/api/properties/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{
  "title": "Luxury Apartment in Lagos",
  "description": "A beautiful 3-bedroom apartment in a secure estate.",
  "property_type": "apartment",
  "address": "123 Victoria Island, Lagos",
  "price": "25000000.00",
  "is_available": true
}'

List Properties
curl -H "Authorization: Bearer <access_token>" \
http://127.0.0.1:8000/api/properties/

Update Property
curl -X PUT http://127.0.0.1:8000/api/properties/<property_id>/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Luxury Apartment",
  "description": "Updated description",
  "property_type": "apartment",
  "address": "123 Victoria Island, Lagos",
  "price": "26000000.00",
  "is_available": true
}'

Delete Property
curl -X DELETE http://127.0.0.1:8000/api/properties/<property_id>/ \
-H "Authorization: Bearer <access_token>"

3. Filtering, Searching, and Ordering

Search by title, type, or address:

curl -H "Authorization: Bearer <access_token>" \
"http://127.0.0.1:8000/api/properties/?search=apartment"


Order by price or creation date:

curl -H "Authorization: Bearer <access_token>" \
"http://127.0.0.1:8000/api/properties/?ordering=price"


Filter by property type, availability, or price (example using query params):

curl -H "Authorization: Bearer <access_token>" \
"http://127.0.0.1:8000/api/properties/?property_type=apartment&is_available=true"

Permissions & Ownership

Only the owner of a property can update or delete it.

Read-only access for all authenticated users on other users’ properties.

Implemented using IsOwnerOrReadOnly permission class.

Testing All in One Go (cURL)
# 1. Register User
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"username": "del", "email": "del@example.com", "password": "woakil123"}'

# 2. Obtain JWT Token
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "del", "password": "woakil123"}'

# 3. Create Property
curl -X POST http://127.0.0.1:8000/api/properties/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{"title": "Luxury Apartment","description":"3-bed","property_type":"apartment","address":"VI Lagos","price":"25000000","is_available":true}'

# 4. List Properties
curl -H "Authorization: Bearer <access_token>" \
http://127.0.0.1:8000/api/properties/

# 5. Update Property
curl -X PUT http://127.0.0.1:8000/api/properties/1/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{"title":"Updated Apartment","description":"Updated","property_type":"apartment","address":"VI Lagos","price":"26000000","is_available":true}'

# 6. Delete Property
curl -X DELETE http://127.0.0.1:8000/api/properties/1/ \
-H "Authorization: Bearer <access_token>"

Notes

Always include the Bearer token in the Authorization header for all property endpoints.

Existing properties in the database will not be accessible unless the JWT belongs to the owner.

Make sure to run migrations before testing.

Server runs at http://127.0.0.1:8000/ by default.

Author

Oladayo Aduragbemi Da-Silva
Email: oladayodasilva87@gmail.com


---

✅ This is **all-inclusive**:
- Setup instructions  
- JWT auth flow  
- CRUD operations  
- Search, filter, and ordering  
- Ownership & permissions  
- Ready-to-use cURL commands for **full testing**  
