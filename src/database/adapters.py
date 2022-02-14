from .models import Topic

def create_topic(row: tuple[int, int, str]) -> Topic:
    return Topic(topic_id=row[0], keyword_id=row[1], keyword=row[2])