import psycopg2
from config import config


def update_citizens_table(citizen_id, name, surname):
    """function to update elements in the table"""
    
    update_sql = """
        UPDATE citizens
        SET name = %s,
            surname = %s
        WHERE citizen_id = %s
        RETURNING * ;
    """
    connect = None
    try:
        params = config()
        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(update_sql, (name, surname, citizen_id))
            output = cursor.fetchall()[0]

        connect.commit()
        print("Successfully updated the citizens table: ", output)
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not update the table: ", _ex)
    finally:
        if connect:
            connect.close()


def update_phone_by_name(name, surname, phone_number):
    """function to update elements in the table"""
    
    update_sql = """
        UPDATE contacts
        SET phone_number = %s
        WHERE citizen_id = (SELECT citizen_id FROM citizens
                            WHERE name = %s AND surname = %s)
        RETURNING * ;
    """
    connect = None
    try:
        params = config()
        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(update_sql, (phone_number, name, surname))
            output = cursor.fetchall()[0]

        connect.commit()
        print("Successfully updated the accounts table: ", output)
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not update the table: ", _ex)
    finally:
        if connect:
            connect.close()

if __name__ == "__main__":
    #update_citizens_table(5, "Elon", "Musk")
    update_phone_by_name("Beket", "Barlykov", 111111)
