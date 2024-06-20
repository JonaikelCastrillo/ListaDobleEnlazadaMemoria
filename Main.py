from ListaDobleEnlazada import ListaDobleEnlazada
from Empleado import Empleado
miLista = ListaDobleEnlazada()
numero = 0
opcion = 0

def es_entero(valor):
    try:
        valor = int(valor)
        return True
    except ValueError:
        return False

while opcion != 6:
    opcion = int(input("Digite la opción que requiera:\n"
                       "1. Agregar \n"
                       "2. Mostrar\n"
                       "3. Modificar\n"
                       "4. Buscar\n"
                       "5. Eliminar\n"
                       "6. Salir: \n"))
    
    match opcion:
        case 1:
            cedula = input("Digite la cedula: ")
            if es_entero(cedula):
                nombre = input("Digite el nombre: ")
                edad = input("Digite la edad: ")
                if es_entero(edad):
                    empleado = Empleado(int(cedula), nombre, int(edad))
                    posicion = input("¿Desea agregarlo al inicio (1) o al final (2)?")
                    if es_entero(posicion):
                        if int(posicion) == 1:
                            miLista.agregar_inicio(empleado)
                        elif int(posicion) == 2:
                            miLista.agregar_final(empleado)
                        else:
                            print("opción inválida")
                    else:
                        print("El valor ingresado debe ser entero")        
                else:
                    print("El valor ingresado debe ser entero")
            else:
                print("El valor ingresado debe ser entero")
        case 2: 
            print(miLista.mostrar())
        case 3:
            dato = input("Digite la cedula de la persona que desea modificar: ")
            if es_entero(dato):
                if miLista.modificar(int(dato)):
                    print("Persona modificada.")
                else:
                    print("Persona no encontrada. No se puede modificar")
            else:
                    print("El valor ingresado debe ser entero")
        case 4:
            dato = input("Digite la cédula de la persona que desea buscar: ")
            if es_entero(dato):
                if miLista.buscar(int(dato)):
                    print("Persona encontrada")
                else:
                    print("Persona no encontrada")
            else:
                    print("El valor ingresado debe ser entero")
        case 5:
            dato = input("Digite la cedula de la persona que desea eliminar: ")
            if es_entero(dato):
                if miLista.eliminar(int(dato)):
                    print("Persona eliminada.")
                else:
                    print("Error. Persona no eliminada")
            else:
                print("El valor ingresado debe ser entero")
        case 6:
            print("Saliendo del programa...")
        case _:
            print("Opción inválida")