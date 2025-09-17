# Notes Backend
A backend service for the Notes application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
It handles **user authentication (JWT)** and **CRUD APIs for notes**.


## 🚀 Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Auth:** JWT (via python-jose & passlib)
- **Server:** Uvicorn


## 📂 Project Structure
```
app/
├── main.py          # Entry point
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── database.py      # DB connection
├── auth.py          # JWT auth
├── routes/
│   ├── users.py     # User APIs
│   └── notes.py     # Notes APIs

````


## ⚙️ Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/rahulgtst/note-backend.git
cd note-backend
````

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create `.env` file in root:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>/<dbname>
SECRET_KEY=your-secret-key

```

## ▶️ Run the app

```bash
uvicorn app.main:app --reload
```

App will be live at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Available APIs

### Auth

* `POST /auth/register` → Register
* `POST /auth/login` → Login & get JWT

### Notes

* `GET /notes/` → Get all notes (auth required)
* `POST /notes/` → Create note
* `PUT /notes/{id}` → Update note
* `DELETE /notes/{id}` → Delete note
