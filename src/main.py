from typing import Optional
from fastapi import FastAPI
import os
import logging
import sys
import database
from database.models import Topic, Publication, Author, Dataset, Alias

# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
LOGLEVEL = os.environ.get("LOGLEVEL")
logger.setLevel(LOGLEVEL)
logger.error(f"Log level {LOGLEVEL}")


tags_metadata = [
    {
        "name": "topics",
        "description": "Operations with topics",
    },
    {
        "name": "authors",
        "description": "Operations with authors",
    },
    {"name": "datasets", "description": "Operations with datasets"},
]


app = FastAPI(
    title="Show US the Data API",
    description="An API for datasets",
    version="0.0.1",
    openapi_tags=tags_metadata,
)


@app.get("/topics", response_model=list[Topic], tags=["topics"])
def get_topics():
    return database.get_topics()


@app.get(
    "/topics/{topic_id}/publications", response_model=list[Publication], tags=["topics"]
)
def get_topic_publications(topic_id: int):
    return database.get_topic_publications(topic_id)


@app.get("/topics/{topic_id}/authors", response_model=list[Author], tags=["topics"])
def get_topic_authors(topic_id: int):
    return database.get_topic_authors(topic_id)


@app.get("/topics/{topic_id}/datasets", response_model=list[Dataset], tags=["topics"])
def get_topic_datasets(topic_id: int):
    return database.get_topic_datasets(topic_id)


@app.get("/authors", response_model=list[Author], tags=["authors"])
def get_authors():
    return database.get_authors()


@app.get(
    "/authors/{author_id}/publications",
    response_model=list[Publication],
    tags=["authors"],
)
def get_author_publications(author_id: int):
    return database.get_author_publications(author_id)


@app.get("/authors/{author_id}/topics", response_model=list[Topic], tags=["authors"])
def get_author_topics(author_id: int):
    return database.get_author_topics(author_id)


@app.get(
    "/authors/{author_id}/datasets", response_model=list[Dataset], tags=["authors"]
)
def get_author_datasets(author_id: int):
    return database.get_author_datasets(author_id)


@app.get("/datasets", response_model=list[Dataset], tags=["datasets"])
def get_datasets():
    return database.get_datasets()


@app.get("/datasets/{parent_alias_id}/aliases", tags=["datasets"])
def get_dataset_aliases(parent_alias_id: int):
    return database.get_dataset_aliases(parent_alias_id)


@app.get("/datasets/{parent_alias_id}/publications", tags=["datasets"])
def get_dataset_publications(parent_alias_id: int):
    return database.get_dataset_publications(parent_alias_id)


@app.get("/datasets/{parent_alias_id}/topics", tags=["datasets"])
def get_dataset_topics(parent_alias_id: int):
    return database.get_dataset_topics(parent_alias_id)


@app.get("/datasets/{parent_alias_id}/authors", tags=["datasets"])
def get_dataset_authors(parent_alias_id: int):
    return database.get_dataset_authors(parent_alias_id)
