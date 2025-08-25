import csv
import datetime
from random import random, choice, randint, uniform

categories = ["Ropa", "Hogar", "Electronica"]
products = ["Televisor", "Celular", "Laptop", "Camisa", "Pantalon", "Zapatos", "Jgo sala", "Sofa Cama", "Closet"]
with open("sales","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Id","Date","Product","Category","Price" ,"Quantity", "Total"])
    for i in range(1,100001):
        date = datetime.date(2025, randint(1,12), randint(1,28))
        product = choice(products)
        categorie = "Electronica" if product in ["Televisor", "Celular", "Laptop"] else "Ropa" if product in ["camisa", "Pantalon", "Zapatos"] else "Hogar"
        price = round(uniform(100, 2000), 2)
        quantity = randint(1, 10)
        total = round(price * quantity, 2)
        writer.writerow([i, date, product, categorie, price, quantity, total])
