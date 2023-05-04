import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = 'зщыепкуы',
    user = 'postgres'
)
current = config.cursor()
arr = []
with open('user.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phone_book VALUES (%s, %s, %s) RETURNING *; 
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()
