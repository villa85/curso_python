# Librería
import os
import unittest

os.chdir("//")
from CalcularArea import calcular_areas


class TestOperaciones(unittest.TestCase):
    def setUp(self):
        # Aquí, opcionalmente, ejecuta lo que deberías ejecutar antes
        # de comenzar cada test.
        print("Paso 1: ejecuta lo que deberías ejecutar antes de comenzar cada test...")
        # pass

    def test_area_cuadrado(self):
        esperado = 225
        actual = calcular_areas.area_cuadrado(15)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)
        #self.assertRaises(TypeError, calcular_areas.area_cuadrado("15"))


    def test_area_rectangulo(self):
        esperado = -225
        actual = calcular_areas.area_rectangulo(-15, 15)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)
        #with self.assertRaises(TypeError):
        #     calcular_areas.area_rectangulo(-15, "15")

    def tearDown(self):
        # Aquí lo contrario de setUp, cuando cada test ha terminado
        print("Pasa cuando cada test ha terminado...")
        # pass


if __name__ == '__main__':
    unittest.main()
