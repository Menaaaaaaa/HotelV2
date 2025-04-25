from domain.Guest import Guest

class GuestRepository:
    def __init__(self):
        pass  # Ya no necesitas nueva conexión aquí

    @staticmethod
    def from_row(row):
        return Guest(row[0], row[1], row[2]) if row else None

    def insert_guest(self, db, id_guest, origin, occupation):
        if not id_guest or not origin or not occupation:
            print("Error: Datos incompletos para la inserción.")
            return False
        try:
            query_check_user = "SELECT COUNT(*) FROM appuser WHERE idUser = %s"
            user_exists = db.execute_query(query_check_user, (id_guest,))
            if user_exists and user_exists[0][0] == 0:
                print(f"Creando usuario en appuser con ID {id_guest}.")
                #query_insert_user = "INSERT INTO appuser (idUser, name, email, password, status) VALUES (%s, %s, %s, %s, %s, %s)"
                #db.execute_query(query_insert_user, (id_guest, 'Nombre', 'correo@example.com', 'pass123', 'active'))

            query_insert_guest = "INSERT INTO guest (idGuest, origin, occupation) VALUES (%s, %s, %s)"
            db.execute_query(query_insert_guest, (id_guest, origin, occupation))
            print(f"Huésped {id_guest} insertado correctamente.")
            return True
        except Exception as e:
            print(f"Error al insertar huésped: {e}")
            return False

    def select_guest(self, db, id_guest):
        try:
            query = "SELECT idGuest, origin, occupation FROM guest WHERE idGuest = %s"
            result = db.execute_query(query, (id_guest,))
            if result:
                return self.from_row(result[0])
            return None
        except Exception as e:
            print(f"Error al buscar huésped: {e}")
            return None

    def select_all_guests(self, db):
        try:
            query = """
                SELECT g.idGuest, g.origin, g.occupation
                FROM guest g
                JOIN appuser u ON g.idGuest = u.idUser
            """
            result = db.execute_query(query)
            return result if result else []
        except Exception as e:
            print(f"Error al recuperar huéspedes: {e}")
            return []

    def update_guest(self, db, id_guest, new_origin, new_occupation):
        try:
            query = "UPDATE guest SET origin = %s, occupation = %s WHERE idGuest = %s"
            db.execute_query(query, (new_origin, new_occupation, id_guest))
            print(f"Huésped {id_guest} actualizado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al actualizar huésped: {e}")
            return False

    def delete_guest(self, db, id_guest):
        try:
            query = "DELETE FROM guest WHERE idGuest = %s"
            db.execute_query(query, (id_guest,))
            print(f"Huésped {id_guest} eliminado correctamente.")
            return True
        except Exception as e:
            print(f"Error al eliminar huésped: {e}")
            return False
