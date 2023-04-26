import psycopg2
from config import config

def create_tables():
    create_citizens_table_sql = """
        CREATE TABLE citizens(
            citizen_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL
        );
    """
    
    create_accounts_table_sql = """
        CREATE TABLE contacts(
            contact_id SERIAL PRIMARY KEY,
            citizen_id INTEGER NOT NULL,
            address VARCHAR(255) NOT NULL,
            phone_number INTEGER NOT NULL,
            FOREIGN KEY (citizen_id)
                REFERENCES citizens (citizen_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
    """


    connect = None

    try:
        params = config()

        connect = psycopg2.connect(**params)

        with connect.cursor() as cursor:
            cursor.execute(create_citizens_table_sql)
            cursor.execute(create_accounts_table_sql)

        connect.commit()
        print("Successfully created tables")
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not create the tables", _ex)
    finally:
        if connect:
            connect.close()


if __name__ == "__main__":
    create_tables()