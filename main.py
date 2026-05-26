from fastapi import FastAPI, Depends, Query, Request

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from datetime import datetime

import random

from database import engine, SessionLocal

from models import Base, Ticket

from schemas import TicketCreate, TicketUpdate


# FastAPI App
app = FastAPI()


# Templates Folder
templates = Jinja2Templates(directory="templates")


# Create Database Tables
Base.metadata.create_all(bind=engine)


# Database Session Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ======================================================
# FRONTEND ROUTES
# ======================================================

# Customer Portal
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# Admin Dashboard
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


# ======================================================
# API ROUTES
# ======================================================

# Create Ticket
@app.post("/api/tickets")
def create_ticket(

    ticket: TicketCreate,

    db: Session = Depends(get_db)

):

    # Generate Random Ticket ID
    ticket_number = f"TKT-{random.randint(1000, 9999)}"

    # Create Ticket Object
    new_ticket = Ticket(

        ticket_id=ticket_number,

        customer_name=ticket.customer_name,

        customer_email=ticket.customer_email,

        subject=ticket.subject,

        description=ticket.description,

        status="Open",

        created_at=datetime.utcnow()
    )

    # Save To Database
    db.add(new_ticket)

    db.commit()

    db.refresh(new_ticket)

    return {

        "ticket_id": new_ticket.ticket_id,

        "created_at": new_ticket.created_at,

        "message": "Ticket Created Successfully"
    }


# Get All Tickets
@app.get("/api/tickets")
def get_all_tickets(

    status: str = Query(None),

    search: str = Query(None),

    db: Session = Depends(get_db)

):

    tickets = db.query(Ticket)

    # Filter By Status
    if status:

        tickets = tickets.filter(
            Ticket.status == status
        )

    # Search Functionality
    if search:

        tickets = tickets.filter(

            (Ticket.customer_name.contains(search)) |

            (Ticket.customer_email.contains(search)) |

            (Ticket.subject.contains(search)) |

            (Ticket.description.contains(search))
        )

    return tickets.all()


# Get Single Ticket
@app.get("/api/tickets/{ticket_id}")
def get_single_ticket(

    ticket_id: str,

    db: Session = Depends(get_db)

):

    ticket = db.query(Ticket).filter(
        Ticket.ticket_id == ticket_id
    ).first()

    if not ticket:

        return {
            "error": "Ticket not found"
        }

    return ticket


# Update Ticket Status
@app.put("/api/tickets/{ticket_id}")
def update_ticket(

    ticket_id: str,

    updated_ticket: TicketUpdate,

    db: Session = Depends(get_db)

):

    ticket = db.query(Ticket).filter(
        Ticket.ticket_id == ticket_id
    ).first()

    if not ticket:

        return {
            "error": "Ticket not found"
        }

    # Update Status
    ticket.status = updated_ticket.status

    # Save Changes
    db.commit()

    db.refresh(ticket)

    return {

        "success": True,

        "updated_status": ticket.status
    }