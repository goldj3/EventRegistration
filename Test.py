from Contacts import *
from Leads import *
from Registrants import *
from EventRegistration import *
import unittest

class TestEventRegistration(unittest.TestCase):


    # Tests registration form creation 
    def test_registration(self):
        reg = Registrants("John", "john@gmail.com", None)
        self.assertEqual(str(reg.get_info()["registrant"]), "{'name': 'John', 'email': 'john@gmail.com', 'phone': None}")

    # Test to add new registrant when Contacts list and Leads list are both empty
    def test_add_registrant_empty(self):
        event_reg = EventRegistration()
        new_reg = Registrants("Joe", "joe@gmail.com", None)
        event_reg.match_registrant(new_reg)
        self.assertEqual(event_reg.ContactsList[0].get_name(), "Joe")
        self.assertEqual(event_reg.ContactsList[0].get_phone(), None)
        self.assertEqual(event_reg.ContactsList[0].get_email(), "joe@gmail.com")

      # Test to make sure when a contact is matched and the phone number is updated, the updated information is added to the Contacts list
    def test_add_registrant_contact_found_update_phone(self):
        event_reg = EventRegistration()
        event_reg.addContact("Lucy Liu", "lliu@gmail.com", None)
        event_reg.addContact("John Liu", None, 2185559320)
        event_reg.addLead(None, "tim@optimum.com", 9125554323)
        new_reg = Registrants("Lucy Liu", "lliu@gmail.com", 9325556677)
        event_reg.match_registrant(new_reg)
        self.assertEqual(event_reg.ContactsList[1].get_name(), "Lucy Liu")
        self.assertEqual(event_reg.ContactsList[1].get_email(), "lliu@gmail.com")
        self.assertEqual(event_reg.ContactsList[1].get_phone(), 9325556677)


    # Test to make sure when a contact is matched and the email is updated, the updated information is added to the Contacts list
    def test_add_registrant_contact_found_update_email(self):
        event_reg = EventRegistration()
        event_reg.addContact("Lucy Liu", None, 9325556677)
        event_reg.addContact("John Liu", None, 2185559320)
        event_reg.addLead(None, "tim@optimum.com", 9125554323)
        new_reg = Registrants("Lucy Liu", "lliu@gmail.com", 9325556677)
        event_reg.match_registrant(new_reg)
        self.assertEqual(event_reg.ContactsList[1].get_name(), "Lucy Liu")
        self.assertEqual(event_reg.ContactsList[1].get_email(), "lliu@gmail.com")
        self.assertEqual(event_reg.ContactsList[1].get_phone(), 9325556677)


    # Test to make sure when a lead is matched, it is removed from the Leads list and added to the Contacts list 
    def test_add_registrant_lead_found(self):
        event_reg = EventRegistration()
        event_reg.addContact("Lucy Liu", "lliu@gmail.com", None)
        event_reg.addContact("John Liu", None, 2185559320)
        event_reg.addLead(None, "tim@optimum.com", 9125554323)
        new_reg = Registrants("Tim Smith", "tim@optimum.com", None)
        event_reg.match_registrant(new_reg)
        self.assertTrue(len(event_reg.LeadsList) == 0)
        self.assertEqual(event_reg.ContactsList[2].get_name(), "Tim Smith")
        self.assertEqual(event_reg.ContactsList[2].get_email(), "tim@optimum.com")
        self.assertEqual(event_reg.ContactsList[2].get_phone(), 9125554323)

    # Runs matching registration algorithm for multiple registrants where Contacts list and Leads list are populated
    def test_multiple_registrants(self):
        new_reg = []
        event_reg = EventRegistration()
        event_reg.addContact("Lucy Liu", "lliu@gmail.com", None)
        event_reg.addContact("John Liu", None, 2185559320)
        event_reg.addLead(None, "tim@optimum.com", 9125554323)
        event_reg.addLead("Mary Middle", "mary@middle.com", 3331112223)
        event_reg.addLead(None, "ole@olsen.com", None)
        new_reg.append(Registrants("Tim Smith", "tim@optimum.com", None))
        new_reg.append(Registrants("Lucy Liu", "lliu@gmail.com", 9325556677))
        new_reg.append(Registrants("Doug", "doug@emmy.com", 4564445556))
        new_reg.append(Registrants("Uma Thurman", "uma@thurs.com", None))
        for registrant in new_reg:
            event_reg.match_registrant(registrant)
        names = []
        emails = []
        phones = []
        for reg in event_reg.ContactsList:
            names.append(reg.get_name())
            emails.append(reg.get_email())
            phones.append(reg.get_phone())
        self.assertEqual(event_reg.ContactsList[0].get_name(), "John Liu")
        self.assertEqual(event_reg.ContactsList[0].get_email(), None)
        self.assertEqual(event_reg.ContactsList[0].get_phone(), 2185559320)
        self.assertEqual(event_reg.ContactsList[1].get_name(), "Tim Smith")
        self.assertEqual(event_reg.ContactsList[1].get_email(), "tim@optimum.com")
        self.assertEqual(event_reg.ContactsList[1].get_phone(), 9125554323)
            
if __name__ == '__main__':
    unittest.main()