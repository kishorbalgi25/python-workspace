# 4.      Update Inventory:

# a.       Allow the librarian to update the number of copies available for a specific book. Prompt the user to enter the title of the book and the new quantity.

# 5.      Exit:

# a.       Provide an option to exit the program.

import os

file_name = os.path.dirname(__file__) + "/library_inventory.txt"

def addBook():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre: ")
    no_of_copies = input("Enter the no of copies: ")
    
    inventory  = open(file_name,"a")
    
    inventory.write(f"{title}, {author}, {genre}, {no_of_copies}\n")
    
    inventory.close()
    
def viewInventory():
    inventory = open(file_name,"r")
    
    items = inventory.readlines()
    
    print("The Inventory Contains: ")
    for item in items:
        title , author, genre, copies = item.split(", ")
        print(f"Title: {title}, Author: {author}, Genre: {genre}, No of copies: {copies}")
        
    inventory.close()
        
def searchBook():
    query = input("Enter the title to search: ")
    
    inventory = open(file_name,"r")
    
    items = inventory.readlines()
    
    print(f"Books with title : {query}")
    for item in items:
        title , author, genre, copies = item.split(", ")
        if title == query:
            print(f"Title: {title}, Author: {author}, Genre: {genre}, No of copies: {copies}")
        
    inventory.close()
    
def updateQuantity():
    update_title = input("Enter the title of the book to update: ")
    new_quantity = int(input("Enter the new quantity: "))

    with open(file_name, 'r') as file:
        lines = file.readlines()

    found = False
    with open(file_name, 'w') as file:
        for line in lines:
            title, author, genre, quantity = line.split(", ")
            if title.lower() == update_title.lower():
                file.write(f"{title}, {author}, {genre}, {new_quantity}\n")
                found = True
            else:
                file.write(line)
    
    if found:
        print("Inventory updated successfully.")
    else:
        print("Book not found in inventory.")
    
def main():
    print("Welcome to library management system:")
    print("1. Add a new book")
    print("2. View Inventory")
    print("3. Search by title")
    print("4. Update quantity")
    print("5. Exit")
    
    while True:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            addBook()
        elif choice == 2:
            viewInventory()
        elif choice == 3:
            searchBook()
        elif choice == 4:
            updateQuantity()
        elif choice == 5:
            print("Exiting the system")
            exit()
        else:
            print("Invalid choice!")
    
    
if __name__=="__main__":
    main()
    