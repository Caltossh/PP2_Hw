import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'зщыепкуы'
)

current = config.cursor()
sql = '''
        CREATE TABLE snake(
            username VARCHAR(100) PRIMARY KEY,
            level VARCHAR(20),
            score VARCHAR(20)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()


