import pandas as pd
import sqlite3
import os

db = sqlite3.connect("bluestock_mf.db")

processed_path = "data/processed"

for file in os.listdir(processed_path):
    if file.endswith(".csv"):
        table_name = file.replace(".csv","")
        df = pd.read_csv(os.path.join(processed_path,file))
        df.to_sql(table_name, db, if_exists="replace", index=False)
        print("Loaded:", table_name)

db.close()

print("Database Created Successfully!")