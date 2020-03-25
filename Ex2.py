class Complex:

    def __init__(self,real,im):
        self.__real = real
        self.__im = im

    def getReal(self):
        return self.__real

    def getIm(self):
        return self.__im

    def __add__(self,obj): #c3
        return Complex(self.__real + obj.__real,self.__im + obj.__im)

    def __sub__(self,obj): #c4
        return Complex(self.__real - obj.__real,self.__im - obj.__im)

    def __mul__(self,obj): #c5
        return(self.__real * obj.__real, self.__im * obj.__im)

    def __div__(self,obj): #c6
        return (self.__real / obj.__real, self.__im / obj.__im)

    def __abs__(self,obj): #c7
        return (self.__real % obj.__real, self.__im % obj.__im)

    def __eq__(self,obj): #c8
        return (self.__real == obj.__real, self.__im == obj.__im)

    def __ne__(self,obj): #c9
        return (self.__real != obj.__real, self.__im != obj.__im)



if __name__== '__main__':

   c1 = Complex(1,2)
   c2 = Complex(2,3)
   c3 = c1 + c2
   c4 = c1 - c2
   c5 = c1 * c2
   c6 = c1 / c2
   c7 = c1 == c2
   c8 = c1 != c2

   print("c3("+str(c3.getReal())+","+str(c3.getIm())+")")
   print("c4("+str(c4.getReal())+","+str(c4.getIm())+")")
   print(c5)
   print(c6)
   print(c7)
   print(c8)







