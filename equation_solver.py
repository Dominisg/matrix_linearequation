from matrix import *
import time 
import copy

class EquationSolver:
    def __init__(self,N,A,b):
        self.N = N
        self.b = b
        self.x = Matrix.ones(N,1)
        self.A = Matrix(A)
    
    def solveGauss(self):
        iter = 0
        while True:
            for i in range(self.N):
                self.x[i][0] = self.b[i][0]
                for j in range(self.N):
                    if j!=i:
                        self.x[i][0] -= self.A[i][j]*self.x[j][0]
                self.x[i][0] /= self.A[i][i]
            iter+=1
            if Matrix.norm(self.A * self.x - self.b) < 1E-9:
                return iter

    def solveJacobi(self):
        x = copy.deepcopy(self.x)
        while True:
            for i in range(self.N):
                x[i][0] = self.b[i][0]
            
                for j in range(self.N):
                    if j!=i:
                        x[i][0] -= self.A[i][j]*self.x[j][0]
                x[i][0] /= self.A[i][i]
            self.x = copy.deepcopy(x)
            print(Matrix.norm(self.A * self.x - self.b))
            if Matrix.norm(self.A * self.x - self.b) < 1E-9:
                return self.x
    
    

if __name__ == '__main__':
    solver = EquationSolver(967,Matrix.fillDiagonal(967,6,-1,-1),Matrix.fillbSin(967))

    # start = time.time()
    #print(solver.solveJacobi())
    # end = time.time()

    # print(end-start)

    start = time.time()
    print(solver.solveGauss())
    end = time.time()

    print(end-start)


 