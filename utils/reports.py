import streamlit as st
import plotly.express as px
from utils.transactions import get_transactions_df

def display_reports():
    st.header("Reports")

    report_type = st.selectbox("Report Type", ["Income Statement", "Category Analysis"])

    df = get_transactions_df()

    if not df.empty:
        if report_type == "Income Statement":
            st.subheader("Income Statement")
            income = df[df['type'] == 'Income']
            expenses = df[df['type'] == 'Expense']

            st.write("**Income**")
            st.dataframe(income.groupby('category')['amount'].sum())
            st.write("**Expenses**")
            st.dataframe(expenses.groupby('category')['amount'].sum())

        elif report_type == "Category Analysis":
            st.subheader("Category Analysis")
            category_data = df.groupby('category')['amount'].sum().reset_index()
            fig = px.pie(category_data, names='category', values='amount')
            st.plotly_chart(fig)
    else:
        st.info("No data available for reports.")
