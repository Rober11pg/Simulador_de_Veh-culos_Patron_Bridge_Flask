class ElectricEngine:
    def __init__(self):
        # Estado inicial del motor
        self._is_on = False

    def turn_on(self):
        # Encender el motor
        self._is_on = True

    def turn_off(self):
        # Apagar el motor
        self._is_on = False

    def get_status(self):
        # Devolver el estado del motor
        return "Encendido" if self._is_on else "Apagado" 