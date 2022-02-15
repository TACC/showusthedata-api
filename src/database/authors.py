from .database import engine
from .database import run_procedure
from .adapters import create_topic, create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def get_authors() -> list[Author]:
    return [create_author(row) for row in run_procedure("get_authors", [])]


def get_author_publications(author_id: int) -> list[Publication]:
    return [
        create_publication(row)
        for row in run_procedure("get_author_publications", [author_id])
    ]


def get_author_topics(author_id: int) -> list[Topic]:
    return [
        create_topic(row) for row in run_procedure("get_author_topics", [author_id])
    ]


def get_author_datasets(author_id: int) -> list[Dataset]:
    return [
        create_dataset(row) for row in run_procedure("get_author_datasets", [author_id])
    ]
