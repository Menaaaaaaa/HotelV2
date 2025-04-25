from traceback import print_tb

from data.BDConnection import Conexion
from application.EmployeeService import EmployeeService
from application.GuestService import GuestService
from application.ReservationService import ReservationService

class Menu:
    def __init__(self):
        # Conexión a la base de datos
        self.db = Conexion("localhost", 3306, "root", "password123", "hotel")
        self.db.connect()

        self.employee_service = EmployeeService(self.db)
        self.guest_service = GuestService(self.db)
        self.reservation_service = ReservationService(self.db)

    def show_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Gestión de Empleados")
            print("2. Gestión de Huéspedes")
            print("3. Gestión de Reservas")
            print("4. Salir")

            choice = input("Seleccione una opción: ")
            if choice == "1":
                self.employee_menu()
            elif choice == "2":
                self.guest_menu()
            elif choice == "3":
                self.reservation_menu()
            elif choice == "4":
                print("Saliendo del sistema...")
                self.db.disconnect()
                break
            else:
                print("Opción inválida, intente nuevamente.")

    def employee_menu(self):
        while True:
            print("\n--- Gestión de Empleados ---")
            print("1. Lista de empleados")
            print("2. Crear empleado")
            print("3. Actualizar datos del empleado")
            print("4. Eliminar empleado")
            print("5. Volver")

            choice = input("Seleccione una opción: ")
            if choice == "1":
                self.employee_service.list_employees()
            elif choice == "2":
                self.employee_service.create_employee()
            elif choice == "3":
                self.employee_service.update_employee()
            elif choice == "4":
                self.employee_service.delete_employee()
            elif choice == "5":
                break
            else:
                print("Opción inválida.")

    def guest_menu(self):
        while True:
            print("\n--- Gestión de Huéspedes ---")
            print("1. Lista de huéspedes")
            print("2. Crear huésped")
            print("3. Actualizar datos del huésped")
            print("4. Eliminar huésped")
            print("5. Volver")

            choice = input("Seleccione una opción: ")
            if choice == "1":
                self.guest_service.list_guests()
            elif choice == "2":
                self.guest_service.create_guest()
            elif choice == "3":
                id_guest = input("Ingrese el ID del huésped a actualizar: ")
                guest = self.guest_service.get_guest(id_guest)
                if guest:
                    self.guest_service.update_guest(guest)
            elif choice == "4":
                id_guest = input("Ingrese el ID del huésped a eliminar: ")
                self.guest_service.delete_guest(id_guest)
            elif choice == "5":
                break
            else:
                print("Opción inválida.")

    def reservation_menu(self):
        while True:
            print("\n--- Gestión de Reservas ---")
            print("1. Lista de reservas")
            print("2. Crear reserva")
            print("3. Eliminar reserva")
            print("4. Volver")

            choice = input("Seleccione una opción: ")
            if choice == "1":
                self.reservation_service.list_reservations()
            elif choice == "2":
                self.reservation_service.create_reservation()
            elif choice == "3":
                self.reservation_service.delete_reservation()
            elif choice == "4":
                break
            else:
                print("Opción inválida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu = Menu()
    menu.show_menu()