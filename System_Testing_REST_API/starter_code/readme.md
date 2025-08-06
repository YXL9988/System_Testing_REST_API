# Stores REST API - with Full Automation Test Suite

This project is a complete RESTful API built with Python and Flask. It provides backend services for a simple online store, allowing for the management of items and stores. The primary focus of this repository is to demonstrate a comprehensive, multi-layered automated testing strategy for a real-world API.

## Core Features

* **User Authentication**: Secure user registration (`/register`) and login (`/login`) endpoints using **JSON Web Tokens (JWT)** for authentication.
* **Protected Resources**: Core business logic (managing items and stores) is protected, requiring a valid JWT access token for all operations.
* **Item Management (CRUD)**: Full Create, Read, Update, and Delete functionality for items in the store.
* **Store Management (CRUD)**: Full Create, Read, Update, and Delete functionality for stores.

## Technology Stack

* **Backend**: Python, Flask, Flask-RESTful
* **Database**: Flask-SQLAlchemy (using SQLite in development)
* **Authentication**: Flask-JWT-Extended
* **Testing**: Pytest, Unittest
* **Password Security**: Werkzeug Security for password hashing

## Project Structure

<pre>
├── models/
│   ├── item.py          # Item database model
│   ├── store.py         # Store database model
│   └── user.py          # User model and password logic
├── resources/
│   ├── item.py          # Item & ItemList API endpoints
│   ├── store.py         # Store & StoreList API endpoints
│   └── user.py          # User Registration & Login APIs
├── tests/
│   ├── unit/            # Unit tests (models, logic)
│   ├── integration/     # Integration tests (API + DB)
│   └── system/          # End-to-end system tests
│       └── base_test.py # Sets up in-memory test DB
├── app.py               # Flask app initialization
├── run.py               # App entry point
└── requirements.txt     # Python dependencies
</pre>

## Testing Strategy

This project features a robust, multi-layered testing strategy to ensure code quality and reliability, mirroring the standard testing pyramid.

* **Unit Tests**: Located in `tests/unit`, these tests validate individual components, like model logic, in complete isolation.
* **Integration Tests**: Located in `tests/integration`, these tests cover the API flow, verifying that different components (API resources, database models, etc.) work together correctly.
* **System Tests**: Located in `tests/system`, these tests validate the complete, integrated system from an end-to-end perspective, simulating real user workflows.
* **Test Isolation**: A base test class (`base_test.py`) is used to create a fresh, in-memory SQLite database for **each test case**, guaranteeing that tests are independent and do not interfere with one another.
* **Comprehensive Coverage**: Tests cover not only successful "happy path" scenarios but also a wide range of error conditions, including invalid user input (`400`), unauthorized access (`401`), and missing resources (`404`).

## Setup and Usage

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/LynnLin/System_Testing_REST_API.git](https://github.com/LynnLin/System_Testing_REST_API.git)
    cd System_Testing_REST_API
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    The application will create a `data.db` (SQLite) file on its first run.
    ```bash
    python run.py
    ```
    The API will be running at `http://127.0.0.1:5000`.

5.  **Run the tests:**
    To execute the full test suite, simply run `pytest` from the project's root directory.
    ```bash
    pytest
    ```
