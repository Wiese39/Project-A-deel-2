def setup():
    size(800, 600)
    background(255)
    global homeButton
    homeButton = loadImage('png-transparent-green-grass-home-screen-button-house-desktop-environment-symbol-aqua-line.png')
    global arrow
    arrow = loadImage('arrow-pointing-to-the-left-115501167743epfu1fapc.png')

menu = 'Hoofdmenu'
def draw():
    global menu1
    global homeButton
    fill(0)
    textSize(25)
    textAlign(LEFT)
    text(menu, 40, 40)
    if menu == 'Instellingen' or menu == 'Game Start Scherm':
        image(homeButton, 725, 20, 40, 40)
    if menu == 'Game Start Scherm':
        image(arrow, 0, 0, 25, 25)

def mouseClicked():
    global menu
    background(255)
    if 25 < mouseX < 400 and 25 < mouseY < 40:
        if menu == 'Hoofdmenu':
            menu = 'Instellingen'
        elif menu == 'Instellingen':
            menu = 'Game Start Scherm'
    elif 650 < mouseX < 760 and 0 < mouseY < 50:
        menu = 'Hoofdmenu'
    elif 0 < mouseX < 25 and 0 < mouseY < 25:
        menu = 'Instellingen'
    else:
        pass
    
