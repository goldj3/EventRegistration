# A class of Leads objects 

class Contacts:
    
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone
    
    def get_email(self):
        return self._email
    