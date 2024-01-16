import random
import re

def check_password_strength(password):
    # Check length
    if not (8 <= len(password) <= 24):
        print("Error: Password length should be between 8 and 24 characters.")
        return None

    # Check allowed characters
    if not re.match("^[A-Za-z0-9!$%^&*()-_=+]+$", password):
        print("Error: Password contains invalid characters.")
        return None

    score = len(password)

    # Add points for character types
    if any(c.isupper() for c in password):
        score += 5
    if any(c.islower() for c in password):
        score += 5
    if any(c.isdigit() for c in password):
        score += 5
    if any(c in "!$%^&*()-_=+" for c in password):
        score += 5

    # Add additional points for a combination of character types
    if all(any(c.isupper() for c in password_type) for password_type in ["upper", "lower", "digit", "symbol"]):
        score += 10

    # Subtract points for consecutive letters on QWERTY keyboard
    qwerty_sequences = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for sequence in qwerty_sequences:
        score -= 5 * sum(1 for _ in re.finditer(f"(?i)({sequence})", password))

    return score

def generate_password():
    while True:
        length = random.randint(8, 12)
        password = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%^&*()-_=+", k=length))
        score = check_password_strength(password)
        if score and score > 20:
            return password, score

def main():
    while True:
        print("\nMenu:")
        print("1. Check Password")
        print("2. Generate Password")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            password = input("Enter the password: ")
            score = check_password_strength(password)
            if score is not None:
                strength = "Strong" if score > 20 else "Weak"
                print(f"\nPassword Strength: {strength}\nPoint Score: {score}")

        elif choice == "2":
            generated_password, generated_score = generate_password()
            print(f"\nGenerated Password: {generated_password}\nPoint Score: {generated_score}")

        elif choice == "3":
            print("Quitting the program")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
