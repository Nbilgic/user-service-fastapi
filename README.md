# 🚀 User Service (FastAPI + PostgreSQL + Docker)

This project is a **production-style User Service** built with FastAPI, PostgreSQL, and Docker.
It demonstrates backend fundamentals including API development, database integration, and authentication-ready architecture.

---

## 🧱 Tech Stack

* Python (FastAPI)
* PostgreSQL (Docker)
* SQLAlchemy (ORM)
* Pytest (testing)
* Docker (containerization)

---

## 📁 Project Structure

```
services/user_service/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── schemas.py
│   ├── db.py
│   ├── auth.py
│   └── __init__.py
│
├── tests/
│   └── test_user.py
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ Setup & Run

### 1. Clone the project

```bash
git clone <your-repo>
cd services/user_service
```

---

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 3. Run PostgreSQL with Docker

Start docker desktop

Run only once to start PostgreSQL container on Docker
```bash
docker run --name postgres-db \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=postgres \
-e POSTGRES_DB=userdb \
-p 5432:5432 \
-d postgres
```

If container already exists:

```bash
docker start postgres-db
```

Check running containers:

```bash
docker ps
```

---

### 4. Run the API

```bash
uvicorn app.main:app --reload --port 8001
```

---

### 5. Open API Docs

```
http://127.0.0.1:8001/docs
```

---

## 🐳 Docker Notes

* PostgreSQL runs inside Docker container
* API runs locally
* Future improvement: full docker-compose setup

---

## 🧠 Key Learnings

* FastAPI service architecture
* SQLAlchemy ORM usage
* Dependency injection (DB session)
* Password hashing
* Debugging import & environment issues
* Docker-based database setup

---

## 🚀 Next Steps

* JWT Authentication (Login)
* Protected endpoints
* Role-based access
* Integration tests
* CI/CD pipeline

---

## 🧪 Run Tests

```bash
cd C:\projects\user_service_project
$env:PYTHONPATH="."
python -m pytest -v
```

---

## 💡 Troubleshooting

### Port already in use

```bash
uvicorn app.main:app --reload --port 8002
```

---
