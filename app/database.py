import sqlite3

def get_db_connection():
    """Connect to an SQLite database (or create it if missing)."""
    conn = sqlite3.connect("mock_data.db")
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

def setup_database():
    """Initialize mock data for the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a simple transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            date TEXT,
            sales INTEGER
        )
    ''')

    # Create a simple users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            signup_date TEXT
        )
    ''')

    # Insert mock data if empty
    cursor.execute("SELECT COUNT(*) FROM transactions")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO transactions (date, sales) VALUES ('2024-03-01', 50000), ('2024-03-02', 100000)")

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (signup_date) VALUES ('2024-03-18'), ('2024-03-19'), ('2024-03-20')")

    conn.commit()
    conn.close()

# Run database setup
setup_database()
