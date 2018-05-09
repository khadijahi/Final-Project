add_library('sound')
import os, time
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
        self.lvlNum = 0
        self.gameOverImg = loadImage(path+"/images/ending.gif")
        self.nextLvlImg = loadImage(path+"/images/ending4.jpg")
        self.gameOver = 0
        self.helpingImg = loadImage(path+"/images/pizza.png")
        self.openingImg = loadImage(path+"/images/ooening.png")

        
    def createGame(self):
        for i in range(10): 
            self.lvls.append(loadImage(path+'/images/level'+str(i+1)+'.png'))
            self.qs.append(loadImage(path+'/images/question'+str(i+1)+'.png'))
            for j in range(4):
                self.answers.append(loadImage(path+'/images/q'+str(i+1)+'a'+str(j+1)+'.png'))

    def display(self):
        #if self.gameOver == 1:
         #   image(g.bgImg, 0,0)
          #  image(self.gameOverImg,200,200)
            #time.sleep(5)
            #g.state = 'menu'
        self.level()

        
    def level(self):
        image(self.lvls[self.lvlNum],0,0,100,100)
        if self.lvlNum == 0:
            image(self.qs[self.lvlNum],self.w//2-(216//2),self.ceiling)
            image(self.answers[self.lvlNum*4+0],self.w//5.5,self.ceiling*3)
            image(self.answers[self.lvlNum*4+1],self.w//5.5,self.ground//1.2)
            image(self.answers[self.lvlNum*4+2],self.w//5.7*3,self.ceiling*3)
            image(self.answers[self.lvlNum*4+3],self.w//5.7*3,self.ground//1.2)
        if self.lvlNum == 1:
            image(self.qs[self.lvlNum],self.w//2-(250//2),self.ceiling)
            image(self.answers[self.lvlNum*4+0],self.w//5.5+50,self.ceiling*3)
            image(self.answers[self.lvlNum*4+1],self.w//5.5+50,self.ground//1.2)
            image(self.answers[self.lvlNum*4+2],self.w//5.7*3+150,self.ceiling*3)
            image(self.answers[self.lvlNum*4+3],self.w//5.7*3+150,self.ground//1.2)
        if self.lvlNum == 2:
            image(self.qs[self.lvlNum],self.w//2-(330//2),self.ceiling)
            image(self.helpingImg,375,190)
            image(self.answers[self.lvlNum*4+0],self.w//5.5,self.ceiling*3)
            image(self.answers[self.lvlNum*4+1],self.w//5.5,self.ground//1.2)
            image(self.answers[self.lvlNum*4+2],self.w//5.7*3+200,self.ceiling*3)
            image(self.answers[self.lvlNum*4+3],self.w//5.7*3+200,self.ground//1.2)
        if self.lvlNum == 3:
            image(self.qs[self.lvlNum],self.w//2-(180//2),self.ceiling)
            image(self.answers[self.lvlNum*4+0],self.w//5.5,self.ceiling*3)
            image(self.answers[self.lvlNum*4+1],self.w//5.5,self.ground//1.2-50)
            image(self.answers[self.lvlNum*4+2],self.w//5.7*3+100,self.ceiling*3)
            image(self.answers[self.lvlNum*4+3],self.w//5.7*3+100,self.ground//1.2-50)
        if self.lvlNum == 4:
            image(self.qs[self.lvlNum],self.w//2-312,self.ceiling)
            image(self.answers[self.lvlNum*4+0],self.w//5.5+60,self.ceiling*3)
            image(self.answers[self.lvlNum*4+1],self.w//5.5+60,self.ground//1.2-50)
            image(self.answers[self.lvlNum*4+2],self.w//5.7*3+100,self.ceiling*3)
            image(self.answers[self.lvlNum*4+3],self.w//5.7*3+100,self.ground//1.2-50)
    
        
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
    if g.state != 'menu'and g.lvlNum==0 and g.w//5.5<=mouseX<=g.w//5.5+300 and g.ground//1.2<=mouseY<=g.ground//1.2+150:
        #print("works")
        time.sleep(0.2)
        g.lvlNum += 1
    elif g.state != 'menu'and g.lvlNum==1 and g.w//5.5<=mouseX<=g.w//5.5+50+144 and g.ceiling*3<=mouseY<=g.ceiling*3+135:
        g.lvlNum += 1
        #print("works")
    elif g.state != 'menu'and g.lvlNum==2 and g.w//5.5<=mouseX<=g.w//5.5+50+104 and g.ceiling*3<=mouseY<=g.ceiling*3+106:
        g.lvlNum += 1
        #print("works")
    elif g.state != 'menu'and g.lvlNum==3 and ((g.w//5.5<=mouseX<=g.w//5.5+187 and g.ground//1.2-50<=mouseY<=g.ground//1.2-50+187) or (g.w//5.7*3+100<=mouseX<=g.w//5.7*3+100+200 and g.ceiling*3<=mouseY<=g.ceiling*3+178)):
        #print("works")
        g.lvlNum += 1
    elif g.state != 'menu'and g.lvlNum==4 and g.w//5.7*3+100<=mouseX<=g.w//5.7*3+100+145 and g.ground//1.2-50<=mouseY<=g.ground//1.2-50+134:
        g.state = "menu"
        g.lvlNum = 0

        
