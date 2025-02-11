import unittest
from vehicles.car import Car
from engines.gasoline_engine import GasolineEngine

class TestCar(unittest.TestCase):
    def setUp(self):
        self.engine = GasolineEngine()
        self.car = Car(self.engine)

    def test_turn_on_engine(self):
        self.car.turn_on_engine()
        self.assertEqual(self.car.get_engine_status(), "Encendido")

    def test_turn_off_engine(self):
        self.car.turn_on_engine()
        self.car.turn_off_engine()
        self.assertEqual(self.car.get_engine_status(), "Apagado")

if __name__ == '__main__':
    unittest.main() 