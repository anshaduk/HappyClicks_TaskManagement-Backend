# 📝 Task Manager App

A full-stack Task Management System built with **Django REST Framework** and **React**. This app allows users to register, log in, and manage personal tasks with priority and status tracking.

---

## 🚀 Tech Stack

### Backend:
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication 

### Frontend:
- React 
- Tailwind CSS 

---

## 🔧 Backend Setup Instructions

1. **Clone the repository:**
   ```bash
   git https://github.com/anshaduk/HappyClicks_TaskManagement-Backend.git
   cd HappyClicks_TaskManagement-Backend

2. **Create a virtual environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   pip install -r requirements.txt

4. **Set up environment variables:**

5. **Run migrations:**
   python manage.py migrate

6. **Start the server:**
   python manage.py runserver

## 📡 API Endpoints

## 🔐 Authentication

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/api/register/`      | Register a new user          |
| POST   | `/api/token/`         | Get access and refresh token |
| POST   | `/api/token/refresh/` | Refresh access token         |


## ✅ Task Management

| Method | Endpoint           | Description                              |
| ------ | ------------------ | ---------------------------------------- |
| GET    | `/api/tasks/`      | List all tasks (authenticated user only) |
| POST   | `/api/tasks/`      | Create a new task                        |
| GET    | `/api/tasks/{id}/` | Retrieve a specific task                 |
| PUT    | `/api/tasks/{id}/` | Update a task                            |
| DELETE | `/api/tasks/{id}/` | Delete a task                            |

## 📊 Dashboard

| Method | Endpoint           | Description                                     |
| ------ | ------------------ | ----------------------------------------------- |
| GET    | `/api/task-stats/` | Get task statistics (total, completed, pending) |




