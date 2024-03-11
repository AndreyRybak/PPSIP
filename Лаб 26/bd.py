import sqlite3
def add_product(name, price, category):
    conn = sqlite3.connect('catalog.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO products (name, price, category) VALUES (?, ?, ?)', (name, price, category))
    conn.commit()

    conn.close()

# Пример использования функции для добавления нового продукта
add_product('Новый товар', 500, 'Категория 2')
