def setup():
    fullScreen()
    background(255)
    
def draw():
    if keyPressed:
        if (key == '1'):
            fill('#F507DA')
            rect(mouseX, mouseY, 40, 40)
        elif (key == '2'):
            fill('#309CA5')
            triangle(mouseX, mouseY, 20, 20 , 60, 60)
        elif (key == '3'):
            background(0)
    elif mousePressed:
        fill('#07F590')
        background('#F51F07')
        ellipse(mouseX, mouseY, 35, 60)
        
