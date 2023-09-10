# main.py

from collect_data_store import create_database  # Move this line here

create_database()  # Call create_database function to ensure the database is created

from web_server import app

if __name__ == '__main__':
    app.run(debug=True)
