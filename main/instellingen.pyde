def mijn_instellingen():
    def setup():
        size(800, 600)
        background(125)
    name = 'Henk'
    def draw():
        global name
        background(0)
        fill(255, 0, 0)
        textSize(25)
        textAlign(LEFT)
        text('name', 40, 40)
    
