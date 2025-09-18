import streamlit as st
from web3_utils import get_eth_balance, get_transactions, get_eth_price

# Page config
st.set_page_config(
    page_title="Blockchain Portfolio Explorer",
    page_icon="🔗",
    layout="wide",
)

# Custom CSS for award-winning design vibes
st.markdown("""
    <style>
    /* Global */
    .stApp {
        background: linear-gradient(180deg, #0f2027, #203a43, #2c5364);
        font-family: 'Inter', sans-serif;
        color: #f5f7fa;
    }
    h1, h2, h3, h4 {
        font-weight: 600;
        color: #ffffff;
    }
    .stMetric {
        background: #1b2735;
        border-radius: 12px;
        padding: 15px;
        margin: 5px;
    }
    a {
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
        color: #82aaff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title + Subtitle
st.markdown("<h1 style='text-align: center;'>🔗 Blockchain Portfolio Explorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #d3d3d3;'>Explore Ethereum wallets with real-time balances, USD value, and on-chain transactions</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Default wallet (Vitalik) for demo
default_wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
address = st.text_input("🔍 Enter Ethereum Wallet Address", value=default_wallet, help="Paste any Ethereum address (0x...) to explore")

if address:
    # Fetch data
    eth_balance = get_eth_balance(address)
    eth_price = get_eth_price()
    usd_value = eth_balance * eth_price

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("ETH Balance", f"{eth_balance:.4f} ETH")
    col2.metric("USD Value", f"${usd_value:,.2f}")
    col3.metric("ETH Price", f"${eth_price:,.2f}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Transactions
    st.subheader("📜 Recent Transactions")
    txs = get_transactions(address, limit=5)

    if txs:
        for tx in txs:
            value_eth = int(tx["value"]) / 1e18
            html = f"""
            <div style="background:#1e2a38; border-radius:12px; padding:16px; margin-bottom:12px;
                        box-shadow:0 4px 8px rgba(0,0,0,0.3); color:#f5f7fa; font-family:Inter, sans-serif; position:relative;">
                
                <!-- ETH Value Badge -->
                <div style="position:absolute; top:16px; right:16px; background:#4cafef; color:#000;
                            padding:4px 10px; border-radius:20px; font-weight:bold; font-size:13px;">
                    {value_eth:.4f} ETH
                </div>

                <!-- Hash -->
                <p style="margin:0; font-size:14px; color:#aaa;">Txn Hash</p>
                <p style="margin:0 0 12px 0; font-size:13px; word-break:break-all;">
                    <a
