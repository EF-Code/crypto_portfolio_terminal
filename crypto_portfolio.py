import requests
import json

def get_crypto_price(crypto_symbol, currency='usd'):
    """Fetches the current price of a cryptocurrency."""
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(crypto_symbol, {}).get(currency, None)
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def display_portfolio(portfolio):
    """Displays the portfolio with current prices."""
    total_value = 0
    print("\n--- Your Crypto Portfolio ---")
    print(f"{'Crypto':<10} {'Amount':<10} {'Price':<10} {'Value':<10}")
    print("-" * 40)
    for crypto, amount in portfolio.items():
        price = get_crypto_price(crypto)
        if price is not None:
            value = price * amount
            total_value += value
            print(f"{crypto:<10} {amount:<10.2f} {price:<10.2f} {value:<10.2f}")
        else:
            print(f"{crypto:<10} {amount:<10.2f} {'Error':<10} {'Error':<10}")
    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def add_to_portfolio(portfolio):
    """Adds a cryptocurrency to the portfolio."""
    crypto = input("Enter the cryptocurrency symbol (e.g., bitcoin): ").strip().lower()
    amount = float(input("Enter the amount you own: "))
    portfolio[crypto] = portfolio.get(crypto, 0) + amount
    print(f"{crypto} added to your portfolio!\n")

def main():
    """Main function to run the portfolio tracker."""
    portfolio = {}
    while True:
        print("\nCrypto Portfolio Tracker")
        print("1. Display Portfolio")
        print("2. Add to Portfolio")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_portfolio(portfolio)
        elif choice == '2':
            add_to_portfolio(portfolio)
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
