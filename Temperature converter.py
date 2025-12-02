# Temperature Converter

print("===== TEMPERATURE CONVERTER =====")

while True:
    print("\nChoose an option:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Celsius to Fahrenheit
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Fahrenheit to Celsius
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")