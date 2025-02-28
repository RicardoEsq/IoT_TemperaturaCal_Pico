import network
import urequests
import utime
import machine

# Configuración Wi-Fi
SSID = "Alumno"
PASSWORD = "Mebe2ege"

# Configuración ThingSpeak
API_KEY = "H9G6Y3DY2Y7K8NIQ"  # El API key que te da el thinkSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Función para conectarse a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF) # Habilita la interfaz Wi-Fi
    wlan.active(True)
    wlan.connect(SSID, PASSWORD) # Intenta conectarse a la red
    
    print("Conectando a Wi-Fi...")
    while not wlan.isconnected(): # Espera hasta que haya conexión
        utime.sleep(1)
    
    print("Conectado a Wi-Fi:", wlan.ifconfig()) # Muestra dirección IP asignada

# Función para leer la temperatura interna del RP2040
def leer_temperatura():
    sensor_temp = machine.ADC(4)  # Canal 4 es el sensor de temperatura interno
    conversion_factor = 3.3 / (65535)  # Conversión a voltaje
    lectura = sensor_temp.read_u16() * conversion_factor
    temperatura = 27 - (lectura - 0.706) / 0.001721  # Fórmula del RP2040
    return round(temperatura, 2) # redondea a 2 puntos decimales 

# Función para enviar datos a ThingSpeak
def enviar_a_thingspeak(temp):
    try:
        respuesta = urequests.get(THINGSPEAK_URL + "?api_key=" + API_KEY + "&field1=" + str(temp)) #Realiza un solicitud GET y con la URL de thinkspeak
        print("Enviado a ThingSpeak:", respuesta.text)  # Imprime la respuesta del servidor para confirmar el envío exitoso
        respuesta.close()
    except Exception as e:
        print("Error enviando datos:", e) # En caso de errores de envio de datos 

# Conectar a Wi-Fi antes de empezar
conectar_wifi()

# Bucle principal
while True:
    temperatura = leer_temperatura()
    print("Temperatura actual:", temperatura, "°C")
    enviar_a_thingspeak(temperatura) # envia el dato a thinspeak
    utime.sleep(180)  # Esperar 180 segundos antes de enviar de nuevo