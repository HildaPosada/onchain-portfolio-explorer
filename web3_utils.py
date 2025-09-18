import requests
import os

# Load your free Etherscan API key (sign up free at etherscan.io)
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "YourApiKeyToken")
COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"

def get_eth_balance(address):
    """Fetch ETH balance from Etherscan API"""
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    resp = requests.get(url).json()
    if resp["status"] == "1":
        wei_balance = int(resp["result"])
        eth_balance = wei_balance / 1e18
        return eth_balance
    return 0

def get_transactions(address, limit=5):
    """Fetch last N transactions from Etherscan API"""
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset={limit}&sort=desc&apikey={ETHERSCAN_API_KEY}"
    resp = requests.get(url).json()
    if resp["status"] == "1":
        return resp["result"]
    return []

def get_eth_price():
    """Fetch ETH price in USD from CoinGecko"""
    url = f"{COINGECKO_API}?ids=ethereum&vs_currencies=usd"
    resp = requests.get(url).json()
    return resp["ethereum"]["usd"]
