import psycopg2
from config import config

def insert_elements():

    insert_element_sql  = """
        INSERT INTO vendors(vendor_name)
        VALUES (%s)
    """

    params = config()

    with psycopg2.connect(**params) as connect:
        with connect.cursor() as cursor:
            cursor.execute(insert_element_sql, ("SAlTA",))
        connect.commit()


def insert_phone_book_data():
    phone: str = input("Enter the phone to add: ")
    username: str = input("Enter your username to add: ")
    sql_query: str = f"INSERT INTO phone_book(phone, owner_name) VALUES ('{phone}', '{username}');"

    params: dict = config()

    with psycopg2.connect(**params) as connect:
        with connect.cursor() as cursor:
            cursor.execute(sql_query)
        connect.commit()

def show_all_user_phones(username: str = "", phone: str = ""):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="зщыепкуы",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        cursor = connection.cursor()
        sql_query: str = f"SELECT * FROM phone_book WHERE owner_name LIKE '%{username}%' AND phone LIKE '%{phone}%';"

        cursor.execute(sql_query)
        all_user_phones = cursor.fetchall()
        for row in all_user_phones:
            print("ID:", row[0], "\t\tphone:", row[1], "\t\tusername", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def change_phone():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="зщыепкуы",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        username: str = input("Input username whose phone you want to change: ")
        cursor = connection.cursor()
        sql_query: str = f"SELECT * FROM phone_book WHERE owner_name LIKE '{username}';"
        cursor.execute(sql_query)
        all_user_phones = cursor.fetchall()
        for row in all_user_phones:
            print("ID:", row[0], "\t\tphone:", row[1], "\t\tusername", row[2])
        phone_id: str = input("Enter phone id: ")
        phone_number: str = input("Enter new phone: ")
        sql_query: str = f"""
            UPDATE phone_book
            SET phone = '{phone_number}'
            WHERE id='{phone_id}'
        """
        cursor.execute(sql_query)
        connection.commit()
        print("Your request completed successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def delete_phone_data(username: str = ""):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="зщыепкуы",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        cursor = connection.cursor()
        sql_query: str = f"SELECT * FROM phone_book WHERE owner_name LIKE '{username}';"
        cursor.execute(sql_query)
        all_user_phones = cursor.fetchall()
        for row in all_user_phones:
            print("ID:", row[0], "\t\tphone:", row[1], "\t\tusername", row[2])
        phone_id: str = input("Enter phone id which you want to delete: ")
        sql_query: str = f"""
            DELETE FROM phone_book
            WHERE id='{phone_id}' AND owner_name LIKE '{username}'
        """
        cursor.execute(sql_query)
        connection.commit()
        print("Your request completed successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#insert_elements()
insert_phone_book_data()
# show_all_user_phones(phone="d")
# change_phone()
#delete_phone_data(username="Salta")
