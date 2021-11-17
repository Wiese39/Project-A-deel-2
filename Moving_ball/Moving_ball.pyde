def setup():
    size(800, 600)
x = 40
y = 45
    
def draw():
    global x
    global y
    fill(0)
    background(255, 2, 75)
    ellipse(x, y, 40, 45)
    if keyPressed:
        if (key == 'w') or (key == 'W'):
            y -= 3
        elif (key == 'a') or (key == 'A'):
            x -= 3
        elif (key == 'd') or (key == 'D'):
            x += 3
        elif (key == 's') or (key == 'S'):
            y += 3
        else:
            pass
            
    
