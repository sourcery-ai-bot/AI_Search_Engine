# collect_data_store.py

import sqlite3

# Create a connection to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('data/search_data.db')
cursor = conn.cursor()

# Create a table to store user search history
cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Create a table to store clicked URLs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clicked_urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_id INTEGER,
        url TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (query_id) REFERENCES search_history (id)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

# Function to create the database
def create_database():
    conn = sqlite3.connect('data/search_data.db')
    cursor = conn.cursor()
    
    # Define any database initialization code here
    
    conn.commit()
    conn.close()
