class Nodo:
    def __init__(self):
        self.__item = 0
        self.__sig = None

    def getItem(self):
        return self.__item

    def setItem(self, unItem):
        self.__item = unItem

    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig