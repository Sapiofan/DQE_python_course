import sqlite3
from haversine import haversine

# connect to SQLite database
conn = sqlite3.connect('cities.db')
c = conn.cursor()

# create table to store cities and their coordinates
c.execute('''CREATE TABLE IF NOT EXISTS cities
             (name TEXT PRIMARY KEY, lat REAL, lon REAL)''')
conn.commit()

# haversine function. Details can be found here:
# https://en.wikipedia.org/wiki/Haversine_formula
# https://pypi.org/project/haversine/
def haversine_fun(lat1, lon1, lat2, lon2):
    city1 = (lat1, lon1)
    city2 = (lat2, lon2)
    return haversine(city1, city2)


# get city coordinates from the database
def get_db_coordinates(city_name):
    c.execute("SELECT lat, lon FROM cities WHERE name=?", (city_name,))
    result = c.fetchone()
    return result


# add new city coordinates to the database
def add_city(city_name, lat, lon):
    c.execute("INSERT INTO cities (name, lat, lon) VALUES (?, ?, ?)", (city_name, lat, lon))
    conn.commit()


def get_valid_coordinates(city_name):
    while True:
        try:
            lat = float(input(f"Please enter the latitude for {city_name}: "))
            lon = float(input(f"Please enter the longitude for {city_name}: "))

            # Validate latitude and longitude range
            if not (-90 <= lat <= 90):
                print("Latitude must be between -90 and 90 degrees. Please try again.")
                continue
            if not (-180 <= lon <= 180):
                print("Longitude must be between -180 and 180 degrees. Please try again.")
                continue

            return lat, lon
        except ValueError:
            print("Invalid input. Please enter numeric values for latitude and longitude.")

# get coordinates from user or db
def get_coordinates(city_name):
    city_name = city_name.strip().upper()
    coords = get_db_coordinates(city_name)

    if coords:
        print(f"Found coordinates for {city_name}: {coords}")
        return coords
    else:
        print(f"Coordinates for {city_name} not found.")
        lat, lon = get_valid_coordinates(city_name)
        add_city(city_name, lat, lon)
        print(f"Coordinates for {city_name} have been saved.")
        return (lat, lon)


def calculate_distance():
    city1 = input("Enter the name of the first city: ")
    city2 = input("Enter the name of the second city: ")

    # Get coordinates for both cities
    lat1, lon1 = get_coordinates(city1)
    lat2, lon2 = get_coordinates(city2)

    # calculate distance
    distance = haversine_fun(lat1, lon1, lat2, lon2)
    print(f"The straight-line distance between {city1} and {city2} is {distance:.2f} kilometers.")


if __name__ == "__main__":
    calculate_distance()

conn.close()