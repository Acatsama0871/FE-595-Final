# text_function
# clean raw_text data and

# modules
import re
import numpy as np
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords


# clean punctuations
def text_symbol_cleanser(text):
    nrow = len(text)
    res = text.copy()

    for i in range(nrow):
        clean_tweet = text["Content"][i]
        clean_tweet = re.sub(r"http\S+", "", clean_tweet)
        clean_tweet = re.sub(r"#(\w+)", "", clean_tweet)
        clean_tweet = re.sub(r"@(\w+)", "", clean_tweet)
        res["Content"][i] = clean_tweet
        if clean_tweet.isspace() == True:
            res["Content"][i] = np.nan
        elif clean_tweet.isspace() == False:
            res["Content"][i] = clean_tweet

    res["Content"].replace("", np.nan, inplace=True)
    # res['Tweet'].replace(' ', np.nan,inplace=True)
    res = res.dropna(axis=0)
    res = res.reset_index(drop=True)
    return res


# remove stopwords
def text_stopword_cleanser(text):
    nrow = len(text)
    res = text.copy()
    for i in range(nrow):
        tokenization = TextBlob(text["Content"][i]).words
        stop_words = set(stopwords.words("english"))
        clean_text = [i for i in tokenization if not i in stop_words]
        clean_text = " ".join(clean_text)
        res["Content"][i] = clean_text

    return res


# assign polarity and subjectivity
def text_scorer(text):
    nrow = len(text)
    res = pd.DataFrame()
    polarity = []
    subjectivity = []

    for i in range(nrow):
        Sentiment = TextBlob(text["Content"][i])
        polarity.append(Sentiment.sentiment.polarity)
        subjectivity.append(Sentiment.sentiment.subjectivity)
    res["Date"] = text["Date"]
    res["Polarity"] = polarity
    res["Subjectivity"] = subjectivity
    res = res.reset_index(drop=True)
    return res


# calculate the weekly sentiment score by averaging daily
def text_average_scorer(sp500, score):
    # The number of row for SPY data
    n_row = len(sp500)

    # T-1 sentiment to forecast T price
    # 2 ~ T date
    head_date = sp500["Date"][1:n_row]
    head_date = head_date.reset_index(drop=True)
    # 1 ~T-1 date
    tail_date = sp500["Date"][0 : n_row - 1]
    tail_date = tail_date.reset_index(drop=True)

    # length of head data
    len1 = len(head_date)
    pol_mean = []
    sub_mean = []

    # Construct average sentiment on each week
    for i in range(0, len1):
        x = score[score["Date"] < head_date[i]]
        x = x[x["Date"] >= tail_date[i]]
        pol_mean.append(np.mean(x["Polarity"]))
        sub_mean.append(np.mean(x["Subjectivity"]))

    res = pd.DataFrame()
    # res['Date'] = sp500['Date'][0:len1]
    res["Date"] = sp500["Date"][1 : len(sp500)].values
    res["Polarity"] = pol_mean
    res["Subjectivity"] = sub_mean

    # replace NA
    res["Polarity"] = res["Polarity"].fillna(0.0)
    res["Subjectivity"] = res["Subjectivity"].fillna(0.5)

    return res
