import os
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Load all transactions
def fetch_data(query):
    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)
    return df

df_transactions = fetch_data("SELECT * FROM transactions ORDER BY transaction_date;")
df_transactions["transaction_date"] = pd.to_datetime(df_transactions["transaction_date"], dayfirst=True)
# print(df_transactions.head())

# Dash constructor
app = Dash()

# App component list
app.layout = [
    html.Div(children='Transaction Data'),
    dash_table.DataTable(data=df_transactions.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df_transactions, x='transaction_date', y='amount', histfunc='avg'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
