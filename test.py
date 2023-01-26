import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='B07o01o15m',
    database='poznamky'
)
user = ('ferko1','feri123')
cursor = db.cursor()
cursor.execute('SELECT * FROM users')

if user in cursor:
    print(f'Cauko {user[0]}')
else:
    print(f'Pal do pice {user[0]}')