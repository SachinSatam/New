class Data():
    def Read_data(self,length,breadth,side):
       self.length=length
       self.breadth=breadth
       self.side=side
     
class Area(Data):
    def Rect(self,length,breadth):
        area1=length*breadth
        print("Area of rectangle is:",area1)
    def Sqr(self,side):
        self.area2=side*side
        print("Area of square is :",self.area2) 
class Test(Area):
    def testfun(self,val=5):
        new=val+self.area2
        print("Test value is:",new)
obj1=Area()
obj1=Test()
obj1.Rect(4,5)
obj1.Sqr(5)
obj1.testfun()