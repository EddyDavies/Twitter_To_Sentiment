import os.path

import pandas as pd
from pandas import DataFrame
import pandas_ta as ta
import yfinance as yf
import matplotlib as plt


from typing import Optional, List, Literal, Dict, Iterable, TypeVar, Tuple, cast, Generator
import os

if __name__ == '__main__':

    df = pd.DataFrame() # Empty DataFrame
    crypto = "bitcoin"
    crypto = "ethereum"

    # Load data
    data_folder = "../data"
    market_folder = os.path.join(data_folder, "market-data")
    source = os.path.join(market_folder, f"{crypto}.csv")
    df = pd.read_csv(source, sep=",")

    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[['open_price', 'close_price', 'percent_change_open', 'percent_change_close',
             'volume', 'market_cap']]


    CustomStrategy = ta.Strategy(
        name="Momo and Volatility",
        description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
        ta=[
            {"kind": "sma", "length": 50},
            {"kind": "sma", "length": 200},
            {"kind": "bbands", "length": 20},
            {"kind": "rsi"},
            {"kind": "macd", "fast": 8, "slow": 21},
            {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
        ]
    )
    # To run your "Custom Strategy"
    df.ta.strategy(CustomStrategy)

    # Apply Strategy
    # df.ta.strategy(ta.CommonStrategy)
    #
    # df.ta.log_return(cumulative=True, append=True)
    # df.ta.percent_return(cumulative=True, append=True)

    # New Columns with results
    df.columns
    df.reset_index(inplace=True)

    df.plot(x='date', y='close_price', figsize=(15, 6), linestyle='--', marker='*', markerfacecolor='r', color='y',
            markersize=10)


    result = os.path.join(market_folder, f"{crypto}_ta.csv")
    df.to_csv(result)


    # plt.xlabel('Date')
    # plt.ylabel('Price')
    plt.show()

    # Take a peek
    df.tail()


# class TechnicalAnalysisUtils:
#     """
#     Uses the pandas-ta to create technical indicators
#     """
#
#     def __init__(self):
#         pass
#
#     def apply_ta(self, cryptos: List[str],
#                                 save_dir: Optional[str] = "../data/market-data",
#                                 time_period: Optional[TimePeriod] = None) -> List[DataFrame]:
#
#         dataframes = [DataFrame(self.market_data_records(crypto, time_period))
#                       for crypto in cryptos]
#
#         if not os.path.exists(save_dir):
#             os.mkdir(save_dir)
#
#         for crypto, df in zip(cryptos, dataframes):
#             df.to_csv(f'{save_dir}/{crypto}.csv')
#
#         return dataframes
#
#
# if __name__ == '__main__':
#     cmu = CryptoMarketUtils()
#
#     cmu.generate_crypto_dataset(["bitcoin", "ethereum"])