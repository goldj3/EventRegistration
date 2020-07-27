from Contacts import *
from Leads import *
from Registrants import *
from EventRegistration import *
import unittest

# A class to test the functionalities of the Event Registration class
class TestEventRegistration(unittest.TestCase):



    ### MAIN TEST USING THE DATA PROVIDED IN THE TASK DESCRIPTION

    # Runs matching registration algorithm for multiple registrants where Contacts list and Leads list are populated with the data provided in the Test Task description
    def test_multiple_registrants_using_given_data(self):
        new_reg = []
        event_reg = EventRegistration()
        
        ## Contacts 
        event_reg.addContact("Alice Brown", None, 1231112223)
        event_reg.addContact("Bob Crown", "bob@crowns.com", None)
        event_reg.addContact("Carlos Drew", "carl@drewess.com", 3453334445)
        event_reg.addContact("Doug Emerty", None, 4564445556)
        event_reg.addContact("Egan Fair", "eg@fairness.com", 5675556667)

        ## Leads
        event_reg.addLead(None, "kevin@keith.com", None)
        event_reg.addLead("Lucy Liu", "lliu@gmail.com", None)
        event_reg.addLead("Mary Middle", "mary@middle.com", 3331112223)
        event_reg.addLead(None, None, 4442223334)
        event_reg.addLead(None, "ole@olsen.com", None)

        ## Registrants
        new_reg.append(Registrants("Lucy Liu", "lliu@gmail.com", 3210001112))
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
        self.assertEqual(event_reg.ContactsList[0].get_name(), "Alice Brown")
        self.assertEqual(event_reg.ContactsList[0].get_email(), None)
        self.assertEqual(event_reg.ContactsList[0].get_phone(), 1231112223)
        self.assertEqual(event_reg.ContactsList[1].get_name(), "Bob Crown")
        self.assertEqual(event_reg.ContactsList[1].get_email(), "bob@crowns.com")
        self.assertEqual(event_reg.ContactsList[1].get_phone(), None)
        self.assertEqual(event_reg.ContactsList[2].get_name(), "Carlos Drew")
        self.assertEqual(event_reg.ContactsList[2].get_email(), "carl@drewess.com")
        self.assertEqual(event_reg.ContactsList[2].get_phone(), 3453334445)
        self.assertEqual(event_reg.ContactsList[3].get_name(), "Egan Fair")
        self.assertEqual(event_reg.ContactsList[3].get_email(), "eg@fairness.com")
        self.assertEqual(event_reg.ContactsList[3].get_phone(), 5675556667)
        self.assertEqual(event_reg.ContactsList[4].get_name(), "Lucy Liu")
        self.assertEqual(event_reg.ContactsList[4].get_email(), "lliu@gmail.com")
        self.assertEqual(event_reg.ContactsList[4].get_phone(), 3210001112)
        self.assertEqual(event_reg.ContactsList[5].get_name(), "Doug")
        self.assertEqual(event_reg.ContactsList[5].get_email(), "doug@emmy.com")
        self.assertEqual(event_reg.ContactsList[5].get_phone(), 4564445556)
        self.assertEqual(event_reg.ContactsList[6].get_name(), "Uma Thurman")
        self.assertEqual(event_reg.ContactsList[6].get_email(), "uma@thurs.com")
        self.assertEqual(event_reg.ContactsList[6].get_phone(), None)


    ### ADDITIONAL TESTS
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

  
            
if __name__ == '__main__':
    unittest.main()