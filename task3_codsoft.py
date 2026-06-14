contacts = {}

def add_contact():

    name = input("Enter Name : ")

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter Phone : ")
    email = input("Enter Email : ")
    address = input("Enter Address : ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact Added Successfully!")


def view_contacts():

    if not contacts:
        print("No Contacts Available!")
        return

    print("\n===== CONTACT LIST =====")

    for name, details in contacts.items():

        print("\nName    :", name)
        print("Phone   :", details["Phone"])
        print("Email   :", details["Email"])
        print("Address :", details["Address"])


def search_contact():

    name = input("Enter Name to Search : ")

    if name in contacts:

        print("\nContact Found")
        print("Phone   :", contacts[name]["Phone"])
        print("Email   :", contacts[name]["Email"])
        print("Address :", contacts[name]["Address"])

    else:
        print("Contact Not Found!")


def update_contact():

    name = input("Enter Name to Update : ")

    if name not in contacts:
        print("Contact Not Found!")
        return

    contacts[name]["Phone"] = input("New Phone : ")
    contacts[name]["Email"] = input("New Email : ")
    contacts[name]["Address"] = input("New Address : ")

    print("Contact Updated Successfully!")


def delete_contact():

    name = input("Enter Name to Delete : ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank You For Using Contact Book")
        break

    else:
        print("Invalid Choice!")