# Support CRM System

A full-stack Customer Support CRM system built using FastAPI, SQLite, HTML, Tailwind CSS, and JavaScript.

This application allows customers to submit support tickets while enabling admins to manage complaints through a professional dashboard.

---

# Features

## Customer Portal
- Create support tickets
- Generate unique ticket IDs
- Responsive UI
- Real-time toast notifications

## Admin Dashboard
- View all tickets
- Search tickets
- Filter tickets by status
- Update ticket status
- Ticket details modal popup
- Dashboard analytics cards
- Real-time updates
- Modern responsive UI

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- SQLite

## Frontend
- HTML
- Tailwind CSS
- JavaScript

---

# Project Structure

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

# API Endpoints

## Create Ticket

### Endpoint
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

## Get All Tickets

### Endpoint
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

## Get Single Ticket

### Endpoint
```http
GET /api/tickets/{ticket_id}
```

### Example
```http
GET /api/tickets/TKT-1234
```

---

## Update Ticket Status

### Endpoint
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

# Installation & Setup

## Step 1 - Clone Repository

```bash
git clone https://github.com/your-username/support-crm-system.git
```

```bash
cd support-crm-system
```

---

## Step 2 - Create Virtual Environment

```bash
python -m venv crm_env
```

---

## Step 3 - Activate Virtual Environment

### Windows
```bash
crm_env\Scripts\activate
```

### Mac/Linux
```bash
source crm_env/bin/activate
```

---

## Step 4 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 - Run Server

```bash
uvicorn main:app --reload
```

---

# Open In Browser

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

# Dashboard Workflow

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

# Dashboard Features

- Total Tickets Card
- Open Tickets Card
- In Progress Tickets Card
- Closed Tickets Card
- Search Functionality
- Status Filtering
- Ticket Detail Modal
- Real-Time Status Updates

---

# Future Improvements

- Authentication System
- Role-Based Access Control
- Email Notifications
- File Attachments
- Ticket Priority Levels
- AI-Based Ticket Categorization

---

# Deployment

This project can be deployed easily using:

- Railway
- Render
- Vercel
- Docker

Recommended:
- FastAPI → Railway.app

---

# Author

## Jay Jadhav

Computer Science Engineering (AI/ML)

### GitHub
https://github.com/jayjadhav04

---
