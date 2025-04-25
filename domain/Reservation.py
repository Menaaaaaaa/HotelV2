class Reservation:

    def __init__(self, id_guest, id_room, additional_services, required_services):
        self.id_guest = id_guest
        self.id_room = id_room
        self.additional_services = additional_services
        self.required_services = required_services
