#web_server.py

from flask import Flask, request, render_template
import sqlite3
from collect_data_store import create_database  # Import the create_database function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    
    # Store the user's search query in the search_history table
    store_search_query(query)

    # Implement the search functionality here
    
    # Log clicked URLs (you can implement this based on user interactions)

    # For now, let's print the query to the console for testing
    print(f"User searched for: {query}")

    # You can return search results or redirect the user as needed

# Function to store user search queries in the database
def store_search_query(query):
    conn = sqlite3.connect('data/search_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO search_history (query) VALUES (?)', (query,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()  # Call the create_database function from collect_data_store module

if __name__ == '__main__':
    app.run(debug=True)
