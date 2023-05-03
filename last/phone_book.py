import psycopg2
import csv
from config import config

# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="зщыепкуы"
# )
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

# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="admin"
# )

# cur = conn.cursor()

# def queryData():
#     cur.execute("SELECT * FROM get_records_by_pattern('John')")
#     data = cur.fetchall()

#     for row in data:
#         print(row)

# def insertData():
#     personName = input('Input new username: ')
#     phoneNumber = input('Input new phone number: ')
#     conn.autocommit = True 
#     cur.execute("CALL insert_data(%s, %s);", (personName, phoneNumber))


# def updateData():
#     personName = input('Input the name of the user that you want the update her/his number: ')
#     phoneNumber = input('Input the new phone number: ')
#     conn.autocommit = True 
#     cur.execute("CALL update_data(%s, %s);", (personName, phoneNumber))

# def insertListOfDate():
#     users = [
#         ['Stark', '80789013456'],
#         ['Admin', '80779903663'],
#         ['Sasha', '80779903663p']
#     ]
#     print('The incorrect data')
#     cur.execute(f"CALL insert_list_of_users(ARRAY{users})")
#     cur.execute(" SELECT * FROM postgres.public.phone_book_incorrect_data ")
#     data = cur.fetchall()

#     for row in data:
#         print(row)

# def getDataFromPagination():
#     limit = 3
#     offset = 0

#     # Define the cursor and call the function
#     cur.execute('SELECT * FROM paginating(%s, %s)', (limit, offset))
#     # conn.autocommit = True 
#     data = cur.fetchall()
#     k = 1
#     for i in data:
#         print(f"{k}.Name: {i[1]}, number: {i[2]}")
#         k += 1
#     # print(data)

# def deleteDataWithNameOrPhone():
#     mode = ''
#     x = input("With what parameter you want to delete the person from phonebook?\n1 - with username\n2 - with number\n")
#     if(x == '1'):
#         mode = 'username'
#         name = input('Input the username: ')
#         cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (mode, name))
#     if(x == '2'):
#         mode = 'phone'
#         number = input('Input the phone number: ')
#         cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (mode, number))



# print("What do you want to do?\n\
#       1. Return data from the table\n\
#       2. Insert contact\n\
#         2.1 update existing contact\n\
#       3. Insert list of users\n\
#       4. Query all data from table\n\
#       5. Delete with user name or number")
# x = input("Enter number 1-5\n")
# if(x == '1'):
#     queryData()
# elif(x == '2'):
#     insertData()
# elif(x == '2.1'):
#     updateData()
# elif(x == '3'):
#     insertListOfDate()
# elif(x == '4'):
#     getDataFromPagination()
# elif(x == '5'):
#     deleteDataWithNameOrPhone()
# conn.commit()
    
# cur.close()
# conn.close()
# # cur.execute(' DELETE FROM postgres.public.phone_book ')


