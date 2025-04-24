class Animal:
    def crier(self):
        print("un cri d'animal")

class chien(Animal):
    def crier(self):
        print("woauf! woauf!")
class chat(Animal):
    def crier(self):
        print("Miaou!")
class inconnu(Animal):
    def crier(self):
        return super().crier()
animal = Animal()
cri_animal = animal.crier()

chien = chien()
cri_chien = chien.crier()

chat = chat()
cri_chat = chat.crier()

inconnu = inconnu()
cri_animal_inconnu = inconnu.crier()