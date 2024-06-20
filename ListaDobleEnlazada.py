from Nodo import Nodo
from Empleado import Empleado
class ListaDobleEnlazada:
    def __init__(self):
        self.raiz = None #tambien se le dice cabeza. Es el inicio de la lista.
        
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo  
        else:
            actual = self.raiz
            while actual.siguiente: 
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual #enlaza la lista con el ultimo nodo
     
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.raiz
            self.raiz.anterior = nuevo_nodo
            self.raiz = nuevo_nodo #esto posiciona el nodo en la posición inicial
            
    def modificar(self, dato):
        nodoActual = self.raiz
        bandera = False
        while nodoActual != None:
            if nodoActual.dato.get_cedula() == dato:
                cedula = nodoActual.dato.get_cedula()
                nuevo_nombre = input("Digite el nuevo nombre: ")
                nueva_edad = int(input("Digite la nueva edad: "))
                empleado = Empleado(cedula, nuevo_nombre, nueva_edad)
                nodoActual.set_dato(empleado)
                bandera = True
            nodoActual = nodoActual.siguiente
        return bandera
               
    def eliminar(self, dato):
        actual = self.raiz
        while actual:
            if actual.dato.get_cedula() == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.raiz = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente
            
    def mostrar(self):
        actual = self.raiz
        while actual:
            print(actual.dato, end=" \n")
            actual = actual.siguiente
    
    def buscar(self, dato):
        nodoActual = self.raiz
        bandera = False
        while nodoActual != None:
            if nodoActual.dato.get_cedula() == dato:
                bandera = True
            nodoActual = nodoActual.siguiente
        return bandera