import streamlit as st
import plotly.express as px
import pandas as pd

from utils.transactions import get_transactions_df

def display_dashboard():
    st.header("Dashboard")

    df = get_transactions_df()

    if not df.empty:
        # Summary Metrics
        col1, col2, col3 = st.columns(3)
        total_income = df[df['type'] == 'Income']['amount'].sum()
        total_expenses = df[df['type'] == 'Expense']['amount'].sum()
        net_income = total_income - total_expenses

        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Expenses", f"${total_expenses:,.2f}")
        col3.metric("Net Income", f"${net_income:,.2f}")

        # Income vs Expenses Chart
        st.subheader("Income vs Expenses")
        fig = px.bar(
            df.groupby('type')['amount'].sum().reset_index(),
            x='type',
            y='amount',
            color='type'
        )
        st.plotly_chart(fig, use_container_width=True)

        # Transaction Timeline
        st.subheader("Transaction Timeline")
        df['date'] = pd.to_datetime(df['date'])
        timeline_data = df.groupby(['date', 'type'])['amount'].sum().reset_index()
        fig = px.line(timeline_data, x='date', y='amount', color='type')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No transactions available. Add some transactions to see the dashboard.")
