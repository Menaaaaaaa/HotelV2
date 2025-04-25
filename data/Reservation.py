from data.BDConnection import Conexion
from domain.Reservation import Reservation

class ReservationRepository:
    def __init__(self):
        self.connection = Conexion(None, None, None, None, None)

    @staticmethod
    def from_row(row):
        return Reservation(row[0], row[1], row[2], row[3])  # idGuest, idRoom, additionalServices, requiredServices

    def insert_reservation(self, db, reservation):
        query = "INSERT INTO Reservation (idGuest, idRoom, additionalServices, requiredServices) VALUES (%s, %s, %s, %s)"
        values = (reservation.id_guest, reservation.id_room, reservation.additional_services, reservation.required_services)
        db.execute_query(query, values)

    def select_reservation(self, db, id_guest, id_room):
        query = "SELECT * FROM Reservation WHERE idGuest = %s AND idRoom = %s"
        result = db.execute_query(query, (id_guest, id_room))
        if result:
            return self.from_row(result[0])
        else:
            print("Reservation not found.")
            return None

    def select_all_reservations(self, db):
        query = "SELECT * FROM Reservation"
        result = db.execute_query(query)
        return [self.from_row(row) for row in result] if result else []

    def update_reservation(self, db, reservation):
        query = "UPDATE Reservation SET additionalServices = %s, requiredServices = %s WHERE idGuest = %s AND idRoom = %s"
        values = (reservation.additional_services, reservation.required_services, reservation.id_guest, reservation.id_room)
        db.execute_query(query, values)

    def delete_reservation(self, db, id_guest, id_room):
        query = "DELETE FROM Reservation WHERE idGuest = %s AND idRoom = %s"
        db.execute_query(query, (id_guest, id_room))
