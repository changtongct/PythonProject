from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

today=date.today()
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo('AXP',start,today)
quotesdf=pd.DataFrame(quotes)

#pd.set_option('display.height', 1000)
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
print quotesdf