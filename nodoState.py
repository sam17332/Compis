class NodoState:
    def __init__(self):
        self.siguiente = ""
        self.codigo = ""
        self.valorTrue = ""
        self.valorFalse = ""

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getValorTrue(self):
        return self.valorTrue

    def setValorTrue(self, valorTrue):
        self.valorTrue = valorTrue

    def getValorFalse(self):
        return self.valorFalse

    def setValorFalse(self, valorFalse):
        self.valorFalse = valorFalse

    def getNodeState(self):
        return [self.siguiente, self.codigo, self.valorTrue, self.valorFalse]