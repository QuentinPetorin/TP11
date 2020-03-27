import numpy as np

class Matrice:

    def __init__(self,data):
        self.__data = data

    def getData(self):
        return self.__data



    def __add__(self,obj): #M1
        return (self.__data + obj.__data)




    def __iadd__(self,obj): #M2
        return (self.__data += obj.__data)




    def __sub__(self,obj): #M3
        return (self.__data - obj.__data)




   # def __isub__(self,obj): #M4




   # def __mul__(self, obj): #M4





    #def __imul__(self,obj): #M5




    def __lt__(self,obj): #M6
        return (self.__data < obj.__data)




    def __gt__(self,obj): #M7
        return (self.__data > obj.__data)


    def __len__(self,obj):
        return len(obj)





if __name__ == '__main__':

    data1 = np.array([[1,2],[3,4]])
    data2 = np.array([[2,2],[1,2]])
    Mat1 = Matrice(data1)
    Mat2 = Matrice(data2)
    Mat3 = Mat1 + Mat2
    Mat4 =
    Mat5 =
    Mat6 =
    Mat7 =
    Mat8 =
    Mat9 =

    print(Mat3)
