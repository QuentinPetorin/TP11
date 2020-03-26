class Duree :

    def __init__(self,heure,minute,seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde

    def getH(self):
        return self.__heure

    def getM(self):
        return self.__minute

    def getS(self):
        return self.__seconde

    def aff(self):
        return self.__heure,"H",self.__minute,"m",self.__seconde,"s"

    def __add__(self,obj):

        temp = self.__heure + obj.__heure,self.__minute + obj.__minute,self.__seconde + obj.__seconde
        Heure = temp[0]
        Minute = temp[1]
        Seconde = temp[2]


        while Seconde >= 60:
            Seconde -= 60
            Minute += 1


        while Minute >= 60 :
            Minute -= 60
            Heure += 1

        return Heure,Minute,Seconde

if __name__ == '__main__':
    d1 = Duree(1,22,34)
    d2 = Duree(3,53,29)
    d3 = d1 + d2

    print(d3)




