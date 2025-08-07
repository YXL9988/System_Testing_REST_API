> 👋 Hi, I'm Lynn — a QA Engineer transitioning into automation testing and SDET roles.  
> This project showcases my hands-on skills in building, testing, and automating RESTful APIs using Python, Flask, and Pytest.  
> I developed this as part of my portfolio to demonstrate my end-to-end understanding of backend systems and multi-layered test strategies.


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
* **Testing**: Python Unittest framework 
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
    git clone https://github.com/LynnLin/System_Testing_REST_API.git
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

Postman Testing with Newman (Optional CI Tool Integration)

To demonstrate compatibility with popular API testing tools, this project includes Postman test collections and environment variables for the full system flow.

You can automate and run these tests using Newman, the CLI companion for Postman. This setup is especially useful for CI/CD pipelines, enabling easy integration of API tests into build workflows.

Steps to Run Postman Tests with Newman in PyCharm:
1. Install Newman globally:
   ```bash
   npm install -g newman
2. Run locally from terminal:
   ```bash
   newman run "Stores REST API.postman_collection.json" -e "Stores REST API.postman_environment.json"

This adds another layer of end-to-end system testing, simulating real user flows outside the Python codebase.


---

### Acknowledgment

This project is inspired by the Udemy course **"Automated Software Testing with Python"**, taught by **Jose Salvatierra (Teclado)** :contentReference[oaicite:1]{index=1}.

I have customized and extended the original material by:

- Rewriting and enhancing the **README** for clarity and portfolio purposes.  
- Updating the **password hashing** implementation for better security.  
- Adjusting the **Postman test scripts** to reflect my project structure.  

This version is used solely for educational purposes and showcases my progress as a QA/SDET engineer-in-training.

---

## 👩‍💻 About the Author

**Lynn Lin**  
QA Engineer | SDET in Progress | Ex-S&P Fixed Income Analyst  

- 🔍 Passionate about quality, detail, and automation.
- 🛠️ Skilled in manual testing, API testing (Postman), SQL, and backend test design.
- 🚀 Currently expanding skill set into Python, Pytest,Playwright, Selenium, and CI/CD pipelines.
- 🌍 Open to global opportunities (remote / hybrid).

📫 Reach me on [LinkedIn] https://www.linkedin.com/in/yan-xi-lynn-l-19b27084
📧 Email: linyanxi915@gmail.com


>  This project is part of my QA/SDET portfolio. Feedback and collaboration are welcome!

