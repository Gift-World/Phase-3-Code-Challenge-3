from __init__ import CURSOR,CONN
from concert import Concert

class Band:
    
    all = {}
    # Initialize band with name, hometown, and an id
    def __init__(self, name, hometown, id=None):
        self.id = id
        self.name = name
        self.hometown = hometown
    

 #  representation for the Band object using strings
    def __repr__(self):
        return f"Band {self.id}: {self.name}:, {self.hometown}:"
    
    

    @classmethod
    # Creates the bands table in the database
    def create_table(cls):
        sql = '''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY,
            name TEXT,
            hometown TEXT
        )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
        DROP TABLE IF EXISTS bands;
        '''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
     # Create an instance of Band from a database row
    def instance_from_db(cls, row):
        return cls(id=row[0], name=row[1], hometown=row[2])

    def save(self):
         # Save the band in the database
        if self.id is None:
            sql = '''
            INSERT INTO bands (name, hometown)
            VALUES (?, ?)
            '''
            CURSOR.execute(sql, (self.name, self.hometown))
            CONN.commit()
            self.id = CURSOR.lastrowid
        Band.all[self.id] = self
       
        
    def concerts(self):
        sql = '''
        SELECT * 
        FROM concerts
        WHERE band_id = ?;
        '''
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Concert.instance_from_db(row) for row in rows]

    def venues(self):
          # Fetch all venues where the band has played
        concerts = self.concerts()
        venues = set()  
        for concert in concerts:
            venue = concert.venue()  
            venues.add(venue)
        return list(venues)  # Convert the set back to a list
    
    
    def play_in_venue(self, venue, date):
        venues_id = CURSOR.execute('SELECT id FROM venues WHERE title = ?', (venue,)).fetchone()
        if venues_id:
            venues_id = venues_id[0]
        else:
            CURSOR.execute('INSERT INTO venues (title) VALUES (?)', (venue,))
            CONN.commit()
            venue_id = CURSOR.lastrowid
        
        sql = '''
        INSERT INTO concerts (date, name, band_id, venue_id)
        VALUES (?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (date, self.name, self.id, venue_id))
        CONN.commit()
        
        pass

    def all_introductions(self):
        concerts = self.concerts()
        introductions = []
        for concert in concerts:
            introduction = concert.introduction()
            introductions.append(introduction)
        return introductions
    
    @classmethod
    def most_performances(cls):
        sql = '''
        SELECT bands.id, bands.name, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        ORDER BY performance_count DESC
        LIMIT 1
        '''
        result = CURSOR.execute(sql).fetchone()
        if result:
            bands_id = result[0]
            return cls.all.get(bands_id)
        return None

