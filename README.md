# googlefinance
Python module to get stock data from Google Finance API

This module provides **no delay**, **real time** stock data in NYSE & NASDAQ. 
 
Another awesome module, [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance)'s data is delayed by 15 min, but it provides convenient apis to fetch historical day-by-day stock data.

##Install
From PyPI with pip:
	
	$pip install googlefinance

From development repo (requires git)

	$git clone https://github.com/hongtaocai/googlefinance.git
	$cd googlefinance
	$python setup.py install

##Usage example

	>>> from googlefinance import getQuotes
	>>> import json
	>>> print json.dumps(getQuotes('AAPL'), indent=2)
	[
	  {
    	"Index": "NASDAQ", 
 	    "LastTradeWithCurrency": "129.09", 
        "LastTradeDateTime": "2015-03-02T16:04:29Z", 
        "LastTradePrice": "129.09", 
        "Yield": "1.46", 
        "LastTradeTime": "4:04PM EST", 
        "LastTradeDateTimeLong": "Mar 2, 4:04PM EST", 
        "Dividend": "0.47", 
        "StockSymbol": "AAPL", 
        "ID": "22144"
      }
    ]
    >>> print json.dumps(getQuotes(['AAPL', 'VIE:BKS']), indent=2)
    [
      {
        "Index": "NASDAQ", 
        "LastTradeWithCurrency": "129.36", 
        "LastTradeDateTime": "2015-03-03T16:02:36Z", 
        "LastTradePrice": "129.36", 
        "LastTradeTime": "4:02PM EST", 
        "LastTradeDateTimeLong": "Mar 3, 4:02PM EST", 
        "StockSymbol": "AAPL", 
        "ID": "22144"
      }, 
      {
        "Index": "VIE", 
        "LastTradeWithCurrency": "17.10", 
        "LastTradeDateTime": "2015-03-03T13:30:30Z", 
        "LastTradePrice": "17.10", 
        "LastTradeTime": "1:30PM GMT+1", 
        "LastTradeDateTimeLong": "Mar 3, 1:30PM GMT+1", 
        "StockSymbol": "BKS", 
        "ID": "978541942832888"
      }
    ]

    >>> from googlefinance import getNews
    >>> import json
    >>> print json.dumps(getNews("GOOG"), indent=2)
    [
      {
        "usg": "AFQjCNEndnF6ktTO4yZ7DO6VWNNKuNLRqA",
        "d": "Feb 26, 2016",
        "tt": "1456499673",
        "sp": "Alphabet logo Alphabet Inc (NASDAQ:GOOG) CEO Lawrence Page sold 33,332 shares of the firm&#39;s stock in a transaction dated Tuesday, March 22nd.",
        "s": "Financial Market News",
        "u": "http://www.financial-market-news.com/alphabet-inc-goog-ceo-lawrence-page-sells-33332-shares/996645/",
        "t": "Alphabet Inc (GOOG) CEO Lawrence Page Sells 33332 Shares",
        "sru": "http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://www.financial-market-news.com/alphabet-inc-goog-ceo-lawrence-page-sells-33332-shares/996645/&cid=52779068349451&ei=jVn_VsrfApXcuATP4JvQBw&usg=AFQjCNHkHXAJIZRMHo9ciTAb7OWzj9pKvA"
      },
      {
        "usg": "AFQjCNHfaafHtJPn5GWu-6RiVG_J_1TYUw",
        "d": "Mar 26, 2016",
        "tt": "1458951075",
        "sp": "You don&#39;t get to $300 billion without overcoming your fair share of problems. This truism certainly applies individually to tech titans Alphabet (NASDAQ:GOOG) (NASDAQ:GOOGL) and Apple (NASDAQ:AAPL) at different points in their respective corporate&nbsp;...",
        "s": "Motley Fool",
        "u": "http://www.fool.com/investing/general/2016/03/25/alphabet-inc-eyes-a-new-road-to-mobile-success-in.aspx",
        "t": "Alphabet Inc Eyes a New Road to Mobile Success in the Most Unlikely Places",
        "sru": "http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://www.fool.com/investing/general/2016/03/25/alphabet-inc-eyes-a-new-road-to-mobile-success-in.aspx&cid=52779068349451&ei=jVn_VsrfApXcuATP4JvQBw&usg=AFQjCNEFa7EPWB-kyl2C23OTRHOWRJN52w"
      }
    ]

