from .database import run_procedure
from .adapters import create_topic, create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def get_publications() -> list[Publication]:
    return [create_publication(row) for row in run_procedure("get_publications", [])]


def get_publication_topics(publication_id: int) -> list[Topic]:
    return [
        create_topic(row)
        for row in run_procedure("get_publication_topics", [publication_id])
    ]


def get_publication_authors(publication_id: int) -> list[Author]:
    return [
        create_author(row)
        for row in run_procedure("get_publication_authors", [publication_id])
    ]


def get_publication_datasets(publication_id: int) -> list[Dataset]:
    return [
        create_dataset(row)
        for row in run_procedure("get_publication_datasets", [publication_id])
    ]
