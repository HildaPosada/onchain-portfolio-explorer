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
    .css-1d391kg, .css-1v3fvcr {
        background-color: #1e2a38 !important;
        border-radius: 16px !important;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stMetric {
        background: #1b2735;
        border-radius: 12px;
        padding: 15px;
        margin: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title + Subtitle
st.markdown("""
    <h1 style='text-align: center;'>🔗 Blockchain Portfolio Explorer</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style='text-align: center; color: #d3d3d3;'>
        Explore Ethereum wallets with real-time balances, USD value, and on-chain transactions
    </p>
""", unsafe_allow_html=True)
