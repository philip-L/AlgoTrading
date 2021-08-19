# simple stock plotter feb 2021
#

import yfinance as yf
import matplotlib.pyplot as plt

class StockPlotter:
	# Initializer / Instance Attributes
	def __init__(self):
		self.font1 = {'family': 'serif',
							'color':  'darkred',
							'weight': 'normal',
							'size': 16,
							}
		self.font2 = {'family': 'serif',
							'color':  'darkred',
							'weight': 'normal',
							'size': 14,
							}



	def get_ticker(self):
		return self.name

	# TODO
	def set_ticker(self, ticker, period='max', interval='1d'):
		self.tickerobj = yf.Ticker(ticker)  # yfinance Ticker object
		self.name = ticker.upper()
		self.exit = []  # calculated from graph
		self.target = [x*4 for x in self.prtflio.entry]
		self.risk = []  # potential for loss
		self.stop = []  # stop loss
		self.tickerobj.ticker = ticker.upper()
		# get historical market data, perform Yahoo Finance API call
		self.hist = self.tickerobj.history(period=period, interval=interval)
		# calculations
		self.hist['tp'] = (self.hist['High'] + self.hist['Low'] + self.hist['Close']) / 3  # typical price
		# n = 20; num days of smoothing, for each point calculate 20-day simple moving avg
		m = 2  # num standard deviations
		self.hist['50dma'] = self.hist['tp'].rolling(50).mean()
		self.hist['200dma'] = self.hist['tp'].rolling(200).mean()
		self.hist['20dma'] = self.hist['tp'].rolling(20).mean()  # 20-day simple moving avg
		self.hist['stdv'] = self.hist['tp'].rolling(20).std()  # moving standard deviation
		self.hist['bolu'] = self.hist['20dma'] + (m * self.hist['stdv'])  # upper bollinger band
		self.hist['bold'] = self.hist['20dma'] - (m * self.hist['stdv'])  # lower bb
		self.hist.fillna(0)

	ticker = property(get_ticker, set_ticker)

	def plt(self):
		# TODO text for open, close, high, and low updating on the cursor value?
		# TODO volume, make pretty, save
		# TODO bar chart (candles)
		threeMonths = self.hist.tail(90)
		year = self.hist.tail(365)

		# _, ax = plt.subplots()
		# plot 3M with 50 & 200 day moving avg
		fig = plt.subplot(311)  # plot max, 1y (with bb), 3m (with ma)
		plt.title("%s Stock Price" % self.name, fontdict=self.font1)
		# moving avg crossing
		plt.plot(threeMonths.index, threeMonths['Close'].values, 'b-')
		plt.plot(threeMonths.index, threeMonths['200dma'].values, 'r-')  # more bearish
		plt.plot(threeMonths.index, threeMonths['50dma'].values, 'r-')
		plt.plot(threeMonths.index, threeMonths['20dma'].values, 'r-')  # more bullish
		# ax.set_xticks(threeMonths.index[[x for x in range(0,89,89//3)]])
		# 1 year with bollinger band
		fig =plt.subplot(312)
		plt.ylabel('Stock Close Price', fontdict=self.font2)
		plt.plot(year.index, year['Close'].values, 'b-')
		plt.plot(year.index, year['bolu'].values, 'r-')
		plt.plot(year.index, year['bold'].values, 'r-')
		# ax.set_xticks(year.index[[x for x in range(0, 364, 364//3)]])
		# max
		fig = plt.subplot(313)
		plt.plot(self.hist.index, self.hist['Close'].values, 'b-')
		plt.xlabel('Date', fontdict=self.font2)
		# ax.set_xticks(self.hist.index[[x for x in range(0, len(self.hist), len(self.hist)//3)]])
		plt.show()
		return fig


