from typing import Optional
from fastapi import FastAPI
import os
import logging
import sys
import database
from database.models import Topic, Publication, Author, Dataset

# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
LOGLEVEL = os.environ.get("LOGLEVEL")
logger.setLevel(LOGLEVEL)
logger.error(f"Log level {LOGLEVEL}")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/topics", response_model=list[Topic])
def get_topics():
    return database.get_topics()


@app.get("/topics/{topic_id}/publications", response_model=list[Publication])
def get_topic_publications(topic_id: int):
    return database.get_topic_publications(topic_id)


@app.get("/topics/{topic_id}/authors", response_model=list[Author])
def get_topic_authors(topic_id: int):
    return database.get_topic_authors(topic_id)


@app.get("/topics/{topic_id}/datasets", response_model=list[Dataset])
def get_topic_datasets(topic_id: int):
    return database.get_topic_datasets(topic_id)
