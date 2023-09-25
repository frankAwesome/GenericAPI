class Address:
    def __init__(self, street, city, state, zip):
        # string: street
        self.street = street

        # string: city
        self.city = city

        # string: state
        self.state = state

        # string: zip
        self.zip = zip

    def to_dict(self):
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
        }
