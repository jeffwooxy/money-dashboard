# src/charts.py
import pandas as pd
import plotly.express as px

def monthly_transaction(df_transactions):
    df_transactions["month"] = df_transactions["transaction_date"].dt.to_period('M')
    monthly_summary = df_transactions.groupby(['month'])['amount'].sum().reset_index()
    monthly_summary['month'] = monthly_summary['month'].dt.to_timestamp() # Convert Period back to Timestamp for plotting
    fig_line = px.line(monthly_summary, x='month', y='amount',
                    title='Monthly Expense', labels={'amount': 'Amount (AUD)', 'month': 'Month'})
    fig_line.update_layout(hovermode="x unified")
    return fig_line