from stockplotter import StockPlotter as splt
from stockscanner import StockScanner as scan
# import requests # for http requests
# import xlsxwriter # excel
# from scipy import stats
# import math
# import pd, np
# Welcome to Alpha Vantage! Here is your API key: J66IOGELPWX2UV00. 
import sys
import keyboard
import datetime
import time
# import matplotlib.pyplot as plt
# import yfinance as yf

# stockplotter.py and stockscanner.py cli
# python3.7.4 virtual environment for mac osx10.15

# for jupyter notebook invoke
# "source bin/activate" in TradingBot dir
# "jupyter notebook playground.ipynb &"

########## USAGE ##############
# python main.py <SYMBOL> <PERIOD> <INTERVAL>
# <SYMBOL> is optional
# <PERIOD> is optional
# <PERIOD> options: 1d, 5d, 1mo, 3mo, 6mo, 1y, 3y, 5y, max is default
# <INTERVAL> is optional
# <INTERVAL> options: 1d, 1h, 30min, 5min

if __name__ == '__main__':

    # Obtain the stock symbol, period and interval (optionals) from the command line
    # Can pass a list of symbols to tickers object in yfinance
    # these could all be treated differently
    # 11 sectors of S&P lists TODO update dynamically
    # Energy: XLE.
    # Materials: XLB.
    # Industrials: XLI.
    # Consumer Discretionary: XLY.
    # Consumer Staples: XLP.
    # Health Care: XLV.
    # Financials: XLF.

    technology = ['lumn', ]  # 20.8%
    healthCare = []  # 14.9%
    consumeDiscretion = ['mcd']  # 10.2%
    commServices = ['viac']  # 9.9%
    industrials = []  # 9.7%
    consumerStaples = []  # 6.7%
    energy = []  # 6.0%
    utilities = []  # 2.8%
    realEstate = []  # 2.7%
    materials = ['gold.to', 'xme', 'xbm', 'slv', 'gld', 'ag', 'fcx', 'pslv', 'goro', 'ar']  # 2.5%

    # positions = ['tlry.to', 'huv.to', 'gold.to', 'wmt', 'ac.to', 'l.to', 'cgx.to', 'vcn.to', 'xei.to', 'xqb.to' ]
    # pos_entry = [6.12, 2.32, 118.26, 22.28, 66.37, 33.95, 32.50, 16.95, 21.07, 149.81]
    etfs = ['potx', 'copx', 'xme', 'subz', 'smh', 'xqb.to' 'huv.to', 'uvxy', 'vcn.to', 'mj', 'slv', 'pslv', 'gld']
    watchlist1 = ['doge-cad', 'btc-cad', 'qqq', 'spy', '^dji', 'f', 'disca', 'vwagy']
    watchlist2 = {'infn', 'mgi', 'pfe', 'ar', 'net', 'fcel', 'food', 'love', 'crox', 'anf', 'kss', 'bke', 'dis', 'jwn',
                'fubo', 'disca', 'cat', 'bynd', 'dash', }  # a set
    growth = ['sono', 'pll']
    retail = ['m', 'anf', 'wmt', 'kss']  # retail and travel doing well march 2021
    hedging = ['slv', 'gld', 'ag', 'fcx', 'pslv', 'doge', 'goro']
    indexes = ['huv.to', 'uvxy', 'xqb.to', 'spy', 'vcn.to', 'qqq', 'dia']
    cannabis = ['tlry.to','grwg', 'mj', 'potx']
    streaming = ['subz', 'fubo', 'disca', 'dis']
    semiconductor = ['smh', 'intc', 'amd']
    auto = ['f', 'tsla', '']
    crypto = ['mara']

    if len(sys.argv) > 1:
        ticker = sys.argv[1]
        if len(sys.argv) > 2:
            period = sys.argv[2]
        if len(sys.argv) != 4:
            pass
        else:
            interval = sys.argv[3]
    # TODO to/from json
    watchlist2.update(etfs)  # join iterable
    print(f'Current watchlist2: {watchlist2}')
    # print('Input ticker symbols to append to watchlist. Press <enter> to skip.')
    # while 1:
    #     t = input()
    #     if t == '':
    #         break
    #     else:
    #         watchlist.add(t)

    # test stock plot / scan
    f = open("info.txt", "a")
    f.write("#################$ Report $#################" + "\n")
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()
    obj = scan()
    for tickr in obj.prtflio.positions:
        obj.ticker = tickr
        obj.scan()  # plot, calculate obj.percent_gain()
        # time.sleep(1)

    for tickr in watchlist1:
        obj.ticker = tickr
        obj.plt()
        obj.scan()  # obj.percent_gain()

# how to make an abstract class
# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(): pass

# class AdvancedArithmetic(object):
#     def divisorSum(n):
#         raise NotImplementedError
#
# class Calculator(AdvancedArithmetic):
#     def divisorSum(self, n):
#         return sum([i for i in range(1,n+1) if n%i == 0])
#
#
# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)