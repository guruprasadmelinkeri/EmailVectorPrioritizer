from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import os
from dotenv import load_dotenv
load_dotenv()
Url=os.getenv("qdrant_cluster_endpoint")
Api_key=os.getenv("qdrant_api_key")

client = QdrantClient(
    url=Url,
    api_key=Api_key
)

COLLECTION = "priority_emails"

client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)
