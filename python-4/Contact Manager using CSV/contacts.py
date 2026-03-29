import csv
FILE_NAME = "contacts.csv"
def initialize_file():
    try:
        with open(FILE_NAME, 'r'):
            pass
    except FileNotFoundError:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone"])
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
    print("Contact saved successfully!\n")
def view_contacts():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        print("\n--- Contact List ---")
        for row in reader:
            print(f"Name: {row[0]} | Phone: {row[1]}")
    print()
def search_contact():
    name = input("Enter name to search: ")
    found = False
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if row[0].lower() == name.lower():
                print(f"Contact Found → Name: {row[0]}, Phone: {row[1]}")
                found = True
                break
    if not found:
        print("Contact not found!\n")
def menu():
    initialize_file()
    while True:
        print("===== CONTACT MANAGER =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")
menu()
