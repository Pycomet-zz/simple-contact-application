## This is a personal contact manager applicatio that stores
## and manipulates your contacts

import pickle

class Contact:

    contacts = []
            
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__phone_number = ""
        self.__email_address = ""
        self.contacts.append(self)

    def __str__(self):
        return f"{self.__first_name}-{self.__last_name}"

    # Setters
    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_phone_number(self, number):
        self.__phone_number = number

    def set_email_address(self, email):
        self.__email_address = email


    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_phone_number(self):
        return self.__phone_number

    def get_email_address(self):
        return self.__email_address

    def delete(self):
        self.contacts.remove(self)
        return "Contact Deleted!"

    @classmethod
    def save(cls):
        """
        Save contacts to text file
        """
        with open("contacts.txt", "wb") as file:

            pickle.dump(cls.contacts, file)

            file.close()

    @classmethod
    def load(cls):
        """
        Write contact objects into list for manipulation
        """
        cls.contacts = []

        with open("contacts.txt", "rb") as file:

            cls.contacts = pickle.load(file)

            file.close()

            return "Done"


class Search:

    def by_first_name(self, name):
        """
        Method to search contacts by first name
        """
        contacts = Contact.contacts
        for each in contacts:
            first_name = each.get_first_name()

            if name == first_name:	
                return each

        return "No Contact Found!"


    def by_last_name(self, name):
        """
        Method to search contacts by first name
        """
        contacts = Contact.contacts
        for each in contacts:
            last_name = each.get_last_name()

            if name == last_name:
                return each

        return "No Contact Found!"


    def by_phone_number(self, number):
        """
        Method to search contacts by phone number
        """
        contacts = Contact.contacts
        for each in contacts:
            phone_number = each.get_phone_number()

            if number == phone_number:
                return each

        return "No Contact Found"



    def by_email(self, email):
        """
        Method to search contact by email address
        """
        contacts = Contact.contacts
        for each in contacts:
            email_address = each.get_email_address()

            if email == email_address:
                return each

        return "No Contact Found"

    