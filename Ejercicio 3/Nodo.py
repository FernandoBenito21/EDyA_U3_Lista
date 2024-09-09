class Nodo:
    def __init__(self):
        self.__item = 0
        self.__sig = -1

    def getItem(self):
        return self.__item

    def setItem(self, unItem):
        self.__item = unItem

    def setSig(self, tope):
        self.__sig = tope

    def getSig(self):
        return self.__sig