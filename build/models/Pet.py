class Pet:
    def __init__(self, id, name, category, photoUrls, tags, status):
        # integer: id
        self.id = id

        # string: name
        self.name = name

        # str: category
        self.category = category

        # array: photoUrls
        self.photoUrls = photoUrls

        # array: tags
        self.tags = tags

        # string: status
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "photoUrls": self.photoUrls,
            "tags": self.tags,
            "status": self.status,
        }
