class Rational:

    def __init__(self,num,denom):
        self.__num = num
        self.__denom = denom

    def getNum(self):
        return self.__num

    def getDenom(self):
        return self.__denom

    def __add__(self,obj): #r3
        return (self.__num + obj.__num,self.__denom + obj.__denom)

    def __sub__(self,obj): #r4
        return (self.__num - obj.__num ,self.__denom - obj.__denom)

    def __div__(self,obj): #r5
        return ((self.__num /obj.__num),self.__denom / obj.__denom)




if __name__== '__main__':

    r1 = Rational(13,7)
    r2 = Rational(5,6)
    r3 = r1 + r2
    r4 = r1 - r2
    r5 = r1 / r2
    print(r3)
    print(r4)
    print(r5)
