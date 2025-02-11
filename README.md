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

Actualmente, no se incluyen pruebas unitarias. Se recomienda implementar pruebas para verificar el correcto funcionamiento de las clases de vehículos y motores.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cambios importantes.

## Licencia

Este proyecto está bajo la Licencia MIT. 