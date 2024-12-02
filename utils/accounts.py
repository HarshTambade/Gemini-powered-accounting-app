import streamlit as st

def display_accounts():
    st.header("Account Management")

    # Account creation form
    with st.form("account_form"):
        account_type = st.selectbox(
            "Account Type",
            ["Assets", "Liabilities", "Income", "Expenses"]
        )
        account_name = st.text_input("Account Name")
        submit = st.form_submit_button("Add Account")

        if submit and account_name:
            if 'accounts' not in st.session_state:
                st.session_state.accounts = {"Assets": [], "Liabilities": [], "Income": [], "Expenses": []}
            if account_name not in st.session_state.accounts[account_type]:
                st.session_state.accounts[account_type].append(account_name)
                st.success(f"Added {account_name} to {account_type}")

    # Display accounts
    for account_type, accounts in st.session_state.get('accounts', {}).items():
        if accounts:
            st.subheader(account_type)
            st.write(", ".join(accounts))
