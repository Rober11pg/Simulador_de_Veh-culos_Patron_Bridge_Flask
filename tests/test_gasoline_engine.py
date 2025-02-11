import unittest
from engines.gasoline_engine import GasolineEngine

class TestGasolineEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GasolineEngine()

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