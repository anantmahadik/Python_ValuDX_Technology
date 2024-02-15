#Ass 3

teledict = {'acount':1001,'hr':1002,'it':1003,'venders':1005}

def display_menu():
    print("A. Look up telephone number")
    print("B. Add new telephone number")
    print("C. Edit telephone number")
    print("D. Delete telephone number")
    print("E . Print phone directry in sequence")
    print("F. Exit")

def look_up_number():
    name = input("Enter the name to look up: ")
    if name in teledict:
        print(f"telephone number for {name}: {teledict[name]}")
    else:
        print(f"{name} not found.")

def add_number():
    name = input("Enter the name: ")
    number = input("Enter the telephone number: ")
    teledict[name] = number
    print(f"Telephone number for {name} added successfully.")

def edit_number():
    name = input("Enter the name: ")
    number = input("Enter the telephone number: ")
    teledict[name] = number
    print(f"Telephone number for {name} update successfully.")

def delete_entry():
    name = input("Enter the name : ")
    teledict.pop(name)

def print_sequence():
    print(sorted(teledict))

while True:
    display_menu()
    choice = input("Enter your choice (A-F): ")

    if choice == 'A':
        look_up_number()
    elif choice == 'B':
        add_number()
    elif choice == 'C':
        edit_number()
    elif choice == 'D':
        delete_entry()
    elif choice == 'E':
        print_sequence()
    elif choice == 'F':
        print("Exiting the program.")
        break
    else:
        print("Invalid")


