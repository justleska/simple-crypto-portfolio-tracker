import requests
import os

ETHERSCAN_API_KEY = "your_etherscan_api_key"
WALLETS_FILE = "wallets.json"

def save_address(address):
    if os.path.exists(WALLETS_FILE):
        with open(WALLETS_FILE, "r") as file:
            wallets = json.load(file)
    else:
        wallets = []

    wallets.append(address)
    with open(WALLETS_FILE, "w") as file:
        json.dump(wallets, file)

def get_all_balances():
    if not os.path.exists(WALLETS_FILE):
        return {}

    with open(WALLETS_FILE, "r") as file:
        wallets = json.load(file)

    balances = {}
    for address in wallets:
        balance = get_eth_balance(address)
        balances[address] = balance
    return balances

def get_eth_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    balance = int(response["result"]) / 10**18  # Convert from Wei to Ether
    return balance
