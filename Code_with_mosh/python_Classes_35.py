class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# object is an instance of the class, class is simply defined blueprint or the template 
# for creating objects are the actual instances based on that blue print.

# Objects are the actual instances based on that blue print. So we can have tens 
# of hundreds of points on the screen, these are the objects or the instances.

point1 = Point()
point1.x = 10 #instances
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point() 
point2.x = 1 # x coordinate of the point2 is 1
print(point2.x)