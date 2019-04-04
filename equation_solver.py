from matrix import Matrix
import time 
import copy
import math
import matplotlib.pyplot as plt

class EquationSolver: 
    def __init__(self,N,A,b):
        self.N = N
        self.b = b
        self.x = Matrix.ones(N)
        self.A = A
    
    def solveGauss(self):
        iter = 0
        start = time.time()
        while True:
            for i in range(self.N):
                cache = self.b.data[i][0]
                for j in range(self.N):
                    if j!=i:
                        cache -= self.A.data[i][j]*self.x.data[j][0]
                self.x.data[i][0] = cache / self.A.data[i][i]
            iter+=1
            norm = Matrix.norm(self.A * self.x - self.b)
            if norm <= 1E-9:
                end = time.time()
                self._presents_results("Algorytm Gaussa-Seidla",end-start,iter,norm)
                return end-start
            if norm > 1E+2:
                print("Algorytm Gaussa-Seidla nie zbiegł się.")
                return

    def solveJacobi(self):
        iter = 0
        start = time.time()
        x = copy.deepcopy(self.x)
        while True:
            iter_time_s = time.time()
            for i in range(self.N):
                cache = self.b.data[i][0]

                for j in range(self.N):
                    if j!=i:
                        cache -= self.A.data[i][j]*self.x.data[j][0]
                x.data[i][0] = cache / self.A.data[i][i]
            self.x.data = copy.deepcopy(x.data)
            iter+=1
            iter_time_e = time.time()
            print(iter_time_e - iter_time_s)
            norm = Matrix.norm(self.A * self.x - self.b)
            #print(norm)
            if norm <= 1E-9:
                end = time.time()
                # print(self.x)
                self._presents_results("Algorytm Jacobiego",end-start,iter,norm)
                return end-start
            if norm > 1E+2:
                print("Algorytm Jacobiego nie zbiegł się.")
                return
    
    def solveLU(self):
        U = copy.deepcopy(self.A)
        L = Matrix.diag(self.N)

        start = time.time()

        for k in range(self.N-1):
            for j in range(k+1,self.N):
                val = L.data[j][k] = U.data[j][k]/U.data[k][k]
                for i in range(k,self.N):
                    U.data[j][i] = U.data[j][i] - val*U.data[k][i]

        y = U*self.x

        for i in range(self.N):
            cache = self.b.data[i][0]
            for k in range(i):
                if i != k:
                    cache -= L.data[i][k]*y.data[k][0]
            y.data[i][0] = cache / L.data[i][i]


        for i in range(self.N-1,-1,-1):
            cache = y.data[i][0]
            for k in range(i,self.N):
                if i != k:
                    cache -= U.data[i][k]*self.x.data[k][0]
            self.x.data[i][0] = cache / U.data[i][i]


        end = time.time()
        self._presents_results("Metoda LU",end - start,0,Matrix.norm(self.A * self.x - self.b))
        return end - start

    def _presents_results(self,name,time,iterations,residuum):
        print(name,"zakończył działanie.")
        print("Czas działania algorytmu:",round(time,3),"s")
        if iterations != 0:
            print("Liczba iteracji:",iterations)
        print("Osiągnięta norma residuum:",residuum)
        

if __name__ == '__main__':

    jacobi_time = []
    gauss_time = []
    lu_time = []


    ##############################zadanie A############################################
    solver_j = EquationSolver(967,Matrix.fillDiagonal(967,6,-1,-1),Matrix.fillbSin(967))
    solver_j.solveJacobi()
    
    solver_g = EquationSolver(967,Matrix.fillDiagonal(967,6,-1,-1),Matrix.fillbSin(967))
    solver_g.solveGauss()
    #############################zadanie B#############################################
    solver_j = EquationSolver(967,Matrix.fillDiagonal(967,3.0,-1.0,-1.0),Matrix.fillbSin(967))
    solver_j.solveJacobi()
    
    solver_g = EquationSolver(967,Matrix.fillDiagonal(967,3.0,-1.0,-1.0),Matrix.fillbSin(967))
    solver_g.solveGauss()

    solver_lu = EquationSolver(967,Matrix.fillDiagonal(967,6.0,-1.0,-1.0),Matrix.fillbSin(967))
    solver_lu.solveLU()
 

    N = [100,500,1000,2000,3000]

    for n in N:
        solver_j = EquationSolver(n,Matrix.fillDiagonal(n,6,-1,-1),Matrix.fillbSin(n))
        jacobi_time.append(solver_j.solveJacobi())

        solver_g = EquationSolver(n,Matrix.fillDiagonal(n,6,-1,-1),Matrix.fillbSin(n))
        gauss_time.append(solver_g.solveGauss())

        solver_lu = EquationSolver(n,Matrix.fillDiagonal(n,6,-1,-1),Matrix.fillbSin(n))
        lu_time.append(solver_lu.solveLU())

plt.plot(N,jacobi_time)
plt.plot(N,gauss_time)
plt.plot(N,lu_time)
plt.ylabel('czas działania[s]')
plt.xlabel('rozmiar macierzy')
plt.show()

