from domain.Reservation import Reservation
from data.Reservation import ReservationRepository

class ReservationService:
    def __init__(self, db):
        self.db = db
        self.reservation_repository = ReservationRepository()

    def create_reservation(self):
        id_guest = input("Ingrese la identificación del huésped: ")
        id_room = input("Ingrese la identificación de la habitación: ")
        additional_services = input("Ingrese los servicios adicionales (SI/NO): ").upper()
        while additional_services not in ['SI', 'NO']:
            print("Entrada inválida. Por favor ingrese 'SI' o 'NO'.")
            additional_services = input("Ingrese los servicios adicionales (SI/NO): ").upper()

        required_services = input("¿Servicios requeridos? (SI/NO): ").upper()
        while required_services not in ['SI', 'NO']:
            print("Entrada inválida. Por favor ingrese 'SI' o 'NO'.")
            required_services = input("¿Servicios requeridos? (SI/NO): ").upper()

        reservation = Reservation(id_guest, id_room, additional_services, required_services)
        self.reservation_repository.insert_reservation(self.db, reservation)

    def list_reservations(self):
        reservations = self.reservation_repository.select_all_reservations(self.db)
        if reservations:
            print("Lista de reservas:")
            for reservation in reservations:
                print(f"Huésped {reservation.id_guest}, Habitación "
                      f"{reservation.id_room}, Servicios adicionales: "
                      f"{reservation.additional_services}, Servicios requeridos: "
                      f"{reservation.required_services}")
        else:
            print("No hay reservas registradas.")

    def delete_reservation(self):
        id_guest = input("Ingrese la identificación del huésped de la reserva a eliminar: ")
        id_room = input("Ingrese la identificación de la habitación de la reserva a eliminar: ")

        # Verificar si la reserva existe
        query_check_reservation = "SELECT COUNT(*) FROM Reservation WHERE idGuest = %s AND idRoom = %s"
        reservation_exists = self.db.execute_query(query_check_reservation, (id_guest, id_room))

        if not reservation_exists or reservation_exists[0][0] == 0:
            print(f"Error: No existe una reserva con Huésped {id_guest} y Habitación {id_room}.")
            return

        query_delete_reservation = "DELETE FROM Reservation WHERE idGuest = %s AND idRoom = %s"
        self.db.execute_query(query_delete_reservation, (id_guest, id_room))
        print(f"Reserva de Huésped {id_guest} en Habitación {id_room} eliminada exitosamente.")
