contacts = []

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for i, c in enumerate(contacts, start=1):
                print(f"{i}. {c['name']} - {c['phone']}")

    elif choice == "3":
        search = input("Enter name or phone to search: ")
        found = False
        for c in contacts:
            if search == c["name"] or search == c["phone"]:
                print("\nContact Found:")
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                print("Address:", c["address"])
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        phone = input("Enter phone number of contact to update: ")
        for c in contacts:
            if c["phone"] == phone:
                c["name"] = input("Enter new name: ")
                c["email"] = input("Enter new email: ")
                c["address"] = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        phone = input("Enter phone number of contact to delete: ")
        for c in contacts:
            if c["phone"] == phone:
                contacts.remove(c)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")