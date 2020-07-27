import json

class Registrants:
    
    def __init__(self, name, email, phone):
        self._info = {"name": name, "email": email, "phone": phone}
        self._registrant = {"registrant":self._info}
        self._json = json.dumps(self._registrant)
   
    def get_registrant(self):
        return json.loads(self._json)
