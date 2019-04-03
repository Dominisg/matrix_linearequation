class Matrix:
    def __init__(self, matrix):
        self.data = matrix

    def __getitem__(self, index):
        return self.data[index]

    def __add__ (self,other):
        for i in range(len(self[i])):
            for j in range(len(self[i])):
                self[j][i] += other[j][i]
        return Matrix(self.data)

    def __sub__(self,other):
        for i in range(len(self)):
            for j in range(len(self[i])):
                self[j][i] -= other[j][i]
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

    

        
        
        

a = Matrix([[2,1,3],[1,1,2],[2,1,2]])
b = Matrix([[1,1,1],[1,1,3],[1,1,4]])

c = a * b
print(c)

c.transpose()

print(c)