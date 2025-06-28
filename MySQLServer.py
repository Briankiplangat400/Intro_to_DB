import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server using your credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Brian@78"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Always close the connection if it was opened
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()




