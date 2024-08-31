# Flask User-Person API

This is a REST API built with Flask for managing users and their associated persons.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RobertoRuben/flask-user-person-api.git
   cd flask-user-person-api

2. Create a virtual environment:
   ```bash
    python -m venv .venv
3. Activate the virtual environment:
* On Windows:
   ```bash
    .venv\Scripts\activate
* On macOS/Linux
   ```bash
    source .venv/bin/activate
4. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
5. Run the application:
   ```bash
    python src/app.py
## Endpoints

### Person Endpoints

• `GET /personas` - Get all persons

• `GET /personas/<id>` - Get a person by ID

• `POST /personas` - Create a new person

• `PUT /personas/<id>` - Update a person by ID

• `DELETE /personas/<id>` - Delete a person by ID

### User Endpoints

• `GET /users` - Get all users

• `GET /users/<id>` - Get a user by ID

• `POST /users` - Create a new user

• `PUT /users/<id>` - Update a user by ID

• `DELETE /users/<id>` - Delete a user by ID

