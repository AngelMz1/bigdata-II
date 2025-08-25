import sqlite3
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def conection():
    try:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        return con, cur
    except sqlite3.Error as e:
        print(f"Error connecting to database{e}")
        return None, None
#crear tabla
def create_table():
    con, cur = conection()
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
    con, cur = conection()
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
    con, cur = conection()
    query = '''
        SELECT category, SUM(total) as total_sales
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    '''
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    #chart data
    category = [row[0] for row in data]
    total_sales = [row[1] / 1_000_000 for row in data]
    plt.figure(figsize=(10, 6))
    plt.bar(category, total_sales)
    plt.xlabel('Category')
    plt.ylabel('Total Sales (millions)')
    plt.title('sales by category')
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig("Category_insight.png")
    #table data
    formatedData = [[row[0], f'{row[1]:,.2f}'] for row in data]
    print(tabulate(formatedData, headers=['Category', 'Total Sales'], tablefmt='psql'))
    print("Insight: sales by category")

def top_5_insight():
    con, cur = conection()
    query = '''
        SELECT product, SUM(quantity) as total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 5
    '''
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    #chart data
    product = [row[0] for row in data]
    quantity = [row[1] for row in data]
    plt.figure(figsize=(10, 6))
    plt.bar(product, quantity)
    plt.xlabel('Product')
    plt.ylabel('Total Quantity')
    plt.title('Top 5 productos más vendidos')
    plt.tight_layout()
    print("Chart 'Top_5_insight.png' saved successfully.")
    plt.savefig("Top_5_insight.png")
    #table data
    formatedData = [[row[0], f'{row[1]:,}'] for row in data]
    print(tabulate(formatedData, headers=['Product', 'Total Quantity'], tablefmt='psql'))
    print("Insight: Top 5 productos más vendidos")

def highest_billing_month_insight():
    con, cur = conection()
    query = '''
        SELECT strftime('%Y-%m', date) as month, SUM(total) as total_sales
        FROM sales
        GROUP BY month
        ORDER BY total_sales DESC
        LIMIT 1
    '''
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    #chart data
    month = [row[0] for row in data]
    total_sales = [row[1] / 1_000_000 for row in data]
    plt.figure(figsize=(10, 6))
    plt.bar(month, total_sales)
    plt.xlabel('Month')
    plt.ylabel('Total Sales (millions)')
    plt.title('Highest billing month')
    plt.tight_layout()
    print("Chart 'Highest_billing_month_insight.png' saved successfully.")
    plt.savefig("Highest_billing_month_insight.png")
    #table data
    formatedData = [[row[0], f'{row[1]:,.2f}'] for row in data]
    print(tabulate(formatedData, headers=['Month', 'Total Sales'], tablefmt='psql'))
    print("Insight: Mes con mayor venta")
   
category_insight()
top_5_insight()
highest_billing_month_insight()