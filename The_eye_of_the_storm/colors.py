color1 = "#44028F"
color2 = "#FF0000"
color3 = "#0000FF"
color4 = "#00FF00"
color5 = "#FF00B7"
color6 = "#FF9100"

bright = 127.5

img1 = loadImage("macock1.jpeg")
img2 = loadImage("ricardo.jpeg")
img3 = loadImage("minecraft.JPEG")
img4 = loadImage("coolbg.jpeg")
img5 = loadImage("bg1.jpeg")
img6 = loadImage("bglight.jpeg")

main_c = color1
    

def colors():
    global main_c, img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    if 15 < mouseX < 90 and 75 < mouseY < 150:
        background(img1)
        main_c = img1
        
    elif 125 < mouseX < 200 and 75 < mouseY < 150:
        background(img2)
        main_c = img2
        
    elif 15 < mouseX < 90 and 175 < mouseY < 250:
        background(img3)
        main_c = img3
        
    elif 125 < mouseX < 200 and 175 < mouseY < 250:
        background(img4)
        main_c = img4
        
    elif 15 < mouseX < 90 and 275 < mouseY < 350:
        background(img5)
        main_c = img5
        
    elif 125 < mouseX < 200 and 275 < mouseY < 350:
        background(img6)
        main_c = img6
        
            
    elif 1180 < mouseX < 1270 and 75 < mouseY < 100:
        background(color1)
        main_c = color1
        
    elif 1180 < mouseX < 1270 and 110 < mouseY < 135:
        background(color2)
        main_c = color2
        
    elif 1180 < mouseX < 1270 and 145 < mouseY < 170:
        background(color3)
        main_c = color3
        
    elif 1180 < mouseX < 1270 and 180 < mouseY < 205:
        background(color4)
        main_c = color4
        
    elif 1180 < mouseX < 1270 and 215 < mouseY < 240:
        background(color5)
        main_c = color5
        
    elif 1180 < mouseX < 1270 and 250 < mouseY < 275:
        background(color6)
        main_c = color6
        
        
    elif width/2.24 < mouseX < 722 and 90 < mouseY < 115:
        background(bright)
        text_color = 255
        line_color = 255
        main_c = bright
        
    elif width/2.24 < mouseX < 722 and height/6 < mouseY < 145:
        background(bright/2)
        text_color = 255
        line_color = 255
        main_c = bright/2
        
    elif width/2.24 < mouseX < 722 and height/4.8 < mouseY < 175:
        background(180)
        text_color = 255
        line_color = 0
        main_c = 180
        
