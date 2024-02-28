from contact import Contact, ContactBook

def ourContactBook():
    cb = ContactBook()

    while True:
        print("\nWelcome to the Contact Book Application!")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. List Contacts")
        print("5. Search Contact")
        print("6. Exit\n\n")

        select = input("Enter your choice (1-6): ")

        if select == '1':
            name = input("Enter contact name: ")
            ph = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, ph, email)
            success, message = cb.add_contact(contact)
            print(message)
        elif select == '2':
            name = input("Enter contact name to delete: ")
            success, message = cb.delete_contact(name)
            print(message)
        elif select == '3':
            name = input("Enter contact name to update: ")
            if cb.get_contact_by_name(name):
                new_ph = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                success, message = cb.update_contact(name, new_ph, new_email)
                print(message)
            else:
                print(f"No {name} found to update")
        elif select == '4':
            contacts = cb.get_all_contacts()
            if contacts:
                for contact in contacts:
                    print(contact)
            else:
                print("Contact Book is empty")
        elif select == '5':
            name = input("Enter contact name to search: ")
            contact = cb.get_contact_by_name(name)
            if contact:
                print(contact)
            else:
                print(f"No {name} found to display")
        elif select == '6':
            print("Exiting Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

ourContactBook()
