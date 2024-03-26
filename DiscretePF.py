"""
Este programa calcula diversos datos de interes para  funciones de probabilidad de masa 
"""
import numpy as np
import matplotlib.pyplot as plt 
import sympy as sy
import scipy.special as sps

#Argumentos: 
#n = Número de ensayos
#x = Valor de la variable aleatoria discreta
#p = Probabilidad de exito
#d = Número de decimales que se desean

class binomial:
    def __init__(self,n,x,p,d):
        self.n = n
        self.x = x
        self.p = p
        self.d = d

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Validate(self):
        if self.p > 0 and self.p < 1 and self.n >= self.x and type(self.n) == int and type(self.x) == int and self.x >= 0 and self.n > 0 and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux
    def Evaluate(self):
        s = 0
        f = np.zeros(3)
    
        f[0] = round(Binomial_Coefficient(self.n,self.x)*self.p**self.x*(1-self.p)**(self.n-self.x),self.d)
        for i in range(0,self.x+1):
            s += Binomial_Coefficient(self.n,i)*self.p**i*(1-self.p)**(self.n-i)
        f[1] = round(s,self.d)
        f[2] = 1-s+f[0]
        return f
    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = round(self.n * self.p,self.d)
        ans[1] = round(self.n * self.p*(1-self.p),self.d)
        ans[2] = round(np.sqrt(self.n * self.p*(1-self.p)),self.d)
        return ans

    def graph(self):
        t = np.arange(0,self.n+1)
        y = Binomial_Coefficient(self.n,t)*self.p**t*(1-self.p)**(self.n-t)
        plt.bar(t,y, color = "#757bc8")
        plt.savefig("Images\Binomial_Graph.png")
        plt.clf()

#Argumentos: 
#N = Número total de objetos
#K = Número de objetos con cierta característica
#n = Número de objetos que se seleccionan al azar
#x = Número de objetos en la muestra que cumplen con la característica
#d = Número de decimales que se desean

class Hipergeometrica:
    def __init__(self,N,k,n,x,d):
        self.N = N
        self.k = k
        self.n = n
        self.x = x
        self.d = d

    def Validate(self):
        if (self.N > self.n) and (self.N > self.k) and (self.x >= self.k+self.n-self.N) and self.x <= self.k and (type(self.n) == int and type(self.x) == int and type(self.k) == int and type(self.N) == int) and self.n > 0 and self.k >= 0 and self.x >= 0 and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Evaluate(self):
        s = 0
        f = np.zeros(3)
        f[0] = round(Binomial_Coefficient(self.k,self.x)*Binomial_Coefficient(self.N-self.k,self.n-self.x)/Binomial_Coefficient(self.N,self.n),self.d)
        
        for i in range(self.k+self.x-self.N,self.x+1):
            s += Binomial_Coefficient(self.k,i)*Binomial_Coefficient(self.N-self.k,self.n-i)/Binomial_Coefficient(self.N,self.n)
        
        f[1] = round(s,self.d)
        f[2] = 1-s+f[0]

        return f

    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = round(self.n*self.k/self.N,self.d)
        ans[1] = round(self.n*self.k/self.n*(self.N-self.k)/self.N*(self.N-self.n)/(self.N-1),self.d)
        ans[2] = round(np.sqrt(self.n*self.k/self.n*(self.N-self.k)/self.N*(self.N-self.n)/(self.N-1)),self.d)
        return ans
    
    def graph(self):
        t = np.arange(0,self.k+1)
        y = Binomial_Coefficient(self.k,t)*Binomial_Coefficient(self.N-self.k,self.n-t)/Binomial_Coefficient(self.N,self.n)
        plt.bar(t,y, color = "#757bc8")
        plt.savefig("Images\Hypergeometric_Graph.png")
        plt.clf()

#Argumentos: 
#M = Parámetro de intensidad (media)
#x = Valor de la variable aleatoria discreta
#d = Número de decimales que se desean

class Poisson:
    def __init__(self,M,x,d):
        self.M = M
        self.x = x
        self.d = d

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Validate(self):
        if self.M >= 0 and self.x >= 0 and type(self.x) == int and type(self.M) != bool and type(self.M) != str and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux

    def Evaluate(self):
        s = 0
        f = np.zeros(3)

        f[0] = round(np.exp(-self.M)*self.M**self.x/sps.gamma(self.x+1),self.d)
        for i in range(0,self.x+1):
            s += np.exp(-self.M)*self.M**i/sps.gamma(i+1)
        f[1] = round(s,self.d)
        f[2] = 1-s+f[0]

        return f
    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = self.M
        ans[1] = self.M
        ans[2] = round(np.sqrt(self.M),self.d)
        return ans

    def graph(self):
        t = np.arange(0,self.x+5)
        y = np.abs(np.exp(-self.M)*self.M**t/sps.gamma(t+1))
        plt.bar(t,y, color = "#757bc8")
        plt.savefig("Images\Poisson_Graph.png")
        plt.clf()






def Binomial_Coefficient(n,x):
    ans = sps.gamma(n+1)/(sps.gamma(x+1)*sps.gamma(n-x+1))
    return ans
