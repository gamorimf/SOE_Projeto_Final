from smbus2 import SMBus
from mlx90614 import MLX90614
from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

buzzer = Buzzer(17)
bus = SMBus(1)
led_red = LED(22)
led_green = LED(27)
sensor = MLX90614(bus, address=0x5A)

print "Ambient Temperature :", sensor.get_ambient()
print "Object Temperature :", sensor.get_object_1()


if sensor.get_object_1()>35.0:
    buzzer.on()
    led_red.on()
    sleep(1)

else:
    led_green.on()
    sleep(1)
    
    bus.close()
