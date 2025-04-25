from domain.Employee import Employee
from data.EmployeeRepository import EmployeeRepository

class EmployeeService:
    def __init__(self, db):
        self.db = db
        self.employee_repository = EmployeeRepository()

    def create_employee(self):

        idUser = input("Ingrese la identificación del empleado (idUser): ")
        name = input("Ingrese el nombre del empleado: ")
        email = input("Ingrese el correo del empleado: ")
        password = input("Ingrese la contraseña del empleado: ")
        status = input("Ingrese el estado del empleado ('active' o 'inactive'): ")
        rol = input("Ingrese el rol del empleado: ")

        query_check_user = "SELECT * FROM appuser WHERE idUser = %s"
        user_exists = self.db.execute_query(query_check_user, (idUser,))
        if not user_exists:

            query_insert_user = """
                INSERT INTO appuser (idUser, name, email, password, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.db.execute_query(query_insert_user, (idUser, name, email, password, status))


        # Crear el empleado en Employee
        employee = Employee(idUser, name, email, password, status, rol)
        self.employee_repository.insert_employee(self.db, employee)
        print("Empleado creado exitosamente.")

    def list_employees(self):
        # Recuperar empleados desde la base de datos
        employees = self.employee_repository.select_all_employees(self.db)
        if employees:
            print("Lista de empleados:")
            for emp in employees:
                print(f"ID: {emp.id}, Rol: {emp.rol}")
        else:
            print("No hay empleados registrados.")

    def delete_employee(self):

        idUser = input("Ingrese la identificación del empleado (idUser) que desea eliminar: ")

        query_check_employee = "SELECT * FROM Employee WHERE idUser = %s"
        employee_exists = self.db.execute_query(query_check_employee, (idUser,))
        if not employee_exists:
            print("Error: El empleado no existe en la tabla 'Employee'.")
            return

        query_delete_employee = "DELETE FROM Employee WHERE idUser = %s"
        self.db.execute_query(query_delete_employee, (idUser,))
        print("Empleado eliminado exitosamente.")

    def update_employee(self):
        idUser = input("Ingrese la identificación del empleado que desea actualizar: ")

        query_check_employee = "SELECT * FROM Employee WHERE idUser = %s"
        employee_exists = self.db.execute_query(query_check_employee, (idUser,))
        if not employee_exists:
            print("Error: El empleado no existe en la tabla 'Employee'.")
            return

        rol = input("Ingrese el nuevo rol del empleado: ")

        query_update_employee = "UPDATE Employee SET rol = %s WHERE idUser = %s"
        self.db.execute_query(query_update_employee, (rol, idUser))
        print("Empleado actualizado exitosamente.")