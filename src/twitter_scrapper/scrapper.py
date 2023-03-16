import pandas
import snscrape.modules.twitter as snstwitter


def get_tweets_by_hashtag(hashtag: str, max_number: int = 10) -> pandas.DataFrame:
    """Get tweets that have the hashtag argument.

    Args:
        hashtag (str): The hashtag to get tweets.
        max_number (int, optional): Max number of  tweets to return. Default is 100.

    Returns:
        pandas.DataFrame: Dataframe with tweets.
    """
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(snstwitter.TwitterHashtagScraper(hashtag).get_items()):
        if i == max_number:
            break
        attributes_container.append(
            [
                tweet.date,
                tweet.url,
                tweet.likeCount,
                tweet.replyCount,
                tweet.retweetCount,
                tweet.hashtags,
                tweet.lang,
                tweet.sourceLabel,
                tweet.content,
            ]
        )

    tweets_df = pandas.DataFrame(
        attributes_container,
        columns=[
            "created_datetime",
            "url",
            "like_count",
            "reply_count",
            "retweet_count",
            "hashtags",
            "language",
            "source",
            "content",
        ],
    )

    return tweets_df
