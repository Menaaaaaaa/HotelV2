from domain.User import User


class Employee(User):

    def __init__(self, id, name, email , password , status, rol):
        super().__init__(id, name, email, password, status)
        self._rol = rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol