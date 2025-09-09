# update_db.py

from app import app, db, StockData, NIFTY_TICKERS
import yfinance as yf
from datetime import datetime

def update_stock_data():
    """
    Fetches latest data from yfinance and updates the database.
    This function should be run periodically (e.g., every 5 minutes).
    """
    # 'app_context' is needed because we're running this outside of a Flask request
    with app.app_context():
        print("Starting database update...")
        for ticker_symbol in NIFTY_TICKERS:
            try:
                stock_yf = yf.Ticker(ticker_symbol)
                info = stock_yf.info

                # Find the existing stock in our database
                stock_db = StockData.query.filter_by(symbol=ticker_symbol).first()

                if stock_db:
                    # If it exists, UPDATE its data
                    stock_db.longName = info.get('longName')
                    stock_db.currentPrice = info.get('currentPrice')
                    stock_db.dayHigh = info.get('dayHigh')
                    stock_db.dayLow = info.get('dayLow')
                    stock_db.previousClose = info.get('previousClose')
                    stock_db.updated_at = datetime.utcnow()
                    print(f"Updated {ticker_symbol}")
                else:
                    # If it doesn't exist, CREATE a new entry
                    new_stock = StockData(
                        symbol=info.get('symbol'),
                        longName=info.get('longName'),
                        currentPrice=info.get('currentPrice'),
                        dayHigh=info.get('dayHigh'),
                        dayLow=info.get('dayLow'),
                        previousClose=info.get('previousClose')
                    )
                    db.session.add(new_stock)
                    print(f"Created {ticker_symbol}")

            except Exception as e:
                print(f"Could not fetch or update data for {ticker_symbol}: {e}")
        
        # Commit all the changes to the database at once
        db.session.commit()
        print("Database update complete.")

if __name__ == '__main__':
    update_stock_data()