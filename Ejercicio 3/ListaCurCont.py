from Nodo import *
import numpy as np

class Lista_Cursores_Contenido:
    def __init__(self, dimension):
        self.__dimension = dimension
        self.__cant = 0
        self.__lista = np.empty(dimension, dtype=object)
        self.__cabeza = -1
        self.__disponible = 0
        i = 0
        while (i < (self.__dimension - 2)):
            nodo = Nodo()
            nodo.setSig(i + 1)
            self.__lista[i] = nodo
            i += 1
        otro_nodo = Nodo()
        otro_nodo.setSig(-1)
        self.__lista[i + 1] = otro_nodo
    
    def Insertar(self, x):
        if (self.__cant <= self.__dimension):
            pos = self.__disponible
            self.__lista[pos].setItem(x)
            self.__disponible = self.__lista[self.__disponible].getSig()
            if (self.__cabeza == -1):
                self.__cabeza = 0
                self.__lista[self.__cabeza].setSig(-1)
            else:
                i = self.__cabeza
                while (i != -1) and (self.__lista[i].getItem() < x):
                    anterior = i
                    i = self.__lista[i].getSig()
                self.__lista[anterior].setSig(pos)
                if (i != -1):
                    self.__lista[pos].setSig(i)
                else:
                    self.__lista[pos].setSig(-1)
            self.__cant += 1
        else:
            print("No hay espacio pa insertar, pibe")
    
    def Suprimir(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                pos = 1
                i = self.__cabeza
                while (pos < p):
                    pos += 1
                    anterior = i
                    i = self.__lista[i].getSig()
                if (i == self.__cabeza):
                    self.__cabeza = self.__lista[self.__cabeza].getSig()
                else:
                    if (i == -1):
                        self.__lista[anterior].setSig(-1)
                    else:
                        self.__lista[anterior].setSig(self.__lista[i].getSig())  
                retorna = self.__lista[i].getItem()
                self.__lista[i].setSig(self.__disponible)
                self.__disponible = i 
                self.__cant -= 1
            else:
                print("Posicion invalida")
        else:
            print("Lista vacia")    
        return retorna
    
    def Recuperar(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                pos = 1
                i = self.__cabeza
                while (pos > p):
                    pos += 1
                    i = self.__lista[i].getSig()
                retorna = self.__lista[i].getItem()
            else:
                print("Posicion invalida")
        else:
            print("Lista vacia")
        return retorna
    
    def Buscar(self, x):
        retorna = -1
        i = self.__cabeza
        while (i != -1) and (self.__lista[i].getItem() != x):
            i = self.__lista[i].getSig()
        if (i != -1):
            retorna = self.__lista[i].getItem()
        return retorna
    
    def Primer_Elemento(self):
        return self.__lista[self.__cabeza].getItem()
    
    def Ultimo_Elemento(self):
        retorna = -1
        i = self.__cabeza
        while (i != -1):
            anterior = i
            i = self.__lista[i].getSig()
        retorna = self.__lista[anterior].getItem()
        return retorna
            
    def Anterior(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 < p) and (p <= self.__cant):
                i = self.__cabeza
                pos = 1
                while (pos < p):
                    pos += 1
                    anterior = i
                    i = self.__lista[i].getSig()
                retorna = self.__lista[anterior].getItem()
            else:
                print("El elemento no tiene anterior")
        else:
            print("Lista vacia")
        return retorna
    
    def Siguiente(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p < self.__cant):
                i = self.__cabeza
                pos = 1
                while (pos < p):
                    pos += 1
                    i = self.__lista[i].getSig()
                siguiente = self.__lista[i].getSig()
                retorna = self.__lista[siguiente].getItem()
            else:
                print("El elemento no tiene siguiente")
        else:
            print("Lista vacia")
        return retorna                      
    
    def Vacia(self):
        return self.__cant == 0
    
    def Recorrer(self):
        i = self.__cabeza
        while (i != -1):
            print(f"{self.__lista[i].getItem()}")
            i = self.__lista[i].getSig()