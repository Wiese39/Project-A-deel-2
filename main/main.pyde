import instellingen

def setup():
    size(800, 600)
    background(255)

hoofdMenu = 'Hoofdmenu'
instellingen = 'Instellingen'
gameStart = 'Spelinstellingen'
credits = 'Credits'
stop = 'Stop'
regels = 'Regels'
def draw():
    global hoofdMenu
    global instellingen
    global gameStart
    fill(0)
    textSize(25)
    textAlign(CENTER)
    text(hoofdMenu, 400, 40)
    fill(0)
    textSize(25)
    textAlign(CENTER)
    text(instellingen, 400, 140)
    fill(0)
    textSize(25)
    textAlign(CENTER)
    text(gameStart, 400, 240)
    textSize(25)
    textAlign(CENTER)
    text(credits, 400, 340)
    textSize(18)
    textAlign(RIGHT)
    text(stop, 750, 550)
    textSize(18)
    textAlign(LEFT)
    text(regels, 50, 550)
    
def mouseClicked():
    if 675 < mouseX < 800 and 500 < mouseY < 600:
        exit()
    else:
        pass
    
    
