import sqlite3

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
                       (f'Product{i}',f'{description[i]}', f'{i * 100}'))
    
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

if __name__ == "__main__":
    initiate_db()
    
    print(get_all_products())