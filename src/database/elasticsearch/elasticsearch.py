import pandas
from elasticsearch import Elasticsearch


def insert_document(document: dict, index_name: str):
    """Insert one document in an Elasticsearch index hospeded in http://localhost:9200.

    Args:
        document (dict): Document to insert into Elasticsearch.
        index_name (str): Elasticsearch index name.
    """
    es = Elasticsearch("http://localhost:9200")
    es.index(index=index_name, document=document)


def insert_batch(dataframe: pandas.DataFrame, index_name: str):
    """Insert a list of documents in an Elasticsearch index hospeded in http://localhost:9200.

    Args:
        dataframe (pandas.DataFrame): Dataframe to insert into Elasticsearch.
        index_name (str): Elasticsearch index to insert.
    """
    for _, row in dataframe.iterrows():
        document = {
            "created_time": row.created_datetime,
            "url": row.url,
            "like_count": row.like_count,
            "reply_count": row.reply_count,
            "retweet_count": row.retweet_count,
            "hashtags": row.hashtags,
            "language": row.language,
            "source": row.source,
            "content": row.content,
        }

        insert_document(document, index_name)
