import pprint

class Tablas:
    def __init__(self):
        self.variables = {}
        self.estructuras = {}
        self.metodos = {}
        self.print = pprint.PrettyPrinter()

    def setMetodo(self, key, name, returnType, arrayParams, padre = ''):
        self.metodos[key] = [name, returnType, arrayParams, padre]

    def getMetodo(self, nombre):
        if len(self.metodos) > 0:
            for i in range(len(self.metodos)):
                valor = self.metodos[i+1]
                if nombre == valor[0]:
                    return valor

    def metodoExists(self, nombre):
        if len(self.metodos) > 0:
            for i in range(len(self.metodos)):
                valor = self.metodos[i+1]
                if nombre == valor[0]:
                    return True
        return False

    def setVariable(self, key, name, type, scope, value = 0, size = 0):
        self.variables[key] = [name, type, value, scope, size]

    def getVariable(self, nombre, scope, existe = False, var = ''):
        if existe:
            return var
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if nombre == valor[0] and scope == valor[3]:
                    existe = True
                    var = valor
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.getVariable(nombre, nuevoScope)
        return var

    def varExistsOnce(self, nombre, scope, existe = False):
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if nombre == valor[0] and scope == valor[3]:
                    return True
        return False

    def varExists(self, nombre, scope, existe = False):
        if existe:
            return True
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if nombre == valor[0] and scope == valor[3]:
                    existe = True
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.varExists(nombre, nuevoScope)
        return existe

    def setValueToVariable(self, nombre, value, scope, existe = False):
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if nombre == valor[0] and scope == valor[3]:
                    valor[2] = value
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.setValueToVariable(nombre, value, nuevoScope)
        return existe

    def setEstructura(self, key, name):
        self.estructuras[key] = [name]

    def estruturaExists(self, nombre):
        if len(self.estructuras) > 0:
            for i in range(len(self.estructuras)):
                valor = self.estructuras[i+1]
                if nombre == valor[0]:
                    return True
        return False

    def showFullDicc(self, name = ""):
        if name == "met":
            self.print.pprint(self.metodos)
        elif name == "var":
            self.print.pprint(self.variables)
        elif name == "est":
            self.print.pprint(self.estructuras)
        else:
            print("Metodos")
            self.print.pprint(self.metodos)
            print()
            print("Variables")
            self.print.pprint(self.variables)
            print()
            print("Estructuras")
            self.print.pprint(self.estructuras)