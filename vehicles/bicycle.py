class Bicycle:
    def __init__(self, engine):
        self.engine = engine

    def turn_on_engine(self):
        self.engine.turn_on()

    def turn_off_engine(self):
        self.engine.turn_off()

    def get_engine_status(self):
        return self.engine.get_status() 