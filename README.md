# Algorithmic Trading

## Motivation

I believe everyone deserves financial freedom. Since 2019 I started taking a deeper interest in the stock market, trying to find trends, and use algorithmic trading. I want to use automation on my personal portfolio and have a conservative strategy. I explore the Long Short-Term Memory (LSTM) Keras model as a stock price indicator. Blog link: https://blog-react-0.herokuapp.com/ 

## Libraries & Environment

Libraries can be found in requirements.txt (pip install -r requirements.txt)

Libraries of note:
- finviz API
- yahoo-finance API
- numpy and pandas
- matplotlib.pyplot
- Keras (tensorflow)

Developped on MacOS Catalina 10.15.4

python version 3.7.4 virtual environment (use "source bin/activate" and "deactivate")

pip version 20.1.1 from /$(yahoo-trading-dir)/lib/python3.7/site-packages/pip

## Files description

Folders / files used by jupyter and virtul environment:

- bin/
- etc/
- include/
- lib/
- share/
- pyenv.cfg

Files used to do analyses:

- PersonalFinance.ipynb -> main notebook for Udacity course (FILE FOR UDACITY)

## Results Summary

Questions/ideas investigated in the jupyter notebook:
Part 1 (first udacity blog post):
  - What companies stock are trending upward?
  - What companies have the best balance sheet?
  - What does the chart show?

From a list of 150 companies retrieved using the unofficial Finviz screener API, I filtered with percent gain, current ratio and intrinsic value to find that Kirkland Lake Gold Ltd. seemed like a good choice in this simple conservative strategy and plotted it's closing price history.

Part 2 (udacity capstone):
- LSTM model as a stock price indicator

LSTM is a model great for regression which was perfect to create a simple stock price indicator. It predicted close to the actual values in the case I tested with. The model could be explored further, for example I expect if there is greater short-term volatility it would perform less well.

## Acknowledgements

Very thankful for https://github.com/mariostoev/finviz, https://github.com/ranaroussi/yfinance, and https://www.youtube.com/watch?v=QIUxPv5PJOY&ab_channel=ComputerScience!

## Steps for setup (on Mac OS 10.15)

1. Clone this repository
3. Download python
4. Open a terminal at the repository folder and type "python -m venv finance" 
5. Type "source "finance/bin/activate"
6. Type "pip install -r requirements.txt"
7. Type "jupyter notebook &"
8. In the browser, open the PersonalFinance notebook (should be something like http://localhost:8889/notebooks/PersonalFinance.ipynb
9. Run the code. The yahoo finance API has a new bug, charting and percent gain analysis might not be working
