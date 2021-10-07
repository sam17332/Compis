class Nodo:
    def __init__(self, numero):
        self.direccion = ""
        self.codigo = ""
        self.numero = numero

    def getDir(self):
        return self.direccion

    def setDir(self, direccion):
        self.direccion = direccion

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getNode(self):
        return [self.direccion, self.codigo, self.numero]