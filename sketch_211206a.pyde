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

def setup():
    size (1280, 720) #Verander voor final edition
    background('#4B0082')

def draw():

    # Rechthoek: Voer namen in!
    fill('#8A2BE2')
    noStroke()
    
    rect(400, 100, 500, 80, 12, 12, 12, 12)
    fill('#ffffff')
    textSize(39)
    text('Voer namen in!', 500, 150)
    

    
    # Rechthoekjes met Speler textboxes
    global notClicked, notClicked2, notClicked3, notClicked4
    def createRect(arg):
        if arg:
            fill('#8A2BE2')
        else: 
            fill('#5f079a')
            
    createRect(notClicked)
    rect(300, 280, 120, 60, 10, 10, 10, 10)  
    
    createRect(notClicked2)   
    rect(500, 280, 120, 60, 10, 10, 10, 10) 

    createRect(notClicked3)
    rect(700, 280, 120, 60, 10, 10, 10, 10)
    
    createRect(notClicked4)
    rect(900, 280, 120, 60, 10, 10, 10, 10)

    global name1, name2, name3, name4
    # 'String Speler 1 t/m 4'
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
    fill('#8A2BE2')
    rondje = ellipse(570, 520, 50, 50)
    rondje2 = ellipse(750, 520, 50, 50)
    fill('#ffffff')    
    plusje = rect(550, 515, 40, 10, 12, 12, 12, 12), rect(745, 500, 10, 40, 12, 12, 12, 12)
    
    minetje = rect(730, 515, 40, 10, 12, 12, 12, 12)
    fill ('#8A2BE2')
    if plusincr == 0:
        fill('#4B0082')
        rect(500, 380, 120, 60, 10, 10, 10, 10)
        rect(700, 380, 120, 60, 10, 10, 10, 10)
        
    elif plusincr == 1:
        createRect(notClicked5)
        rect(500, 380, 120, 60, 10, 10, 10, 10)
        fill('#4B0082')
        rect(700, 380, 120, 60, 10, 10, 10, 10)
    
    elif plusincr > 1:
        createRect(notClicked5)
        rect(500, 380, 120, 60, 10, 10, 10, 10)
        
        createRect(notClicked6)
        rect(700, 380, 120, 60, 10, 10, 10, 10)
        
    fill('#ffffff')    
    if plusincr == 1:
        text (name5, 500 + 20, 420)
    elif plusincr > 1:
        text (name5, 500 + 20, 420)
        text (name6, 700 + 20, 420)
    
    #Back, en start knoppen
    textSize(30)
    text("Back", 130, 600) 
    text("Start", 1100, 600)

    
def mousePressed():
    global notClicked, notClicked2, notClicked3, notClicked4, notClicked5, notClicked6
    global name1, name2, name3, name4, name5, name6
    
    if 300 < mouseX < 420 and 280 < mouseY < 340: # speler 1                                         
        notClicked = not notClicked
    else:
        notClicked  = True 
    
    if 300 + 200 < mouseX < 620  and 280 < mouseY < 340 : # speler 2                                       
        notClicked2 = not notClicked2
    else:
        notClicked2 = True
        
    if 300 + 400 < mouseX < 820  and 280 < mouseY < 340 : # speler 3                                          
        notClicked3 = not notClicked3
    else:
        notClicked3 = True
        
    if 300 + 600 < mouseX < 1020  and 280 < mouseY < 340: # speler 4                                              
        notClicked4 = not notClicked3
    else:
        notClicked4 = True
    
    if 300 + 200 < mouseX < 620 and 380 < mouseY < 440:
        notClicked5 = not notClicked5
    else: 
        notClicked5 = True
    
    if 300 + 400 < mouseX < 820 and 380 < mouseY < 440:
        notClicked6 = not notClicked6
    else: 
        notClicked6 = True 

    #Plus en minnetje
    global plusincr
    
    if 700 < mouseX < 800 and  470 < mouseY <570:
        plusincr += 1
        if plusincr > 2:
            plusincr = 2 

    if 520 < mouseX < 620 and  470 < mouseY <570:
        plusincr -= 1
        if plusincr < 0:
            plusincr = 0
            
   #if 120 < mouseX < 220 and 600 < mouseY < 620: 
        
    #if 1100 < mouseX < 1200 and 600 < mouseY < 620:
    
   
#Functionaliteit: Invoeren van namen
def keyPressed():
    global notClicked
    global name1, name2, name3, name4 , name5, name6
    global chars

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
