from Contacts import *
from Leads import *
from Registrants import *

class EventRegistration():

    def __init__(self):
        self.ContactsList = []
        self.LeadsList = []
        self.match_found = False

# Follows steps mentioned in task description to add all registrants to the ContactList
# First tries to match registrant's email to Contacts list
# Then tries to match registrant's phone to Contacts list
# Then tries to match email with Leads list
# Then tries to match phone with Leads list
# If registrant's information is not in neither Contacts list or Leads list, creates a new contact for the registrant

    def match_registrant(self, in_registrant):
        if not isinstance(in_registrant, Registrants):
                raise TypeError("Only Registrants can be matched and added to the Contacts")
        registrant_info = in_registrant.get_info()
        registrant_name = registrant_info["registrant"]["name"]
        registrant_email = registrant_info["registrant"]["email"]
        registrant_phone = registrant_info["registrant"]["phone"]
        for contact in self.ContactsList:
            if(registrant_email is not None and contact.get_email() == registrant_email):
                if(contact.get_phone() is None and registrant_phone is not None):
                    contact.update_phone(registrant_phone)
                self.match_found = True
                break
            elif(registrant_phone is not None and contact.get_phone() == registrant_phone):
                if(contact.get_email() is None and registrant_email is not None):
                    contact.update_email(registrant_email)
                self.match_found = True
                break
            else:
                for i in range(len(self.LeadsList)):
                    if(registrant_email is not None and self.LeadsList[i].get_email() == registrant_email):
                        if(self.LeadsList[i].get_phone() is None):     # if there was no number in the leads list, but there was a number in the registration form, adds the number in the registration form
                            self.addContact(registrant_name, registrant_email, registrant_phone)
                        else:
                            self.addContact(registrant_name, registrant_email, self.LeadsList[i].get_phone())
                        self.LeadsList.pop(i)
                        self.match_found = True
                        break
                    elif(registrant_phone is not None and self.LeadsList[i].get_phone() == registrant_phone):
                        self.addContact(registrant_name, registrant_email, registrant_phone)
                        self.LeadsList.pop(i)
                        self.match_found = True
                        break
        if not self.match_found:
            self.addContact(registrant_name, registrant_email, registrant_phone)
    
    # helper method to create new contact and add it to Contacts list
    def addContact(self, name, email, phone):
        newcontact = Contacts(name, email, phone)
        self.ContactsList.append(newcontact)


    # helper method to create new lead and add it to Leads list
    def addLead(self, name, email, phone):
        newcontact = Leads(name, email, phone)
        self.LeadsList.append(newcontact)

        


    
