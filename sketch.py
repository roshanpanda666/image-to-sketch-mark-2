from sketchpy import canvas
from playsound import playsound
while(True):
    name=input("enter the name of that person you want to make the sketch : ")
    
    def sketch(s):
        
        name==s
        pen=canvas.sketch_from_image(name+'.jpg')
        pen.draw()
        

    if name=="roshan":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)
    if name=="gang":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)
    if name=="sunil":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)
    if name=="mama":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
    
        sketch(name)

    else:
        print("data not found")
        playsound('notfound.mp3')
