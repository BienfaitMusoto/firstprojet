class stagiaire:
    def __init__(self,numi,age,nom,premom,note1,note2):
        self.numinscription = numi
        self.__age = age
        self.__nom = nom
        self.__prenom = Prenom
        self.__note1 =  note1
        self.__note2 = note2
    def calculMoyenne(self):
        moy =(self.__note1 + self.__note2)/2
        print("la moyenne",moy) 
    def getnumi(self):
        return self.__numi
    def setnumi(self):
        self.__numi =numi
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age = age
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom = nom
    def getprenom(self):
        return self.__prenom
    def setprenom(self,prenom):
        self.__prenom = prenom
    def getnote1(self):
        return self.__note1
    def setnote1(self,note1):
        self.__note1 = note1
    def getnote2(self):
        return self__note2
    def setnote2(self,note2):
        self.__note2 = note2