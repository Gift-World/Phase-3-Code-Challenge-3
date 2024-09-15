from __init__ import CURSOR,CONN
from concert import Concert
from band import Band

class Venue:
    
    all = {}
    
    def __init__(self, title, city, id=None):
        self.title = title
        self.city = city
        self.id = id
        
    def __repr__(self):
        return f"Venue {self.id}: {self.title}, {self.city}"
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise ValueError("City must be a string")
        self._city = value
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value

    
    
    @classmethod
    def create_table(cls):
        sql = '''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY,
            title TEXT,
            city TEXT
        )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
        DROP TABLE IF EXISTS venues;
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        return cls(id=row[0], title=row[1], city=row[2])
    
    def save(self):
        if self.id is None:
            sql = '''
            INSERT INTO venues (title, city)
            VALUES (?, ?)
            '''
            CURSOR.execute(sql, (self.title, self.city))
            CONN.commit()
            self.id = CURSOR.lastrowid
            Venue.all[self.id] = self
        else:
            sql = '''
            UPDATE venues
            SET title = ?, city = ?
            WHERE id = ?
            '''
            CURSOR.execute(sql, (self.title, self.city, self.id))
            CONN.commit()
        Venue.all[self.id] = self
        
    def concerts(self):
        sql = '''
        SELECT * 
        FROM concerts
        WHERE venue_id = ?;
        '''
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Concert.instance_from_db(row) for row in rows]


    def bands(self):
        sql = '''
        SELECT DISTINCT bands.*
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?;
        '''
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Band.instance_from_db(row) for row in rows]

    def most_frequent_band(self):
        sql = '''
        SELECT bands.id, bands.name, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        '''
        result = CURSOR.execute(sql, (self.id,)).fetchone()
        
        if result:
            band_id = result[0]
            return Band.instance_from_db(result)  
        return None

    def concert_on(self, date):
        sql = '''
        SELECT * 
        FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1;
        '''
        result = CURSOR.execute(sql, (self.id, date)).fetchone()
        return Concert.instance_from_db(result) if result else None