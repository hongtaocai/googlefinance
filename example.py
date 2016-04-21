from googlefinance import getQuotes
from googlefinance import getNews

import json
print json.dumps(getQuotes('GOOG'), indent=2)
print json.dumps(getNews("GOOG"), indent=2)