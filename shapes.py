from cmath import pi

class Circle:
   
    def __init__(self,r):
        self.radius=r
    def area(self):
        a=pi*(self.radius**2)
        return a
    def circumference(self):
        p=2*pi*self.radius
        return p
class Square:
    def __init__(self,a):
        self.side=a
    def area(self):
        a=self.side**2
        return a
    def perimeter(self):
        p=4*self.side
        return p
    
class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.length=l
    def area(self):
        a=self.width*self.length
        return a
    def perimeter(self):
        p=2*(self.width + self.length)
        return p

class Sphere:

    def __init__(self,r):
        self.radius=r
    def surface_area(self):
        a= 4* pi*(self.radius**2)
        return a
    def volume(self):
        v=(4/3)*(pi*(self.radius**3))
        return v
