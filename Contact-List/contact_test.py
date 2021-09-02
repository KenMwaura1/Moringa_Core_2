import unittest
import pyperclip
from contact import Contact


class MyTestContact(unittest.TestCase):
    """
    Test class that defines test cases for the contact class.
    Args: unittest.TestCase: TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """
        Set up method to run before each test case
        :return: new_contact
        """
        self.new_contact = Contact("zoo", "vier", 254719702373, "kemwaura@gmail.com")

    def tearDown(self):
        """
        tear method to clean up after each test case has run
        :return: empty contact_list
        """
        Contact.contact_list = []

    def test_init(self):
        """
        test case whether Contact object is initialized properly.
        :return: bool
        """
        self.assertEqual(self.new_contact.first_name, "zoo")
        self.assertEqual(self.new_contact.last_name, "vier")
        self.assertEqual(self.new_contact.phone_number, 254719702373)
        self.assertEqual(self.new_contact.email, "kemwaura@gmail.com")

    def test_save_contact(self):
        """
        test_save_contact to test whether contact object is saved into the contact list
        :return: bool
        """
        self.new_contact.save_contact()  # saving the new contact
        self.assertEqual(len(Contact.contact_list), 1)

    def test_save_multiple_contacts(self):
        """
        check if we save multiple contact objects in our contact list.
        :return: bool
        """
        self.new_contact.save_contact()  # saving the new contact
        test_contact = Contact("Test", "User", 254712345678, "test@user.com")  # new user
        test_contact.save_contact()  # saving the new contact
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        """
        Test whether we can remove a contact from the contact_list
        :return: True if we can remove the contact
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", 254712345678, "test@user.com")  # new contact
        test_contact.save_contact()
        self.new_contact.delete_contact()  # delete a contact object
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact(self):
        """
        check whether we can find contact by phone number and display information
        :return: True if we can find contact
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", 254711223344, "test@user.com")
        test_contact.save_contact()
        found_contact = Contact.find_by_phone(254711223344)

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        """
        test to check if contact exists return True if found
        :return: True if contact exists
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", 254711223344, "test@user.com")
        test_contact.save_contact()
        contact_exists = Contact.contact_exist(254711223344)
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        """
        method that returns all contacts in the list
        :return: list of contacts
        """
        self.assertEqual(Contact.display_all_contacts(), Contact.contact_list)

    def test_copy_email(self):
        """
        Test to confirm we copy the email address of the email address of the contact found
        :return: True
        """
        self.new_contact.save_contact()
        Contact.copy_email(254719702373)

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
