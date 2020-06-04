class AddressBook:
    def __init__(self):  # Create the address book
        self.contacts = []

    def add(self, name, adr, phNo):  # Allows the user to add a contact
        self.contacts.append([name, adr, phNo])

    def lookup(self, name):  # Allows the user to lookup a contact
        for item in self.contacts:
            if item[0] == name:
                return item[0], item[1], item[2]
        return none
