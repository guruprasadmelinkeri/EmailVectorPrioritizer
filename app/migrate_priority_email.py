import sqlite3
from .database import SessionLocal
from .models import Email

FEEDBACK_DB_PATH = "./feedback.db"

ALLOWED_PRIORITY = {"high", "medium"}

def migrate_priority_emails_from_feedback():
    """
    Pull high + medium priority emails from feedback.db
    and insert ONLY NEW ones into emails.db
    """
    src = sqlite3.connect(FEEDBACK_DB_PATH)
    cursor = src.cursor()

    cursor.execute("""
        SELECT subject, body, sender, priority
        FROM emails
        WHERE LOWER(priority) IN ('high', 'medium')
    """)

    rows = cursor.fetchall()
    src.close()

    db = SessionLocal()
    inserted = 0

    for subject, body, sender, priority in rows:
        if not subject or not body:
            continue

        priority_norm = priority.strip().lower()
        if priority_norm not in ALLOWED_PRIORITY:
            continue

        # 🔒 Dedup check (VERY IMPORTANT)
        exists = db.query(Email).filter(
            Email.subject == subject,
            Email.body == body,
            Email.sender == sender
        ).first()

        if exists:
            continue

        email = Email(
            subject=subject,
            body=body,
            sender=sender,
            is_high_priority=True  # high + medium → True
        )

        db.add(email)
        inserted += 1

    if inserted > 0:
        db.commit()
    else:
        db.rollback()

    db.close()
    return inserted
