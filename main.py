import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DB_URL)
conn = engine.connect()

df = pd.read_csv("data.csv")
print("Данные загружены:", df.head())

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["date"] = pd.to_datetime(df["date"])

print("🔧 Данные очищены:", df.head())

df.to_sql("process_data", con = conn, if_exists="replace", index = False)
print("✅ Данные загружены в PostgreSQL!")

conn.close()