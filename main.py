
import ipdb

from __init__ import CONN, CURSOR
from Classes.band import Band
from Classes.venue import Venue
from Classes.concert import Concert
if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    Band.drop_table()
    Band.create_table()
    
    Concert.drop_table()
    Concert.create_table()
    
    Venue.drop_table()
    Venue.create_table()
    
    band1 = Band(name="Hart the Band", hometown="Kenya")
    band1.save()

    band2 = Band(name="Sauti Sol", hometown="Uganda")
    band2.save()

    band3 = Band(name="Westlife", hometown="London")
    band3.save()

    # Create some venues
    venue1 = Venue(title="Nairobi Cinema", city="Nairobi")
    venue1.save()

    venue2 = Venue(title="Syokimau", city="Machakos")
    venue2.save()

    venue3 = Venue(title="Carnivore", city="Nairobi")
    venue3.save()
    
    concert1 = Concert(date="2024-10-05", name="Hart the Band", band=band1.name, venue=venue1.title)
    concert1.save()

    concert2 = Concert(date="2024-10-13", name="Sauti Sol", band=band2.name, venue=venue2.title)
    concert2.save()

    concert3 = Concert(date="2024-12-08", name="Westlife", band=band3.name, venue=venue3.title)
    concert3.save()
    
    
    
    print(concert1.band())  
    print(concert1.venue())  
    
    venue = Venue.all[1]
    venue.concerts()
    venue.bands()
    
    band = Band.all[1]
    band.concerts()
    band.venues()
    
    
    ipdb.set_trace()