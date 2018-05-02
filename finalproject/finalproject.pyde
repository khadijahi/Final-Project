import os
##So I realized the lines for ceiling and ground are not needed as we are 
#not worried about gravity in this but merely just where the pictures will be placed
#so just use the self.ceiling and self.ground as a basis on where it should and could
#be placed

class Game:
    def __init__(self):
        self.w = 1029
        self.h = 600
        self.ground = 600-100
        self.ceiling = 600-500
        self.state = "menu"

    def display(self):
        self.state == "play"

g = Game()
def setup():
    size(g.w,g.h)
    background(0)
    global bgImg
    bgImg = loadImage("background.png") 

def draw():
    image(bgImg, 0,0)
    g.display()
    if g.state == "start":
        background(0)
        fill(255)
        textSize(50)
        text("Play", 450,300)
    elif g.state == "play":
        background(0)
        background(100)
        g.display()
