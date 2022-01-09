# coding= utf-8

import os
import cursorPos
import schermen as s
import colors as c

text_color = 255 #Initiële tekstkleur defineren

line_color = 255 #Defineren kleur initiële lijn voor de verdeling van het scherm

scherm = 0 #Startscherm

bright = 127.5 #Defineren kleur voor zwart-wit keuze

#Defineren van de kopjes
titel = 'Instellingen'
back = "Hoofdmenu"
spelMenu = "Speel menu"
zwart_wit = "Zwart-Wit achtergrond"
achtergrond = "Achtergronden"
kleurenkiezer = "Kleuren"
regels = 'Spelregels'
path = 'EOTS.pdf'
stop = "Stop"

#De breedte in een variable plaatsen (anders was er een error)
width = 1280
x = width/2

#Het eenmalig tekenen van het scherm, zie module 'schermen.py'
def settings_draw():
    noLoop()
    if scherm == 0:
        s.iScherm0()

#Defineren van posities waar als de muis wordt ingedrukt er dingen veranderen aan de achtergrond
def settings_mouseClicked():
    redraw()
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    global text_color, line_color, scherm, path
    background(c.main_c)
    c.colors()
        
    if width/64 < mouseX < width/64 + 45 and 676 < mouseY < 700:
        exit()

    #Spelregels openen
    if width/1.2 < mouseX < width/1.01 and 676 < mouseY < 700:
        os.system(path)
        

    
           
        
        
