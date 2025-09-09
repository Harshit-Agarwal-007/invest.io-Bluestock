Invest.io - A Financial Dashboard Web Application
Invest.io is a full-stack web application that displays real-time financial data for top companies from the Nifty 100 index. It is built with a Python and Flask backend and a simple HTML, CSS, and JavaScript frontend.

This project serves as an excellent educational tool for understanding core web development concepts, including API creation, frontend-backend communication, and database caching for performance optimization.

Core Concepts Illustrated
Backend API Development: Building a robust API with Flask to serve data.

Data Fetching: Interacting with an external API (yfinance) to get live financial data.

Database Caching: Using a local SQLite database with Flask-SQLAlchemy to dramatically improve performance by caching API results.

Separation of Concerns: Creating a separate, automated script (update_db.py) to handle slow data-fetching tasks, ensuring the web application remains fast for users.

Frontend-Backend Communication: Using the JavaScript fetch API to request data from the Flask backend and dynamically render it on the webpage.

Production Deployment: Understanding the difference between a development server and a production-ready setup using Gunicorn.

Tech Stack
Backend: Python, Flask, Flask-SQLAlchemy, yfinance

Database: SQLite

Frontend: HTML, CSS, JavaScript

Deployment Server: Gunicorn

Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
Python 3.6 or higher installed on your system.

git for cloning the repository.

2. Clone the Repository
git clone [https://github.com/your-username/invest.io.git](https://github.com/your-username/invest.io.git)
cd invest.io

3. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

On Windows:

python -m venv venv
venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
Install all the required Python libraries from the requirements.txt file.

pip install -r requirements.txt

5. Create and Populate the Database
The application uses a local SQLite database for caching.

Step A: Create the database schema
Open a Python interactive shell and run the following commands to create the stocks.db file.

# In your terminal
python

# In the Python shell
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...
>>> exit()

Step B: Populate the database with data
Run the update_db.py script. This will fetch data from the Yahoo Finance API for all tickers and save it to your local database. This step might take a few minutes.

python update_db.py

6. Run the Application
You can now run the Flask development server.

python app.py

Open your web browser and navigate to http://127.0.0.1:5000. Click the "Load Dashboard" button to see the data load instantly from your database.

Running for Production
The built-in Flask server is not suitable for production. Use a WSGI server like Gunicorn.

gunicorn --workers 4 --bind 0.0.0.0:8000 app:app

Automating Data Updates
To keep the financial data fresh, the update_db.py script should be run on a schedule.

On Windows: Use the Task Scheduler to create a task that runs python update_db.py every 15-30 minutes.

On Linux/macOS: Use a cron job. Open your crontab with crontab -e and add a line like this to run the script every 15 minutes:

*/15 * * * * /path/to/your/invest.io/venv/bin/python /path/to/your/invest.io/update_db.py

Project Structure
invest.io/
├── static/
│   └── style.css       # Basic CSS for styling
├── templates/
│   └── index.html      # The main HTML page for the dashboard
├── .gitignore          # Tells Git which files to ignore
├── app.py              # Main Flask application file
├── README.md           # This file
├── requirements.txt    # List of Python dependencies
├── update_db.py        # Script to fetch data and update the database
└── stocks.db           # The SQLite database file (created automatically)
