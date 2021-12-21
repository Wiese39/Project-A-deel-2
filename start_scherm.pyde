#import setup_scherm

def setup():
    size(1280, 720)
    background('#4B0082')

naam = 'The Eye Of The Storm'
#start = 'Start'
#stop = 'Stop'
spel_instellingen = 'Settings'
credits = 'Credits'
rect1 = 'Start'
rect2 = 'Stop'

def draw():
    global naam
    global spel_instellingen
    #global gameStart
    #global stop
    global credits
    global rect1
    global rect2    
                      
    #De titel
    textSize(50)
    fill(255)
    textSize(50)
    textAlign(CENTER)
    text(naam, 650, 70)
    
    #Start
    #textSize(30)
    #fill(255)
    #textSize(30)
    #textAlign(CENTER)
    #text(start, 630, 170)
    
    #Stop
    #textAlign(CENTER)
    #text(stop, 630, 290)
    #fill(255)
    
    #Spel instellingen
    textSize(25)
    fill(70,0,135) #Kleur rect  
    rect(570, 370, 120, 55, 30)
    fill(255) 
    text(spel_instellingen, 632, 405)
    
    #Credits
    textSize(30)
    textAlign(LEFT)
    text(credits, 20, 670)
    fill(255)
    
    #rect start
    textSize(30)
    fill(0,191,25) #Kleur rect    
    rect(570, 287, 120, 55, 30) #Vorm/Positie rect
    fill(255) #Kleur tekst
    text(rect1, 596, 325) #Tekst + positie tekst
    
    #rect stop
    textSize(30)
    fill(191,0,0)    
    rect(570, 450, 120, 55, 30)
    fill(255)
    text(rect2, 598, 487)
    
def mouseClicked(): 
    if rect2 == 'Stop' and 570 <= mouseX <= 690 and 508 >= mouseY >= 454: #Links-Rechts/Onder-Boven
        exit()
    else:
        pass
