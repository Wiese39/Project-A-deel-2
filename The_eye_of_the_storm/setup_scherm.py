notClicked = True
notClicked2 = True
notClicked3 = True
notClicked4 = True
notClicked5 = True
notClicked6 = True

plusincr = 0

name1 = 'Speler 1'
name2 = 'Speler 2'
name3 = 'Speler 3'
name4 = 'Speler 4'
name5 = 'Speler 5'
name6 = 'Speler 6'

chars = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_"}

def setup_draw():
    global notClicked, notClicked2, notClicked3, notClicked4
    
    background('#4B0082')
    # Rechthoek: Voer namen in!
    fill('#571692')
    noStroke()
    rect(400, 100, 500, 80, 7)
    fill('#ffffff')
    textSize(39)
    text('Voer namen in!', 500, 150)
    
    # Rechthoekjes met Speler textboxes
    def createRect(arg):
        if arg:
            fill('#8A2BE2')
        else: 
            fill('#5f079a')
 
    def hoverMouse(x, y=280, xi= 120, yi=60):
        if x < mouseX < x + xi and y < mouseY < y + yi:
            fill('#5f079a')
            cursor(HAND)
        else: 
            cursor(ARROW)
    
    def hoverMouseWhite(x, y=280, xi= 120, yi=60):
        if x < mouseX < x + xi and y < mouseY < y + yi:
            fill('#d6d5d7')

                            
    def hoverMouse2(x, y=280, xi= 120, yi=60):
        if x < mouseX < x + xi and y < mouseY < y + yi:
            fill('#55068a')
            cursor(HAND)
        else: 
            cursor(ARROW)
             
               
    def createRect2(arg, x, y=280):
        if arg:
            fill('#8A2BE2')
        else: 
            fill('#5f079a')
        hoverMouse(x, y)
    
    def visual():
        global plusincr
        if plusincr == 0:
            fill('#8A2BE2')
        elif plusincr == 1:
            fill('#8A2BE2')
        else:
            fill('#5f079a')
    def visual2():
        if plusincr == 0:
            fill('#5f079a')
        elif plusincr == 1:
            fill('#8A2BE2')
        else:
            fill('#8A2BE2')
    
    createRect2(notClicked, 300)
    rect(300, 280, 120, 60, 7)  
    
    createRect2(notClicked2, 500)   
    rect(500, 280, 120, 60, 7) 

    createRect2(notClicked3, 700)
    rect(700, 280, 120, 60, 7)
    
    createRect2(notClicked4, 900)
    rect(900, 280, 120, 60, 7)
    
    # 'String Spel er 1 t/m 4'
    fill('#ffffff')
    textSize(20)    
    text(name1, 300 + 20, 320)
    text(name2, 500 + 20, 320)
    text(name3, 700 + 20, 320)
    text(name4, 900 + 20, 320)
    if plusincr == 1:
        text (name5, 500 + 20, 420)
    elif plusincr > 1:
        text (name6, 700 + 20, 420)
    
    # rondje met plusje om meer spelers toe tevoegen
    visual()
    hoverMouse(700, 470, 100, 100)
    rondje2 = ellipse(750, 520, 50, 50)
    visual2()
    hoverMouse(520, 470, 100, 100)
    rondje = ellipse(570, 520, 50, 50)
    fill('#ffffff')
    hoverMouseWhite(700, 470, 100, 100)  
    plusje = rect(730, 515, 40, 10, 12), rect(745, 500, 10, 40, 12)
    fill('#ffffff')
    hoverMouseWhite(520, 470, 100, 100)
    minetje = rect(550, 515, 40, 10, 12)
    fill ('#8A2BE2')
    if plusincr == 0:
        fill('#4B0082')
        rect(500, 380, 120, 60, 7)
        rect(700, 380, 120, 60, 7)
        
    elif plusincr == 1:
        createRect2(notClicked5,500, 380)
        rect(500, 380, 120, 60, 7)
        fill('#4B0082')
        rect(700, 380, 120, 60, 7)
        fill('#ffffff')
        text (name5, 500 + 20, 420)
        
    elif plusincr > 1:
        createRect2(notClicked5,500 , 380)
        rect(500, 380, 120, 60, 7)
        createRect2(notClicked6, 700, 380)
        rect(700, 380, 120, 60, 7)
        fill('#ffffff')
        text (name5, 500 + 20, 420)
        text (name6, 700 + 20, 420)
        
    #Backknop, en startknop
    fill('#5f079a')
    hoverMouse2(120, 565, 90, 50)
    rect(120,565,90,50,7)
    fill('#5f079a')
    hoverMouse2(1090, 565, 90, 50)
    rect(120 + 970, 565, 90 ,50,7)
    fill('#ffffff')
    textSize(30)
    text("Back", 130, 600) 
    text("Start", 1100, 600)
    #Pauzeknop
    fill('#5f079a')
    hoverMouse2(10, 10, 50, 50)
    rect(10,10,50,50,7)
    fill('#ffffff')
    hoverMouseWhite(10,10, 50, 50)
    icoontje = rect(15, 23, 40, 5, 7), rect(15, 33, 40, 5, 7), rect(15, 43, 40, 5, 7)
    

def setup_mousePressed():
    global notClicked, notClicked2, notClicked3, notClicked4, notClicked5, notClicked6
    global plusincr
    
    if 300 < mouseX < 420 and 280 < mouseY < 340: # speler 1                                         
        notClicked = not notClicked
    else:
        notClicked  = True

    if 300 + 200 < mouseX < 620  and 280 < mouseY < 340 : # speler 2                                       
        notClicked2 = not notClicked2
    else:
        notClicked2 = True
        
    if 300 + 400 < mouseX < 820  and 280 < mouseY < 340 : #  speler 3                                          
        notClicked3 = not notClicked3
    else:
        notClicked3 = True
        
    if 300 + 600 < mouseX < 1020  and 280 < mouseY < 340: # speler 4                                              
        notClicked4 = not notClicked3
    else:
        notClicked4 = True
    
    if 300 + 200 < mouseX < 620 and 380 < mouseY < 440: # speler 5
        notClicked5 = not notClicked5
    else: 
        notClicked5 = True
    
    if 300 + 400 < mouseX < 820 and 380 < mouseY < 440: # speler 6
        notClicked6 = not notClicked6
    else: 
        notClicked6 = True 

    #Plus en minnetje
    if 700 < mouseX < 800 and  470 < mouseY <570:
        plusincr += 1
        if plusincr > 2:
            plusincr = 2 

    if 520 < mouseX < 620 and  470 < mouseY <570:
        plusincr -= 1
        if plusincr < 0:
            plusincr = 0



#Functionaliteit: Invoeren van namen
def setup_keyPressed():
    global name1, name2, name3, name4 , name5, name6, chars

    if notClicked == False:
        if len(name1) < 8:   
            if key in chars:
                name1 += key   
            if key == ' ':
                name1 += '_'  
        if key == BACKSPACE:
            name1 = name1[:-1]  
        if key == DELETE:
            name1 = ''       
        if key == ENTER or key == RETURN:
            print(name1)      
            
    if notClicked2 == False:
        if len(name2) < 8:   
            if key in chars:
                name2 += key   
            if key == ' ':
                name2 += '_'  
        if key == BACKSPACE:
            name2 = name2[:-1]  
        if key == DELETE:
            name2 = ''       
        if key == ENTER or key == RETURN:
            print(name2)      
            
    if notClicked3 == False:
        if len(name3) < 8:   
            if key in chars:
                name3 += key  
            if key == ' ':
                name3 += '_'  
        if key == BACKSPACE:
            name3 = name3[:-1]  
        if key == DELETE:
            name3 = ''       
        if key == ENTER or key == RETURN:
            print(name3)     
            
    if notClicked4 == False:
        if len(name4) < 8:   
            if key in chars:
                name4 += key  
            if key == ' ':
                name4 += '_'
        if key == BACKSPACE:
            name4 = name4[:-1]
        if key == DELETE:
            name4 = ''        
        if key == ENTER or key == RETURN:
            print(name4)
            
    if plusincr == 1:    
        if notClicked5 == False:
            if len(name5) < 8:   
                if key in chars:
                    name5 += key  
                if key == ' ':
                    name5 += '_'
            if key == BACKSPACE:
                name5 = name5[:-1]
            if key == DELETE:
                name5 = ''        
            if key == ENTER or key == RETURN:
                print(name5) 
    if plusincr > 1:    
        if notClicked5 == False:
            if len(name5) < 8:   
                if key in chars:
                    name5 += key  
                if key == ' ':
                    name5 += '_'
            if key == BACKSPACE:
                name5 = name5[:-1]
            if key == DELETE:
                name5 = ''        
            if key == ENTER or key == RETURN:
                print(name5) 
                
        if notClicked6 == False:
            if len(name6) < 8:   
                if key in chars:
                    name6 += key  
                if key == ' ':
                    name6 += '_'
            if key == BACKSPACE:
                name6 = name6[:-1]
            if key == DELETE:
                name6 = ''        
            if key == ENTER or key == RETURN:
                print(name6)
               
#Backknop, PauzeKnop (Startknop)
# def setup_mouseClicked():
#     if 120 < mouseX < 210 and  565 < mouseY < 615:
#         print("Start Menu, geopend")
#         game_state = 0   
#     if 120 < mouseX < 210 and  300 < mouseY < 350:
#         print("Pauzescherm, geopend")
#         game_state = 3
