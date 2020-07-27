import pytest
from Contacts import *
from Leads import *
from Registrants import *

def test_registration():
    reg = Registrants("John Doe", "john@gmail.com", None)
    print(reg.get_registrant()["registrant"])


if __name__ == '__main__':
    test_registration()