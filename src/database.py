# src/database.py

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def create_tables():
    """Creates tables based on the SQL schema file"""
    try:
        with open('sql/db_schema.sql', 'r') as f:
            schema_sql = f.read()
        with engine.connect() as connection:
            connection.execute(text(schema_sql))
        print("Tables created/verfied successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    create_tables()