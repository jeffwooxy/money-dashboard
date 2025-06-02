import pandas as pd
from sqlalchemy.types import Date, String, Numeric
from database import engine, create_tables # From database.py

column_names = ['transaction_date', 'amount', 'description', 'balance']

def load_csv_to_db(csv_filepath, table_name='transactions'):
    """Loads data from CSV file into specified database table"""
    try:
        df = pd.read_csv(csv_filepath, header=None, names=column_names)

        # Data Cleaning/Transformation
        # Convert date column to datetime objects, then to date only for SQL
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True).dt.date

        # Convert amount to numeric, handling errors
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df.dropna(subset=['amount'], inplace=True) # Remove rows where amount cannot be converted. To update.

        if 'currency' not in df.columns:
            df['currency'] = 'AUD'

        # Select and reorder columns to match SQL table
        # Ensure all columns in SQL table are present in the data frame
        # expected_columns = ['transaction_date', 'description', 'amount', 'category', 'transaction_type', 'currency']
        expected_columns = ['transaction_date', 'description', 'amount', 'currency']
        df = df[expected_columns]

        # Define SQLAlchemy data types for mapping
        dtype_mapping = {
            'transaction_date': Date,
            'description': String,
            'amount': Numeric,
            # 'category': String,
            # 'transaction_type': String,
            'currency': String
        }

        # Load into PostgreSQL
        print(f"Loaded {len(df)} rows into '{table_name}' table...")
        df.to_sql(table_name, engine, if_exists='append', index=False,dtype=dtype_mapping)
        print(f"Data loaded successfully from {csv_filepath} to {table_name}.")
    
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")

if __name__ == "__main__":
    create_tables() # Ensure tables exist
    csv_file_path = 'data/CSVData.csv'
    load_csv_to_db(csv_file_path)