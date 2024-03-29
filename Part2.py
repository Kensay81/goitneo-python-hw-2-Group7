from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if self.validate_number(phone):
            super().__init__(phone)
        else:
            raise ValueError("Invalid phone number format")

    def validate_number(self, phone):
        patterns = ["(", "-", ")", "+", " "]
        clear_phone = phone.strip()
        for pattern in patterns:
            clear_phone = clear_phone.replace(pattern, "")
        return len(clear_phone) == 10 and clear_phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record objects can be added to AddressBook")
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            raise Exception(f"{name} is not in the Address book")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise Exception(f"{name} is not in the Address book")

