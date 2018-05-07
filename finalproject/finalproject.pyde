add_library('sound')
import os
path = os.getcwd()

class Game:
    def __init__(self):
        self.w = 1029
        self.h = 600
        self.ground = 600-100
        self.ceiling = 600-550
        self.state = "menu"
        self.lvls=[]
        self.qs=[]
        self.answers=[]
        self.bgImg = loadImage(path+"/images/background.png") 
        self.nextLevel = False
        
    def createGame(self):
        for i in range(10): 
            self.lvls.append(loadImage(path+'/images/level'+str(i+1)+'.png'))
            self.qs.append(loadImage(path+'/images/question'+str(i+1)+'.png'))
            for j in range(4):
                self.answers.append(loadImage(path+'/images/q'+str(i+1)+'a'+str(j+1)+'.png'))

    def display(self):
        self.state == "play"
        while self.nextLevel == False:
            image(self.qs[0],self.w//2-(216//2),self.ceiling)
            image(self.lvls[0],0,0,100,100)
            image(self.answers[0],self.w//5.5,self.ceiling*3)
            image(self.answers[1],self.w//5.5,self.ground//1.2)
            image(self.answers[2],self.w//5.7*3,self.ceiling*3)
            image(self.answers[3],self.w//5.7*3,self.ground//1.2)
<<<<<<< HEAD
        else:
            pass
=======
>>>>>>> ccf7342785ad2df94decc88db02c365f9040a68d
    
        
g = Game()
def setup():
    size(g.w,g.h)
    background(0)
    g.createGame()

def draw():
    image(g.bgImg, 0,0)
    if g.state=='menu':
        background(0)
        if g.state == 'menu' and g.w//2-80 < mouseX < g.w//2+80 and g.h//2-30 < mouseY < g.h//2+10:
            fill(219,112,147)
        else:
            fill(255)
        textSize(32)
        text("Play Game",g.w//2-80,g.h//2)
        noFill()
        stroke(0)
        rect(g.w//2-80, g.h//2-30,160,40)
    elif g.state == 'play':
        image(g.bgImg,g.w,g.h)
        g.display()
        
def mouseClicked():
    if g.state == 'menu' and g.w//2-80 < mouseX < g.w//2+80 and g.h//2-30 < mouseY < g.h//2+10:
        g.state='play'
    if g.w//5.5<=mouseX<=g.w//5.5+300 and g.ground//1.2<=mouseY<=g.ground//1.2+150:
        g.nextLevel = True
<<<<<<< HEAD
=======
        
>>>>>>> ccf7342785ad2df94decc88db02c365f9040a68d
