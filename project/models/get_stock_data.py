from yahoo_fin import stock_info as yahoo_fin
import yfinance as yf

import json


# msft = yf.Ticker('TCS.NS')

def get_stock_info(ticker, full_data = False):
    ticker_obj = yf.Ticker(ticker)
    raw_data = ticker_obj.info
    print(raw_data)
    data = {}
    if full_data:
        data = raw_data
    else:
        # print("inside else")
        # yahoo.get_quote_table("TCS.NS")
        data['stock_full_name'] = raw_data['longName']
        # print(raw_data['longName'])
        # print(data['stock_full_name'])
        data['stock_summary'] = raw_data['longBusinessSummary']
        data['stock_symbol'] = raw_data['symbol']
        data['stock_market_cap'] = raw_data['marketCap']
        data['stock_current_price'] = raw_data['regularMarketPrice']
        data['stock_52_high'] = raw_data['regularMarketDayHigh']
        data['stock_52_low'] = raw_data['regularMarketDayLow']
        data['stock_book_value'] = raw_data['bookValue']
        data['stock_pe'] = round(raw_data['trailingPE'])
        data['stock_dividend'] = raw_data['fiveYearAvgDividendYield']
        data['stock_roce'] = "NA"
        data['stock_roe'] = "NA"
        data['stock_growth_3'] = "NA"
        data['stock_website'] = raw_data['website']
        data['stock_face_value'] = "9"
    return data
