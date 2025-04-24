from abc import abc
class shap(abc):
    def area(self):
        return 0
class square(shap):
    def __init__(self,length):
        self.length= length
    def area(self):
        return self.length *self.length
square = square(4)
square_area =square_area()
print(square_area)