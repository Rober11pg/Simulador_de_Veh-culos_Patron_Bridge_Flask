import unittest
from engines.electric_engine import ElectricEngine

class TestElectricEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ElectricEngine()

    def test_initial_state(self):
        self.assertEqual(self.engine.get_status(), "Apagado")

    def test_turn_on(self):
        self.engine.turn_on()
        self.assertEqual(self.engine.get_status(), "Encendido")

    def test_turn_off(self):
        self.engine.turn_on()
        self.engine.turn_off()
        self.assertEqual(self.engine.get_status(), "Apagado")

if __name__ == '__main__':
    unittest.main() 