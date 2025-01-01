import wallet_utils
import json

def main():
    print("Welcome to Crypto Wallet Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add a wallet address")
        print("2. View wallet balances")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            address = input("Enter wallet address: ")
            wallet_utils.save_address(address)
            print("Wallet address saved!")
        elif choice == "2":
            balances = wallet_utils.get_all_balances()
            print("\nWallet Balances:")
            for address, balance in balances.items():
                print(f"{address}: {balance} ETH")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
