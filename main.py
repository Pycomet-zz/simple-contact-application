from script import *


def add_contact():
    "Add Contact"

    contact = Contact()

    contact.set_first_name(input("Input First Name --> "))
    contact.set_last_name(input("Input Last Name --> "))
    contact.set_phone_number(input("Input Phone Number --> "))
    contact.set_email_address(input("Input Email Address --> "))

    Contact.save()

    print("New Contact Created!")


def search_contact():
    "Search Contact"

    Contact.load()
    search = Search()

    print(
        """
    Press 1 to search by first name
    Press 2 to search by last name
    Press 3 to search by phone number
    Press 4 to search by email address

        """)

    choice = int(input("--> "))

    if choice == 1:
        name = input("What is the contact's first name? ")
        result = search.by_first_name(name)
        return result

    elif choice == 2:
        name = input("What is the contact's last name? ")
        result = search.by_last_name(name)
        return result


    elif choice == 3:
        name = input("What is the contact's phone number? ")
        result = search.by_phone_number(name)
        return result

    elif choice == 4:
        name = input("What is the contact's email? ")
        result = search.by_email_address(name)
        return result

    else:
        return "Wrong Command Input! Try Again."

        
        
def update_contact():
    """
    Search And Update Contact
    """
    contact = search_contact()

    if type(contact) != str:

        print(
            f"""
        Press 1 to update first name from {contact.get_first_name()}
        Press 2 to update last name from {contact.get_last_name()}
        Press 3 to update phone number from {contact.get_phone_number()}
        Press 4 to update email address from {contact.get_email_address()}
            
            """)

        choice = int(input("--> "))

        if choice == 1:
            name = input("Input New First Name --> ")
            contact.set_first_name(name)

        elif choice == 2:
            name = input("Input New Last Name --> ")
            contact.set_last_name(name)
        
        elif choice == 3:
            number = input("Input New Phone Number --> ")
            contact.set_phone_number(number)

        elif choice == 4:
            email = input("Input New Email Address --> ")
            contact.set_email_address(email)

        else:
            return "Wrong Command Input! Try Again."

        Contact.save()

        print("Update Completed!!")

    else:

        print("No Contact Found")


def delete_contact():
    "Delete Specific User"

    contact = search_contact()

    contact.delete()

    Contact.save()

    print("Contact Deleted!")



main_menu = """
    ----------------------------------------
    Contact Manager Application Main Menu
    -----------------------------------------
    Input a number to select from these options;
    1) Add Contact
    2) Search Contact
    3) Update Contact
    4) Delete Contact

    """


while True:

    print(main_menu)

    option = int(input("-->  "))

    if option == 1:
        
        add_contact()

    elif option == 2:
        
        print(search_contact())

    elif option == 3:

        update_contact()

    elif option == 4:

        delete_contact()
        

    else:
        print("Wrong Option Command")


