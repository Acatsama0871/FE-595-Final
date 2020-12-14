# feature_engineering.py
# process raw_text features


# module
import os
import numpy as np
import pandas as pd
from stockstats import StockDataFrame as Sdf
import functions.data_functions.text_function as tf
import functions.data_functions.market_function as af
import functions.data_functions.download as df


def main():

    # setting working directory
    current_path = os.getcwd()
    data_path = current_path + "/Data"

    print("Market features:")
    # market features
    # download market data
    names = ["SPY", "MSFT", "AAPL", "AMZN", "GOOGL", "JNJ", "BRK-B", "JPM"]
    stockprice_weekly = []
    for i in names:
        stockprice_weekly.append(
            df.stockprice_downloader(
                i, start="2015-11-30", end="2020-12-11", period="1d", interval="1wk"
            )
        )

    # calculate the log return
    logreturn_weekly = []
    for cur_stock in stockprice_weekly:
        logreturn_weekly.append(af.stockprice_logreturn(cur_stock))

    # calculate the volatility
    vol_weekly = []
    for cur_log in logreturn_weekly:
        vol_weekly.append(af.stockprice_volatility(cur_log, 5))

    # technical indicator
    stock_df = Sdf.retype(stockprice_weekly[0])
    rsi = stock_df["rsi_14"].values
    macd = stock_df["macd"].values
    macds = stock_df["macds"].values
    macd_ = np.where(macd > macds, 1, 0)

    # find price movement directions
    direction = np.where(logreturn_weekly[0].iloc[:, 1] >= 0, 1, 0)

    # assemble market result
    market_features = pd.DataFrame()
    market_features["Date"] = logreturn_weekly[0]["Date"][5 : len(logreturn_weekly[0])]
    market_features["direction"] = direction[5 : len(direction)]

    for i in range(len(names)):
        cur_vol_name = names[i] + "_vol"
        cur_log_name = names[i] + "_log"
        condition1 = vol_weekly[i]["Date"] >= "2016-01-11"
        market_features[cur_vol_name] = vol_weekly[i][condition1].iloc[:, 1].values
        condition2 = logreturn_weekly[i]["Date"] >= "2016-01-11"
        market_features[cur_log_name] = (
            logreturn_weekly[i][condition2].iloc[:, 1].values
        )

    market_features["rsi14"] = rsi[6 : len(rsi)]
    market_features["macd"] = macd_[6 : len(macd_)]
    market_features = market_features.reset_index(drop=True)
    market_features["Date"] = market_features["Date"].astype(str)
    print("Done!")

    # text features
    # file names
    file_names = ["Lisa_tweets.csv", "OilPrice_tweets.csv", "SentimentTrader_tweets.csv", "YahooFinance_tweets.csv"]

    print("\nText features:")
    # process raw_text
    processes_text = []
    count = 1
    for name in file_names:
        print("{} of total {}".format(count, len(file_names)))
        cur_text = pd.read_csv(os.path.join(data_path, "raw_text/" + name))  # load data
        cur_text = tf.text_symbol_cleanser(cur_text)  # remove symbols
        cur_text = tf.text_stopword_cleanser(cur_text)  # remove stop words
        cur_text = tf.text_scorer(cur_text)  # assign polarity + subjectivity
        cur_text = tf.text_average_scorer(
            market_features, cur_text
        )  # calculate weekly score by averaging daily
        processes_text.append(cur_text)
        count += 1
    print("Done!")

    # assemble to data frame
    print("\nAssemble to a dataframe:")
    names = ["Lisa", "OilPrice", "SenTrader", "Yahoo"]
    for i in range(len(processes_text)):
        cur_pol_name = names[i] + "_Pol"
        cur_sub_name = names[i] + "_Sub"
        cur_text_dataframe = processes_text[i]
        market_features[cur_pol_name] = cur_text_dataframe["Polarity"]
        market_features[cur_sub_name] = cur_text_dataframe["Subjectivity"]

    # feature engineering
    col = np.shape(market_features)[1]
    row = np.shape(market_features)[0]

    y_part = market_features.iloc[1:row, 0:2]
    y_part = y_part.reset_index(drop=True)

    x_part = market_features.iloc[0:row-1, 2:col]
    x_part = x_part.reset_index(drop=True)

    features = pd.concat([y_part, x_part], axis=1)
    features.to_csv(os.path.join(data_path, "features.csv"), index=False)
    print("Done! Process finished!")


if __name__ == "__main__":
    main()
