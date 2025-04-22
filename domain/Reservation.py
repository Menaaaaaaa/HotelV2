class Reservation:

    def __init__(self, id_guest, id_room, additional_services, required_services):
        self._id_guest = id_guest
        self._id_room = id_room
        self._additional_services = additional_services
        self._required_services = required_services

    @property
    def id_guest(self):
        return self._id_guest

    @id_guest.setter
    def id_guest(self, id_guest):
        self._id_guest = id_guest

    @property
    def id_room(self):
        return self._id_room

    @id_room.setter
    def id_room(self, id_room):
        self._id_room = id_room

    @property
    def additional_services(self):
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        self._additional_services = additional_services

    @property
    def required_services(self):
        return self._required_services

    @required_services.setter
    def required_services(self, required_services):
        self._required_services = required_services
