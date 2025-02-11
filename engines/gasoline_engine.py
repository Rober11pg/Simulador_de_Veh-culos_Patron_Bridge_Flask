class GasolineEngine:
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def get_status(self):
        return "Encendido" if self._is_on else "Apagado" 