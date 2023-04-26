import psycopg2
from config import config


def select_citizens_with_filter(value):
    """function that queries from the specified table, with specified filter and value"""
    sql = """
        SELECT * FROM citizens
        WHERE name = %s;
    """
    
    connect = None
    response = None
    
    try:

        params = config()

        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(sql, (value,))
                response = cursor.fetchone()
            connect.commit()
            print("Successfully handled the query: ", response)

    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not resolve the query: ", _ex)


def select_contacts_with_filters(name):
    sql = """
        SELECT * FROM contacts
        WHERE citizen_id = (SELECT citizen_id FROM citizens
                            WHERE name = %s)
    """
    
    connect = None
    response = None
    
    try:

        params = config()

        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(sql, (name,))
                response = cursor.fetchone()
            connect.commit()
            print("Successfully handled the query: ", response)

    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not resolve the query: ", _ex)


if __name__ == "__main__":
   
    select_contacts_with_filters('Salta')