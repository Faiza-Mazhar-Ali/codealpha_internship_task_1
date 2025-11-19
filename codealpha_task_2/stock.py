import csv
import os

# Simplified Scope 1: Hardcoded dictionary to define stock prices
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.20,
    "AMZN": 95.80,
    "MSFT": 310.00
}

def get_portfolio_data():
    """
    Prompts the user to input stock names and quantities for their portfolio.
    Returns a dictionary mapping stock ticker to quantity.
    """
    portfolio = {}
    print("--- Enter Your Stock Holdings ---")
    print("Available stocks and prices:")
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker}: ${price:,.2f}")
    print("---------------------------------")
    
    while True:
        # Get stock ticker from user
        ticker = input("Enter a stock ticker (e.g., AAPL) or type 'done' to finish: ").upper().strip()
        
        if ticker == 'DONE':
            break
        
        # Validate ticker against hardcoded prices
        if ticker not in STOCK_PRICES:
            print(f"Error: '{ticker}' is not a valid stock ticker in our list. Please try again.")
            continue
            
        # Get quantity from user
        while True:
            try:
                # Key Concept: input/output
                quantity_input = input(f"Enter the quantity of {ticker} you hold: ").strip()
                if not quantity_input:
                     raise ValueError("Quantity cannot be empty.")
                quantity = int(quantity_input)
                
                if quantity <= 0:
                    print("Quantity must be a positive whole number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number for the quantity.")
        
        # Store the valid data
        portfolio[ticker] = quantity
        print(f"Added {quantity} shares of {ticker}.")

    return portfolio

def calculate_portfolio_value(portfolio):
    """
    Calculates the total market value and investment per stock.
    Returns the total portfolio value and a list of detailed results.
    """
    total_value = 0.0
    detailed_results = []
    
    for ticker, quantity in portfolio.items():
        # Key Concept: dictionary (using the hardcoded prices)
        price = STOCK_PRICES.get(ticker)
        
        # Key Concept: basic arithmetic
        stock_value = price * quantity
        total_value += stock_value
        
        detailed_results.append({
            "Stock": ticker,
            "Quantity": quantity,
            "Price": price,
            "Value": stock_value
        })
        
    return total_value, detailed_results

def save_to_file(detailed_results, total_value):
    """
    (Optional) Saves the portfolio details and total value to a CSV file.
    Key Concept: file handling
    """
    file_name = "portfolio_summary.csv"
    
    try:
        # 'w' means write mode, which overwrites the file if it exists
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['Stock', 'Quantity', 'Price', 'Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(detailed_results)

            # Add the total value at the end
            writer.writerow({'Stock': 'TOTAL', 'Quantity': '', 'Price': '', 'Value': total_value})
            
        print(f"\n✅ Success: Portfolio summary saved to **{os.path.abspath(file_name)}**")
    except IOError:
        print(f"\n❌ Error: Could not write to the file {file_name}. Check permissions.")


def run_tracker():
    """Main function to run the Stock Portfolio Tracker."""
    
    portfolio_data = get_portfolio_data()

    if not portfolio_data:
        print("\nPortfolio is empty. Exiting tracker.")
        return

    # Calculate values
    total_value, detailed_results = calculate_portfolio_value(portfolio_data)

    # Display results
    print("\n" + "="*45)
    print("📈 PORTFOLIO SUMMARY")
    print("="*45)
    
    # Print the detailed breakdown
    print(f"{'Stock':<8} | {'Qty':<8} | {'Price':<10} | {'Total Value':<10}")
    print("-" * 45)
    for item in detailed_results:
        print(f"{item['Stock']:<8} | {item['Quantity']:<8} | ${item['Price']:<9.2f} | ${item['Value']:<10,.2f}")
    
    print("-" * 45)
    # Display total investment value
    print(f"**Total Investment Value:** ${total_value:,.2f}")
    print("="*45)

    # Ask the user if they want to save the results
    save_option = input("Do you want to save the results to a file? (yes/no): ").lower().strip()
    if save_option == 'yes':
        save_to_file(detailed_results, total_value)


if __name__ == "__main__":
    run_tracker()