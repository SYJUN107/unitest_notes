import unittest
from Suma2 import suma
from Suma2 import sumafloat

class MyTestCase(unittest.TestCase):
    def test_suma_ok(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_float(self):
        self.assertAlmostEqual(sumafloat(1.2, 2.4), 3,6)