from api.geo_data import geo_data_fetch_save
from api.weather import weather_data_fetch_save

from database.schema import db_schema, connection, DB_PATH
from database.create_tables import initialize_database
from database.insert_data import insert_data_from_csv
from database.queries import test_get_all_cities

def main():
    #  geoloc
    geo_data_fetch_save()
    #  data weather cities
    weather_data_fetch_save()

    # init db
    db_schema(connection)
    initialize_database(DB_PATH)

    insert_data_from_csv(connection, 'data_csv/weather_data.csv')

    # queries
    cities = test_get_all_cities(connection)
    print(cities)

    connection.close()

if __name__ == "__main__":
    main()
