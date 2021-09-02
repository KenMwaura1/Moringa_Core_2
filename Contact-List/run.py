#!//home/zoo/anaconda3/envs/projects/bin/python
from contact import Contact


def create_contact(fname, lname, email):
    """
    function to create a new contact
    :param fname:
    :param lname:
    :param email:
    :return: new_contact
    """
    return new_contact()


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
