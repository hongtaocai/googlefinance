from distutils.core import setup
setup(
  name = 'googlefinance',
  packages = ['googlefinance'], # this must be the same as the name above
  version = '0.7',
  description = 'Python module to get real-time (no delay) stock data from Google Finance API',
  author = 'Hongtao Cai',
  author_email = 'caiht.ht@gmail.com',
  url = 'https://github.com/hongtaocai/googlefinance', # use the URL to the github repo
  download_url = 'https://github.com/hongtaocai/googlefinance/tarball/0.4', # I'll explain this in a second
  keywords = ['googlefinance', 'stock', 'price' , 'finance', 'google', 'real-time'], # arbitrary keywords
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
  ],
)
