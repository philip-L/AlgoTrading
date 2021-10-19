# Yahoo Trading

## Motivation

I believe everyone deserves financial freedom. Since 2019 I started taking a deeper interest in the stock market, trying to find trends, and use algorithmic trading. I want to use automation on my personal portfolio and have a conservative strategy. Blog link: https://blog-react-0.herokuapp.com/ 

## Libraries & Environment

Libraries can be found in requirements.txt (pip install -r requirements.txt)

Libraries of note:
- finviz API
- yahoo-finance API
- numpy and pandas
- matplotlib.pyplot

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
- playground.ipynb -> testing things
- main.py -> driver for stockplotter.py / stockscanner.py (classes in progress for algorithmic trading & portfolio tracking)
- info.txt -> to print stock info to file for a record

## Results Summary

From a list of 150 companies retrieved using the unofficial Finviz screener API, I filtered with percent gain, current ratio and intrinsic value to find that Kirkland Lake Gold Ltd. is a good choice for a conservative strategy.

## Acknowledgements

Very thankful for https://github.com/mariostoev/finviz and https://github.com/ranaroussi/yfinance!

## Steps for setup (on Mac OS 10.15)

1. Clone this repository
3. Download python
4. Open a terminal at the repository folder and type "python -m venv finance" 
5. Type "source "finance/bin/activate"
6. Type "pip install -r requirements.txt"
7. Type "jupyter notebook &"
8. In the browser, open the PersonalFinance notebook (should be something like http://localhost:8889/notebooks/PersonalFinance.ipynb
9. Run the code. The yahoo finance API has a new bug, charting and percent gain analysis might not be working
