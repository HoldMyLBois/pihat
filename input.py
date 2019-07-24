from sense_hat import SenseHat

sense = SenseHat()

password = input("Password Please:")

if password == "bob":
    name = input("Type Your Sentence:")
    r = input("r:")
    g = input("g:")
    b = input("b:")
    rb = input("r*:")
    gb = input("g*:")
    bb = input("b*:")
    s = input("whats the speed?")
    loop = input("how much does it loop?")

    loop = (int(loop))    
    speed = (float(s))
    bcolor = (int(rb),int(gb),int(bb))
    color = (int(r),int(g),int(b))
    


    for i in range(0,loop):   
        sense.show_message(name, text_colour=color, back_colour=bcolor, scroll_speed=speed)
    sense.clear()
else:
    KeyboardInterrupt
