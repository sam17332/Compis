from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from DecafLexer import DecafLexer
from DecafListener import DecafListener
from DecafParser import DecafParser
from tablas import *
import sys

class KeyPrinter(DecafListener):
    def __init__(self):
        self.notMainFunction = True
        self.error = []
        self.tablas = Tablas()
        self.contVariables = 0
        self.contEstructuras = 0
        self.contFunciones = 0
        self.contStatements = 0
        self.scopes = ["global"]
        self.scopeActual = "global"

    def getErrors(self):
        return self.error

    def enterStatement(self, ctx: DecafParser.StatementContext):
        if ctx.IF() or ctx.WHILE():
            self.contStatements += 1
            if ctx.WHILE():
                scope = 'while'+ str(self.contStatements)
            elif ctx.IF():
                scope = 'if'+ str(self.contStatements)
            self.scopes.append(scope)
            self.scopeActual = scope
            binOp = ctx.expr().bin_op().getText()
            arraySplit = []
            arrayTypes = []
            error = False
            if ctx.expr().bin_op().eq_op():
                if binOp == "==" or binOp == "!=":
                    arraySplit = ctx.expr().getText().split(binOp)
                    for i in arraySplit:
                        var = self.tablas.getVariable(i, self.scopes[len(self.scopes)-2])
                        if isinstance(var, list):
                            if var[1] == 'int' or var[1] == 'boolean' or var[1] == 'string':
                                arrayTypes.append(var[1])
                            else:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'ERROR: La condicion no es valida, linea: {ctx.start.line}')
                        elif i == 'True' or i == 'False':
                            arrayTypes.append('boolean')
                        elif "'" in i:
                            arrayTypes.append('string')
                        else:
                            try:
                                int(i)
                                arrayTypes.append('int')
                            except:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'ERROR: La condicion no es valida, linea: {ctx.start.line}')
                    setTypes = set(arrayTypes)
                    if len(setTypes) > 1:
                        self.contStatements -= 1
                        error = True
                        self.error.append(f'ERROR: Ambos lados de la condicion deben ser el mismo tipo, linea: {ctx.start.line}')
            elif ctx.expr().bin_op().rel_op():
                if binOp == ">=" or binOp == "<=" or binOp == ">" or binOp == "<":
                    arraySplit = ctx.expr().getText().split(binOp)
                    for i in arraySplit:
                        var = self.tablas.getVariable(i, self.scopes[len(self.scopes)-2])
                        if isinstance(var, list):
                            if var[1] == 'int':
                                arrayTypes.append(var[1])
                            else:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'ERROR: La condicion no es valida, linea: {ctx.start.line}')
                        else:
                            try:
                                int(i)
                                arrayTypes.append('int')
                            except:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'ERROR: La condicion no es valida, linea: {ctx.start.line}')
                    setTypes = set(arrayTypes)
                    if len(setTypes) > 1:
                        self.contStatements -= 1
                        error = True
                        self.error.append(f'ERROR: Ambos lados de la condicion deben ser el mismo tipo, linea: {ctx.start.line}')
            # elif ctx.expr().bin_op().arith_op():
            # elif ctx.expr().bin_op().cond_op():
            if error == False:
                self.contFunciones += 1
                self.tablas.setMetodo(self.contFunciones, scope, '', [], self.scopes[len(self.scopes)-2])
        elif ctx.FOR():
            print('forrrr')
        elif ctx.ELSE():
            scope = 'else'+ str(self.contStatements)
            self.scopes.append(scope)
            self.scopeActual = scope
            self.contFunciones += 1
            self.tablas.setMetodo(self.contFunciones, scope, '', [], self.scopes[len(self.scopes)-2])
        elif ctx.RETURN():
            metodo = self.tablas.getMetodo(self.scopeActual)
            returnType = metodo[1]
            if returnType == 'void':
                self.error.append(f'ERROR: Hay un error en el método "{self.scopeActual}", es de tipo void y tiene un return, linea: {ctx.start.line}')
            else:
                if ctx.expr().location():
                    # TODO: Condicion para validar cuando se quiere retornar un struct
                    if ctx.expr().location().var_id():
                        varDerName = ctx.expr().location().var_id().getText()
                        if self.tablas.varExists(varDerName, self.scopeActual):
                            variableDer = self.tablas.getVariable(varDerName, self.scopeActual)
                            if variableDer[1] != returnType:
                                self.error.append(f'ERROR: El tipo de la variable "{varDerName}" no es del tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                        else:
                            self.error.append(f'ERROR: La variable "{varDerName}" no existe, linea: {ctx.start.line}')
                    elif ctx.expr().location().array_id():
                        var = ctx.expr().location().array_id().ID()
                        posi = 0
                        if ctx.expr().location().array_id().int_literal():
                            posi = ctx.expr().location().array_id().int_literal().getText()
                        else:
                            self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                        if self.tablas.arrayExists(var, self.scopeActual):
                            variableIgual = self.tablas.getArray(var, self.scopeActual)
                            tipoIgual = variableIgual[1]
                            if not returnType == tipoIgual:
                                self.error.append(f'ERROR: El tipo de la variable "{variableIgual[0]}" no es igual al tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                            if int(posi) <= 0 or int(posi) > variableIgual[4]:
                                self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                elif ctx.expr().literal():
                    tipo = ''
                    if ctx.expr().literal().int_literal():
                        tipo = 'int'
                    elif ctx.expr().literal().bool_literal():
                        tipo = 'boolean'
                    elif ctx.expr().literal().string_literal():
                        tipo = 'string'
                    else:
                        self.error.append(f'ERROR: El tipo de lo que retorna el método "{metodo[0]}" no es valido, linea: {ctx.start.line}')

                    if returnType != tipo:
                        self.error.append(f'ERROR: Lo que retorna el método "{metodo[0]}" no igual al tipo del método, linea: {ctx.start.line}')
                elif ctx.expr().method_call():
                    methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                    if self.tablas.metodoExists(methodName):
                        params = ctx.expr().method_call().method_call_inter().expr()
                        metodoDer = self.tablas.getMetodo(methodName)
                        metodoType = metodoDer[1]
                        metodoParams = metodoDer[2]
                        if metodoDer[4]:
                            if returnType != metodoType:
                                self.error.append(f'ERROR: El tipo del método "{metodo[0]} ({returnType})" es diferente del tipo del método "{methodName} ({metodoType})",linea: {ctx.start.line}')
                            else:
                                if len(params) == len(metodoParams):
                                    cont = 0
                                    var = ''
                                    tipo = ''
                                    for i in params:
                                        if i.literal():
                                            if i.literal().int_literal():
                                                tipo = 'int'
                                            elif i.literal().bool_literal():
                                                tipo = 'boolean'
                                            elif i.literal().string_literal():
                                                tipo = 'string'
                                        elif i.location():
                                            if i.location().var_id():
                                                var = i.location().var_id().getText()
                                                if self.tablas.varExists(var, self.scopeActual):
                                                    tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                else:
                                                    self.error.append(f'ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                            elif i.location().array_id():
                                                var = i.location().array_id().ID().getText()
                                                cantLocal = ''
                                                if i.location().array_id().int_literal():
                                                    cantLocal = i.location().array_id().int_literal().getText()
                                                else:
                                                    self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')

                                                if self.tablas.arrayExists(var, self.scopeActual):
                                                    arrayVar = self.tablas.getArray(var, self.scopeActual)
                                                    tipo = arrayVar[1]
                                                    cant = arrayVar[4]
                                                    if int(cantLocal) < 0 or int(cantLocal) > cant:
                                                        self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                                else:
                                                    self.error.append(f'ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                        if metodoParams[cont][0] != tipo:
                                            self.error.append(f'ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                        cont += 1
                                else:
                                    self.error.append(f'ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                        else:
                            self.error.append(f'ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                    else:
                        self.error.append(f'ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
                else:
                    if ctx.expr():
                        varDer = ctx.expr().getText()
                        arraySplit = []
                        if "+" in varDer:
                            varDer = varDer.replace("+", " ")
                        if "-" in varDer:
                            varDer = varDer.replace("-", " ")
                        if "/" in varDer:
                            varDer = varDer.replace("/", " ")
                        if "*" in varDer:
                            varDer = varDer.replace("*", " ")
                        if "%" in varDer:
                            varDer = varDer.replace("%", " ")
                        if "(" in varDer:
                            varDer = varDer.replace("(", " ")
                        if ")" in varDer:
                            varDer = varDer.replace(")", " ")
                        arraySplit = varDer.split(" ")
                        arrayTypes = []
                        for i in arraySplit:
                            if self.tablas.varExists(i, self.scopeActual):
                                varInfo = self.tablas.getVariable(i, self.scopeActual)
                                arrayTypes.append(varInfo[1])
                            elif i == 'True' or i == 'False':
                                arrayTypes.append('boolean')
                            elif "'" in i:
                                arrayTypes.append('string')
                            else:
                                try:
                                    int(i)
                                    arrayTypes.append('int')
                                except:
                                    self.error.append(f'ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                        setArrayTypes = set(arrayTypes)
                        if len(setArrayTypes) > 1:
                            self.error.append(f'ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
                        else:
                            arrayTypes2 = list(arrayTypes)
                            if arrayTypes2[0] != returnType:
                                self.error.append(f'ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
        elif ctx.location():
            if ctx.location().var_id():
                name = ctx.location().var_id().getText()
                error = False
                valor = ''
                # print(self.scopeActual)
                if self.tablas.varExists(name, self.scopeActual):
                    variable = self.tablas.getVariable(name, self.scopeActual)
                    tipo = variable[1]
                    # print('variable', variable)
                    # Condicion si se iguala a una literal
                    if ctx.expr().literal():
                        if ctx.expr().literal().int_literal():
                            valor = ctx.expr().literal().int_literal().getText()
                        elif ctx.expr().literal().bool_literal():
                            valor = ctx.expr().literal().bool_literal().getText()
                        elif ctx.expr().literal().string_literal():
                            valor = ctx.expr().literal().string_literal().getText()

                        if tipo == "string":
                            if "'" not in valor:
                                error = True
                        elif tipo == "int":
                            if "'" in valor or valor == 'True' or valor == 'False':
                                error = True
                            else:
                                try:
                                    int(valor)
                                except ValueError:
                                    error = True
                        elif tipo == "boolean":
                            if "'" in valor:
                                error = True
                            else:
                                try:
                                    int(valor)
                                    error = True
                                except:
                                    pass
                        if not error:
                            self.tablas.setValueToVariable(name, valor, self.scopeActual)
                        else:
                            self.error.append(f'ERROR: Hay un error en el valor de la variable "{name}", linea: {ctx.start.line}')
                    # Si se iguala a una variable
                    elif ctx.expr().location():
                        var = ctx.expr().location().getText()
                        if ctx.expr().location().array_id():
                            var = ctx.expr().location().array_id().ID()
                            posi = 0
                            if  ctx.expr().location().array_id().int_literal():
                                posi = ctx.expr().location().array_id().int_literal().getText()
                            else:
                                self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')

                        if self.tablas.varExists(var, self.scopeActual):
                            variableIgual = self.tablas.getVariable(var, self.scopeActual)
                            tipoIgual = variableIgual[1]
                            if not tipo == tipoIgual:
                                self.error.append(f'ERROR: El tipo de la variable "{variableIgual[0]}" no es igual que al de "{variable[0]}", linea: {ctx.start.line}')
                        elif self.tablas.arrayExists(var, self.scopeActual):
                            variableIgual = self.tablas.getArray(var, self.scopeActual)
                            tipoIgual = variableIgual[1]
                            if not tipo == tipoIgual:
                                self.error.append(f'ERROR: El tipo de la variable "{variableIgual[0]}" no es igual que al de "{variable[0]}", linea: {ctx.start.line}')
                            if int(posi) < 0 or int(posi) > variableIgual[4]:
                                self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                    # Condicion si se iguala a un metodo
                    elif ctx.expr().method_call():
                        methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                        if self.tablas.metodoExists(methodName):
                            params = ctx.expr().method_call().method_call_inter().expr()
                            metodo = self.tablas.getMetodo(methodName)
                            metodoType = metodo[1]
                            metodoParams = metodo[2]
                            varType = variable[1]
                            if metodo[4]:
                                if varType != metodoType:
                                    self.error.append(f'ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{name} ({varType})",linea: {ctx.start.line}')
                                else:
                                    if len(params) == len(metodoParams):
                                        cont = 0
                                        for i in params:
                                            if i.literal():
                                                if i.literal().int_literal():
                                                    tipo = 'int'
                                                elif i.literal().bool_literal():
                                                    tipo = 'boolean'
                                                elif i.literal().string_literal():
                                                    tipo = 'string'
                                            elif i.location():
                                                var = i.location().getText()
                                                if self.tablas.varExists(var, self.scopeActual):
                                                    tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                else:
                                                    self.error.append(f'ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                            if metodoParams[cont][0] != tipo:
                                                self.error.append(f'ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                            cont += 1
                                    else:
                                        self.error.append(f'ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                        else:
                            self.error.append(f'ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
                    else:
                        # Validar caso por si se iguala a una operacion de literales o variables
                        if ctx.expr():
                            varDer = ctx.expr().getText()
                            arraySplit = []
                            if "+" in varDer:
                                varDer = varDer.replace("+", " ")
                            if "-" in varDer:
                                varDer = varDer.replace("-", " ")
                            if "/" in varDer:
                                varDer = varDer.replace("/", " ")
                            if "*" in varDer:
                                varDer = varDer.replace("*", " ")
                            if "%" in varDer:
                                varDer = varDer.replace("%", " ")
                            if "(" in varDer:
                                varDer = varDer.replace("(", " ")
                            if ")" in varDer:
                                varDer = varDer.replace(")", " ")
                            arraySplit = varDer.split(" ")
                            arrayTypes = []
                            for i in arraySplit:
                                if self.tablas.varExists(i, self.scopeActual):
                                    varInfo = self.tablas.getVariable(i, self.scopeActual)
                                    arrayTypes.append(varInfo[1])
                                elif i == 'True' or i == 'False':
                                    arrayTypes.append('boolean')
                                elif "'" in i:
                                    arrayTypes.append('string')
                                else:
                                    try:
                                        int(i)
                                        arrayTypes.append('int')
                                    except:
                                        self.error.append(f'ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                            setArrayTypes = set(arrayTypes)
                            if len(setArrayTypes) > 1:
                                self.error.append(f'ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                            else:
                                arrayTypes2 = list(arrayTypes)
                                if arrayTypes2[0] != tipo:
                                    self.error.append(f'ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                else:
                    self.error.append(f'ERROR: La variable "{name}" no esta definida, linea: {ctx.start.line}')
            elif ctx.location().array_id():
                varName = ctx.location().array_id().ID().getText()
                if self.tablas.arrayExists(varName, self.scopeActual):
                    variable = self.tablas.getArray(varName, self.scopeActual)
                    tipo = variable[1]
                    if ctx.location().array_id().int_literal():
                        posi = ctx.location().array_id().int_literal().getText()
                        if int(posi) <= int(variable[4]):
                            # TODO: Condicion para verificar si se iguala a una estructura
                            if ctx.expr().location():
                                varDerName = ctx.expr().location().var_id().getText()
                                if self.tablas.varExists(varDerName, self.scopeActual):
                                    variableDer = self.tablas.getVariable(varDerName, self.scopeActual)
                                    if variableDer[1] != tipo:
                                        self.error.append(f'ERROR: El tipo de la variable "{variable[0]}" no es igual que al de "{variableDer[0]}", linea: {ctx.start.line}')
                            # Validar caso por si se iguala a una literal
                            elif ctx.expr().literal():
                                tipoDer = ''
                                if ctx.expr().literal().int_literal():
                                    tipoDer = 'int'
                                elif ctx.expr().literal().string_literal():
                                    tipoDer = 'string'
                                elif ctx.expr().literal().bool_literal():
                                    tipoDer = 'boolean'

                                if tipoDer != tipo:
                                    self.error.append(f'ERROR: El tipo de la variable "{variable[0]}" no es igual al tipo al que se esta igualando", linea: {ctx.start.line}')
                            # Validar caso por si se iguala a un metodo
                            elif ctx.expr().method_call():
                                methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                                if self.tablas.metodoExists(methodName):
                                    params = ctx.expr().method_call().method_call_inter().expr()
                                    metodo = self.tablas.getMetodo(methodName)
                                    metodoType = metodo[1]
                                    metodoParams = metodo[2]
                                    varType = variable[1]
                                    if metodo[4]:
                                        if varType != metodoType:
                                            self.error.append(f'ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{variable[0]} ({varType})",linea: {ctx.start.line}')
                                        else:
                                            if len(params) == len(metodoParams):
                                                cont = 0
                                                for i in params:
                                                    if i.literal():
                                                        if i.literal().int_literal():
                                                            tipo = 'int'
                                                        elif i.literal().bool_literal():
                                                            tipo = 'boolean'
                                                        elif i.literal().string_literal():
                                                            tipo = 'string'
                                                    elif i.location():
                                                        var = i.location().getText()
                                                        if self.tablas.varExists(var, self.scopeActual):
                                                            tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                        else:
                                                            self.error.append(f'ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                    if metodoParams[cont][0] != tipo:
                                                        self.error.append(f'ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                                    cont += 1
                                            else:
                                                self.error.append(f'ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                                    else:
                                        self.error.append(f'ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                                else:
                                    self.error.append(f'ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
                            # Validar caso por si se iguala a una operacion de literales o variables
                            else:
                                if ctx.expr():
                                    varDer = ctx.expr().getText()
                                    arraySplit = []
                                    if "+" in varDer:
                                        varDer = varDer.replace("+", " ")
                                    if "-" in varDer:
                                        varDer = varDer.replace("-", " ")
                                    if "/" in varDer:
                                        varDer = varDer.replace("/", " ")
                                    if "*" in varDer:
                                        varDer = varDer.replace("*", " ")
                                    if "%" in varDer:
                                        varDer = varDer.replace("%", " ")
                                    if "(" in varDer:
                                        varDer = varDer.replace("(", " ")
                                    if ")" in varDer:
                                        varDer = varDer.replace(")", " ")
                                    arraySplit = varDer.split(" ")
                                    arrayTypes = []
                                    for i in arraySplit:
                                        if self.tablas.varExists(i, self.scopeActual):
                                            varInfo = self.tablas.getVariable(i, self.scopeActual)
                                            arrayTypes.append(varInfo[1])
                                        elif i == 'True' or i == 'False':
                                            arrayTypes.append('boolean')
                                        elif "'" in i:
                                            arrayTypes.append('string')
                                        else:
                                            try:
                                                int(i)
                                                arrayTypes.append('int')
                                            except:
                                                self.error.append(f'ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                                    setArrayTypes = set(arrayTypes)
                                    if len(setArrayTypes) > 1:
                                        self.error.append(f'ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                                    else:
                                        arrayTypes2 = list(arrayTypes)
                                        if arrayTypes2[0] != tipo:
                                            self.error.append(f'ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                        else:
                            self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                    else:
                        self.error.append(f'ERROR: La posición del array no es valida, linea: {ctx.start.line}')
            # Caso de una variable de una estructura
            # elif
        elif ctx.method_call():
            name = ctx.method_call().method_call_inter().method_name().getText()
            actualParams = ctx.method_call().method_call_inter().expr()
            if self.tablas.metodoExists(name):
                methodParams = self.tablas.getMetodo(name)[2]
                if len(actualParams) == len(methodParams):
                    cont = 0
                    for i in actualParams:
                        var = i.getText()
                        if i.location():
                            var2 = i.location().array_id().ID()
                        tipo = ''
                        if self.tablas.varExists(var, self.scopeActual):
                            varInfo = self.tablas.getVariable(var, self.scopeActual)
                            tipo = varInfo[1]
                        elif self.tablas.arrayExists(var2, self.scopeActual):
                            varInfo = self.tablas.getArray(var2, self.scopeActual)
                            tipo = varInfo[1]
                        elif var == 'True' or var == 'False':
                            tipo = 'boolean'
                        elif "'" in var:
                            tipo = 'string'
                        else:
                            try:
                                int(var)
                                tipo = 'int'
                            except:
                                self.error.append(f'ERROR: El parametro "{var}" no es una variable existente ni un tipo valido, linea: {ctx.start.line}')
                        if tipo != '':
                            param = methodParams[cont]
                            if param[0] != tipo:
                                self.error.append(f'ERROR: El tipo del parametro "{cont + 1}" no es el esperado en la funcion "{name}", se espera "{param[0]}" y se envio "{tipo}", linea: {ctx.start.line}')
                        cont += 1
                else:
                    self.error.append(f'ERROR: La cantidad de parametros enviados al método "{name}" no es la correcta, linea: {ctx.start.line}')
            else:
                self.error.append(f'ERROR: El método "{name}" no es esta definido, linea: {ctx.start.line}')
        elif 'struct' in ctx.getText():
            print('struct')
            print(ctx.getText())
        elif "[" in ctx.getText() and "]" in ctx.getText():
            name = ctx.location().array_id().ID()
            if self.tablas.arrayExists(name, self.scopeActual):
                var = self.tablas.getArray(name, self.scopeActual)
                if isinstance(var, list):
                    if var[2] != 'array':
                        self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
                else:
                    self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
            else:
                self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')

    def exitStatement(self, ctx: DecafParser.StatementContext):
        if 'if' in ctx.getText() or 'for' in ctx.getText() or 'while' in ctx.getText() or 'else' in ctx.getText():
            # print('antes')
            # print(self.scopes)
            self.scopes.pop()
            self.scopeActual = self.scopes[len(self.scopes)-1]
            # print('exit: ', ctx.getText())
            # print('despues')
            # print(self.scopes)
            # print(self.scopeActual)

    def enterVardeclr(self, ctx: DecafParser.VardeclrContext):
        for i in range(len(ctx.field_var())):
            fieldVar = ctx.field_var()[i]
            type = ctx.var_type()[i].getText()
            if fieldVar.var_id():
                name = fieldVar.var_id().getText()
                if not self.tablas.varExistsOnce(name, self.scopeActual):
                    self.contVariables += 1
                    self.tablas.setVariable(self.contVariables, name, type, self.scopeActual)
                else:
                    self.error.append(f'ERROR: La variable "{name}" ya existe en el método "{self.scopeActual}", linea: {ctx.start.line}')
            elif fieldVar.array_id():
                name = fieldVar.array_id().ID().getText()
                if fieldVar.array_id().int_literal():
                    tam = int(fieldVar.array_id().int_literal().getText())
                    if tam <= 0 or tam == None:
                        self.error.append(f'ERROR: El tamaño del array "{name}" debe de ser un número mayor a 0, linea: {ctx.start.line}')
                    else:
                        if not self.tablas.varExistsOnce(name, self.scopeActual):
                            self.contEstructuras += 1
                            self.tablas.setEstructura(self.contEstructuras, name, type, 'array', self.scopeActual, tam)
                        else:
                            self.error.append(f'ERROR: La variable "{name}" ya existe en el método "{self.scopeActual}", linea: {ctx.start.line}')
                else:
                    self.error.append(f'ERROR: El tamaño del array "{name}" debe de ser un numero mayor a 0, linea: {ctx.start.line}')

    def enterMethod_declr(self, ctx: DecafParser.Method_declrContext):
        name = ctx.method_name().getText()
        if not self.tablas.metodoExists(name):
            self.contFunciones += 1
            returnName = ctx.return_type().getText()
            self.scopes.append(name)
            self.scopeActual = name
            retorna = False
            for i in ctx.block().statement():
                if i.RETURN():
                  retorna = True
            if name == "main":
                self.notMainFunction = False
            arrayParams = []
            if ctx.VOID():
                arrayParams.append(ctx.VOID().getText())
            else:
                for i in range(len(ctx.var_id())):
                    param1 = ctx.var_type()[i].getText()
                    param2 = ctx.var_id()[i].getText()
                    if not self.tablas.varExistsOnce(name, self.scopeActual):
                        self.contVariables += 1
                        self.tablas.setVariable(self.contVariables, param2, param1, self.scopeActual)
                        arrayParams.append([param1, param2])
                    else:
                        self.error.append(f'ERROR: La variable "{param2}" ya existe en el método "{self.scopeActual}", linea: {ctx.start.line}')

            self.tablas.setMetodo(self.contFunciones, name, returnName, arrayParams, self.scopes[len(self.scopes)-2], retorna)
        else:
            self.error.append(f'ERROR: El método "{name}" ya existe, linea: {ctx.start.line}')

    def exitMethod_declr(self, ctx: DecafParser.Method_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    def enterStruct_declr(self, ctx: DecafParser.Struct_declrContext):
        self.contEstructuras += 1
        name = ctx.ID().getText()
        self.scopes.append(name)
        self.scopeActual = name
        if not self.tablas.estruturaExists(name):
            self.tablas.setEstructura(self.contEstructuras, name, '', 'struct', 'global')

    def exitStruct_declr(self, ctx: DecafParser.Struct_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

def main():
    # data = open('./pruebas/simpletests.txt').read()
    data = open('./pruebas/multiple_tests.txt').read()
    lexer = DecafLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()

    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    print()
    printer.tablas.showFullDicc()

    if printer.notMainFunction:
        printer.error.append("El metodo main no esta defindo")
    if len(printer.getErrors()) > 0:
        print()
        print('Errores')
        for i in printer.getErrors():
            print(i)



main()