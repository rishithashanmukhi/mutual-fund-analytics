import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(raw_path, file))
        df.drop_duplicates(inplace=True)
        df=df.bfill()
        df.to_csv(os.path.join(processed_path, file), index=False)
        print("Cleaned:", file)