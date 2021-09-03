import RPi.GPIO as GPIO
import time
import picamera

    
GPIO.setmode(GPIO.BCM)

TRANSMISSOR = 20
RECEPTOR = 21

GPIO.setwarnings(False)

GPIO.setup(TRANSMISSOR,GPIO.OUT)
GPIO.setup(RECEPTOR,GPIO.IN)

print("Projeto 16 - Sensor Ultrassônico")

def distancia ():
    #COLOCAR O TRANSMISSOR EM NÍVEL HIGH POR 10 MICROSSEGUNDOS
    GPIO.output(TRANSMISSOR,1) 
    time.sleep(0.000001)
    GPIO.output(TRANSMISSOR,0)
    tempo_inicial = time.time()
    tempo_final = time.time()
    
    #Obter tempo inicial
    while GPIO.input(RECEPTOR) == 0:
        tempo_inicial = time.time()
    #Obter tempo FINAL
    while GPIO.input(RECEPTOR) == 1:
        tempo_final = time.time()
    
    tempo_distancia =  tempo_final - tempo_inicial
    
    #Multiplicar pela velocidade do som 34300 cm/s
    #Dividir por 2 pois o tempo compreende a ida e volta do sinal
    distancia = (tempo_distancia*34300)/2
    return distancia

try:
    while True:
        print("Distancia = %.1f cm" % distancia())
        time.sleep(1.0)
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            # Camera warm-up time
            time.sleep(2)
            camera.capture('foo.jpg')

except KeyboardInterrupt:
    GPIO.cleanup()
    
