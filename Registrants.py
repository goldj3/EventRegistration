import json

class Registrants:
    
    def __init__(self, in_name, in_email, in_phone):
        self._name = in_name
        self._email = in_email
        self._phone = in_phone
        self._info = {"name": self._name, "email": self._email, "phone": self._phone}
        self._registrant = {"registrant":self._info}
        self._json = json.dumps(self._registrant)
   
    def get_registrant(self):
        return json.loads(self._json)
