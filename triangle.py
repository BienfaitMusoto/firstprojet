from abc import ABC

class shap(ABC):
    def area(self):
        return 0
class square(shap):
    def __init__ (self,length):
        self.length= length
    def area(self):
        return self.length *self.length
#square = square(4)
#square_area =square_area()
#print(square_area)

class Triange(square):
   def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur
   def area(self):
        return (self.hauteur * self.base)/2

triange =Triange(base =7,hauteur =5)
triange2 =Triange(base =12,hauteur =43)
surface = triange.area()
surface2 =triange2.area()
print(surface)
print(surface2)
    
      