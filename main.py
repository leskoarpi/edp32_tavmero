# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C, RTC
import ssd1306
from hcsr04 import HCSR04
from time import sleep

#hangszoro pinout
spkr = Pin(26, Pin.OUT)

#gomb pinin
push_button = Pin(13, Pin.IN)

# ESP32 oled "init?"
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP32 ultrahangos tavmero
sensor = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000)

#sajat fuggvenyek
def beep():
    for x in range(60):
        spkr.value(1)
        sleep(0.00125)
        spkr.value(0)


#oled kijelzo alapbeallitasok
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



mertekegyseg = "cm"
while True:
    int_min = 10
    int_max = 15

    logic_state = push_button.value()
    if logic_state == 0:
        int_min += 5
        int_max += 5
      
      
    mertekegyseg = "cm"    
    distance = int(sensor.distance_cm())
    if distance > 100:
        mertekegyseg = "m"
        distance /= 100
        
    elif distance < int_max and distance > int_min:
        beep()
    #print('Distance:', distance, 'cm')
    disttex = ("tavolsag: " + str(distance)+str(mertekegyseg))
    oled.text(disttex, 0, 35)
    oled.show()
    oled.fill(0)
    
    
    
    
    
    
    
    
