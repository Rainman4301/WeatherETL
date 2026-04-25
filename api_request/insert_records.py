from api_request import *
import psycopg2

# print(mock_fetch_data())


def connect_to_db():
    print("Connecting to the database...")

    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        # print(conn)

        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise


def create_table(conn):
    print("Creating the weather_data table if it doesn't exist...")

    try:
        cursor = conn.cursor()
        
        cursor.execute( """

            CREATE SCHEMA IF NOT EXISTS dev;

            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );

            """)


        conn.commit()
        print("Table created successfully.")


        cursor.close()


    except psycopg2.Error as e:
        print("Error creating the table:", e)
        raise

    




def insert_record(conn, data):
    print("Inserting a record into the database...")

    try:

        weather = data['current']
        location = data['location']

        cursor = conn.cursor()
        cursor.execute(
        """
            INSERT INTO dev.raw_weather_data (
            city,
            temperature, 
            weather_description, 
            wind_speed, 
            time, 
            inserted_at,
            utc_offset
            )
            VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """,
        
        (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0] if weather['weather_descriptions'] else None,
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        )
        )

        conn.commit()
        print("Record inserted successfully.")
        cursor.close()

    except psycopg2.Error as e:
        print("Error inserting the record:", e)
        raise



def main():

    try:
        # data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_record(conn, data)
    except Exception as e:
        print("An error occurred:", e)

    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")
    

 
