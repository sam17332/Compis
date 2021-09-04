import pprint

class Tablas:
    def __init__(self):
        self.variables = {}
        self.estructuras = {}
        self.metodos = {}
        self.print = pprint.PrettyPrinter()

    def setMetodo(self, key, name, returnType, arrayParams, padre = '', retorna = False):
        self.metodos[key] = [name, returnType, arrayParams, padre, retorna]

    def getMetodo(self, nombre):
        if len(self.metodos) > 0:
            for i in range(len(self.metodos)):
                valor = self.metodos[i+1]
                if nombre == valor[0]:
                    return valor
    
    def metodoSetReturn(self, nombre):
        if len(self.metodos) > 0:
            for i in range(len(self.metodos)):
                valor = self.metodos[i+1]
                if str(nombre) == str(valor[0]):
                    valor[4] = True

    def metodoExists(self, nombre):
        if len(self.metodos) > 0:
            for i in range(len(self.metodos)):
                valor = self.metodos[i+1]
                if str(nombre) == str(valor[0]):
                    return True
        return False

    def setVariable(self, key, name, type, scope, value = 0, size = 0, struct = False):
        self.variables[key] = [name, type, value, scope, size, struct]

    def getVariable(self, nombre, scope, existe = False, var = ''):
        if existe:
            return var
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if str(nombre) == str(valor[0]) and str(scope) == str(valor[3]):
                    existe = True
                    var = valor
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.getVariable(nombre, nuevoScope)
        return var

    def varExistsOnce(self, nombre, scope):
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

    def getStructVar(self, nombre, scope, existe = False, var = ''):
        if existe:
            return var
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if str(nombre) == str(valor[0]) and str(scope) == str(valor[3]) and valor[5]:
                    existe = True
                    var = valor
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.getStructVar(nombre, nuevoScope)
        return var

    def structVarExists(self, nombre, scope, existe = False):
        if existe:
            return True
        if len(self.variables) > 0:
            for i in range(len(self.variables)):
                valor = self.variables[i+1]
                if nombre == valor[0] and scope == valor[3] and valor[5]:
                    existe = True
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.structVarExists(nombre, nuevoScope)
        return existe

    def setEstructura(self, key, name, tipo, defi, scope = '', tam = 0, struct = False):
        self.estructuras[key] = [name, tipo, defi, scope, tam, struct]

    def getArray(self, nombre, scope, existe = False, var = ''):
        if existe:
            return var
        if len(self.estructuras) > 0:
            for i in range(len(self.estructuras)):
                valor = self.estructuras[i+1]
                if str(nombre) == str(valor[0]) and scope == valor[3]:
                    existe = True
                    var = valor
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.getArray(nombre, nuevoScope)
        return var

    def estruturaExists(self, nombre):
        if len(self.estructuras) > 0:
            for i in range(len(self.estructuras)):
                valor = self.estructuras[i+1]
                if nombre == valor[0]:
                    return True
        return False

    def arrayExists(self, nombre, scope, existe = False):
        if existe:
            return True
        if len(self.estructuras) > 0:
            for i in range(len(self.estructuras)):
                valor = self.estructuras[i+1]
                if str(nombre) == str(valor[0]) and scope == valor[3]:
                    existe = True
            if self.metodoExists(scope) and existe == False:
                metodo = self.getMetodo(scope)
                nuevoScope = metodo[3]
                if nuevoScope != '':
                    return self.arrayExists(nombre, nuevoScope)
        return existe

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