from .database import run_procedure
from .adapters import create_topic, create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def get_topics() -> list[Topic]:
    return [create_topic(row) for row in run_procedure("get_topics", [])]


def get_topic_publications(topic_id: int) -> list[Publication]:
    return [create_publication(row) for row in run_procedure("get_topic_publications", [topic_id])]


def get_topic_authors(topic_id: int) -> list[Author]:
    return [create_author(row) for row in run_procedure("get_topic_authors", [topic_id])]


def get_topic_datasets(topic_id: int) -> list[Dataset]:
    return [create_dataset(row) for row in run_procedure("get_topic_datasets", [topic_id])]

