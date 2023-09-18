class Customer:
    def __init__(self, id, username, address):
        # integer: id
        self.id = id

        # string: username
        self.username = username

        # array: address
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "address": self.address,
        }
