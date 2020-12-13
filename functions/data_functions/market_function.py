# market_function.py
# process the market data

# modules
import numpy as np
import pandas as pd


# calculate log return
def stockprice_logreturn(asset):

    head = asset["Open"][0 : len(asset) - 1].values
    tail = asset["Open"][1 : len(asset)].values

    week_return = np.log(tail) - np.log(head)

    res = pd.DataFrame()
    res["Date"] = asset["Date"][1 : len(asset)]
    res["Return"] = week_return
    res = res.reset_index(drop=True)
    return res


# calculate simple return
def stockprice_return(asset):

    head = asset["Open"][0 : len(asset) - 1].values
    tail = asset["Open"][1 : len(asset)].values

    week_return = (tail - head) / head

    res = pd.DataFrame()
    res["Date"] = asset["Date"][1 : len(asset)]
    res["Return"] = week_return
    res = res.reset_index(drop=True)
    return res


# calculate volatility
def stockprice_volatility(asset_weekly_return, window):
    first_index = window - 1
    volatility = []
    weekly_date = asset_weekly_return["Date"]

    for i in range(len(asset_weekly_return) - window):
        the_stockprice = asset_weekly_return["Return"][0 + i : first_index + i].values
        volatility.append(np.std(the_stockprice) / np.sqrt(window / 252))

    daily_vol = pd.DataFrame()
    daily_vol["Date"] = weekly_date[first_index + 1 : len(asset_weekly_return)]
    daily_vol["Volatility"] = volatility
    daily_vol = daily_vol.reset_index(drop=True)

    return daily_vol
