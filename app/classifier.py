from .embedding import scrub_text, secure_embed
from .vector_store import client, COLLECTION

def is_high_priority(subject: str, body: str, threshold=0.80) -> bool:
    text = scrub_text(subject + " " + body)
    vector = secure_embed(text)

    results = client.query_points(
        collection_name=COLLECTION,
        query=vector.tolist(),
        limit=1
    )

    client.query_points

    if not results.points:
        return False

    ##return results[0].score >= threshold
    return results.points[0].score