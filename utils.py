import pandas as pd
import os

DB_FILE = "database.csv"

# Create database if not exists
if not os.path.exists(DB_FILE):
    df = pd.DataFrame(columns=["user_rating", "user_review", "ai_summary"])
    df.to_csv(DB_FILE, index=False)

def save_entry(rating, review, summary):
    df = pd.read_csv(DB_FILE)
    df.loc[len(df)] = [rating, review, summary]
    df.to_csv(DB_FILE, index=False)

def load_entries():
    return pd.read_csv(DB_FILE)
