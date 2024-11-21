def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid option")


def get_currency(label):
    currencies = ("USD", "NGN", "EUR", "GBP")
    while True:
        currency = input(f"{label} currency (USD/NGN/EUR/GBP): ").upper()
        if currency not in currencies:
            print("Invalid currency")
        return currency


def convert(amount, source_currency, target_currency, exchange_rates):

    if source_currency == target_currency:
        return amount
    return amount * \
        exchange_rates[source_currency][target_currency]


def main():
    exchange_rates = {
        'USD': {'EUR': 0.95, 'NGN': 1750, 'GBP': 0.79},
        'EUR': {'USD': 1.05, 'NGN': 1771.80, 'GBP': 0.83},
        'NGN': {'USD': 0.00060, 'EUR': 0.00056, 'GBP': 0.00047},
        'GBP': {'NGN': 2125.43, 'USD': 1.27, 'EUR': 1.20}
    }
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")

    # Coverting to single currency
    converted_amount = convert(
        amount, source_currency, target_currency, exchange_rates)
    print(f"{amount:.2f} {source_currency} is equal to {
          converted_amount:.2f} {target_currency}")

    # converting to multiple currency
    print("\nOther currencies")
    for currency, _ in exchange_rates[source_currency].items():
        if currency != target_currency:
            converted_amount = convert(
                amount, source_currency, currency, exchange_rates)
            if converted_amount is not None:
                print(f"{amount:.2f} {source_currency} is equal to {
                    converted_amount:.2f} {currency}")


# if __name__ == "__main__":
#     main()

main()
