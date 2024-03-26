"""
Este programa calcula diversos datos de interes para  funciones de probabilidad de densidad
"""
import numpy as np
import matplotlib.pyplot as plt 
import sympy as sy
import scipy.special as sps

#Argumentos: 
#M = Media
#x = Valor de la variable aleatoria continua
#d = Número de decimales que se desean

class exponencial:
    def __init__(self,M,x,d):
        self.M = M
        self.x = x
        self.d = d

    #Validate verifica que los datos de entrada sean correctos
    def Validate(self):
        if  self.M > 0 and self.x >= 0 and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Evaluate(self):
        f = np.zeros(3)
    
        f[0] = round(1/self.M*np.exp(-self.x/self.M),self.d)
        f[1] = round(1-np.exp(-self.x/self.M),self.d)
        f[2] = round(np.exp(-self.x/self.M),self.d)
        return f

    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = self.M
        ans[1] = self.M**2
        ans[2] = self.M
        return ans

    def graph(self):
        t = np.arange(0,1.3*self.x+3, 0.01)
        y = 1/self.M*np.exp(-t/self.M)
        plt.plot(t,y, color = "#757bc8")
        plt.fill_between(t,y, where = t<=self.x, color = "#757bc8")
        plt.savefig("Images\Exponential_Graph.png")
        plt.clf()

#Argumentos: 
#M = Media
#DE = Desviación Estandar
#x = Valor de la variable aleatoria continua
#d = Número de decimales que se desean

class normal:
    def __init__(self,M,DE,x,d):
        self.M = M
        self.DE = DE
        self.x = x
        self.d = d

    #funcion de densidad de probabilidad gamma
    def function(self,y):
        return 1/(self.DE*np.sqrt(2*np.pi))*np.exp(-0.5*((y-self.M)/self.DE)**2)
    
    #Función para integrar
    def integral(self,lower, upper, precision=1000):
        sign = 1
        if lower > upper:
            lower, upper = upper, lower
            sign = -1
        number_of_points = (upper - lower) * precision
        xs = np.linspace(lower, upper, int(number_of_points))
        integral = 0
        super_sum = 0
        sub_sum = 0
        for index in range(len(xs) - 1):
            delta = xs[index + 1] - xs[index]
            try:
                y1 = self.function(xs[index])
                sub_area = y1 * delta
                integral += sub_area
                
            except ZeroDivisionError:
                print(f"\nAvoided pole")

        return sign * integral
    
    #Validate verifica que los datos de entrada sean correctos
    def Validate(self):
        if  self.DE > 0  and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Evaluate(self):
        f = np.zeros(3)
        f[0] = round(1/(self.DE*np.sqrt(2*np.pi))*np.exp(-0.5*((self.x-self.M)/self.DE)**2),self.d)

        if self.x<= self.M-5*self.DE:
            f[1] = 0
        
        elif self.x >= self.M+5*self.DE:
            f[1] = 1
        else:
            f[1] = round(self.integral(self.M-5*self.DE,self.x),self.d)

        f[2] = round(1-self.integral(self.M-5*self.DE,self.x),self.d)
        return f

    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y el tercero es la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = self.M
        ans[1] = self.DE**2
        ans[2] = self.DE
        return ans

    def graph(self):
        if self.x<= self.M-2*self.DE:
            t = np.arange(self.x,3,0.001)
        else:
            t = np.arange(self.M-2*self.DE,1.3*self.x+3, 0.001)

        y = 1/(self.DE*np.sqrt(2*np.pi))*np.exp(-0.5*((t-self.M)/self.DE)**2)
        plt.plot(t,y, color = "#757bc8")
        plt.fill_between(t,y, where = t<=self.x, color = "#757bc8")
        plt.savefig("Images\\Normal_Graph.png")
        plt.clf()
    
#Argumentos: 
#a = Paramétro alpha
#b = Paramétro beta
#x = Valor de la variable aleatoria continua
#d = Número de decimales que se desean

class gamma:
    def __init__(self,a,b,x,d):
        self.a = a
        self.b = b
        self.x = x
        self.d = d
    
    #funcion de densidad de probabilidad gamma
    def function(self,y):
        return 1/(sps.gamma(self.a)*self.b**self.a)*y**(self.a-1)*np.exp(-y/self.b)
    
    #Función para integrar
    def integral(self,lower, upper, precision=1000):
        sign = 1
        if lower > upper:
            lower, upper = upper, lower
            sign = -1
        number_of_points = (upper - lower) * precision
        xs = np.linspace(lower, upper, int(number_of_points))
        integral = 0
        super_sum = 0
        sub_sum = 0
        for index in range(len(xs) - 1):
            delta = xs[index + 1] - xs[index]
            try:
                y1 = self.function(xs[index])
                sub_area = y1 * delta
                y2 = self.function(xs[index + 1])
                super_area = y2 * delta

                area = (y2 + y1) / 2 * delta
                integral += area
                sub_sum += sub_area
                super_sum += super_area
            except ZeroDivisionError:
                print(f"\nAvoided pole")

        return sign * integral

    #Validate verifica que los datos de entrada sean correctos
    def Validate(self):
        if  self.a> 0 and self.b> 0 and self.x >= 0 and type(self.d) == int and self.d>=0 and self.d<=8:
            aux = 1
        else: 
            aux = 0
        return aux

    #Evaluate devuelve un array, donde la primera entrada es la probabilidad x, 
    #el segundo al probabilidad de x o menores y el tercero x o mayores
    def Evaluate(self):
        f = np.zeros(3)
        f[0] = round(1/(sps.gamma(self.a)*self.b**self.a)*self.x**(self.a-1)*np.exp(-self.x/self.b),self.d)
        f[1] = round(self.integral(0,self.x),self.d)
        f[2] = round(1-self.integral(0,self.x),self.d)
        return f

    #Estadisticos devuelve un array, donde la primera entrada es media, 
    #el segundo la varianza y la desviación estándar
    def Estadisticos(self):
        ans = np.zeros(3)
        ans[0] = round(self.a*self.b,self.d)
        ans[1] = round(self.a*self.b**2,self.d)
        ans[2] = round(np.sqrt(self.a*self.b**2),self.d)
        return ans

    def graph(self):
        t = np.arange(0,1.3*self.x+3, 0.01)
        y = 1/(sps.gamma(self.a)*self.b**self.a)*t**(self.a-1)*np.exp(-t/self.b)
        plt.plot(t,y, color = "#757bc8")
        plt.fill_between(t,y, where = t<=self.x, color = "#757bc8")
        plt.savefig("Images\Gamma_Graph.png")
        plt.clf()


