# download.py
# download data functions


# modules
import pandas as pd
import yfinance as yf
import snscrape.modules.twitter as tw


# market data
# download stock price
def stockprice_downloader(symbol, start, end, period, interval) :
    stock = yf.download(
        symbol, start=start, end=end, period=period, interval=interval
    )  # period="1d",interval="1d"
    stock = stock.dropna()
    stock = stock.reset_index()

    return stock


# text data
# twitter scraper
def twitter_scraper(tw_id, since="2020-01-01", to="2020-02-01") :
    """

    scrape twitter from given account

    Args:
        tw_id (str): the twitter account id
        since (str, optional): from date. Defaults to "2020-01-01".
        to (str, optional): to date. Defaults to "2020-02-01".
    Returns:

    """
    # initialize
    tweet_time = []
    tweet_dates = []
    tweets_content = []

    # scrape from twitter
    the_query = "from:" + tw_id + " since:" + since + " until:" + to
    for tweet in tw.TwitterSearchScraper(query=the_query).get_items() :
        tweet_dates.append(tweet.date.strftime("%Y-%m-%d"))
        tweet_time.append(tweet.date.strftime("%Y-%m-%d %H:%M:%S"))
        tweets_content.append(tweet.content)

    # convert to dataframe
    tweets = pd.DataFrame(
        {"Time" : tweet_time, "Content" : tweets_content, "Date" : tweet_dates}
    ).set_index("Time")
    tweets = tweets.iloc[
             : :-1
             ]  # reverse the order, retrieved from: https://stackoverflow.com/questions/20444087/right-way-to-reverse-pandas-dataframe

    return tweets
