
from __init__ import CURSOR,CONN
from band import Band
from venue import Venue
class Concert:
    
    all = {}
    
    def __init__(self, date, name, bands, venues, id=None):
        self.name = name
        self.date = date
        self.bands_names = bands
        self.venues_titles = venues
        self.id = id
        
        self.bands_id = self._get_bands_id(bands)
        self.venues_id = self._get_venues_id(venues)
    
    def __repr__(self):
        return (f"Concert {self.id}: [ Date: {self.date!r}, Name : {self.name!r}, "
                f"bands_name: {self.bands_name!r}, venues_titles : {self.venues_titles!r}, "
                f"bands_id: {self.bands_id}, venue_id: {self.venue_id} ]")
    
    def _get_band_id(self, bands_names):
        result = CURSOR.execute('SELECT id FROM bands WHERE name = ?', (bands_names,)).fetchone()
        if result:
            return result[0]  

        CURSOR.execute('INSERT INTO bands (name) VALUES (?)', (bands_names,))
        CONN.commit()
        return CURSOR.lastrowid  

    def _get_venues_id(self, venues_titles):
        result = CURSOR.execute('SELECT id FROM venues WHERE title = ?', (venues_titles,)).fetchone()
        if result:
            return result[0] 

        CURSOR.execute('INSERT INTO venues (title) VALUES (?)', (venues_titles,))
        CONN.commit()
        return CURSOR.lastrowid  
    
  
    @classmethod
    def create_table(cls):
        sql = '''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            name TEXT,
            band_id INTEGER,
            venue_id INTEGER,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        )
        '''
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = '''
        DROP TABLE IF EXISTS concerts;
        '''
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        if self.id is None:
            sql = '''
            INSERT INTO concerts (date, name, band_id, venue_id)
            VALUES (?, ?, ?, ?)
            '''
            CURSOR.execute(sql, (self.date, self.name, self.band_id, self.venue_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
            Concert.all[self.id] = self
       
    @classmethod
    def instance_from_db(cls, row):
        if row:
            return cls(date=row[1], name=row[2], band=row[3], venue=row[4], id=row[0])
        return None
    
    def band(self):
        sql = '''
        SELECT * 
        FROM bands
        WHERE id = ?;
        '''
        row = CURSOR.execute(sql, (self.band_id,)).fetchone()
        return Band.instance_from_db(row)
    
    def venue(self):
        sql = '''
        SELECT * 
        FROM venues
        WHERE id = ?;
        '''
        row = CURSOR.execute(sql, (self.venue_id,)).fetchone()
        return Venue.instance_from_db(row)

    def hometown_show(self):
        sql = '''
        SELECT bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?;
        '''
        result = CURSOR.execute(sql, (self.id,)).fetchone()
    
        if result:
            band_hometown, venue_city = result

            return band_hometown == venue_city
    
        print("No result found for concert ID:", self.id)
        return False


    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
