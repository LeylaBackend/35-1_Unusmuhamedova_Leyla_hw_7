import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as You_have_a_sql_error:
        print(You_have_a_sql_error)

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as You_have_a_sql_error:
        print(You_have_a_sql_error)


def create_products(connection):
    products = [
    ('Kefir', 58.25, 5),
    ('Carrots', 45.15, 8),  #штучно
    ('ASU', 45.07, 1),
    ('Chips', 65.30, 2),
    ('Cookies', 80.38, 10),  #штучно
    ('Milk', 35.15, 2),
    ('Eggs', 15.00, 10),     #штучно
    ('Sausages', 70.25, 4),
    ('Butter', 40.40, 2),
    ('мыло', 68.15, 1),
    ('Жидкое мыло', 45.15, 1), #мешок
    ('Хозяйственное мыло', 65.05, 1),     #мешок
    ('Детское мыло', 25.00, 2),
    ('Лечебно-косметическое мыло', 70.10, 2),
    ('Bread', 35.15, 2)
]
    sql = """
         INSERT INTO products 
         (product_title, price, quantity) 
         VALUES (?, ?, ?)
         """
    cursor = connection.cursor()
    cursor.execute(sql, connection)
    connection.commit()

# def changes_quantity_of_product(connection, new_quantity, product_id):
#     sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
#     cursor = connection.cursor()
#     cursor.execute(sql, (new_quantity, product_id))
#     connection.commit()

# def changes_price_of_products(connection, new_price, product_id):
#     sql = '''UPDATE products SET price = ? WHERE id = ?'''
#     cursor = connection.cursor()
#     cursor.execute(sql, (new_price, product_id))
#     connection.commit()

# def delete_products(connection, products_id):
#     sql = '''DELETE FROM products WHERE id = ?'''
#     cursor = connection.cursor()
#     cursor.execute(sql, (products_id,))
#     connection.commit()

# def select_all_products(connection):
#     sql = '''SELECT * FROM products'''
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def choose_product(connection):
#     sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

def find_products():
    sql = '''
    SELECT * FROM products WHERE product_title LIKE '%мыло%'
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


connection = create_connection('hw_7.db')

sql_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,  
    quantity INTEGER NOT NULL
);
'''

if connection is not None:
    print("The connection to the database has been established")
    # create_table(connection, sql_create_products_table)
    # changes_price_of_products(connection, 90, 1)
    # changes_quantity_of_product(connection, 12, 15)
    # delete_products(connection, 3)
    # select_all_products(connection)
    # choose_product(connection)
    find_products()

    connection.close()