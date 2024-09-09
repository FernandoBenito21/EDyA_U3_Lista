from Nodo import *

class Lista_Encadenada_Contenido:
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
        self.__ultimo = None
    
    def Insertar(self, x):
        Elemento = Nodo()
        Elemento.setItem(x)
        Elemento.setSig(None)
        if (self.__cabeza == None):
            self.__cabeza = Elemento
        else:
            i = self.__cabeza
            while (i != None) and ((i.getItem()) < x):
                anterior = i
                i = i.getSig()
            if (i != None):
                anterior.setSig(Elemento)
                Elemento.setSig(i)
            else: 
                self.__ultimo.setSig(Elemento)
        self.__ultimo = Elemento
        self.__cant += 1
    
    def Suprimir(self, p):
        retorna = None
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                i = 1
                elem = self.__cabeza
                while (i < p):
                    anterior = elem
                    elem = elem.getSig()
                    i += 1
                if (elem == None):
                    self.__ultimo = anterior
                    anterior.setSig(None)
                else:
                    anterior.setSig(elem.getSig())
                    retorna = elem.getItem()
                self.__cant -= 1
        return retorna
    
    def Primer_Elemento(self):
        retorna = None
        if (self.Vacia() == False):
            retorna = self.__cabeza.getItem()
        return retorna
    
    def Ultimo_Elemento(self):
        retorna = None
        if (self.Vacia() == False):
            retorna = self.__ultimo.getItem()
        return retorna
    
    def Recuperar(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p <= self.__cant):
                i = 1
                elem = self.__cabeza
                while (i < p):
                    elem = elem.getSig()
                    i += 1
                retorna = elem.getItem()
        return retorna
    
    def Buscar(self, x):
        p = 1
        i = self.__cabeza
        while (i.getItem() != x) and (i != None):
            i = i.getSig()
            p += 1
        if (i == None):
            p = -1
        return p
    
    def Siguiente(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 <= p) and (p < self.__cant):
                pos = 1
                i = self.__cabeza
                while (i < p):
                    i = i.getSig()
                    pos += 1
                retorna = i.getItem()
        return 
    
    def Anterior(self, p):
        retorna = -1
        if (self.Vacia() == False):
            if (1 < p) and (p <= self.__cant):
                pos = 1
                i = self.__cabeza
                while (i < p):
                    anterior = i
                    i = i.getSig()
                    pos += 1
                retorna = anterior.getItem()
        return retorna
                 
    def Vacia(self):
        return self.__cant == 0
    
    def Recorrer(self):
        aux = self.__cabeza
        while(aux != None):
            print(f"{aux.getItem()}")
            aux = aux.getSig()