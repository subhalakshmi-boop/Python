import csv
FILE_NAME = "students.csv"
def initialize_file():
    try:
        with open(FILE_NAME, 'r'):
            pass
    except FileNotFoundError:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "OOPS", "Web", "Python"])
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    oops = int(input("Enter OOPS Marks: "))
    web = int(input("Enter Web Marks: "))
    python = int(input("Enter Python Marks: "))
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, oops, web, python])
    print("Student Added Successfully!\n")
def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()
def search_student():
    sid = input("Enter Student ID to search: ")
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                found = True
                break
    if not found:
        print("Student Not Found\n")
def generate_report():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sid, name, oops, web, python = row
            oops, web, python = int(oops), int(web), int(python)
            avg = (oops + web + python) / 3
            if avg >= 90:
                grade = "A"
            elif avg >= 75:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "Fail"
            print(f"ID: {sid}, Name: {name}, OOPS: {oops}, Web: {web}, Python: {python}, Avg: {avg:.2f}, Grade: {grade}")
    print()
def menu():
    initialize_file()
    while True:
        print("====== Student Report Generator ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Exiting... ")
            break
        else:
            print("Invalid Choice!\n")
menu()
