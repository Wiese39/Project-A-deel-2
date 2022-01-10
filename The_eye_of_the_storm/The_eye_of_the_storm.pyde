import setup_scherm as setp
import gamepause
import settings_scherm as ss
import colors as c

# def mouseTint(x, y, xi ,yi):
#     if x < mouseX < x + xi and y < mouseY < y+ yi:
#         fill('#505150', 50)
game_state = 0
def setup():
    global main_c
    size(1280, 720)
    c.colors()
    background(c.main_c)
    if game_state == 3:
        gamepause.gmp_setup()
    font = createFont("fortnite.otf", 30, True)
    textFont(font)

gameTitel = 'The Eye Of The Storm'
#start = 'Start'
#stop = 'Stop'
spel_instellingen = 'Instellingen'
credits = 'Credits'
rect1 = 'Start'
rect2 = 'Stop'

def draw():
    global naam, spel_instellingen, credits, rect1, rect2, game_state, main_c, color1, color2
    if game_state == 0:
        clear()
        background(c.main_c)
        noStroke()               
        #De titel
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
        clear()
        background(c.main_c)
        redraw()
        setp.setup_draw()
        
    elif game_state == 2:
        clear()
        background(c.main_c)
        redraw()
        ss.settings_draw()
            
    elif game_state == 3:
        clear()
        background(c.main_c)
        redraw()
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
        elif 570 < mouseX < 690 and 370 < mouseY < 425:
            game_state = 2
    
    elif game_state == 2:
        ss.settings_mouseClicked()
    
    if game_state ==2 and 15 < mouseX < 145 and 5 < mouseY < 25:
        game_state = 0
        clear()
        loop()
        cursor(ARROW)    
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
            clear()
            game_state = 1
        if 540 < mouseX < 740 and 325 < mouseY < 375:
            clear()
            background(c.main_c)
            game_state = 2
        if 540 < mouseX < 740 and 400 < mouseY < 450:
            exit()
            

        
