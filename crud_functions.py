import sqlite3

DEFAULT_BALANCE = 1000

def initiate_db():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )                
    ''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
    )                
    ''')
    connection.commit()
    connection.close()

def set_all_products():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    description = ['', 'Сладенькая и в некоторых случаях даже полезная',
                   'Неведомых свойств волшебная жидкость',                   
                   'Истинно органическая субстанция неведомого назначения',
                   'Много не пить - можно отравиться']
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Микстура {i}',f'{description[i]}', f'{i * 100}'))
    
    connection.commit()
    connection.close()    

def get_all_products():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM Products')
    
    result = cursor.fetchall()
    
    connection.commit()
    connection.close()
    return result

def add_user(username, email, age):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, DEFAULT_BALANCE ))
        
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT id FROM Users WHERE username = ?', (username,))
    result = cursor.fetchall()
         
    connection.commit()
    connection.close()
    if result == []:
        return False
    else:
        return True
    
if __name__ == "__main__":
    initiate_db()
    print(is_included(''))
    