# Support CRM System

A full-stack Customer Support CRM system built using FastAPI, SQLite, HTML, Tailwind CSS, and JavaScript.

This application allows customers to submit support tickets while enabling admins to manage complaints through a modern dashboard interface.

---

# 🚀 Live Demo

🔗 https://support-crm-system-production.up.railway.app/

---

# 📌 Features

## 👨‍💻 Customer Portal
- Submit support tickets
- Generate unique ticket IDs
- Responsive UI
- Real-time toast notifications

## 🛠️ Admin Dashboard
- View all tickets
- Search tickets
- Filter tickets by status
- Update ticket status
- Ticket details popup modal
- Dashboard analytics cards
- Real-time updates
- Professional responsive UI

---

# 🧠 Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- SQLite

## Frontend
- HTML
- Tailwind CSS
- JavaScript

## Deployment
- Railway.app

---

# 📂 Project Structure

```text
support-crm/
│
├── crm_env/
│
├── static/
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── support_crm.db
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/jayjadhav04/support-crm-system.git
```

```bash
cd support-crm-system
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv crm_env
```

---

## 3️⃣ Activate Virtual Environment

### Windows
```bash
crm_env\Scripts\activate
```

### Linux / Mac
```bash
source crm_env/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

# 🌐 Open In Browser

## Customer Portal
```text
http://127.0.0.1:8000
```

## Admin Dashboard
```text
http://127.0.0.1:8000/dashboard
```

## Swagger API Documentation
```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## ➕ Create Ticket

```http
POST /api/tickets
```

### Request Body

```json
{
  "customer_name": "John",
  "customer_email": "john@gmail.com",
  "subject": "Payment Issue",
  "description": "Money deducted but payment failed"
}
```

---

## 📋 Get All Tickets

```http
GET /api/tickets
```

### Optional Query Parameters
- status
- search

### Examples

```http
GET /api/tickets?status=Open
```

```http
GET /api/tickets?search=Payment
```

---

## 🔍 Get Single Ticket

```http
GET /api/tickets/{ticket_id}
```

### Example

```http
GET /api/tickets/TKT-1234
```

---

## ✏️ Update Ticket Status

```http
PUT /api/tickets/{ticket_id}
```

### Request Body

```json
{
  "status": "Closed"
}
```

---

# 🔄 Workflow

```text
Customer submits complaint
        ↓
Ticket stored in SQLite database
        ↓
Admin opens dashboard
        ↓
Admin manages ticket status
        ↓
Dashboard updates in real-time
```

---

# 📊 Dashboard Features

- Total Tickets Card
- Open Tickets Card
- In Progress Tickets Card
- Closed Tickets Card
- Search Functionality
- Status Filtering
- Ticket Detail Modal
- Real-Time Status Updates

---

# 🎯 Future Improvements

- Authentication System
- Role-Based Access Control
- Email Notifications
- File Attachments
- Ticket Priority Levels
- AI-Based Ticket Categorization

---

# 🚀 Deployment

This project is deployed on Railway.app.

### Deployment Platform
- Railway.app

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# 👨‍💻 Author

## Jay Jadhav

Computer Science Engineering (AI/ML)

### GitHub
https://github.com/jayjadhav04

### LinkedIn
https://www.linkedin.com/in/jayjadhav04

---
