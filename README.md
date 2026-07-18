# student-management-api
# 🚀 FastAPI Student CRUD API

A simple RESTful API built with **FastAPI** that allows users to perform CRUD (Create, Read, Update, Delete) operations on student records. The project uses **Pydantic** for request validation and stores data in memory using a Python list.

## ✨ Features

- ➕ Create a new student
- 📋 Retrieve all students
- 🔍 Retrieve a student by ID
- ✏️ Update student details
- 🗑️ Delete a student
- ✅ Input validation with Pydantic
- 📧 Email validation using EmailStr
- 📖 Automatic interactive API documentation

---

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

## 📋 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
fastapi
uvicorn
pydantic
email-validator
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-student-crud-api.git
```

Navigate to the project directory:

```bash
cd fastapi-student-crud-api
```

Start the server:

```bash
uvicorn main:app --reload
```

> Replace **main** with your Python filename if different.

---

## 📖 API Documentation

Once the server is running, open:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/students` | Create a student |
| GET | `/students` | Get all students |
| GET | `/student/{student_id}` | Get student by ID |
| PUT | `/student/{student_id}` | Update student |
| DELETE | `/student/{student_id}` | Delete student |

---

## 📥 Example Request

### Create Student

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 20,
  "email": "john@example.com",
  "skills": [
    "Python",
    "FastAPI",
    "SQL"
  ]
}
```

---

## 📤 Example Response

```json
{
  "message": "student created",
  "data": {
    "id": 1,
    "name": "John Doe",
    "age": 20,
    "email": "john@example.com",
    "skills": [
      "Python",
      "FastAPI",
      "SQL"
    ]
  }
}
```

---

## 📂 Project Structure

```
fastapi-student-crud-api/
│── main.py
│── requirements.txt
│── README.md
```

---

## 📚 Concepts Used

- REST APIs
- CRUD Operations
- FastAPI
- Pydantic Models
- Request Validation
- Path Parameters
- HTTP Methods
- JSON Responses

---

## 🎯 Future Improvements

- Connect to a database (SQLite/PostgreSQL/MySQL)
- Add authentication with JWT
- Implement password hashing
- Add pagination
- Add search and filtering
- Prevent duplicate student IDs
- Store data permanently
- Add unit tests
- Dockerize the application

---

## 👨‍💻 Author

Your Name

---

This project was built to practice REST API development using FastAPI, request validation with Pydantic, and CRUD operations in Python.
