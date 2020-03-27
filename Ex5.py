import numpy as np

class Matrice:

    def __init__(self,data):
        self.__data = data


    def getData(self):
        return self.__data



    def __add__(self,obj): #M3
        return (self.__data + obj.__data)




    def __iadd__(self,data2): #M4
        self.__data += data2.__data
        return self.__data




    def __sub__(self,obj): #M5
        return (self.__data - obj.__data)




    def __isub__(self,data2): #M6
        self.__data -= self.__data2
        return self.__data




    def __mul__(self, obj): #M7
        return (self.__data * obj.__data)





    def __imul__(self,obj): #M8
        return self.__data




    def __lt__(self,obj): #M9
        return (self.__data < obj.__data)




    def __gt__(self,obj): #M10
        return (self.__data > obj.__data)


    def __len__(self): #M11
        return len(self.__data)





if __name__ == '__main__':

    data1 = np.array([[1,2],[3,4]])
    data2 = np.array([[2,2],[1,2]])

    Mat1 = Matrice(data1)
    Mat2 = Matrice(data2)
    Mat3 = Mat1 + Mat2
 #   print(Mat1 += Mat2)
    Mat5 = Mat1 - Mat2
 #   Mat6 =
 #   Mat7 = Mat1 * Mat2
 #   Mat8 =
    Mat9 = Mat1 < Mat2
    Mat10 = Mat1 > Mat2
    Mat11 = len(Mat1)

    print(Mat3)

    print(Mat5)
#    print(Mat6)
 #   print(Mat7)
#    print(Mat8)
    print(Mat9)
    print(Mat10)
    print("longueur:",Mat11)


