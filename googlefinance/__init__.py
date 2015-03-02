'''
MIT License
'''

from urllib2 import Request, urlopen
import json
import sys

__author__ = 'hongtaocai@gmail.com'

googleFinanceKeyToFullName = {
    u'id'     : u'ID',
    u't'      : u'StockSymbol',
    u'e'      : u'Index',
    u'l'      : u'LastTradePrice',
    u'l_cur'  : u'LastTradeWithCurrency',
    u'ltt'    : u'LastTradeTime',
    u'lt_dts' : u'LastTradeDateTime',
    u'lt'     : u'LastTradeDateTimeLong',
    u'div'    : u'Dividend',
    u'yld'    : u'Yield'
}

def buildUrl(symbols):
    symbol_list = ','.join([symbol for symbol in symbols])
    # a deprecated but still active & correct api
    return 'http://finance.google.com/finance/info?client=ig&q=' \
        + symbol_list

def request(symbols):
    url = buildUrl(symbols)
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode().strip()
    content = content[3:]
    return content

def replaceKeys(quotes):
    global googleFinanceKeyToFullName
    quotesWithReadableKey = []
    for q in quotes:
        qReadableKey = {}
        for k in googleFinanceKeyToFullName:
            if k in q:
                qReadableKey[googleFinanceKeyToFullName[k]] = q[k]
        quotesWithReadableKey.append(qReadableKey)
    return quotesWithReadableKey

def getQuotes(symbols):
    '''
    get real-time quotes (index, last trade price, last trade time, etc) for stocks, using google api:
    http://finance.google.com/finance/info?client=ig&q=symbols
    Unlike python package 'yahoo-finance', There is no delay for NYSE and NASDAQ stocks in googlefinance.
    :param symbols: a list of stock symbols
    :return: real-time quotes
    '''
    content = json.loads(request(symbols))
    return replaceKeys(content);

if __name__ == '__main__':
    try:
        symbols = sys.argv[1]
    except:
        symbols = "GOOG,AAPL"

    symbols = symbols.split(',')

    try:
        print json.dumps(getQuotes(symbols), indent=2)
    except:
        print "Fail"
