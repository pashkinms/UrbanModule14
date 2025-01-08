import sqlite3

connection = sqlite3.connect('not_telegram1.db')
cursor = connection.cursor()
"""
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)             
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?) ",
                   (f'User{i}', f'example{i}@gmail.com', str(i*10), str(1000), ))


for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ('500', f'User{i}',))


for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}', ) )


cursor.execute("SELECT * FROM Users WHERE NOT age = 60")
users = cursor.fetchall()

for user in users:
    print(user)
"""

# cursor.execute("DELETE FROM Users WHERE id = 6")
cursor.execute('SELECT COUNT(*) FROM Users')
totalUsers = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
totalBalance = cursor.fetchone()[0]

print(totalBalance/totalUsers)
connection.commit()
connection.close()