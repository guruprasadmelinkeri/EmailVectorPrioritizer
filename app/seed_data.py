from .database import SessionLocal, engine
from .models import Email, Base

Base.metadata.create_all(bind=engine)

db = SessionLocal()

emails = [
    Email(
        subject="URGENT: Payment Failure",
        body="Payment failed multiple times, action required immediately",
        sender="billing@company.com",
        is_high_priority=True
    ),
    Email(
        subject="Server down",
        body="Production server is unreachable, customers affected",
        sender="devops@company.com",
        is_high_priority=True
    ),
    Email(
        subject="Team lunch",
        body="Let's plan team lunch for Friday",
        sender="hr@company.com",
        is_high_priority=False
    ),
]

db.add_all(emails)
db.commit()
db.close()
