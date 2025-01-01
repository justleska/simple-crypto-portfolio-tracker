# Simple Crypto Wallet Tracker  

**DISCLAMER:** This is mainly an educational project to train me in the coding space & maybe help others, so this is not intended for a real use. TL;DR: things might break :P 

---

## Features  
- Add and manage multiple cryptocurrency wallet addresses.  
- Track wallet balances on the Ethereum network.  
- Simple and intuitive CLI.  

## Prerequisites  
- Python 3.8 or higher  
- [Etherscan API key](https://etherscan.io/apis) (for fetching wallet balances)  

## Project Structure  

```plaintext
crypto-wallet-tracker/  
├── main.py               # CLI interface and main program logic  
├── wallet_utils.py       # Utilities for managing wallets and fetching data  
└── README.md             # Project documentation  
```  

## Setup Instructions  

### Clone the Repository  
```bash  
git clone https://github.com/yourusername/simple-crypto-portfolio-tracker.git  
cd crypto-wallet-tracker  
```  

### Install Dependencies  
```bash  
pip install requests  
```  

### Add Your API Key  
1. Open `wallet_utils.py`.  
2. Replace `your_etherscan_api_key` with your actual API key:  
   ```python  
   ETHERSCAN_API_KEY = "your_etherscan_api_key"  
   ```  

## How to Use  

1. **Run the Program**  
   ```bash  
   python main.py  
   ```  

2. **Options in the CLI**  
   - Add a new wallet address.  
   - View wallet balances for all saved addresses.  

## Contributing  
Feel free to submit issues and pull requests to help improve this project!  

## License  
MIT License - feel free to use this project for your own purposes.  
