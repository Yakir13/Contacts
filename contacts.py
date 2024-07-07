class Contact:
    def __init__(self, first_name, last_name, phone_number) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def show_contact(self):
        return f"Full name: {self.first_name} {self.last_name}, Phone number: {self.phone_number}"

    def show_fullname(self):
        return f"Hello, my full name is: {self.first_name} {self.last_name}"

    def show_phonenumber(self):
        return f"Hello, my phone number is: {self.phone_number}"
        
        
contact_1 = Contact(first_name="qwerty", last_name="asdf", phone_number="123")
contact_2 = Contact(first_name="uiop", last_name="ghjkl", phone_number="456")


print(Contact.show_contact(contact_1))
print(Contact.show_contact(contact_2))

# print(Contact.show_fullname(contact_1))
# print(Contact.show_fullname(contact_2))

# print(Contact.show_phonenumber(contact_1))
# print(Contact.show_phonenumber(contact_2))
