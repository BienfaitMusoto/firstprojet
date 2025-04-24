
class Rectangle:
    def __init__(self,longeur,largeur, couleur="red"):
        self.longeur = longeur
        self.largeur = largeur
        self.couleur = couleur


    def calculer_surface(self):

        return self.longeur * self.largeur

rectangle = Rectangle(5,3)
print(rectangle.longeur)
print(rectangle.largeur)
print(rectangle.couleur)
print(rectangle.calculer_surface())


 