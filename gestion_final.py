
from contacto_final import Contacto

class SistemaGestion:
    def __init__(self):
        self.contactos = []
        self.indice = {}

    def agregar(self, nombre, tel, mail, dir):
        nuevo = Contacto(nombre, tel, mail, dir)
        self.contactos.append(nuevo)
        self.indice[nombre.lower()] = nuevo
        return "¡Contacto guardado con éxito!"

    def buscar(self, dato):
        dato = dato.lower()
        return [c for c in self.contactos if dato in c.nombre.lower() or dato in c.telefono]

    def editar(self, nombre, tel=None, mail=None, dir=None):
        contacto = self.indice.get(nombre.lower())
        if contacto:
            contacto.editar(tel, mail, dir)
            return True
        return False

    def eliminar(self, nombre):
        contacto = self.indice.get(nombre.lower())
        if contacto:
            self.contactos.remove(contacto)
            del self.indice[nombre.lower()]
            return True
        return False
