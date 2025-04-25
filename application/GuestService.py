from data.GuestRepository import GuestRepository

class GuestService:
    def __init__(self, db):
        self.db = db
        self.guest_repository = GuestRepository()

    def create_guest(self):
        id_guest = input("Ingrese la identificación del huésped: ")
        origin = input("Ingrese la ciudad de origen: ")
        occupation = input("Ingrese la ocupación: ")

        self.guest_repository.insert_guest(self.db, id_guest, origin, occupation)

    def list_guests(self):
        guests = self.guest_repository.select_all_guests(self.db)
        if guests:
            print("\nLista de huéspedes:")
            for guest in guests:
                print(f"ID: {guest[0]}, Origen: {guest[1]}, Ocupación: {guest[2]}")
        else:
            print("No hay huéspedes registrados.")

    def get_guest(self, id_guest):
        guest = self.guest_repository.select_guest(self.db, id_guest)
        if guest is None:
            print(f"No se encontró el huésped con ID {id_guest}.")
        return guest

    def update_guest(self, guest):
        new_origin = input("Ingrese la nueva ciudad de origen: ")
        new_occupation = input("Ingrese la nueva ocupación: ")

        self.guest_repository.update_guest(self.db, guest.id_guest, new_origin, new_occupation)

    def delete_guest(self, id_guest):
        guest = self.get_guest(id_guest)
        if guest:
            self.guest_repository.delete_guest(self.db, id_guest)
