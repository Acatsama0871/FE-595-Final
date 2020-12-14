# twitter_downloads.py
# downloads data from twitter

# modules
import os
import time
from functions.data_functions.download import twitter_scraper


def main():
    # set save path
    data_path = os.path.join(os.getcwd(), "Data/raw_text")

    # set downloads params
    names = ["Lisa", "YahooFinance", "SentimentTrader", "OilPrice"]
    twitter_ids = [
        "lisaabramowicz1",  # https://twitter.com/lisaabramowicz1
        "YahooFinance",  # https://twitter.com/YahooFinance
        "sentimentrader",  # https://twitter.com/sentimentrader
        "OilandEnergy",  # https://twitter.com/OilandEnergy
    ]
    download_dates = ("2016-01-01", "2020-11-27")

    # download
    for i in range(len(names)):
        print("Task {} of total {}".format(i + 1, len(names)))
        cur_result = twitter_scraper(
            twitter_ids[i], download_dates[0], download_dates[1]
        )
        cur_result.to_csv(os.path.join(data_path, names[i] + "_tweets.csv"))
        print("Done\n")
        time.sleep(10)  # frequent request will cause time run out error


if __name__ == "__main__":
    main()
