add_library('sound')
import os
path = os.getcwd()

class Game:
    def __init__(self):
        self.w = 1029
        self.h = 600
        self.ground = 600-100
        self.ceiling = 600-500
        self.state = "menu"
        self.qs=[]
        self.answers=[]
        self.bgImg = loadImage(path+"/images/background.png") 
        
def createGame(self):
    for i in range(10): 
        self.qs.append(loadImage(path+'/images/question'+str(i+1)+'.png'))
        for j in range(4):
            self.answers.append(loadImage(path+'/images/q'+str(i+1)+'a'+str(j+1)+'.png'))
 #so basically in these for loops we would have the questions, 
 #10 of them to begin with, and 4 possible answers for each
 #also, i renamed the pictures so it fits the loadImage thing 
 #so we don't have to do it manually for each level

    def display(self):
        self.state == "play"

g = Game()
def setup():
    size(g.w,g.h)
    background(0)
    g.createGame

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
