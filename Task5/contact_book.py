class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print(f"Contact for '{name}' added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts found.")
            return
        
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact['name']} | Phone: {contact['phone']}")

    def search_contact(self):
        print("\n--- Search Contact ---")
        query = input("Enter Name or Phone Number to search: ").lower()
        results = [c for c in self.contacts if query in c['name'].lower() or query in c['phone']]
        
        if results:
            for c in results:
                print(f"\nFound: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
        else:
            print("No matching contact found.")

    def update_contact(self):
        self.view_contacts()
        if not self.contacts: return
        
        try:
            choice = int(input("\nEnter the number of the contact to update: ")) - 1
            if 0 <= choice < len(self.contacts):
                print("Leave blank to keep current value.")
                name = input(f"New Name [{self.contacts[choice]['name']}]: ")
                phone = input(f"New Phone [{self.contacts[choice]['phone']}]: ")
                email = input(f"New Email [{self.contacts[choice]['email']}]: ")
                address = input(f"New Address [{self.contacts[choice]['address']}]: ")

                if name: self.contacts[choice]['name'] = name
                if phone: self.contacts[choice]['phone'] = phone
                if email: self.contacts[choice]['email'] = email
                if address: self.contacts[choice]['address'] = address
                print("Contact updated!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts: return
        
        try:
            choice = int(input("\nEnter the number of the contact to delete: ")) - 1
            if 0 <= choice < len(self.contacts):
                removed = self.contacts.pop(choice)
                print(f"Contact '{removed['name']}' deleted.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    book = ContactBook()
    while True:
        print("\n======================")
        print(" CONTACT BOOK MENU ")
        print("======================")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == '1': book.add_contact()
        elif choice == '2': book.view_contacts()
        elif choice == '3': book.search_contact()
        elif choice == '4': book.update_contact()
        elif choice == '5': book.delete_contact()
        elif choice == '6': 
            print("Goodbye!")
            break
        else: 
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
