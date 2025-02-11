import unittest
from vehicles.bicycle import Bicycle
from engines.electric_engine import ElectricEngine

class TestBicycle(unittest.TestCase):
    def setUp(self):
        self.engine = ElectricEngine()
        self.bicycle = Bicycle(self.engine)

    def test_turn_on_engine(self):
        self.bicycle.turn_on_engine()
        self.assertEqual(self.bicycle.get_engine_status(), "Encendido")

    def test_turn_off_engine(self):
        self.bicycle.turn_on_engine()
        self.bicycle.turn_off_engine()
        self.assertEqual(self.bicycle.get_engine_status(), "Apagado")

if __name__ == '__main__':
    unittest.main() 