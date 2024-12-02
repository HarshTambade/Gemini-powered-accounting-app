import streamlit as st
import pandas as pd
from datetime import datetime

def display_transactions():
    st.header("Transaction Management")

    # Transaction Form
    with st.form("transaction_form"):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Date", datetime.now())
            amount = st.number_input("Amount", min_value=0.0, step=0.01)
        with col2:
            description = st.text_input("Description")
            category = st.selectbox("Category", ["Sales", "Salary", "Rent", "Utilities", "Other"])
            type_ = st.selectbox("Type", ["Income", "Expense"])
        submit = st.form_submit_button("Add Transaction")

        if submit:
            save_transaction(date, description, amount, category, type_)
            st.success("Transaction added successfully!")

    # Display Recent Transactions
    st.subheader("Recent Transactions")
    df = get_transactions_df()
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No transactions available.")

def save_transaction(date, description, amount, category, type_):
    if 'transactions' not in st.session_state:
        st.session_state.transactions = []
    st.session_state.transactions.append({
        'date': date,
        'description': description,
        'amount': float(amount),
        'category': category,
        'type': type_
    })

def get_transactions_df():
    if 'transactions' in st.session_state:
        return pd.DataFrame(st.session_state.transactions)
    return pd.DataFrame()
