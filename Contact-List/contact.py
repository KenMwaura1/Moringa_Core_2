import pyperclip


class Contact:
    """
    class that generates new instances of Contact objects
    """

    contact_list = []

    def __init__(self, first_name: str, last_name: str, phone_number: int, email: str):
        """
        __init__ method helps us define properties for our Contact object
        :param first_name: str
        :param last_name:
        :param phone_number:
        :param email:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        """
        save_contact method to save contact objects into contact list
        :return: list of contact details
        """
        Contact.contact_list.append(self)
        return Contact.contact_list

    def delete_contact(self):
        """
        deletes a saved contact from the contact list
        :return: item to be removed
        """

        Contact.contact_list.remove(self)
        return f"{self} removed from the list"

    @classmethod
    def find_by_phone(cls, number: int):
        """
        Method that takes in a number and returns a  contact that matches that number
        :param number: phone_number to search for
        :return: contact of  a person that matches the number
        """
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        """
        method to check if a contact exists in the contact list.
        :param number:
        :return:bool: True or False depending on the whether the contact exists
        """
        return any(contact.phone_number == number for contact in cls.contact_list)

    @classmethod
    def display_all_contacts(cls):
        """
        method that returns all the contacts in the list.
        :return: contact list
        """
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        """
        Method to copy email to clipboard when user is found
        :param number:
        :return: email
        """
        contact_found = Contact.find_by_phone(number)
        pyperclip.copy(contact_found.email)

