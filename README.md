# IoT_TemperaturaCal_Pico
Monitoreo de temperatura con Raspberry Pi Pico W y ThingSpeak.

Este proyecto permite medir la temperatura del procesador RP2040 de la Raspberry Pi Pico W usando su sensor interno y enviar los datos a ThingSpeak para su almacenamiento y visualización en la nube. Originalmente, se iba a utilizar un sensor externo LM35, pero debido a problemas técnicos se decidió utilizar el sensor interno. El sistema se conecta automáticamente a Wi-Fi, toma una lectura de temperatura cada 180 segundos y la envía a ThingSpeak para su análisis. Además, ThingSpeak permite calcular el promedio de las últimas 10 mediciones y generar alertas cuando la temperatura supera los 35°C.

## Instrucciones de instalación y uso

Paso 1: Conectar la Raspberry Pi Pico W a la PC

- Conectar la Raspberry Pi Pico W a la computadora con un cable micro USB de Transferencia de datos 
- Instalar MicroPython en la Raspberry si aún no está instalado
- Descargar e instalar Thonny

Paso 2: Configurar ThingSpeak

- Crear una cuenta en ThingSpeak en la página oficial
- Crear un canal nuevo y copiar la API Key que generó ThingSpeak
- Configurar un gráfico en field1 para visualizar la temperatura en tiempo real

Paso 3: Subir el código a la Raspberry Pi Pico W

- Descargar el archivo Codigo-Temperatura-Rasbery-Pi-Pico.py de este repositorio
- Abrir Thonny, cargar el archivo Codigo-Temperatura-Rasbery-Pi-Pico.py y modificar las siguientes líneas con la información de la red Wi-Fi:
  ```python
  SSID = "TuRedWiFi"
  PASSWORD = "TuContraseñaWiFi"
  ```
- Reemplazar la API Key de ThingSpeak en esta línea:
  ```python
  API_KEY = "TU_API_KEY"
  ```
- Guardar y ejecutar el script en la Raspberry Pi Pico W

Paso 4: Visualizar los datos en ThingSpeak

- Ir al canal de ThingSpeak creado en el paso 2
- Revisar el gráfico de field1 donde se actualizan los valores cada 180 segundos
- Si se habilita MathWorks, se podrá ver el cálculo del promedio de temperatura y una alerta cuando la temperatura supere los 35°C



Autores

Ricardo Esquivel Palacios Materia: Internet de las Cosas (IoT)

Notas Adicionales

- Si la Raspberry Pi Pico W no se conecta a Wi-Fi, revisar que las credenciales sean correctas
- Si no se envían datos a ThingSpeak, verificar que la API Key esté bien configurada
- Ten en cuenta que la red de wifi a la que te conectes no sea 5G suele no conectarse.

