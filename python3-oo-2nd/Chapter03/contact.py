# -*- coding: utf-8 -*-

class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value 
        int their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order, self.name))
        
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)

class EmailableContact(Contact, MailSender):
    pass
        
if __name__ == '__main__':

    c1 = Contact("John A", "johna@example.net")
    c2 = Contact("John B", "johnb@exmaple.net")
    c3 = Contact("Jenna C", "jennac@exmaple.net")
    for name in [c.name for c in Contact.all_contacts.search('John')]:
        print(name)

    e = EmailableContact("John Smith", "jsmith@example.net")
    
    for contact in Contact.all_contacts:
        print("{}:{}".format(contact.name, contact.email))
        
    e.send_mail("Hello, test e-mail here")

    