import streamlit as st
from utils.dashboard import display_dashboard
from utils.transactions import display_transactions
from utils.reports import display_reports
from utils.accounts import display_accounts
from utils.config import Config

def main():
    st.set_page_config(
        page_title="Financial Management System",
        page_icon="💰",
        layout="wide"
    )

    st.title("Financial Management System")

    # Sidebar Navigation
    page = st.sidebar.selectbox(
        "Select Module",
        ["Dashboard", "Transactions", "Reports", "Accounts", "Settings"]
    )

    # Module Routing
    if page == "Dashboard":
        display_dashboard()
    elif page == "Transactions":
        display_transactions()
    elif page == "Reports":
        display_reports()
    elif page == "Accounts":
        display_accounts()
    elif page == "Settings":
        display_settings()

def display_settings():
    st.header("Settings")
    st.write("Configure your application settings here.")
    # Add settings-related options here.

if __name__ == "__main__":
    main()
