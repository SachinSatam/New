class Circle():
    def __init__(self,radius):
        self.radius=radius
    def Area(self,radius):
        area1=3.14*radius*radius
        print("Area of circle is:",area1)
    def Perimeter(self,radius):
        area2=2*3.14*radius
        print("Perimeter of circle is:",area2)
obj1=Circle(3)
obj1.Area(3)
obj1.Perimeter(3)
