from .database import SessionLocal
from .models import Email
from .embedding import scrub_text, secure_embed
from .vector_store import client, COLLECTION

def index_priority_emails():
    db = SessionLocal()
    emails = db.query(Email).filter(Email.is_high_priority == True).all()

    points = []
    for email in emails:
        text = scrub_text(email.subject + " " + email.body)
        vector = secure_embed(text)

        points.append({
            "id": email.id,
            "vector": vector.tolist()
        })

    if points:
        client.upsert(
            collection_name=COLLECTION,
            points=points
        )

    db.close()
    print("priority emails indexed")
