import unittest
from engines.diesel_engine import DieselEngine

class TestDieselEngine(unittest.TestCase):
    def setUp(self):
        self.engine = DieselEngine()

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