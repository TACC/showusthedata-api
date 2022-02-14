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
        description='A unique ID that can be used to retrieve the keyword for a topic',
        example='1',
    )
    keyword: str = Field(
        None,
        title='Keyword',
        description='The keyword for a topic',
        example='Water Quality'
    )

class Publication(BaseModel):
    """
    A publication
    """
    publication_id: int = Field(
        None,
        title='Publication ID',
        description='A unique ID that can be used to retrieve publications',
        example='366'
    )
    title: str = Field(
        None,
        title='Title',
        description='The title of the article within the publication',
        example='Reintroducing the Current Insights Feature'
    )
    doi: str = Field(
        None,
        title='DOI',
        description='Digital Object Identifier',
        example='10.3386/w18780'
    )
    year: int = Field(
        None,
        title='Year',
        description='Year of the publication',
        example='2017'
    )
    month: int = Field(
        None,
        title='Month',
        description='Month of the publication',
        example='3'
    )
    pub_type: str = Field(
        None,
        title='Publication Type',
        description='Publication type',
        example='journal'
    )
    citation_count: int = Field(
        None,
        title='Citation Count',
        description='The number of citations for this publication',
        example='5'
    )
    fw_citation_impact: float = Field(
        None,
        title='Citation Impact',
        description='The impact of this citation (DRAFT)'
    )
    journal: str = Field(
        None,
        title='Journal',
        description='The name of the publication'
    )
