from datetime import datetime

def get_customer_details():
    name = input("Enter customer name: ")
    postcode = input("Enter customer postcode: ")
    loyalty_card_number = input("Enter 8-digit loyalty card number: ")
    return name, postcode, loyalty_card_number

def check_expiry(expiry_date):
    today = datetime.now()
    expiry_date = datetime.strptime(expiry_date, "%m/%d/%Y")
    return today < expiry_date

def validate_loyalty_card(loyalty_card_number):
    check_digit = int(loyalty_card_number[-1])
    reversed_digits = list(map(int, loyalty_card_number[:-1][::-1]))

    multiplied_digits = [(digit * 2 - 9) if digit * 2 > 9 else digit * 2 for digit in reversed_digits[::2]]

    total = sum(multiplied_digits + reversed_digits[1::2])

    return (total + check_digit) % 10 == 0

def main():
    name, postcode, loyalty_card_number = get_customer_details()

    expiry_date = input("Enter loyalty card expiry date (MM/DD/YYYY): ")
    if not check_expiry(expiry_date):
        print("Loyalty card has expired.")
        return

    if len(loyalty_card_number) != 8 or not loyalty_card_number.isdigit():
        print("Invalid loyalty card number format.")
        return

    if validate_loyalty_card(loyalty_card_number):
        print("Loyalty card is valid.")
        print("\nCustomer Details:")
        print(f"Name: {name}")
        print(f"Postcode: {postcode}")
        print(f"Loyalty Card Number: {loyalty_card_number}")
    else:
        print("Loyalty card is not valid.")

if __name__ == "__main__":
    main()
