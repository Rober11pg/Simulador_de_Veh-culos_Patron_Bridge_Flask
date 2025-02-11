import unittest
from vehicles.motorcycle import Motorcycle
from engines.diesel_engine import DieselEngine

class TestMotorcycle(unittest.TestCase):
    def setUp(self):
        self.engine = DieselEngine()
        self.motorcycle = Motorcycle(self.engine)

    def test_turn_on_engine(self):
        self.motorcycle.turn_on_engine()
        self.assertEqual(self.motorcycle.get_engine_status(), "Encendido")

    def test_turn_off_engine(self):
        self.motorcycle.turn_on_engine()
        self.motorcycle.turn_off_engine()
        self.assertEqual(self.motorcycle.get_engine_status(), "Apagado")

if __name__ == '__main__':
    unittest.main() 