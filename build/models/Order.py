class Order:
    def __init__(self, id, petId, quantity, shipDate, status, complete):
        # integer: id
        self.id = id

        # integer: petId
        self.petId = petId

        # integer: quantity
        self.quantity = quantity

        # string: shipDate
        self.shipDate = shipDate

        # string: status
        self.status = status

        # boolean: complete
        self.complete = complete

    def to_dict(self):
        return {
            "id": self.id,
            "petId": self.petId,
            "quantity": self.quantity,
            "shipDate": self.shipDate,
            "status": self.status,
            "complete": self.complete,
        }
