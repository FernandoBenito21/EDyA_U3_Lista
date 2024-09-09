import numpy as np

class Lista_Secuencial_Posicion:
    def __init__(self, dimension):
        self.__dimension = dimension
        self.__lista = np.empty(dimension, dtype = int)
        self.__cant = 0
        self.__ultimo = -1
    
    def Insertar(self, x, p):
        if (self.__cant <= self.__dimension):
            if ((0 <= p) and (p <= (self.__ultimo + 1))):
                i = self.__ultimo + 1
                while (i > p):
                    self.__lista[i] = self.__lista[i - 1]
                    i -= 1
                self.__lista[p] = x
                self.__cant += 1
                self.__ultimo += 1
            else:
                print ("La posicion ingresada no es valida")
        else:
            print ("La lista esta llena")
    
    def Surpimir(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                retorna = self.__lista[p]
                for i in range(p, self.__ultimo, -1):
                    self.__lista[i] = self.__lista[i + 1]
                self.__cant -= 1
                self.__ultimo = self.__cant - 1
            else:
                print("Posicion no valida")
        else:
            print("La lista esta vacia")
        return retorna
    
    def Recuperar(self, p):
        return self.__lista[p]
    
    def Buscar(self, x):
        retorna = -1
        i = 0
        while (i < self.__cant) and (self.__lista[i] != x):    
            i += 1
        if (i < self.__cant):
            retorna = self.__lista[i]
        return retorna
    
    def Primer_Elemento(self):
        return self.__lista[0]
    
    def Ultimo_Elemento(self):
        return self.__lista[self.__ultimo]
    
    def Siguiente(self, p):
        retorna = -1
        if (1 <= p) and (p < self.__cant):
            retorna = self.__lista[p + 1]
        return retorna
    
    def Anterior(self, p):
        retorna = -1
        if (1 < p) and (p <= self.__cant):
            retorna = self.__lista[p - 1]
        return retorna
    
    def Vacia(self):
        return self.__cant == 0
    
    def Recorrer(self):
        i = 0
        while (i <= self.__ultimo):
            print(f"{self.__lista[i]}")
            i += 1