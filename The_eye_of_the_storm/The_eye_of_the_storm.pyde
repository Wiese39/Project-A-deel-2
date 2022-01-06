import setup_scherm as setp
import gamepause

# def mouseTint(x, y, xi ,yi):
#     if x < mouseX < x + xi and y < mouseY < y+ yi:
#         fill('#505150', 50)
        
game_state = 0
def setup():
    size(1280, 720)
    if game_state == 0:
        background('#4B0082')
    elif game_state == 3:
        gamepause.gmp_setup()

gameTitel = 'The Eye Of The Storm'
#start = 'Start'
#stop = 'Stop'
spel_instellingen = 'Instellingen'
credits = 'Credits'
rect1 = 'Start'
rect2 = 'Stop'

def draw():
    global naam, spel_instellingen, credits, rect1, rect2, game_state
    
    if game_state == 0: 
        noStroke()               
        #De titel
        background('#4B0082')
        textSize(50)
        fill(255)
        textSize(50)
        textAlign(CENTER)
        text(gameTitel, 650, 70)

        #Credits
        fill('#5f079a')
        rect(20, 630, 90, 40, 7)
        fill(255)
        textSize(20)
        textAlign(LEFT)
        text(credits, 28, 655)
        
        #rect start
        textSize(30)
        fill('#179f17') #Kleur rect
        if 570 < mouseX < 690 and 287 < mouseY < 342:
            fill('#158215')
        rect(570, 287, 120, 55, 7) #Vorm/Positie rect
        fill(255) #Kleur tekst
        text(rect1, 596, 325) #Tekst + positie tekst
        
        #Spel instellingen
        textSize(20)
        fill('#5f079a') #Kleur rect
        if 570 < mouseX < 690 and 370 < mouseY < 425:
            fill('#55068a')  
        rect(570, 370, 120, 55, 7)
        fill(255) 
        text(spel_instellingen, 575, 405)
        
        #rect stop
        textSize(30)
        fill('#af2020')
        if 570 < mouseX < 690 and 450 < mouseY < 505:
            fill('#9f0f0f')    
        rect(570, 450, 120, 55, 7)
        fill(255)
        text(rect2, 598, 487)
    
    elif game_state == 1:
        setp.setup_draw()
            
    elif game_state == 3:
        gamepause.gmp_draw()
def mousePressed():
    global game_state
    if game_state == 0:
        pass
    elif game_state == 1:
        setp.setup_mousePressed()
def keyPressed():
    if game_state == 0:
        pass
    elif game_state == 1:
        setp.setup_keyPressed()
def mouseClicked(): 
    global game_state
    if game_state ==0:
        if rect2 == 'Stop' and 570 <= mouseX <= 690 and 508 >= mouseY >= 454: #Links-Rechts/Onder-Boven
            exit()
        elif 570 <= mouseX <= 690 and  287 <= mouseY <= 287 + 55:
            game_state = 1
            
    elif game_state == 1:
        if 120 < mouseX < 210 and  565 < mouseY < 615:
            print("Terug naar het start menu")
            game_state = 0   
        if 10 < mouseX < 60 and  10 < mouseY < 60:
            print("pauze scherm ,geopend")
            game_state = 3
    elif game_state == 3:
        if 540 < mouseX <740  and 250 < mouseY <300:
            print("setup scherm ,geopend")
            game_state = 1
