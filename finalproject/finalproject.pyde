import os, time
path = os.getcwd()

class Game:
    def __init__(self):
        self.w = 1029
        self.h = 600
        self.ground = 600-100
        self.ceiling = 600-550
        self.state = "start"
        self.lvls=[]
        self.qs=[]
        self.answers=[]
        self.bgImg = loadImage(path+"/images/background.png") 
        self.lvlNum = 0
        self.gameOverImg = loadImage(path+"/images/ending.gif")
        self.winImg = loadImage(path+"/images/congrats.png")
        #self.winImg2 = loadImage(path+"/images/congratss.png")
        self.helpingImg = loadImage(path+"/images/pizza.png")
        self.openingImg = loadImage(path+"/images/opening.png")

        
    def createGame(self):
        for i in range(10): 
            self.lvls.append(loadImage(path+'/images/level'+str(i+1)+'.png'))
            self.qs.append(loadImage(path+'/images/question'+str(i+1)+'.png'))
            for j in range(4):
                self.answers.append(loadImage(path+'/images/q'+str(i+1)+'a'+str(j+1)+'.png'))

    def display(self):
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
    if g.state == "start":
        background(234,29,44)
        image(g.openingImg,250,0)
        textSize(20)
        text("Press anywhere",10,g.h-20)
        #time.sleep(2)
        #g.state="menu"  
              
    elif g.state=='menu':
        background(234,29,44)
        if g.state == 'menu' and g.w//2-80 < mouseX < g.w//2+80 and g.h//2-30 < mouseY < g.h//2+10:
            fill(0)
        else:
            fill(255)
        textSize(32)
        text("Play Game",g.w//2-80,g.h//2)
        noFill()
        stroke(234,29,44)
        rect(g.w//2-80, g.h//2-30,160,40)
    
    elif g.state == 'play':
        image(g.bgImg,g.w,g.h)
        g.display()
        
    elif g.state == "game over":
        background(255,255,255)
        image(g.gameOverImg,300,100)
        #g.state = 'menu'
        #g.display()
        
    elif g.state == "win":
        background(255,255,255)
        image(g.winImg,300,180)
        #image(g.winImg2,200,400)
        
    elif g.state == "play again?":
        background(234,29,44)
        textSize(50)
        text("Play again?",g.w//2-110,g.h//2-100)
        if  g.w//2+110 < mouseX < g.w//2+110+70 and g.h//2+20 < mouseY < g.h//2+20+40:
            fill(0,0,255)
        elif g.w//2-130 < mouseX < g.w//2-130+80 and g.h//2+20 < mouseY < g.h//2+20+40:
            fill(0,255,0)
        else:
            fill(255)
            
        textSize(30)
        
        text("No.",g.w//2+120,g.h//2+50)
        noFill()
        stroke(234,29,44)
        rect(g.w//2+110,g.h//2+20,70,40)
        
        text("Yes!",g.w//2-120,g.h//2+50)        
        noFill()
        stroke(234,29,44)
        
        rect(g.w//2-130,g.h//2+20,80,40)
                   
    
        
def mouseClicked():
    if g.state == "start":
        if mouseClicked:
            g.state = 'menu'
    elif g.state == 'menu' and g.w//2-80 < mouseX < g.w//2+80 and g.h//2-30 < mouseY < g.h//2+10:
        g.state='play'
    elif g.state == 'play':
        if g.lvlNum==0:
            if g.w//5.5<=mouseX<=g.w//5.5+300 and g.ground//1.2<=mouseY<=g.ground//1.2+150:
                #print("works")
                time.sleep(0.2)
                g.lvlNum += 1
            else:
                g.state ="game over"
        elif g.lvlNum==1:
            if g.w//5.5<=mouseX<=g.w//5.5+50+144 and g.ceiling*3<=mouseY<=g.ceiling*3+135:
                g.lvlNum += 1
                #print("works")
            else:
                g.state ="game over"
        elif g.lvlNum==2:
            if g.w//5.5<=mouseX<=g.w//5.5+50+104 and g.ceiling*3<=mouseY<=g.ceiling*3+106:
                g.lvlNum += 1
                #print("works")
            else:
                g.state ="game over"
        elif g.lvlNum==3:
            if (g.w//5.5<=mouseX<=g.w//5.5+187 and g.ground//1.2-50<=mouseY<=g.ground//1.2-50+187) or (g.w//5.7*3+100<=mouseX<=g.w//5.7*3+100+200 and g.ceiling*3<=mouseY<=g.ceiling*3+178):
                #print("works")
                g.lvlNum += 1
            else:
                g.state ="game over"
        elif g.lvlNum==4: 
            if g.w//5.7*3+100<=mouseX<=g.w//5.7*3+100+145 and g.ground//1.2-50<=mouseY<=g.ground//1.2-50+134:
                g.state = "win"
                g.lvlNum = 0
            else:
                g.state ="game over"    
    elif g.state == "game over":
        if mouseClicked:
            g.state = 'play again?'
    elif g.state == "win":
        if mouseClicked:
            g.state = 'play again?'
    elif g.state == "play again?":
        if g.w//2+110 < mouseX < g.w//2+110+70 and g.h//2+20 < mouseY < g.h//2+20+40:
            exit()
        elif g.w//2-130 < mouseX < g.w//2-130+80 and g.h//2+20 < mouseY < g.h//2+20+40:
            g.lvlNum = 0
            g.state = "play"
          
