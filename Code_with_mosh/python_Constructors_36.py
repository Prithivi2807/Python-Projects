class Point:
    def __init__(self, x, y): # initialize the method
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point = Point(10, 20) # Object
# point.x = 10
print(point.x)
print(point.y)
point.x = 11
print(point.x ) 

# Person have name- attribute, talk()