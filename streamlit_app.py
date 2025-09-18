import streamlit as st
from web3_utils import get_eth_balance, get_transactions, get_eth_price

st.set_page_config(page_title="Blockchain Portfolio Explorer", layout="wide")

st.title("🔗 Blockchain Portfolio Explorer")
st.write("Enter an Ethereum wallet address to explore balances and recent transactions.")

address = st.text_input("Ethereum Wallet Address (0x...)", value="")

if address:
    # Fetch ETH balance
    eth_balance = get_eth_balance(address)
    eth_price = get_eth_price()
    usd_value = eth_balance * eth_price

    st.metric(label="ETH Balance", value=f"{eth_balance:.4f} ETH", delta=f"${usd_value:,.2f} USD")

    # Fetch transactions
    st.subheader("Recent Transactions")
    txs = get_transactions(address, limit=5)
    if txs:
        for tx in txs:
            st.write(f"Hash: {tx['hash']}")
            st.write(f"From: {tx['from']}")
            st.write(f"To: {tx['to']}")
            st.write(f"Value: {int(tx['value']) / 1e18:.4f} ETH")
            st.write("---")
    else:
        st.write("No recent transactions found.")
