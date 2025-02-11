from flask import Flask, render_template, request
from engines.electric_engine import ElectricEngine
from engines.diesel_engine import DieselEngine
from engines.gasoline_engine import GasolineEngine
from vehicles.car import Car
from vehicles.motorcycle import Motorcycle
from vehicles.bicycle import Bicycle
import unittest

app = Flask(__name__)

# Diccionario para almacenar las clases de vehículos (Abstracción)
vehicles = {
    'Automóvil': Car,
    'Motocicleta': Motorcycle,
    'Bicicleta': Bicycle
}

# Diccionario para almacenar las clases de motores (Implementación)
engines = {
    'Eléctrico': ElectricEngine,
    'Diésel': DieselEngine,
    'Gasolina': GasolineEngine
}

@app.route('/', methods=['GET', 'POST'])
def index():
    vehicle_type = None
    engine_type = None
    engine_status = None

    if request.method == 'POST':
        # Obtener las selecciones del formulario
        vehicle_type = request.form.get('vehicle')
        engine_type = request.form.get('engine')
        action = request.form.get('action')

        # Obtener las clases correspondientes
        vehicle_class = vehicles.get(vehicle_type)
        engine_class = engines.get(engine_type)

        if vehicle_class and engine_class:
            # Crear instancia del vehículo con el motor seleccionado
            vehicle = vehicle_class(engine_class())
            if action == 'start':
                vehicle.turn_on_engine()
            elif action == 'stop':
                vehicle.turn_off_engine()
            engine_status = vehicle.get_engine_status()

    # Renderizar la plantilla con el estado actual
    return render_template('index.html', vehicle_type=vehicle_type, engine_type=engine_type, engine_status=engine_status)

if __name__ == '__main__':
    app.run(debug=True)

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