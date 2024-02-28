class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.number}, Email: {self.email}"
    
    def to_dict(self):
        return {"name": self.name, "number": self.number, "email": self.email}


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if self.get_contact_by_name(contact.name):
            return False, f"Contact with name {contact.name} already exists"
        else:
            self.contacts.append(contact)
            return True, f"Contact {contact.name} added successfully"

    def delete_contact(self, name):
        contact = self.get_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            return True, f"Contact with name {name} deleted successfully"
        return False, f"No contact with name {name} found"

    def update_contact(self, name, ph=None, email=None):
        contact = self.get_contact_by_name(name)

        if contact:
            if ph:
                contact.number = ph
            if email:
                contact.email = email
            return True, f"Contact {name} updated successfully"
        return False, f"No contact with name {name} found"

    def get_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def get_all_contacts(self):
        return [contact.to_dict() for contact in self.contacts]
