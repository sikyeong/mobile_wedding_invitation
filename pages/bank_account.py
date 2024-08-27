import streamlit as st
import json



def app() :
    # Load bank account information from data/bank_account.json
    with open("./data/bank_account.json", "r") as f:
        bank_accounts = json.load(f)

    st.subheader("Bank Account Information")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Bride: {bank_accounts['bride']['name']}**")
        st.write(f"Account Number: {bank_accounts['bride']['account_number']}")
        st.write(f"Bank Name: {bank_accounts['bride']['bank_name']}")

    with col2:
        st.write(f"**Groom: {bank_accounts['groom']['name']}**")
        st.write(f"Account Number: {bank_accounts['groom']['account_number']}")
        st.write(f"Bank Name: {bank_accounts['groom']['bank_name']}")

if __name__ == "__main__":
    app()