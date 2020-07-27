from Contacts import *
from Leads import *
from Registrants import *

ContactsList = []
LeadsList = []
match_found = False

# Follows steps mentioned in task description to add all registrants to the ContactList
# First tries to match registrant's email to Contacts list
# Then tries to match registrant's phone to Contacts list
# Then tries to match email with Leads list
# Then tries to match phone with Leads list
# If registrant's information is not in neither Contacts list or Leads list, creates a new contact for the registrant

def match_registrant(in_registrant):
    if not isinstance(in_registrant, Registrants):
            raise TypeError("Only Registrants can be matched and added to the Contacts")
    registrant_info = in_registrant.get_info()
    registrant_name = registrant_info["registrant"]["name"]
    registrant_email = registrant_info["registrant"]["email"]
    registrant_phone = registrant_info["registrant"]["phone"]
    for contact in ContactsList:
        if(contact.get_email() == registrant_email):
            if(contact.get_phone() is None and registrant_phone is not None):
                contact.update_phone(registrant_phone)
            match_found = True
            break
        elif(contact.get_phone() == registrant_phone):
            if(contact.get_email() is None and registrant_email is not None):
                contact.update_email(registrant_email)
            match_found = True
            break
        else:
            for i in range(len(LeadsList)):
                if(LeadsList[i].get_email() == registrant_email):
                    addContact(registrant_name, registrant_email, registrant_phone)
                    LeadsList.remove(i)
                    match_found = True
                    break
                elif(LeadsList[i].get_phone() == registrant_phone):
                    addContact(registrant_name, registrant_email, registrant_phone)
                    LeadsList.remove(i)
                    match_found = True
                    break
        if not match_found:
            addContact(registrant_name, registrant_email, registrant_phone)
   

# helper method to create new contact and add it to Contacts list
def addContact(name, email, phone):
    newcontact = Contacts(name, email, phone)
    ContactsList.append(newcontact)

if __name__ == '__main__':
    ContactsList.append(Contacts("Joe", None, 932222222))
    x = Registrants("Joe", "joe@gmail.com", 932222222)
    match_registrant(x)
    print(ContactsList[0].get_email())
        


    
