r = 255
g = 255
b = 255

r1 = 0
g1 = 0
b1 = 0

r2 = 0
g2 = 0
b2 = 0
def setup():
    global r
    global g
    global b
    size(800, 600)
    background(r, g, b)
    
titel = 'Instellingen'
bg = 'Achtergrondinstellingen'
helderOmhoog = 'Helderheid omhoog'
helderOmlaag = 'Helderheid omlaag'
roodOmhoog = 'Meer rood'
roodOmlaag = 'Minder rood'
groenOmhoog = 'Meer groen'
groenOmlaag = 'Minder groen'
blauwOmhoog = 'Meer blauw'
blauwOmlaag = 'Minder blauw'
ringenTitel = 'Kies het aantal ringen'

def draw():
    global titel
    global bg
    global r1
    global g1
    global b1
    global r2
    global g2
    global b2
    global ringenTitel
    
    fill(r1, g1, b1)
    textSize(30)
    textAlign(CENTER)
    text(titel, 400, 30)
    
    fill(r2, g2, b2)
    textSize(18)
    textAlign(LEFT)
    text(bg, 10, 40)
    
    textAlign(RIGHT)
    text(ringenTitel, 790, 40)
    
    textSize(15)
    textAlign(LEFT)
    text(helderOmhoog, 10, 70)
    
    textAlign(LEFT)
    text(helderOmlaag, 10, 100)
    
    text(roodOmhoog, 10, 130)
    text(roodOmlaag, 110, 130)
    
    text(groenOmhoog, 10, 160)
    text(groenOmlaag, 110, 160)
    
    text(blauwOmhoog, 10, 190)
    text(blauwOmlaag, 110, 190)
    
def mouseClicked():
    global r
    global g
    global b
    global r1
    global g1
    global b1
    global r2
    global g2
    global b2
    
    if 0 < mouseX < 150 and 50 < mouseY < 80:
        r += 7
        g += 7
        b += 7
        r1 -= 7
        g1 -= 7
        b1 -= 7
        r2 -= 7
        g2 -= 7
        b2 -= 7
        background(r, g, b)
    elif 0 < mouseX < 150 and 90 < mouseY < 110:
        r -= 7
        g -= 7
        b -= 7
        r1 += 7
        g1 += 7
        b1 += 7
        r2 += 7
        g2 += 7
        b2 += 7
        background(r, g, b)
    elif 0 < mouseX < 85 and 120 < mouseY < 140:
        r += 50
        r1-= 50
        r2 -= 50
        background(r, g, b)
    elif 100 < mouseX < 220 and 120< mouseY < 140:
        r -= 50
        r1 += 50
        r2 += 50
        background(r, g, b)
    elif 0 < mouseX < 85 and 150 < mouseY < 170:
        g += 50
        g1 -= 50
        g2 -= 50
        background(r, g, b)
    elif 100 < mouseX < 220 and 150 < mouseY < 170:
        g -= 50
        g1 += 50
        g2 += 50
        background(r, g, b)
    elif 0 < mouseX < 85 and 180 < mouseY < 200:
        b += 50
        b1 -= 50
        b2 -= 50
        background(r, g, b)
    elif 100 < mouseX < 220 and 180 < mouseY < 200:
        b -= 50
        b1 += 50
        b2 += 50
        background(r, g, b)
    else:
        pass
