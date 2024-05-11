def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts,  name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} isn't found."


def show_phone(contacts,  name):
    if name in contacts:
        print(f"{name} phone is {contacts[name]}")
    else:
        print(f"Contact {name} isn't found.")


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")