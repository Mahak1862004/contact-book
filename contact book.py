contacts = {}  # Initialize an empty dictionary to store contacts

def add_contact(name, phone_number, email, address):
    """Add a new contact to the contact book."""
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def delete_contact(name):
    """Delete a contact from the contact book."""
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(name, field, new_value):
    """Update a field of an existing contact."""
    if name in contacts:
        if field in contacts[name]:
            contacts[name][field] = new_value
            print(f"{field.capitalize()} updated for contact '{name}'.")
        else:
            print(f"Field '{field}' not found for contact '{name}'.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact(name):
    """Search for a contact in the contact book."""
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name]['phone_number']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    """Display all contacts in the contact book."""
    if contacts:
        print("Contacts:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("-------------------")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            field = input("Enter field to update (phone_number, email, address): ")
            new_value = input(f"Enter new {field}: ")
            update_contact(name, field, new_value)
        elif choice == '4':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
