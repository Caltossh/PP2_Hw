import psycopg2
from config import config


def delete_citizen(name, surname):
    '''function delele from citizens table and from contacts table phone number of the same citizen'''
    delete_citizen_sql = """
    DELETE FROM citizens 
    WHERE name = %s AND surname = %s
    RETURNING citizen_id
    """
    delete_contact_sql = """
    DELETE FROM contacts
    WHERE citizen_id = %s
    """
    citizen_id = None

    params = config()

    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(delete_citizen_sql, (name, surname))
                citizen_id = cursor.fetchone()[0]
                cursor.execute(delete_contact_sql, (citizen_id,))
            connect.commit()
            print("Successfully deleted data")
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not complete delete query: ", _ex)


if __name__ == "__main__":
    delete_citizen('Benjamin', 'Franklin')
    