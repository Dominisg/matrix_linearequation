import math
import time
import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.data = matrix

    #practically not used, using slows down algorithms twice
    # def __getitem__(self,index):
    #     return self.data[index]

    def __add__ (self,other):
        for i in range(len(self.data[i])):
            for j in range(len(self.data[i])):
                self.data[i][j] += other.data[i][j]
        return Matrix(self.data)

    def __sub__(self,other):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] -= other.data[i][j]
        return Matrix(self.data)

    def __len__(self):
        return self.data.__len__()

    def __str__(self):
        return self.data.__str__()

    def __mul__(self,other):
        return Matrix([[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*other.data)] for X_row in self.data])
        
    # def __mul__(self,other):
    #     return Matrix(np.matmul(self.data,other.data))


    def transpose(self):
        self.data = [*zip(*self.data)]
        return self

    def copy(self):
        return Matrix(self.data.copy())

    @staticmethod
    def ones(m=1,n=1):
        return Matrix([[1.0 for i in range(n)] for j in range(m)])

    @staticmethod
    def zeros(m=1,n=1):
        return Matrix([[0.0 for i in range(n)] for j in range(m)])

    @staticmethod
    def diag(N,a=1.0):
        tmp = Matrix.zeros(N,N)
        for i in range(N):
            tmp.data[i][i] = a
        return tmp

    @staticmethod
    def fillDiagonal(N,a1,a2,a3):
        tmp = Matrix.zeros(N,N)
        for i in range(N):
            tmp.data[i][i] = a1
            if(i+1<N):
                tmp.data[i+1][i] = a2
                tmp.data[i][i+1] = a2
                if(i+2<N):
                    tmp.data[i+2][i] = a3
                    tmp.data[i][i+2] = a3
        return tmp

    @staticmethod
    def fillbSin(N):
        return Matrix([[math.sin(j*(3)) for i in range(1)] for j in range(N)])
            

    @staticmethod
    def norm(mat):
        sum = 0
        for i in range(len(mat.data)):
            for j in range(len(mat.data[0])):
                sum += mat.data[i][j]*mat.data[i][j]
        return math.sqrt(sum)


if __name__ == '__main__':
    a = Matrix.ones(400,400)
    b = Matrix.ones(400,400)

    print(len(a))
    start = time.time()
    a*b
    end = time.time()

    print(end-start)
    