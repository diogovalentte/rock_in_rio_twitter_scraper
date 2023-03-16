from pymongo import MongoClient


def insert_batch(
    documents: list, db_name: str, collection_name: str, username: str, password: str
):
    """Insert a list of documents in a Mongo database hospeded in http://localhost:27017.

    Args:
        documents (list): List of dictionaries.
        db_name (str): Mongo database name.
        collection_name (str): Collection name.
        username (str): Username to access database.
        password (str): Password to access database.
    """
    client = MongoClient("localhost", 27017, username=username, password=password)
    db = client[db_name]
    collection = db[collection_name]

    collection.insert_many(documents).inserted_ids
