import numpy as np
from Nodo import *


class Lista_Cursores:
    def __init__(self, dimension):
        self.__lista = np.empty(dimension, dtype = object)
        self.__cant = 0
        self.__dimension = dimension
        self.__primero = -1
        self.__ultimo = 0
        self.__libre = 0
    
    def Insertar(self, x):
        if (self.__cant <= self.__dimension):
            Elemento = Nodo()
            Elemento.setItem(x)
            Elemento.setSig(-1)
            if(self.__primero == -1):
                self.__primero = self.__libre
                self.__lista[self.__libre] = Elemento
                self.__libre = 1
                self.__lista[self.__libre] = Nodo()
            else:
                p = self.__libre
                self.__libre = self.__lista[self.__libre].getSig()
                self.__lista[self.__libre] = Nodo()
                self.__lista[p] = Elemento
                self.__lista[self.__ultimo].setSig(p)
                self.__ultimo = p
            self.__lista[self.__libre].setSig(self.__libre + 1)
            self.__cant += 1
        else:
            print("La lista esta llena")
    
    def Suprimir(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                retorna = self.__lista[p - 1].getItem()
                if ((p - 1) == self.__primero):
                    self.__primero = self.__lista[self.__primero].getSig()
                else:
                    ant = self.Anterior(p - 1)
                    if ((p - 1) == self.__ultimo):
                        self.__ultimo = ant
                        self.__lista[ant].setSig(-1)
                    else:
                        sig = self.Siguiente(p - 1)
                        self.__lista[ant].setSig(sig)
                self.__lista[p - 1].setSig(self.__libre)
                self.__libre = (p - 1)
                self.__cant -= 1
            else:
                print("La posicion indicada no es valida")
        else:
            print("No se puede suprimir porque la lista esta vacia")
        return retorna
    
    def Primer_Elemento(self):
        return (self.__lista[self.__primero].getItem())
        
    def Ultimo_Elemento(self):
        return (self.__lista[self.__ultimo].getItem())
    
    def Siguiente(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p < self.__dimension):
                retorna = self.__lista[p].getSig()
            else:
                print("La posicion indicada no es valida")
        else:
            print("La lista esta vacia")
        return retorna
    
    def Anterior(self, p):
        retorna = -1
        if(self.Vacia() == False):
            if (1 < p) and (p <= self.__cant):
                anterior = self.__primero
                actual = self.__primero
                while (actual < p):
                    anterior = actual
                    actual = self.__lista[actual].getSig() 
                retorna = anterior
            else:
                print("La posicion indicada no es valida")
        else:
            print("La lista esta vacia")
        return retorna                                                  
    
    def Recuperar(self, p):
        retorna = -1
        if (1 <= p) and (p <= self.__cant):
            pos = 1
            aux = self.__lista[self.__primero]
            while (pos != p):
                aux = aux.getSig()
                pos += 1
            retorna = self.__lista[aux].getItem()
        else:
            print("La posicion indicada no es valida")
        return retorna   
    
    def Buscar(self, x):
        p = -1
        actual = self.__primero
        while(actual != -1) and ((self.__lista[actual]) == x):
                actual = self.__lista[actual].getSig()
        if (actual != -1):
            p = actual
        return p
    
    def Vacia(self):
        return (self.__cant == 0)
    
    def Recorrer(self):
        actual = self.__primero
        while (actual != -1):
            print(f"{self.__lista[actual].getItem()}")
            actual = self.__lista[actual].getSig()