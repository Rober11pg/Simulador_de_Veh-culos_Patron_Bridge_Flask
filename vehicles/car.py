class Car:
    def __init__(self, engine):
        # Asignar el motor al vehículo
        self.engine = engine

    def turn_on_engine(self):
        # Delegar la acción de encender el motor
        self.engine.turn_on()

    def turn_off_engine(self):
        # Delegar la acción de apagar el motor
        self.engine.turn_off()

    def get_engine_status(self):
        # Obtener el estado del motor
        return self.engine.get_status() 