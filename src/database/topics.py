from .database import engine
from .adapters import create_topic
from .models import Topic

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