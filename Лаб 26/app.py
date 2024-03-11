from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_products(sort_by=None, category=None):
    conn = sqlite3.connect('catalog.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM products'

    if category:
        query += ' WHERE category = ?'

    if sort_by:
        query += f' ORDER BY {sort_by}'

    if category:
        cursor.execute(query, (category,))
    else:
        cursor.execute(query)

    products = cursor.fetchall()

    conn.close()
    return products

@app.route('/')
def index():
    products = get_products(sort_by='price', category='Категория 1')
    return render_template('index.html', products=products)

@app.route('/sort', methods=['POST'])
def sort():
    sort_by = request.form['sortBy']
    products = get_products(sort_by=sort_by)
    return render_template('products_table.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)


    @app.route('/add_to_cart', methods=['POST'])
    def add_to_cart():
        product_id = request.form['productId']
        # Здесь вы можете выполнить логику добавления товара в корзину
        # Например, вы можете использовать сессии Flask для хранения состояния корзины
        # Но для этого примера просто воспользуемся алертом
        return 'Товар добавлен в корзину!'

