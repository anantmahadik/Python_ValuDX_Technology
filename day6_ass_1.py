numbers = []
while True:
    ui = input("enter val : ")

    if ui.lower() == 'end':
        break

    try:
        number = float(ui)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'end' to finish.")

if numbers:
    ttl = sum(numbers)
    avg = ttl / len(numbers)
    print(f"Total: {ttl}, Average: {avg}")
else:
    print("No numbers entered.")
