import sqlite3
import pandas as pd

con = sqlite3.connect("cadastro.db")

df = pd.read_sql_query("SELECT * FROM clientes", con)

print(df)

con.close()
