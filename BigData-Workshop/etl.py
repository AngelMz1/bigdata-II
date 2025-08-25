import sqlite3
import csv
from tabulate import tabulate

def conection():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    return con, cur
#crear tabla
def create_table():
    conection()
    query = '''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            date DATE,
            product TEXT,
            category TEXT,
            price REAL,
            quantity INTEGER,
            total REAL
        )
    '''
    cur.execute(query)
    con.commit()
    con.close()
    print("Tabla creada")


#insertar datos
def insert_data():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    with open('sales', 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            query = '''
                INSERT INTO sales (id, date, product, category, price, quantity, total)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            cur.execute(query, row)
    con.commit()
    con.close()
    print("Datos insertados")

#create_table()
#insert_data()

#Insights
def category_insight():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = '''
        SELECT category, SUM(total) as total_sales
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    '''
    cur.execute(query)
    data = cur.fetchall()
    formatedData = [[row[0], f'{row[1]:,.2f}'] for row in data]
    con.close()
    print(tabulate(formatedData, headers=['Category', 'Total Sales'], tablefmt='psql'))
    print("Insight: Ventas por categoría")

def top_5_insight():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = '''
        SELECT product, SUM(quantity) as total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 5
    '''
    cur.execute(query)
    data = cur.fetchall()
    formatedData = [[row[0], f'{row[1]:,.2f}'] for row in data]
    con.close()
    print(tabulate(formatedData, headers=['Product', 'Total Quantity'], tablefmt='psql'))
    print("Insight: Top 5 productos más vendidos")


category_insight()
top_5_insight()