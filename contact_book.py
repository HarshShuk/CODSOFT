# ==========================
# Contact Book Application
# ==========================

contacts = []


# --------------------------
# Add Contact
# --------------------------
def add_contact():
    print("\n----- Add Contact -----")

    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    # Check duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("\nContact with this phone number already exists!")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("\nContact Added Successfully!")


# --------------------------
# View Contacts
# --------------------------
def view_contacts():

    print("\n----- Contact List -----")

    if not contacts:
        print("No contacts available.")
        return

    print(f"\n{'Name':20}{'Phone'}")
    print("-" * 35)

    for contact in contacts:
        print(f"{contact['name']:20}{contact['phone']}")


# --------------------------
# Search Contact
# --------------------------
def search_contact():

    print("\n----- Search Contact -----")

    search = input("Enter Name or Phone Number: ").strip().lower()

    found = False

    for contact in contacts:

        if (contact["name"].lower() == search or
                contact["phone"] == search):

            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True
            break

    if not found:
        print("\nContact Not Found!")


# --------------------------
# Update Contact
# --------------------------
def update_contact():

    print("\n----- Update Contact -----")

    search = input("Enter Contact Name: ").strip().lower()

    for contact in contacts:

        if contact["name"].lower() == search:

            print("\nLeave blank to keep old value.\n")

            new_name = input(f"Name ({contact['name']}): ")
            new_phone = input(f"Phone ({contact['phone']}): ")
            new_email = input(f"Email ({contact['email']}): ")
            new_address = input(f"Address ({contact['address']}): ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("\nContact Updated Successfully!")
            return

    print("\nContact Not Found!")


# --------------------------
# Delete Contact
# --------------------------
def delete_contact():

    print("\n----- Delete Contact -----")

    search = input("Enter Contact Name: ").strip().lower()

    for contact in contacts:

        if contact["name"].lower() == search:

            contacts.remove(contact)

            print("\nContact Deleted Successfully!")
            return

    print("\nContact Not Found!")


# --------------------------
# Main Program
# --------------------------

while True:

    print("\n")
    print("=" * 40)
    print("        CONTACT BOOK")
    print("=" * 40)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter Your Choice (1-6): ")

    match choice:

        case "1":
            add_contact()

        case "2":
            view_contacts()

        case "3":
            search_contact()

        case "4":
            update_contact()

        case "5":
            delete_contact()

        case "6":
            print("\nThank You for using Contact Book!")
            break

        case _:
            print("\nInvalid Choice! Please enter a number between 1 and 6.")