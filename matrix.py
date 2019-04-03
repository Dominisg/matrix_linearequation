import math

class Matrix:
    def __init__(self, matrix):
        self.data = matrix

    def __getitem__(self, index):
        return self.data[index]

    def __add__ (self,other):
        for i in range(len(self[i])):
            for j in range(len(self[i])):
                self[i][j] += other[i][j]
        return Matrix(self.data)

    def __sub__(self,other):
        for i in range(len(self)):
            for j in range(len(self[i])):
                self[i][j] -= other[i][j]
        return Matrix(self.data)

    def __len__(self):
        return self.data.__len__()

    def __str__(self):
        return self.data.__str__()

    def __mul__(self,other):
        if len(self[0]) != len(other):
            raise ValueError('Matrixs cannot be multiplicated.')
        tmp = []
        for i in range(len(self)):
            row = []
            for j in range(len(other[0])):
                elem = 0
                for k in range(len(self[0])):
                    elem += self[i][k]*other[k][j]
                row.append(elem)
            tmp.append(row)
        return Matrix(tmp)

    def transpose(self):
        self.data = [*zip(*self.data)]
        return self

    def copy(self):
        return Matrix(self.data.copy())

    @staticmethod
    def ones(m=1,n=1):
        return Matrix([[1 for i in range(n)] for j in range(m)])

    @staticmethod
    def zeros(m=1,n=1):
        return Matrix([[0 for i in range(n)] for j in range(m)])

    @staticmethod
    def fillDiagonal(N,a1,a2,a3):
        tmp = Matrix.zeros(N,N)
        for i in range(N):
            tmp[i][i] = a1
            if(i+1<N):
                tmp[i+1][i] = a2
                tmp[i][i+1] = a2
                if(i+2<N):
                    tmp[i+2][i] = a3
                    tmp[i][i+2] = a3
        return tmp

    @staticmethod
    def fillbSin(N):
        return Matrix([[math.sin(j*(3)) for i in range(1)] for j in range(N)])
            

    @staticmethod
    def norm(mat):
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sum += mat[i][j]*mat[i][j]
        return math.sqrt(sum)


if __name__ == '__main__':
    pass
