huidig_scherm = 1
def gmp_setup():
    # size(1280,720)                                     #  size delen door 2
    background(0)
def gmp_draw():
    background('#4B0082')
    #Hervatten
    fill('#8A2BE2')
    if 540 < mouseX <740  and 250 < mouseY <300: 
        fill('#5f079a')
        cursor(HAND)
    else:
        cursor(ARROW)
    rect(540, 250, 200, 50, 7)                      # size delen door 2
    fill('#FFFFFF')
    textSize(31)
    text('Hervatten', 565, 257, 150, 50)    # size delen door 2  
        
    #Instellingen 
    fill('#8A2BE2')
    if 540 < mouseX <740  and 325 < mouseY <375: 
        fill('#5f079a')
        cursor(HAND)
    else:
        cursor(ARROW)
    rect(540, 325, 200, 50, 7)                     # size delen door 2
    fill('#FFFFFF')
    text('Instellingen', 555, 332, 200, 50)      # size delen door 2
    textSize(30)                                 # deze size pakt zomaar 'stoppen'
        
        #Stoppen
    fill('#8A2BE2')
    if 540 < mouseX <740  and 400 < mouseY <450: 
        fill('#5f079a')
        cursor(HAND)
    else:
        cursor(ARROW)
    rect(540, 400, 200, 50, 7)                     # size delen door 2
    fill('#FFFFFF')
    text('Stoppen', 577, 407, 200, 50)
    textSize(27) 
