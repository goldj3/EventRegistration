class Leads:

    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    def update_email(self, email):
        self._email = email

    def update_phone(self, phone):
        self._phone = phone
    
    def match_email(self, email):
        return self._email == email

    def match_phone(self, phone):
        return self._phone == phone 