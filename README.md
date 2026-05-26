# Support CRM System

A full-stack Customer Support CRM system built using FastAPI, SQLite, HTML, Tailwind CSS, and JavaScript.

This project allows customers to submit support tickets and enables admins to manage complaints through a professional dashboard interface.

---

# Features

## Customer Portal
- Submit support tickets
- Generate unique ticket IDs
- Responsive UI
- Success toast notifications

## Admin Dashboard
- View all tickets
- Search tickets
- Filter tickets by status
- Update ticket status
- Ticket detail modal popup
- Dashboard analytics cards
- Real-time updates
- Professional UI design

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

---

# API Endpoints

## Create Ticket
POST /api/tickets

Request Body:
{
  "customer_name": "John",
  "customer_email": "john@gmail.com",
  "subject": "Payment Issue",
  "description": "Money deducted but payment failed"
}

---

## Get All Tickets
GET /api/tickets

Optional Query Params:
- status
- search

Examples:
GET /api/tickets?status=Open
GET /api/tickets?search=Payment

---

## Get Single Ticket
GET /api/tickets/{ticket_id}

Example:
GET /api/tickets/TKT-1234

---

## Update Ticket Status
PUT /api/tickets/{ticket_id}

Request Body:
{
  "status": "Closed"
}

---

# Installation & Setup

## Step 1 - Clone Repository

git clone https://github.com/your-username/support-crm-system.git

cd support-crm-system

---

## Step 2 - Create Virtual Environment

python -m venv crm_env

---

## Step 3 - Activate Virtual Environment

### Windows
crm_env\Scripts\activate

---

## Step 4 - Install Requirements

pip install -r requirements.txt

---

## Step 5 - Run Server

uvicorn main:app --reload

---

# Open In Browser

## Customer Portal
http://127.0.0.1:8000

## Admin Dashboard
http://127.0.0.1:8000/dashboard

## Swagger API Docs
http://127.0.0.1:8000/docs

---

# Dashboard Workflow

Customer submits complaint
↓
Ticket stored in SQLite database
↓
Admin opens dashboard
↓
Admin manages ticket status
↓
Dashboard updates in real-time

---

# Future Improvements

- Authentication System
- Role-Based Access
- Email Notifications
- File Attachments
- Ticket Priority Levels
- AI-based Ticket Categorization

---

# Author

Jay Jadhav

Computer Science Engineering (AI/ML)

GitHub:
https://github.com/jayjadhav04
