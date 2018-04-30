class Game:
    def __init__(self):
        self.w = 1029
        self.h = 600
        self.ground = 600-100
        self.ceiling = 600 - 500
        self.state = "menu"
        

img = ""
def setup():
    global img
    img = loadImage("/Users/khadijahiqbal/Desktop/Final-Project/images/background.png")
    size(1029,600)
    background(0)
def draw():
    image(img,0,0)
    
