import json

# A class for making JSON objects with registrant information
class Registrants:
    
    def __init__(self, name, email, phone):
        self._info = {"name": name, "email": email, "phone": phone}
        self._registrant = {"registrant":self._info}
        self._json = json.dumps(self._registrant)
   
   # Returns JSON object for a registrant 
    def get_info(self):
        return json.loads(self._json)
