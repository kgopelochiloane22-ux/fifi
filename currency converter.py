# Currency Converter (USD <-> ZAR)

# Fixed exchange rate (example)
USD_TO_ZAR = 18.50   # 1 USD = 18.50 ZAR
ZAR_TO_USD = 1 / USD_TO_ZAR

print("===== CURRENCY CONVERTER =====")

while True:
    print("\nChoose an option:")
    print("1. Convert USD to ZAR")
    print("2. Convert ZAR to USD")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # USD → ZAR
    if choice == "1":
        try:
            usd = float(input("Enter amount in USD: "))
            zar = usd * USD_TO_ZAR
            print(f"${usd} is equal to R{zar:.2f}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # ZAR → USD
    elif choice == "2":
        try:
            zar = float(input("Enter amount in ZAR: "))
            usd = zar * ZAR_TO_USD
            print(f"R{zar} is equal to ${usd:.2f}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")