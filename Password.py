from sense_hat import SenseHat

sense = SenseHat()

password = input("Enter The Password:")

if password == "999":
 
    user = ("Access Granted")
    color= (0,255,0)
    
    sense.show_message(user,text_colour=color)

    sense.clear()
    KeyboardInterrupt

else:
    KeyboardInterrupt 
