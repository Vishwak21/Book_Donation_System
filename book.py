import csv

def add_record():
    with open('book_donation.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter the name of the donor/receiver: ")
        email = input("Enter the email address: ")
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        writer.writerow([name, email, book_title, book_author])
    print("Record added successfully!")

def delete_record():
    email = input("Enter the email address of the donor/receiver to be deleted: ")
    with open('book_donation.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('book_donation.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[1] != email:
                writer.writerow(row)
    print("Record deleted successfully!")

def update_record():
    email = input("Enter the email address of the donor/receiver to be updated: ")
    with open('book_donation.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('book_donation.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[1] == email:
                book_title = input("Enter the new title of the book: ")
                book_author = input("Enter the new author of the book: ")
                row[2] = book_title
                row[3] = book_author
            writer.writerow(row)
    print("Record updated successfully!")

def search_book():
    search_text = input("Enter the book author or title to search: ")
    with open('book_donation.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if search_text.lower() in row[2].lower() or search_text.lower() in row[3].lower():
                print(row)

def display_all():
    with open('book_donation.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

while True:
    print("\nBOOK DONATION SYSTEM")
    print("1. Add record of donor/receiver")
    print("2. Delete record of donor/receiver")
    print("3. Record Update")
    print("4. Search a particular Book (Using Book Author/Title)")
    print("5. Displaying all record of Donor/Receiver")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        search_book()
    elif choice == 5:
        display_all()
    elif choice == 6:
        break
    else:
        print("Invalid choice, please try again!")
