stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

print("=== Stock Portfolio Tracker ===")

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity

    print("\n----- Portfolio Summary -----")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Price per Share:", stocks[stock_name])
    print("Total Investment Value =", total)
else:
    print("Stock not found")