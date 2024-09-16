# CONCERTS DATABASE

## Project Overview
- This application is a Concerts Database System. It allows users to manage concerts, bands, and venues through a set of functions that inserts and manages concert data. The application does operations such as retrieving concert details, adding bands and venues, and tracking performances at specific venues on certain dates.

## Features

1. Adds and manages informations about bands including their name and hometown.
2. Adds and manages venue information such as name and city.
3. Schedules concerts by associating bands with venues and dates.
4. Retrieves concerts for a specific band or venue.
5. Gets details of bands performing at specific venues.

6.Checks if a concert is taking place in the band's hometown.
7. Tracks which band has performed the most concerts.

8.Identifies the most frequent band at a particular venue.


## Technologies Used

- Python
- SQLite
## Tables
The application consists of the following tables:

### 1. Bands:
- `id` (Primary Key)
- `name` (String)
- `hometown` (String)
### 2. Venues:
- `id` (Primary Key)
- `title` (String)
- `city` (String)
### 3. Concerts:
-`id` (Primary Key)
- `band_id` (Foreign Key from bands)
- `venue_id` (Foreign Key from venues)
- `date` (String representing the concert date)

## Installation
1. Clone the repository using the command below.
        git@github.com:Gift-World/Phase-3-Code-Challenge-3.git

2. Run the application using the command below:
        python concerts_database.py
        


## Prerequisites
You will need the following installed to run this project:

- Python 3.x
- SQLite3 or PostgreSQL
- sqlite3 library (built into Python) or psycopg2 for - - PostgreSQL


## Setup
1. Clone the repository
        git@github.com:Gift-World/Phase-3-Code-Challenge-3.git

### 2.Set up the database      
#### Using SQLite

1. Create the SQLite database and tables by running the provided migration script:

    ```bash
    python concerts_database.py
    ```

    This script will create the `bands`, `venues`, and `concerts` tables in an SQLite database named `concerts_database.db`.



