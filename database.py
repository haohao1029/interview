import sqlite3

DATABASE = "vending_machine.db"

conn = sqlite3.connect(DATABASE, check_same_thread=False)

def init_db():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, quantity INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, item_id INTEGER, amount_paid INTEGER, date TEXT)''')
    conn.commit()


def add_item(name, price, quantity):
    c = conn.cursor()
    c.execute('INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()


def get_items():
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    return items


def update_item(item_id, name=None, price=None, quantity=None):
    c = conn.cursor()
    if name:
        c.execute('UPDATE items SET name = ? WHERE id = ?', (name, item_id))
    if price:
        c.execute('UPDATE items SET price = ? WHERE id = ?', (price, item_id))
    if quantity is not None:
        c.execute('UPDATE items SET quantity = ? WHERE id = ?', (quantity, item_id))
    conn.commit()


def delete_item(item_id):
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()


def create_transaction(item_id, amount_paid, date):
    c = conn.cursor()
    c.execute('INSERT INTO transactions (item_id, amount_paid, date) VALUES (?, ?, ?)', (item_id, amount_paid, date))
    conn.commit()


def get_transactions():
    c = conn.cursor()
    c.execute('SELECT * FROM transactions')
    transactions = c.fetchall()
    return transactions


# Don't forget to initialize the database by calling init_db() when your application starts.
init_db()
