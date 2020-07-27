from Contacts import *
from Leads import *
from Registrants import *

ContactsList = []
LeadsList = []

# Follows steps mentioned in task description to add all registrants to the ContactList
# First tries to match registrant's email to Contacts list
# Then tries to match registrant's phone to Contacts list
# Then tries to match email with Leads list
# Then tries to match phone with Leads list
# If registrant's information is not in neither Contacts list or Leads list, creates a new contact for the registrant

def match_registrant(in_registrant):
    reg_info = in_registrant.get_info()
    newcontact = Contacts(reg_info["registrant"]["name"],reg_info["registrant"]["email"],reg_info["registrant"]["phone"])
    ContactsList.append(newcontact)


if __name__ == '__main__':
    x = Registrants("Joe", "joe@gmail.com", 932222222)
    match_registrant(x)
    print(ContactsList)
        


    
