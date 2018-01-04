"""
A program designed to implement a simple contact list that maps names to phone numbers.
"""

contacts = {'Zephyr Kwon': '1-101-555-1234',
            'Joe Black': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}

def lookup(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    if name in contacts:
        return contacts[name]
    else:
        return ""


print(lookup(contacts, "Bryant "))

def lookup2(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    if name in contacts:
        return contacts[name]
    else:
        return contacts.get(name, "")


print(lookup2(contacts, "Joe Black"))


def print_contacts(contacts):
    """
    Print the names of the contacts in our contacts list.
    """
    for name in contacts:
        print(name)


def print_contact_list(contacts):
    """
    Print the names and phone numbers of the contacts in
    our contacts list.
    """
    for name, number in contacts.items():
        print(name, ":", number)

def print_ordered(contacts):
    """
    Print the names and phone numbers of the contacts
    in our contacts list in alphabetical order.
    """
    keys = contacts.keys()
    names = sorted(keys)
    for name in names:
        print(name, ":", contacts[name])


def add_contact(contacts, name, number):
    """
    Add a new contact (name, number) to the contacts list.
    """
    if name in contacts:
        print(name, "is already in contacts list!")

    else:
        print("\nAdding New Contact...")
        contacts[name] = number
        return print_ordered(contacts)


def update_contact(contacts, name, newnumber):
    """
    Update an existing contact's number in the contacts list.
    """
    if name in contacts:
        contacts[name] = newnumber
        return print_ordered(contacts)
    else:
        print(name, "is not in contacts list!")

# def add_or_update_contact(contacts, name, number):
#     """
#     Add contact or update it if it is already in the contacts list.
#     """
#     contacts[name] = number

print_ordered(contacts)
update_contact(contacts, "Joe Blow", "1-800-Kick-Ass")
update_contact(contacts, "Zephyr Kwon", "1-800-KICK-ASS")
add_contact(contacts, "The Terminator", "1-800-IBE-BACK")

