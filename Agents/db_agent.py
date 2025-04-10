import sqlite3

# Initialize Database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS matches
                 (name TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

# Save Match to Database
def save_match(name, score):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO matches (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

# Retrieve Past Matches from Database
def get_matches():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM matches ORDER BY score DESC")
    data = c.fetchall()
    conn.close()
    return data
