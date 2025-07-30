Overview


The Children's Home Management System is a Flask-based web application designed to manage children's homes, including their details, associated children, photos, donations, reviews, visits, and volunteer registrations. It offers user authentication, admin functionalities, and secure data handling for a non-profit organization supporting children's homes. Built with SQLAlchemy, Flask-JWT-Extended, and Marshmallow, this project emphasizes scalability and security.

Developed collaboratively for a school assignment, it showcases robust API development and best practices.

Features
- User Management: Register users (name, email, password, phone) with auto-admin assignment for trusted domains (e.g., @unicef.org, @redcross.org).
- Admin Dashboard: View user/admins counts and manage promotions/demotions.
- Children's Homes: CRUD operations for homes, children, and photos (admin-restricted).
- Donations: Record and track donations with total amount visibility.
- Reviews: User-authored reviews with CRUD for personal entries.
- Visits: Schedule and view visits (admin-restricted).
- Volunteers: Register and manage volunteer profiles.
- Authentication: JWT-based login with role-based access control.

Technologies
- Backend: Flask, Python
- Database: SQLAlchemy (ORM) with PostgreSQL
- Authentication: Flask-JWT-Extended
- Serialization: Marshmallow (SQLAlchemySchema)
- Utilities: Custom decorators for admin and user access
- Environment: Python 3.12.3
- Dependencies: See requirements.txt

Project Structure

<pre> ```plaintext Back-end/ ├── app/ │ ├── __init__.py │ ├── models/ │ │ ├── __init__.py │ │ ├── children_home.py │ │ ├── user.py │ │ ├── donation.py │ │ ├── review.py │ │ ├── visit.py │ │ └── volunteer.py │ ├── schemas/ │ │ ├── __init__.py │ │ ├── home_schema.py │ │ ├── user_schema.py │ │ ├── donation_schema.py │ │ ├── review_schema.py │ │ ├── visit_schema.py │ │ └── volunteer_schema.py │ ├── controllers/ │ │ ├── __init__.py │ │ ├── admin_controller.py │ │ ├── auth_controller.py │ │ ├── home_controller.py │ │ ├── donation_controller.py │ │ ├── review_controller.py │ │ ├── user_controller.py │ │ ├── visitor_controller.py │ │ └── volunteer_controller.py │ └── config.py ├── utils/ │ ├── __init__.py │ ├── decorators.py │ ├── auth.py │ └── constants.py ├── migrations/ │ ├── versions/ │ └── env.py ├── .env ├── seed.py ├── manage.py ├── render.yaml ├── requirements.txt └── README.md ``` </pre>


Key Components
- Models: Use id = db.Column(db.Integer, primary_key=True, autoincrement=True) for unique, auto-incrementing IDs.
- Schemas: Leverage SQLAlchemySchema with auto_field(dump_only=True) for IDs and a Meta class for model mapping.
  python
  class UserSchema(SQLAlchemySchema):
      class Meta:
          model = User
          sqla_session = db.session
          load_instance = True
      id = auto_field(dump_only=True)
      name = auto_field()
      email = auto_field()
      phone_number = auto_field()
      role = auto_field()
  
- Utils:
  - decorators.py: admin_required decorator for admin-only endpoints.
  - auth.py: get_current_user decorator for authenticated user retrieval.
  - constants.py: Defines TRUSTED_ADMIN_DOMAINS (e.g., ['unicef.org', 'redcross.org']) and ALLOWED_PROMOTION_DOMAINS (e.g., ['gmail.com', 'yahoo.com']).
- Seeding: seed.py populates the database with initial data.

Installation
1. Clone the Repository:
   bash
   git clone https://github.com/Children-s-Home-Collective/Back-end.git
   cd Back-end
   

2. Set Up Pipenv:
   bash
   pip install pipenv
   pipenv install --dev
   pipenv shell
   

3. Install Dependencies:
   bash
   pip install -r requirements.txt
   

4. Configure Environment:
   Create/edit .env:
   env
   FLASK_APP=manage.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///childrens_home.db
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-jwt-secret-key
   

5. Initialize Database:
   bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   

6. Seed the Database:
   bash
   python seed.py
   

7. Run the Application:
   bash
   flask run
   
   The API is available at http://localhost:5000.

API Endpoints
Authentication
- POST /auth/login: Authenticate and get JWT token.
  - Request: {"email": "user@example.com", "password": "Passw0rd!"}
  - Response: {"user": {...}, "access_token": "...", "type": "Bearer"}

User Management
- POST /users/register: Register a user.
  - Request: {"name": "John Doe", "email": "john@example.com", "password": "Passw0rd!", "phone_number": "+254700123456"}
  - Response: {"user": {...}, "access_token": "...", "type": "Bearer"}
- GET /users/<user_id>: Get user details.

Admin Dashboard
- GET /admin/dashboard: View user/admins counts.
- GET /admin/admins: List admins.
- PATCH /admin/promote/<user_id>: Promote user to admin.
- PATCH /admin/demote/<user_id>: Demote admin to user.
- PATCH /admin/demote-all/<user_id>: Demote specific admin.

Children's Homes
- GET /homes: List all homes.
- GET /homes/<home_id>: Get home details.
- POST /homes: Create home (admin only).
  - Request: {"name": "Hope Home", "location": "Nairobi", "phone_number": "+254700123456", "email": "hope@home.org", "description": "A children home", "children": [{"first_name": "Alice", "last_name": "Smith", "age": 10, "gender": "F"}], "photos": [{"image_url": "http://example.com/photo.jpg"}]}
- PATCH /homes/<home_id>: Update home (admin only).
- DELETE /homes/<home_id>: Delete home (admin only).
- GET /homes/<home_id>/children: List children (admin only).
- GET /homes/<home_id>/children/<child_id>: Get child (admin only).
- GET /homes/<home_id>/photos: List photos.
- GET /homes/<home_id>/photos/<photo_id>: Get photo.

Donations
- POST /donations: Record donation.
  - Request: {"amount": 100, "donation_type": "cash", "home_id": 1}
- GET /donations: List donations (admin only).
- GET /donations/total: Get total amount.

Reviews
- POST /reviews: Create review.
  - Request: {"rating": 5, "comment": "Great home!", "home_id": 1}
- GET /reviews: List reviews.
- GET /reviews/<review_id>: Get review.
- PUT /reviews/<review_id>: Update own review.
- DELETE /reviews/<review_id>: Delete own review.

Visits
- POST /visitor: Schedule visit.
  - Request: {"full_name": "John Doe", "phone_number": "+254700123456", "day_to_visit": "2025-08-01", "home_id": 1, "number_of_visitors": 2}
- GET /visitor: List visits (admin only).
- GET /visitor/user/<user_id>: List user visits (admin only).

Volunteers
- POST /volunteers: Register volunteer.
  - Request: {"name": "Jane Smith", "email": "jane@gmail.com", "phone_number": "+254700123457", "description": "Experienced volunteer"}
- GET /volunteers: List volunteers (admin only).
- GET /volunteers/<volunteer_id>: Get volunteer.
- PUT /volunteers/<volunteer_id>: Update own profile.
- DELETE /volunteers/<volunteer_id>: Delete own profile.

Testing with Thunder Client
Use Thunder Client (VS Code extension) to test endpoints. Steps:

1. Setup:
   - Install Thunder Client.
   - Create ChildrensHomeAPI collection.
   - Set base URL to http://localhost:5000.

2. Test Authentication:
   - POST /auth/login
     - Method: POST
     - URL: http://localhost:5000/auth/login
     - Body: {"email": "user@example.com", "password": "Passw0rd!"}
     - Response: 200 OK
       json
       {
           "user": {
               "id": 1,
               "name": "John Doe",
               "email": "user@example.com",
               "phone_number": "+254700123456",
               "role": "user",
               "created_at": "2025-07-30T15:15:00+03:00"
           },
           "access_token": "<token>",
           "type": "Bearer"
       }
       
     - Save access_token.

3. Test User Registration:
   - POST /users/register
     - Method: POST
     - URL: http://localhost:5000/users/register
     - Body: {"name": "Jane Doe", "email": "jane@example.com", "password": "Passw0rd!", "phone_number": "+254700123457"}
     - Response: 201 Created
       json
       {
           "user": {
               "id": 2,
               "name": "Jane Doe",
               "email": "jane@example.com",
               "phone_number": "+254700123457",
               "role": "user",
               "created_at": "2025-07-30T15:15:00+03:00"
           },
           "access_token": "<token>",
           "type": "Bearer"
       }
       

4. Test Creating a Home:
   - POST /homes
     - Method: POST
     - URL: http://localhost:5000/homes
     - Headers: Authorization: Bearer <token> (optional)
     - Body:
       json
       {
           "name": "Hope Home",
           "location": "Nairobi",
           "phone_number": "+254700123456",
           "email": "hope@home.org",
           "description": "A children home",
           "children": [{"first_name": "Alice", "last_name": "Smith", "age": 10, "gender": "F"}],
           "photos": [{"image_url": "http://example.com/photo.jpg"}]
       }
       
     - Response: 201 Created
       json
       {
           "id": 1,
           "name": "Hope Home",
           "location": "Nairobi",
           "phone_number": "+254700123456",
           "email": "hope@home.org",
           "description": "A children home",
           "created_at": "2025-07-30T15:15:00+03:00",
           "children": [{"id": 1, "first_name": "Alice", "last_name": "Smith", "age": 10, "gender": "F", "created_at": "2025-07-30T15:15:00+03:00"}],
           "photos": [{"id": 1, "image_url": "http://example.com/photo.jpg"}]
       }
       

5. Notes:
   - jwt_required and admin_required are commented out; add headers for production.
   - Use admin tokens (e.g., @unicef.org) for restricted endpoints.

Notes
- Authentication: Uses JWT (Authorization: Bearer <token>); enable decorators for production.
- ID Handling: IDs are auto-incremented (autoincrement=True) and dump_only=True in schemas.
- Email Domains: TRUSTED_ADMIN_DOMAINS for auto-admins; ALLOWED_PROMOTION_DOMAINS for promotions.
- Error Handling: Covers ValidationError, SQLAlchemyError, and more.

Future Improvements
- Google Maps: Integrate API to show home locations.
- M-Pesa/PayPal: Add payment options for donations.
- Pagination: Enhance GET endpoint efficiency.
- Email Notifications: Send confirmations for visits, volunteers, donations.
- Frontend: Build a React app with Tailwind CSS.

Troubleshooting
- DB Errors: Check DATABASE_URL in .env and run flask db upgrade.
- JWT Errors: Verify JWT_SECRET_KEY and token validity.
- Schema Issues: Ensure id is dump_only=True.
- Testing: Review logs for 500 errors.


