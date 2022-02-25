import unittest
from lib.BusquedaHeuristica import BusquedaHeuristica, Base


class TestDescargarDatos(unittest.TestCase):

    def test_descarga_correcta(self):
        """
        Comprobar que la descarga de los datos se realice correctamente
        """
        base = Base("https://mach-eight.uc.r.appspot.com/")
        self.assertIsNotNone(base.data)

    def test_descarga_incorrecta(self):
        """
        Comprobar que la descarga de los datos se realice correctamente
        """
        base = Base("https://mach_eight.uc.r.appspot.com/")
        self.assertIsNone(base.data)

    def test_url_tipo_incorrecto_dato(self):
        try:
            base = Base(12345678)
            rta = True
        except Exception as e:
            rta = False
        self.assertFalse(rta)


class TestHeuristicSearch(unittest.TestCase):
    bh = BusquedaHeuristica("https://mach-eight.uc.r.appspot.com/")

    def test_evaluar_ejemplo(self):
        """
        Test que evalua la respuesta de ejemplo entregada junto al problema
        """
        self.bh.search(139)
        valor_hallado = self.bh.solve()
        resultado_esperado = [('Nate Robinson', 'Brevin Knight'), ('Mike Wilks', 'Nate Robinson')]
        self.assertEqual(valor_hallado, resultado_esperado)

    def test_tipo_dato_invalido(self):
        """
        Test que evalua que el valor a buscar pareja no sea un tipo valido
        """
        try:
            self.bh.search("139")
            rta = True
        except Exception as e:
            rta = False
        self.assertFalse(rta)

    def test_valor_buscar_sin_solucion(self):
        """
        Test que evalua la respuesta de ejemplo entregada junto al problema
        """
        self.bh.search(15)
        valor_hallado = self.bh.solve()
        self.assertIsNone(valor_hallado)

    def test_url_tipo_incorrecto_dato(self):
        try:
            bh = BusquedaHeuristica(12345678)
            rta = True
        except Exception as e:
            rta = False
        self.assertFalse(rta)


if __name__ == '__main__':
    unittest.main()