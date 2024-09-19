def currency_converter(amount, from_currency, to_currency):
    # Hardcoded exchange rates (as an example)
    exchange_rates = {
        'USD': {'EUR': 0.85, 'JPY': 110.0},
        'EUR': {'USD': 1.18, 'JPY': 129.53},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077},
    }

    # Check if the conversion is possible
    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return None

    # Convert the amount
    converted_amount = amount * exchange_rates[from_currency][to_currency]
    return converted_amount

# Example usage
try:
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("Enter the currency you are converting from (USD, EUR, JPY): ").upper()
    to_currency = input("Enter the currency you want to convert to (USD, EUR, JPY): ").upper()
    
    converted_amount = currency_converter(amount, from_currency, to_currency)
    
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Conversion not possible. Please check the currencies.")

except ValueError:
    print("Invalid input. Please enter a numeric value for the amount.")
