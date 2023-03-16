import os
from dotenv import dotenv_values
from src.database.mongodb import mongodb
from src.database.elasticsearch import elasticsearch
from src.twitter_scrapper.scrapper import get_tweets_by_hashtag


def main(configs: dict):
    tweets_df = get_tweets_by_hashtag(configs["HASHTAG"], configs["TWEETS_LIMIT"])

    elasticsearch.insert_batch(tweets_df, configs["ELASTICSEARCH_INDEX_NAME"])
    mongodb.insert_batch(
        tweets_df.to_dict("records"),
        configs["MONGODB_NAME"],
        configs["MONGODB_COLLECTION_NAME"],
        username=configs["MONGODB_USERNAME"],
        password=configs["MONGODB_PASSWORD"],
    )


if __name__ == "__main__":
    absolute_path = os.path.abspath(os.path.dirname(__file__))
    env_path = os.path.join(absolute_path, ".env")
    configs = dotenv_values(env_path)

    main(configs)
