def calculate_lucky_number(name):

    letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                     'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
                     'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8}

    #upper case convert
    name = name.upper().split()
    first_name_value = sum(letter_values[letter] for letter in name[0])
    surname_value = sum(letter_values[letter] for letter in name[1])

    # calculate
    total = first_name_value + surname_value
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    return total

def get_meaning(lucky_number):
    meanings = {
        1: "Natural leaders",
        2: "Natural peacemakers",
        3: "Creative and optimistic",
        4: "Hard workers",
        5: "Value freedom",
        6: "Carers and providers",
        7: "Thinkers",
        8: "Have diplomatic skills",
        9: "Selfless and generous"
    }
    return meanings.get(lucky_number, "Unknown meaning")

def main():
    # Input name
    name = input("Enter a person's full name (first name and surname): ")

    # Calculate lucky num
    lucky_number = calculate_lucky_number(name)

    print("\nResults:")
    print(f"Name: {name}")
    print(f"Lucky Name Number: {lucky_number}")
    print(f"Meaning: {get_meaning(lucky_number)}")

if __name__ == "__main__":
    main()
