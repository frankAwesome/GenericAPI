class User:
    def __init__(self, id, username, firstName, lastName, email, password, phone, userStatus):
        # integer: id
        self.id = id

        # string: username
        self.username = username

        # string: firstName
        self.firstName = firstName

        # string: lastName
        self.lastName = lastName

        # string: email
        self.email = email

        # string: password
        self.password = password

        # string: phone
        self.phone = phone

        # integer: userStatus
        self.userStatus = userStatus

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus,
        }
