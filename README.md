# Simulador de Vehículos

Este proyecto es un simulador de vehículos implementado con Flask, que utiliza el patrón arquitectónico Bridge para desacoplar la abstracción (vehículos) de la implementación (motores). Esto permite que ambos puedan variar independientemente.

## Objetivos del Proyecto

- Demostrar el uso del patrón Bridge en una aplicación web.
- Proveer una interfaz sencilla para seleccionar vehículos y motores.
- Permitir la extensión fácil del sistema con nuevos tipos de vehículos y motores.

## Instalación

1. Clona el repositorio en tu máquina local.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
2. Abre tu navegador y visita `http://127.0.0.1:5000`.
3. Selecciona un tipo de vehículo y motor, y usa los botones para encender o apagar el motor.

## Ejemplos de Uso

- Selecciona "Automóvil" y "Eléctrico", luego enciende el motor para ver el mensaje personalizado.
- Cambia a "Motocicleta" con motor "Diésel" y apaga el motor para ver el estado actualizado.

## Pruebas

El proyecto incluye un conjunto de pruebas unitarias para verificar el correcto funcionamiento de los motores, vehículos y la aplicación web. Las pruebas se encuentran en el directorio `tests/`.

### Ejecución de Pruebas

Para ejecutar todas las pruebas, utiliza el siguiente comando:

```bash
python -m unittest discover -s tests
```

### Cobertura de Pruebas

Las pruebas cubren los siguientes aspectos:

- **Motores**: Verificación de los estados inicial, encendido y apagado para los motores eléctricos, diésel y de gasolina.
- **Vehículos**: Verificación de la integración de los motores con los vehículos (automóvil, motocicleta, bicicleta) y el cambio de estado del motor.
- **Aplicación Web**: Verificación de la carga de la página principal y el manejo de solicitudes POST para diferentes combinaciones de vehículos y motores.

### Ejemplos de Pruebas

- **Encender Motor**: Verifica que el mensaje correcto se muestre cuando se enciende el motor de un automóvil eléctrico.
- **Apagar Motor**: Verifica que el mensaje correcto se muestre cuando se apaga el motor de un automóvil eléctrico.
- **Combinaciones de Vehículo y Motor**: Verifica que el sistema maneje correctamente diferentes combinaciones de vehículos y motores, como una motocicleta con motor diésel.

Estas pruebas aseguran que el sistema funcione correctamente en diferentes escenarios y que los mensajes se generen como se espera.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cambios importantes.

## Licencia

Este proyecto está bajo la Licencia MIT. 