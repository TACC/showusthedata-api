from datetime import datetime

from pydantic import BaseModel, Field


class Topic(BaseModel):
    """
    A searchable topic
    """
    topic_id: int = Field(
        None, 
        title='Topic ID',
        description='A unique ID that can be used to retrieve topics',
        example='32'
    )
    keyword_id: int = Field(
        None,
        title='Keyword ID',
        description='A unique ID that can be used to retrieve the keyword for this topic',
        example='1',
    )
    keyword: str = Field(
        None,
        title='Keyword',
        description='The keyword for this topic'
    )
