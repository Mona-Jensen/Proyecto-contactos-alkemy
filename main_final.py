
from gestion_final import SistemaGestion

def menu():
    sistema = SistemaGestion()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            n = input("Nombre: ")
            t = input("Teléfono: ")
            m = input("Correo: ")
            d = input("Dirección: ")
            print(sistema.agregar(n, t, m, d))

        elif opcion == "2":
            b = input("Buscar por nombre o teléfono: ")
            for c in sistema.buscar(b):
                print(c)

        elif opcion == "3":
            n = input("Nombre del contacto a editar: ")
            t = input("Nuevo teléfono (enter para omitir): ")
            m = input("Nuevo correo (enter para omitir): ")
            d = input("Nueva dirección (enter para omitir): ")
            if sistema.editar(n, t or None, m or None, d or None):
                print("Contacto actualizado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == "4":
            n = input("Nombre a eliminar: ")
            if sistema.eliminar(n):
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
