import cursorPos, schermen as s

color1 = "#E535E5"
color2 = "#FF0000"
color3 = "#0000FF"
color4 = "#00FF00"
color5 = "#FF00B7"
color6 = "#FF9100"
text_color = 255
line_color = 255

scherm = 0

bright = 127.5

titel = 'Instellingen'
back = "Hoofdmenu"
spelMenu = "Speel menu"
zwart_wit = "Zwart-Wit achtergrond"
achtergrond = "Achtergronden"
kleurenkiezer = "Kleuren"

width = 1280
x = width/2

def setup():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    background(color1)
    size(1280, 720)

def draw():
    global img1, img2, img3, img4, img5, img6, font
    if scherm == 0:
        font = createFont("fortnite.otf", 30, True)
        textFont(font)
        imageMode(CORNER)
        image(img1, width/64, height/9.5, 75, 75)
        image(img2, width/10, height/9.5, 75, 75)
        image(img3, width/64, height/4, 75, 75)
        image(img4, width/10, height/4, 75, 75)
        image(img5, width/64, height/2.55, 75, 75)
        image(img6, width/10, height/2.55, 75, 75)
        noStroke()
        fill(text_color)
        textAlign(LEFT)
        text(back, width/64, 24)
        text(achtergrond, width/64, height/11)
        textAlign(RIGHT)
        text(spelMenu, width/1.01, 24)
        text(kleurenkiezer, width/1.01, height/11)
        textAlign(CENTER)
        text(zwart_wit, width/2, height/11)
        textAlign(CENTER)
        textSize(33)
        text(titel, width/2 , 26)
        
        stroke(0)
        fill(color1)
        rect(1180, 75, 90, 25)
        fill(color2)
        rect(1180, 110, 90, 25)
        fill(color3)
        rect(1180, 145, 90, 25)
        fill(color4)
        rect(1180, 180, 90, 25)
        fill(color5)
        rect(1180, 215, 90, 25)
        fill(color6)
        rect(1180, 250, 90, 25)
        
        stroke(0)
        fill(bright)
        rect(width/2.24, height/8, 150, 25, 3)
        
        fill(bright/2)
        rect(width/2.24, height/6, 150, 25, 3)
        
        fill(bright*1.5)
        rect(width/2.24, height/4.8, 150, 25, 3)
        
        fill(255)
        rect(width/2.24, height/4, 150, 25, 3)
        
        stroke(line_color)
        line(0, 35, width, 35)
    
    
    noLoop()
    
    if scherm == 1:
        s.scherm1()
        
    if scherm == 2:
        s.scherm2()
    
    if scherm == 3:
        s.scherm3()
    
    if scherm == 4:
        s.scherm4()
            
    if scherm == 5:
        s.scherm5()
    
    if scherm == 6:
        s.scherm6()
        
    if scherm == 7:
        s.scherm7()
        
    if scherm == 8:
        s.scherm8()
    
    if scherm == 9:
        s.scherm9()
        
    if scherm == 10:
        s.scherm10()
        
    if scherm == 11:
        s.scherm11()
        
    if scherm == 12:
        s.scherm12()
        
    if scherm == 13:
        s.scherm13()
        
    if scherm == 14:
        s.scherm14()
        
    if scherm == 15:
        s.scherm15()
        
    if scherm == 16:
        s.scherm16()

    cursorPos.mouseCursor()
    loop()

def mouseClicked():
    global text_color, line_color, scherm
    if 15 < mouseX < 90 and 75 < mouseY < 150:
        background(img1)
        scherm = 1
    elif 125 < mouseX < 200 and 75 < mouseY < 150:
        background(img2)
        scherm = 2
    elif 15 < mouseX < 90 and 175 < mouseY < 250:
        background(img3)
        scherm = 3
    elif 125 < mouseX < 200 and 175 < mouseY < 250:
        background(img4)
        scherm = 4
    elif 15 < mouseX < 90 and 275 < mouseY < 350:
        background(img5)
        scherm = 5
    elif 125 < mouseX < 200 and 275 < mouseY < 350:
        background(img6)
        scherm = 6
            
    elif 1180 < mouseX < 1270 and 75 < mouseY < 100:
        background(color1)
        scherm = 7
    elif 1180 < mouseX < 1270 and 110 < mouseY < 135:
        background(color2)
        scherm = 8
    elif 1180 < mouseX < 1270 and 145 < mouseY < 170:
        background(color3)
        scherm = 9
    elif 1180 < mouseX < 1270 and 180 < mouseY < 205:
        background(color4)
        scherm = 10
    elif 1180 < mouseX < 1270 and 215 < mouseY < 240:
        background(color5)
        scherm = 11
    elif 1180 < mouseX < 1270 and 250 < mouseY < 275:
        background(color6)
        scherm = 12
        
    elif width/2.24 < mouseX < 722 and 90 < mouseY < 115:
        background(bright)
        text_color = 255
        line_color = 255
        scherm = 13
    elif width/2.24 < mouseX < 722 and height/6 < mouseY < 145:
        background(bright/2)
        text_color = 255
        line_color = 255
        scherm = 14
    elif width/2.24 < mouseX < 722 and height/4.8 < mouseY < 175:
        background(bright*1.75)
        text_color = bright/2
        line_color = 0
        scherm = 15
    elif width/2.24 < mouseX < 722 and height/4 < mouseY < 205:
        background(bright*2)
        text_color = bright/2
        line_color = 0
        scherm = 16
        
        

        

    
    

        

 
    

    
    
    
