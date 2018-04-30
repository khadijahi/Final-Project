img = ""
def setup():
    global img
    img = loadImage("/Users/khadijahiqbal/Desktop/finalproject/images/background.png")
    size(1031,576)
    background(0)
def draw():
    image(img,0,0)
    
