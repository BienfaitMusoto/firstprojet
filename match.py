fruit = "pomme"
match fruit:
    cas "pommer":
      print(" j'aime les pommes!")
    cas "banane":
       print("je n'aime pas les bananes")
    cas "orange":
       print("Les oranges sont bonnes pour la sante")
    cas _:
       print(" je ne connais pas ce fruit")