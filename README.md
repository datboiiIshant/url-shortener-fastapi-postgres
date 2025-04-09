URL Shortener API

A simple and lightweight **URL Shortener** built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This API allows users to convert long URLs into shortened versions and retrieve the original using the shortened identifier.

---

Features

- Shorten any valid URL
- Retrieve original URL using the ID
- Uses FastAPI for quick and efficient backend development
- PostgreSQL database with SQLAlchemy ORM

---

Tech Stack

- **FastAPI** – Web framework for building APIs
- **SQLAlchemy** – ORM for Python
- **PostgreSQL** – Relational Database
- **Uvicorn** – ASGI server for running FastAPI
- **Pydantic** – Data validation and serialization

---

How to run the project ?
1. Open your terminal and run <git clone <reporsitory_link>>
2. Create & Activate Virtual Environment: Write the following commands in your terminal ->
    1. python -m venv myenv
    2. Run the Activate script in <myenv/Scripts/activate> for Windows and <source myenv/bin/activate> for Linux/MacOS
3. Install Dependencies: <pip install -r requirements.txt>
4. PostgreSQL Setup:
    1. Ensure PostgreSQL is running and accessible.
    2. Run the command <CREATE DATABASE URL_Shortener;> to create a new DB.
    3. Then, update the URL_DATABASE string in database.py with your PostgreSQL username and password.
5. Run the application: <uvicorn main:app --reload>

---

Visit FastAPI Swagger UI for interactive API usage directly 
Link -> <http://127.0.0.1:8000/docs>

---

API Endpoints
    POST /URLs/?URL=<your_long_url> → returns shortened URL
    GET /URLs/{id} → returns original URL by ID

---