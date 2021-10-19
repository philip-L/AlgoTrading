# Could use requests to create short list of strong stocks

# Performs analysis on a stock <SYMBOL> using yfinance. Can get options.
# Find if the stock is on a overall upward trend. Calculate Bollinger Band.

# Use ratios for determining intrins. value. Find undervalued assets
# TODO look for below 52w average, find max, min, average for mean reversion
# momentum -> above 300% average volume with 5% increase in price

# TODO trade signal, entry, exit, stop loss, target
# swing trade, trend trade, big market moves, set and forget approach
# 1, 2, 3, or 4R in a month

# webpages visited :
# - https://smallbusiness.chron.com/calculate-companys-stock-price-21802.html#:~:text=The%20most%20popular%20method%20used,its%2012%2Dmonths%20trailing%20earnings.

import math
import numpy as np
import pandas as pd

# from abc import ABCMeta, abstractmethod

# import keyboard

from stockplotter import StockPlotter

class Portfolio:
	def __init__(self, positions, entry):
		# idk
		# positions = ['tlry.to', 'gold.to', 'wmt', 'ac.to', 'l.to', 'cgx.to', 'vcn.to', 'xei.to', 'xqb.to', 'huv.to']
		# entry = [6.12, 2.32, 118.26, 22.28, 66.37, 33.95, 32.50, 16.95, 21.07, 149.81]
		self.positions = positions
		self.entry = entry
		#  self.positions = dict(zip(positions, entry))  # make dictionary from two lists
		self.positions_dict = {'Symbol': positions, 'entry': entry}
		# self.df_positions = pd.DataFrame.from_dict(self.positions_dict)
		self.portfolio_size = 11000
		self.cash = 6000

	def add_position(self, position, entry):
		pass
		# append to dataframe
		#self.df_positions
	def remove_position(self, position):
		pass

class StockScanner (StockPlotter):  # doesn't need to be like this just have def plot
	# Initializer / Instance Attributes
	def __init__(self):
		StockPlotter.__init__(self)
		# stock/etf list currently holding / going long
		# how to know when to exit? know when to take a loss?
		# questrade: apha, gold, vcn, xei
		# qtrade: xqb, ac, wmt
		# scotia: l, cgx, huv, cnq
		positions = ['tlry.to', 'gold.to', 'wmt', 'ac.to', 'l.to', 'cgx.to', 'vcn.to', 'xei.to', 'xqb.to', 'huv.to', 'cnq.to']
		pos_entry = [6.12, 2.32, 118.26, 22.28, 66.37, 33.95, 32.50, 16.95, 21.07, 149.81]
		self.portfolio = Portfolio(positions, pos_entry)
		exit = []
		# 	buylimit - price limit to buy - entry
		self.buy_limit = 0
		#	target and selllimit - price limit to sell.
		self.target = 0
		self.sell_limit = 0
		# 	stoplimit - stop loss - a price to sell if things don't go as expected 
		self.stop_limit = 0
		self.figlist = []  # used in scan(self) to store figures plotted
		#  dataframe for calculating percent_gain stats (fastest movers or most reliable?)
		my_cols = ['Symbol', 'Max-percent-gain', '10y-percent-gain', '5y-percent-gain', '1y-percent-gain']
		self.percent_gain_df = pd.DataFrame(columns=my_cols)
		# TODO return:
		# 	stocklist - top 10 stock percent gain list in S&P 500
		self.stock_list = pd.DataFrame(columns=my_cols)

	# @abstractmethod
	def scan(self):
		# TODO notify moving avgs and bollinger bands, trend is above, below, between
		# should use requesets to get lists finviz idk
		self.plt()
		# is intrinsic value undervalued? print to file info.txt
		self.BGF()
		self.PEratio()
		self.DDM()
		self.percent_gain()

	def calculate_pivots(self):
		#  weekly/ monthly high + low + close / 3
		# support/demand resistance/supply
		# calculate all weekly and monthly pivots
		weeklyPivot = self.hist.tail(7)['High'].max() + self.hist.tail(7)['Low'].min() + self.hist.tail()['Close'] / 3
		monthlyPivot = self.hist.tail(30)['High'].max() + self.hist.tail(30)['Low'].min() + self.hist.tail()['Close'] / 3

	def percent_gain(self):
		# calc 1M, 3M, 1y, 3y, 5y, 10y, max percent gain/loss
		# TODO use a dataframe? fix error
		ranges_num = [30, 90, 365, 1095, 1825, 3650, len(self.hist)]
		ranges_string = ['1M', '3M', '1y', '3y', '5y', '10y', 'max']
		price_now = self.hist.tail()

		i = 0
		for num in ranges_num:
			if len(self.hist) < num:
				break
			try:
				# date index not working using int
				#a += datetime.timedelta(days=1)
				val = (price_now/self.hist.loc[len(self.hist)-num].at['Close'] - 1) * 100
				f = open("info.txt", "a")
				f.write("{}: percent g/l = {}\n".format(ranges_string[i], val))
				f.close()
				i+=1
			except Exception as err:
				print("Error in percent_gain: ", err)



	def PEratio(self):
		#  intrinsic value calculation with price/earning ratio
		#  Intrinsic Value = P/E Ratio X Earnings Per Share
		#  TODO use dataframe for all thses
		try:
			val = self.tickerobj.info['trailingPE'] * self.tickerobj.info['trailingEps']
			if val > self.tickerobj.info['previousClose']:
				f = open("info.txt", "a")
				f.write("{} is undervalued with PE ratio method by {}\n".format(self.name, val-self.tickerobj.info['previousClose']))
				f.close()
		except Exception as error:
			print("Error in PEratio: ", error)
			# print("There was an error in PE ratio")
		# return val

	def BGF(self):
		#  benjamin graham formula intrinsic value calculation
		#  Maximum Intrinsic Value = Square root of (15 X 1.5 (Earnings per share) X(Book Value per share))
		try:
			val = math.sqrt(15 * 1.5 * self.tickerobj.info['trailingEps'] * self.tickerobj.info['bookValue'])
			if val > self.tickerobj.info['previousClose']:
				f = open("info.txt", "a")
				f.write(f"{self.name} is undervalued with benjys method! BGF Value={val} \n")
				f.close()
		except Exception as error:
			print("Error in BGF: ", error)
		# return val

	def DDM(self):
		#  dividend discount model intrinsic value calculation
		#  Value of Stock = Dividends per share/(Stockholders rate of return - dividend growth rate)
		#  TODO: find dividend growth rate / not sure if working correctly
		try:
			divgrowth = (self.tickerobj.info['dividendRate'] - self.tickerobj.info['trailingAnnualDividendRate']) \
						/ self.tickerobj.info['trailingAnnualDividendRate']
			val = self.tickerobj.info['trailingAnnualDividendYield'] / (0.11 - divgrowth)
			if val > self.tickerobj.info['previousClose']:
				f = open("info.txt", "a")
				f.write(f"{self.name} is undervalued with dividend growth method! Value={val} \n")
				f.close()
		except Exception as error:
			print("Error in DDM: ", error)
			# print("There was an error in DDM")
		# return val
