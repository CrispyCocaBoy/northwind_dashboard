import duckdb
import pandas as pd

df = duckdb.query("""
SELECT cat.categoryname,  sum(od.Quantity) as Quantity
FROM sqlite_scan('northwind.db', 'Categories') as cat
JOIN sqlite_scan('northwind.db', 'products')as pd ON cat.CategoryID = pd.CategoryID
JOIN sqlite_scan('northwind.db', 'OrderDetails') as od ON pd.ProductID = od.ProductID
GROUP BY cat.categoryname
""").df()

# Creazione della dash




