class Category:
    def __init__(self, id, name):
        # integer: id
        self.id = id

        # string: name
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
