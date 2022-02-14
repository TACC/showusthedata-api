from .database import engine
from .adapters import create_topic, create_publication
from .models import Topic, Publication

def get_topics() -> list[Topic]:
    connection = engine.raw_connection()
    try:
        cursor_obj = connection.cursor()
        cursor_obj.callproc("get_topics", [])
        rows = list(cursor_obj.fetchall())
        results = [ create_topic(row) for row in rows ]
        cursor_obj.close()
        connection.commit()
        return results
    finally:
        connection.close()


def get_topic_publications(topic_id: int) -> list[Publication]:
    connection = engine.raw_connection()
    try:
        cursor_obj = connection.cursor()
        cursor_obj.callproc("get_topic_publications", [topic_id])
        rows = list(cursor_obj.fetchall())
        results = [ create_publication(row) for row in rows ]
        cursor_obj.close()
        connection.commit()
        return results
    finally:
        connection.close() 