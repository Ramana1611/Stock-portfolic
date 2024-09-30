import yfinance as yf

# Stock Portfolio class
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stock data
    
    # Add stock to portfolio
    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.portfolio:
            print(f"{symbol} is already in your portfolio.")
        else:
            self.portfolio[symbol] = {
                'quantity': quantity,
                'purchase_price': purchase_price
            }
            print(f"Added {symbol} to your portfolio.")
    
    # Remove stock from portfolio
    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")
    
    # Fetch real-time stock price using yfinance
    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        stock_data = stock.history(period='1d')
        if not stock_data.empty:
            return stock_data['Close'][0]
        else:
            print(f"Error fetching data for {symbol}.")
            return None
    
    # Display portfolio performance
    def display_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        
        print("\nYour Portfolio:")
        for symbol, data in self.portfolio.items():
            quantity = data['quantity']
            purchase_price = data['purchase_price']
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                total_value = current_price * quantity
                profit_loss = (current_price - purchase_price) * quantity
                print(f"Stock: {symbol} | Quantity: {quantity} | Purchase Price: ${purchase_price:.2f} | Current Price: ${current_price:.2f} | Total Value: ${total_value:.2f} | P/L: ${profit_loss:.2f}")
    
    # Calculate total portfolio value
    def calculate_total_value(self):
        total_value = 0
        for symbol, data in self.portfolio.items():
            quantity = data['quantity']
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                total_value += current_price * quantity
        return total_value

# Main program
def main():
    portfolio = StockPortfolio()

    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Calculate total portfolio value")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            portfolio.add_stock(symbol, quantity, purchase_price)
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
        
        elif choice == '3':
            portfolio.display_portfolio()
        
        elif choice == '4':
            total_value = portfolio.calculate_total_value()
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
