import yfinance as yf

reliance_stock = yf.Ticker("RELIANCE.NS")

stock_info = reliance_stock.info
print("Company Name: ", stock_info['longName'])
print("Current Market Price: ", stock_info['currentPrice'])
print("Sector: ", stock_info['sector'])