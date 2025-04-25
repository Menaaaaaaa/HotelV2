class Guest:
    def __init__(self, id_guest, origin, occupation):
        self.id_guest = id_guest
        self.origin = origin
        self.occupation = occupation

    def __str__(self):
        return f"ID: {self.id_guest}, Origen: {self.origin}, Ocupación: {self.occupation}"

    def __repr__(self):
        return self.__str__()
