import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# SQLite connection
sqlite_conn = sqlite3.connect("inventory.db")

# MySQL connection
mysql_engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/inventory"
)

# Get all table names from SQLite
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    sqlite_conn
)

# Copy each table to MySQL
for table in tables["name"]:
    df = pd.read_sql(f"SELECT * FROM {table}", sqlite_conn)
    df.to_sql(table, mysql_engine, if_exists="replace", index=False)
    print(f"Imported {table}")

sqlite_conn.close()