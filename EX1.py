class Cercle:

    def __init__(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def __add__(self,obj):
        return Cercle(self.__radius + obj.__radius)

    def __lt__(self,obj):
        return self.__radius < obj.__radius





if __name__== '__main__':
   c1 = Cercle(2)
   c2 = Cercle(3)
   c3 = c1 + c2
   c4 = c1 < c2
   c5 = c2 > c3
   print(str(c3.getRadius()))
   print(c4)
   print(c5)


