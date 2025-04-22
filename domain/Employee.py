from domain.User import User


class Employee(User):

    def __init__(self, id, name, last_name , email , password , status, rol):
        super.__init__(id, name , email , password , status)
        self.rol = rol

    @property
    def rol(self):
        return self.rol

    @rol.setter
    def rol(self, rol):
        self.rol = rol