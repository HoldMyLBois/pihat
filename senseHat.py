from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)

for i in range(0,5):

    sense.show_letter("J", red)
    sleep(1)
    sense.show_letter("A", yellow)
    sleep(1)
    sense.show_letter("Y", blue)    
    sleep(1.5)
