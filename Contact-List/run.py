#!//home/zoo/anaconda3/envs/projects/bin/python
from contact import Contact


def create_contact(fname, lname, phone, email):
    """
    function to create a new contact
    :param phone:
    :param fname:
    :param lname:
    :param email:
    :return: new_contact
    """
    new_contact = Contact(fname, lname, phone, email)
    return new_contact


def save_contacts(contact):
    """
    function to save contact
    :param contact:
    :return: new contact
    """
    contact.save_contact()


def del_contact(contact):
    """
    function to delete a contact
    :param contact:
    :return:
    """
    contact.delete_contact()


def find_contact(number):
    """
    function that finds a contact by number and returns the contact
    :param number:
    :return: contact
    """
    return Contact.find_by_phone(number)


def check_existing_contacts(number):
    """
    function to check if a contact exists and returns with a boolean value.
    :param number:
    :return: boolean
    """
    return Contact.contact_exist(number)


def display_contacts():
    """
    function to display all the saved contacts
    :return: all contacts
    """
    return Contact.display_all_contacts()


def copy_email(number):
    """
    Method to copy email to clipboard when user is found
    :param number:
    :return: email
    """
    return Contact.copy_email(number)


def main():
    print("Hello welcome to your contact list, What is your name?")
    user_name = str(input("Enter your name: "))

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: cc - create a new contact, dc - display contacts, "
              "fc - find a contact,cp - copy email to clipboard,  del - delete a contact, ex - exit the contact ")
        short_code = input().lower()
        if short_code == 'cc':
            print("New Contact")
            print("--" * 10)
            print("First name ....")
            f_name = input()
            print("Last name ....")
            l_name = input()
            print("Phone number ....")
            p_number = int(input())
            print("Email Address ....")
            e_address = input()
            save_contacts(create_contact(f_name, l_name, p_number, e_address))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = int(input())
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code == "cp":
            print("Enter number to search for")
            search_number = int(input())
            if find_contact(search_number):
                copy_email(search_number)
                print("Email copied in clipboard")
                print('-' * 20)
            else:
                print("Number not found")

        elif short_code == "del":
            print("Enter number of contact to delete")
            search_number = int(input())
            contact_found = find_contact(search_number)
            if contact_found:
                print("Are you sure you want delete this contact: Y or N")
                response = input().lower()
                if response == 'y':
                    del_contact(contact_found)
                    print("Contact deleted")
            else:
                print("Contact Not Found")


        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == "__main__":
    main()
