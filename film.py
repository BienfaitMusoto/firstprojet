class Film:
    def __init__(self,name):
        self.name=name
    def watch(self):
        print("bon visionnage")
class Filmcassete(Film):
    pass

film =Film("2001:l'odyssee de l'espace")
film_cassette = Filmcassete("blader Runner")

film.name
film.watch()

film_cassette.name
film_cassette.watch()

# debut de heritage

