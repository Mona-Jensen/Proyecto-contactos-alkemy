
import unittest
from gestion_final import SistemaGestion

class TestSistemaGestion(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaGestion()
        self.sistema.agregar("Ana", "123", "ana@mail.com", "Santiago")

    def test_agregar(self):
        self.assertEqual(len(self.sistema.contactos), 1)

    def test_buscar(self):
        self.assertEqual(len(self.sistema.buscar("Ana")), 1)

    def test_editar(self):
        self.sistema.editar("Ana", tel="999")
        self.assertEqual(self.sistema.buscar("Ana")[0].telefono, "999")

    def test_eliminar(self):
        self.assertTrue(self.sistema.eliminar("Ana"))

if __name__ == "__main__":
    unittest.main()
