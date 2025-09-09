# app.py

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import yfinance as yf

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# Set the location of the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the database extension
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# This class defines the structure of our database table
class StockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(15), unique=True, nullable=False, index=True)
    longName = db.Column(db.String(100))
    currentPrice = db.Column(db.Float)
    dayHigh = db.Column(db.Float)
    dayLow = db.Column(db.Float)
    previousClose = db.Column(db.Float)
    # Store the last time this record was updated
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Converts the object to a dictionary for easy JSON serialization."""
        return {
            'symbol': self.symbol,
            'longName': self.longName,
            'currentPrice': self.currentPrice,
            'dayHigh': self.dayHigh,
            'dayLow': self.dayLow,
            'previousClose': self.previousClose
        }

# --- TICKER LIST ---
NIFTY_TICKERS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS",
    "HINDUNILVR.NS", "BHARTIARTL.NS", "ITC.NS", "SBIN.NS", "LICI.NS",
] # Shortened for brevity

# --- API ENDPOINTS ---
@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/nifty100')
def get_nifty_100():
    # THE BIG CHANGE: We now query OUR OWN database, not yfinance!
    stocks_from_db = StockData.query.all()
    
    # Convert the list of StockData objects into a list of dictionaries
    stocks_list = [stock.to_dict() for stock in stocks_from_db]
    
    return jsonify(stocks_list)

if __name__ == '__main__':
    app.run(debug=True)