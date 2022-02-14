from .models import Topic, Publication, Author

def create_topic(row: tuple[int, int, str]) -> Topic:
    return Topic(topic_id=row[0], keyword_id=row[1], keyword=row[2])

def create_publication(row: tuple[int, str, str, int, int, str, int, float, str]):
    return Publication(
        publication_id=row[0],
        title=row[1],
        doi=row[2],
        year=row[3],
        month=row[4],
        pub_type=row[5],
        citation_count=row[6],
        fw_citation_impact=row[7],
        journal=row[8]
    )

def create_author(row: tuple[int, str, str]):
    return Author(
        author_id=row[0],
        given_name=row[1],
        family_name=row[2]
    )