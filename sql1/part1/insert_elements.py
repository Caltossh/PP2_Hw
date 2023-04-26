import pandas as pd
import psycopg2
from config import config

def console_insert_into_citizens():
    """function to insert into citizens table through console """
    insert_sql = """
        INSERT INTO citizens(name, surname, age)
        VALUES (%s, %s, %s)
        RETURNING citizen_id;
    """
    name = input("Write the name of the citizen: ").strip()
    surname = input("Write the surname of the citizen: ").strip()
    age = int(input("Enter the age: "))
    connect = None
    citizen_id = None
    try:
        params = config()

        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(insert_sql, (name, surname, age))
            citizen_data = cursor.fetchone()[0]
        connect.commit()
        print("Successfully inserted new citizen: ", citizen_data)

    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not complete insert query", _ex)
    finally:
        if connect:
            connect.close()


def console_insert_into_contacts():
    """function to insert into accounts through console"""
    insert_sql = """
        INSERT INTO contacts(citizen_id, address, phone_number)
        VALUES (%s, %s, %s)
        RETURNING *;
    """

    find_citizen_id_sql = """
        SELECT citizen_id FROM citizens
        WHERE name = %s AND surname = %s;
    """
    name = input("Enter name: ").strip()
    surname = input("Enter surname: ").strip()
    address = input("Enter the address: ").strip()
    phone_number = int(input("Enter the phone number: "))
    connect = None
    contacts_id = None
    citizen_id = None
    try:
        params = config()

        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(find_citizen_id_sql, (name, surname))
            citizen_id = cursor.fetchone()[0]
            cursor.execute(insert_sql, (citizen_id, address, phone_number))
            contact_data = cursor.fetchone()[0]
            
        connect.commit()
        print("Successfully inserted new phone_number: ", contact_data)

    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not complete insert query: ", _ex)
    finally:
        if connect:
            connect.close()


def csv_insert_into_citizens():
    """function to insert from csv into citizens"""
    insert_sql = """
        INSERT INTO citizens(name, surname, age)
        VALUES (%s, %s, %s)
        RETURNING *;
    """
    df = pd.read_csv('./citizens_input.csv')
    print(df['name'][0])
    print(df["surname"][0])
    print(df["age"][0])
    connect = None
    name = df['name'][0]
    surname = df['surname'][0]
    age = int(df['age'][0])

    citizen_id = None
    try:
        params = config()
        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(insert_sql, (name, surname, age))
            citizen_data = cursor.fetchone()[0]
        connect.commit()
        print("Successfully inserted: ", citizen_data)
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not complete insert query: ", _ex)
    finally:
        if connect:
            connect.close()



def csv_insert_into_contacts():
    """function to insert into contacts table through console"""
    insert_sql = """
        INSERT INTO contacts(citizen_id, address, phone_number)
        VALUES ((SELECT citizen_id FROM citizens
                 WHERE name = %s AND surname = %s), %s, %s)
        RETURNING *;
    """
    df = pd.read_csv('./accounts_input.csv')
    name = df['name'][0]
    surname = df['surname'][0]
    address = df['address'][0]
    phone_number = int(df['phone_number'][0])
    connect = None
    account_id = None

    try:
        params = config()

        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(insert_sql, (name, surname, address, phone_number))
            contact_data = cursor.fetchone()[0]
            
        connect.commit()
        print("Successfully inserted new phone_number: ", contact_data)

    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not complete insert query: ", _ex)
    finally:
        if connect:
            connect.close()
        



if __name__ == "__main__":
    #console_insert_into_citizens()
    console_insert_into_contacts()
    #csv_insert_into_citizens()
    #csv_insert_into_contacts()