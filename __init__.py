import sqlite3

conn=sqlite3.connect("concerts_database.db")
cursor=conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY,
        band_id INTEGER NOT NULL,
        venue_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(venue_id) REFERENCES venues(id)
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY ,
        name TEXT ,
        hometown TEXT 
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY ,
        title TEXT,
        city TEXT 
    );
    ''')


conn.commit()
conn.close()



def insert_data():
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    # Bands
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Sauti Sol', 'Kenya')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Hart the Band', 'Uganda')")
    
    # Venues
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Carnivore', 'Nairobi')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Syomikau', 'Machakos')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-05')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-13')")
    
    conn.commit()
    conn.close()

insert_data()
    