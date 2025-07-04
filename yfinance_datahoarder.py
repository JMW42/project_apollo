# -*- coding: utf-8 -*-

"""
FILENAME: yfinance_datahoarder.py
AUTHOR: Jonathan Will
CREATED: 2024-07-4
UPDATED: 2025-07-04
DESCRIPTION: script for capturing data specified in a ticker.txt file and saving the stock market information from yahoo finance.
"""

# ########################################################################################################################
# ########################################################################################################################
# IMPORT

import yfinance as yf
import pandas as pd
import datetime
import os


# ########################################################################################################################
# ########################################################################################################################
# VARIABLES

filepath_tickers:str = "tickers.txt"
dirpath_archive:str = "data/"
str_interval = "1m"

# ########################################################################################################################
# ########################################################################################################################
# METHODS

def main():
    """ main function"""
    # read tickers file line by line and load the corresponding data

    # get needed datetime objects
    datetime_today = datetime.datetime.now()
    datetime_yesterday = datetime_today - datetime.timedelta(days=1)

    # needed datetimes in formated strings
    str_today = datetime_today.strftime("%Y-%m-%d")
    str_yesterday = datetime_yesterday.strftime("%Y-%m-%d")


    print(f"loading tickers file: {filepath_tickers}")

    # open tickers file
    
    with open(filepath_tickers) as file_tickers:

        # itterate over individual lines of tickers file 
        for line in file_tickers.readlines():
            ticker_name = line.replace("\n", "") # get ticker name
            print(f"< Ticker: {ticker_name}")
            check_create_directory(f"data/{ticker_name}") # check for ticker data directory and create it if needed

            # get ticker finance data
            df_data = yf.download(ticker_name, interval=str_interval, start=str_yesterday, end=str_today, auto_adjust=False) # download data given timeframe
            
            # sav date to archive
            filepath_save = f"{dirpath_archive}/{ticker_name}/{str_yesterday}.csv"
            print(f" svaing data to {filepath_save }")
            df_data.to_csv(filepath_save , sep="\t")




def check_create_directory(dir):
    if not os.path.exists(dir):
        print(f"cant find directory: {dir}")
        
        os.makedirs(dir)
        print(f"created new directory: {dir}")



# ########################################################################################################################
# ########################################################################################################################
# MAIN CODE

print("="*100)
print(f"### - YFINANCE datahoarder by JMW -".ljust(97) +"###")
print("="*100)

main() # run main function

print("="*100)
print("DONE")