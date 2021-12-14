#Het defineren van alle schermen (16 in totaal), elk scherm werkt hetzelfde. Kan sneler; nog even naar kijken :)
import cursorPos as cP

scherm = 0

color1 = "#44028F"
color2 = "#FF0000"
color3 = "#0000FF"
color4 = "#00FF00"
color5 = "#FF00B7"
color6 = "#FF9100"
text_color = 255
line_color = 255

titel = 'Instellingen'
back = "Hoofdmenu"
spelMenu = "Speel menu"
zwart_wit = "Zwart-Wit achtergrond"
achtergrond = "Achtergronden"
kleurenkiezer = "Kleuren"
regels = 'Spelregels'
stop = "Stop"

bright = 127.5

height= 720
width = 1280
x = width/2

def scherm0():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
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
    text(stop, width/64, 696)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    text(regels, width/1.01, 696)
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
    line(0, 665, width, 665)
    
    noLoop()
    cP.mouseCursor()
    loop()

def scherm1():
    scherm0()
    
def scherm2():
    scherm0() 
            
def scherm3():
    scherm0()
    
def scherm4():
   scherm0()
    
def scherm5():
    scherm0()
    
def scherm6():
    scherm0()
    
def scherm7():
    scherm0()
    
def scherm8():
    scherm0()
    
def scherm9():
    scherm0()
    
def scherm10():
    scherm0()
    
def scherm11():
    scherm0()
    
def scherm12():
    scherm0()
    
def scherm13():
   scherm0()
    
def scherm14():
   scherm0()
    
def scherm15():
   scherm0()
    
def scherm16():
    scherm0()
    

    
