from typing import Optional
from fastapi import FastAPI
import os
import logging
import sys
import database
from database.models import Topic, Publication

# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
    results = database.get_topics()
    return results

@app.get("/topics/{topic_id}/publications", response_model=list[Publication])
def get_topic_publications(topic_id: int):
    results = database.get_topic_publications(topic_id)
    return results