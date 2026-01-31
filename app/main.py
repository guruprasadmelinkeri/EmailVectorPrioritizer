from fastapi import FastAPI
from .classifier import is_high_priority
from .indexer import index_priority_emails
from .migrate_priority_email import migrate_priority_emails_from_feedback
from pydantic import BaseModel
import os 
app = FastAPI()

class EmailIn(BaseModel):
    subject: str
    body: str

@app.on_event("startup")
def startup():
    index_priority_emails()

@app.post("/classify")
def classify(email: EmailIn):
    return {
        "high_priority": is_high_priority(email.subject, email.body)
    }


@app.post("/train/priority")
def train_priority_classifier():
    inserted = migrate_priority_emails_from_feedback()
    index_priority_emails()

    return {
        "status": "ok",
        "new_samples_added": inserted,
        "indexed": True
    }

import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
