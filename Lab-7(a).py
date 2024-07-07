import math
class shape:
    def __init__(self):
        self.name=" "
        self.area=0
    def show_area(self):
        print("The area of ",self.name+"is",self.area)
class circle(shape):
    def __init__(self,radius):
        self.name="Circle"
        self.area=0
        self.radius=radius
    def calc_area(self):
        self.area=math.pi*self.radius*self.radius
class rectangle(shape):
    def __init__(self,length,breadth):
        self.name="Rectangle"
        self.area=0
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        self.area=self.length*self.breadth
class traingle(shape):
    def __init__(self,base,height):
        self.name="Triangle"
        self.area=0
        self.base=base
        self.height=height
    def calc_area(self):
        self.area=self.base*self.height/2
c1=circle(3)
c1.calc_area()
c1.show_area()
r1=rectangle(3,2)
r1.calc_area()
r1.show_area()
t=traingle(3,2)
t.calc_area()
t.show_area()