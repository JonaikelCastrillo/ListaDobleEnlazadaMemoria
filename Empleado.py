class Empleado:
    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        
    def get_cedula(self):
        return self.cedula
    def set_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def get_edad(self):
        return self.edad
    def set_edad(self, nueva_edad):
        self.edad = nueva_edad
        
    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Edad: {self.edad}"