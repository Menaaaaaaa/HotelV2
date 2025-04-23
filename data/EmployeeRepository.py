from domain.Employee import Employee
from data.BDConnection import Conexion

class EmployeeRepository:
    def _init_(self):
        self.connection = Conexion(None, None, None, None, None)

    @staticmethod
    def from_row(row):
        return Employee(row[0], None, None, None, None, row[1])

    def insert_employee(self, db, employee):
        query = "INSERT INTO Employee (idUser, rol) VALUES (%s, %s)"
        values = (employee.id, employee.rol)
        db.execute_query(query, values)

    def select_employee(self, db, idUser):
        query = "SELECT * FROM Employee WHERE idUser = %s"
        result = db.execute_query(query, (idUser,))
        if result:
            return self.from_row(result[0])
        else:
            print("Empleado no encontrado.")
            return None

    def select_all_employees(self, db):
        query = "SELECT * FROM Employee"
        result = db.execute_query(query)
        return [self.from_row(row) for row in result] if result else []

    def update_employee(self, db, employee):
        query = "UPDATE Employee SET rol = %s WHERE idUser = %s"
        values = (employee.rol, employee.id)
        db.execute_query(query, values)

    def delete_employee(self, db, idUser):
        query = "DELETE FROM Employee WHERE idUser = %s"
        db.execute_query(query, (idUser,))