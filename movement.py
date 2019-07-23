from sense_hat import SenseHat
from time import sleep
import signal
sense = SenseHat()
sense.clear()
event = sense.stick.get_events()

while True:
    
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    if event == "pressed" and event.direction == "Middle":
        break
