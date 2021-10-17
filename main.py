from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from DecafLexer import DecafLexer
from DecafListener import DecafListener
from DecafParser import DecafParser
from tablas import *
import pickle5 as pickle
import sys

class Proyecto1(DecafListener):
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
        self.offsetDicc = {}

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
            self.contFunciones += 1
            self.tablas.setMetodo(self.contFunciones, scope, '', [], self.scopes[len(self.scopes)-2])
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
                            if var[1] == 'int' or var[1] == 'boolean' or var[1] == 'char':
                                arrayTypes.append(var[1])
                            else:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'50ERROR: La condicion no es valida, linea: {ctx.start.line}')
                        elif "." in i:
                            arraySplit2 = i.split(".")
                            tam = len(arraySplit2)
                            contNuevo = 1
                            structNameDer = self.scopeActual
                            tipo = ''
                            for i in arraySplit2:
                                if "[" in i and "]" in i:
                                    index = i.find("[")
                                    value = i[0:index]
                                    if self.tablas.arrayExists(value, structNameDer):
                                        var = self.tablas.getArray(value, structNameDer)
                                        structNameDer = var[1]
                                        tipo = var[1]
                                        if contNuevo == tam:
                                            arrayTypes.append(tipo)
                                    else:
                                        self.error.append(f'67ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                else:
                                    if contNuevo == tam:
                                        if self.tablas.varExists(i, structNameDer):
                                            var = self.tablas.getVariable(i, structNameDer)
                                            tipo = var[1]
                                            arrayTypes.append(tipo)
                                        else:
                                            self.error.append(f'76ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                    else:
                                        if self.tablas.structVarExists(i, structNameDer):
                                            struct = self.tablas.getStructVar(i, structNameDer)
                                            structNameDer = struct[1]
                                        else:
                                            self.error.append(f'82ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                contNuevo += 1
                            # if tipo != returnType:
                            #     self.error.append(f'ERROR: El tipo de la variable "{var[0]}" no es del tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                        elif '[' in i and ']' in i:
                            pass
                        elif i == 'True' or i == 'False':
                            arrayTypes.append('boolean')
                        elif "'" in i:
                            arrayTypes.append('char')
                        else:
                            try:
                                int(i)
                                arrayTypes.append('int')
                            except:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'97ERROR: La condicion no es valida, linea: {ctx.start.line}')

                    setTypes = set(arrayTypes)
                    if len(setTypes) > 1:
                        self.contStatements -= 1
                        error = True
                        self.error.append(f'103ERROR: Ambos lados de la condicion deben ser el mismo tipo, linea: {ctx.start.line}')
            elif ctx.expr().bin_op().rel_op():
                if binOp == ">=" or binOp == "<=" or binOp == ">" or binOp == "<":
                    arraySplit = ctx.expr().getText().split(binOp)
                    for i in arraySplit:
                        if '[' in i and ']' in i:
                            var = self.tablas.getArray(i[0:i.find('[')], self.scopes[len(self.scopes)-2])
                        else:
                            var = self.tablas.getVariable(i, self.scopes[len(self.scopes)-2])
                        if isinstance(var, list):
                            if var[1] == 'int':
                                arrayTypes.append(var[1])
                            else:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'115ERROR: La condicion no es valida, linea: {ctx.start.line}')
                        else:
                            try:
                                int(i)
                                arrayTypes.append('int')
                            except:
                                self.contStatements -= 1
                                error = True
                                self.error.append(f'123ERROR: La condicion no es valida, linea: {ctx.start.line}')
                    setTypes = set(arrayTypes)
                    if len(setTypes) > 1:
                        self.contStatements -= 1
                        error = True
                        self.error.append(f'128ERROR: Ambos lados de la condicion deben ser el mismo tipo, linea: {ctx.start.line}')
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
            if "if" not in metodo[0]:
                if returnType == 'void' or returnType == '':
                    self.error.append(f'141ERROR: Hay un error en el método "{self.scopeActual}", es de tipo void y tiene un return, linea: {ctx.start.line}')
                else:
                    if ctx.expr().location():
                        if ctx.expr().location().var_id():
                            if ctx.expr().location().var_id().POINT():
                                exp = ctx.expr().getText()
                                if "." in exp:
                                    arrayExp = exp.split(".")
                                    tam = len(arrayExp)
                                    contNuevo = 1
                                    structNameDer = self.scopeActual
                                    tipo = ''
                                    for i in arrayExp:
                                        if "[" in i and "]" in i:
                                            index = i.find("[")
                                            value = i[0:index]
                                            if self.tablas.arrayExists(value, structNameDer):
                                                var = self.tablas.getArray(value, structNameDer)
                                                structNameDer = var[1]
                                                if contNuevo == tam:
                                                    tipo = var[1]
                                            else:
                                                self.error.append(f'165ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                        else:
                                            if contNuevo == tam:
                                                if self.tablas.varExists(i, structNameDer):
                                                    var = self.tablas.getVariable(i, structNameDer)
                                                    tipo = var[1]
                                                else:
                                                    self.error.append(f'173ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if self.tablas.structVarExists(i, structNameDer):
                                                    struct = self.tablas.getStructVar(i, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'179ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                        contNuevo += 1

                                    if tipo != returnType:
                                        self.error.append(f'182ERROR: El tipo de la variable "{var[0]}" no es del tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                            else:
                                varDerName = ctx.expr().location().var_id().getText()
                                if self.tablas.varExists(varDerName, self.scopeActual):
                                    variableDer = self.tablas.getVariable(varDerName, self.scopeActual)
                                    if variableDer[1] != returnType:
                                        self.error.append(f'188ERROR: El tipo de la variable "{varDerName}" no es del tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                                else:
                                    self.error.append(f'190ERROR: La variable "{varDerName}" no existe, linea: {ctx.start.line}')
                        elif ctx.expr().location().array_id():
                            if ctx.expr().location().array_id().POINT():
                                exp = ctx.expr().getText()
                                if "." in exp:
                                    arrayExp = exp.split(".")
                                    tam = len(arrayExp)
                                    contNuevo = 1
                                    structNameDer = self.scopeActual
                                    tipo = ''
                                    for i in arrayExp:
                                        if "[" in i and "]" in i:
                                            index = i.find("[")
                                            value = i[0:index]
                                            if self.tablas.arrayExists(value, structNameDer):
                                                var = self.tablas.getArray(value, structNameDer)
                                                structNameDer = var[1]
                                                if contNuevo == tam:
                                                    tipo = var[1]
                                            else:
                                                self.error.append(f'165ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                        else:
                                            if contNuevo == tam:
                                                if self.tablas.varExists(i, structNameDer):
                                                    var = self.tablas.getVariable(i, structNameDer)
                                                    tipo = var[1]
                                                else:
                                                    self.error.append(f'173ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if self.tablas.structVarExists(i, structNameDer):
                                                    struct = self.tablas.getStructVar(i, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'179ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                        contNuevo += 1

                                    if tipo != returnType:
                                        self.error.append(f'182ERROR: El tipo de la variable "{var[0]}" no es del tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                            else:
                                var = ctx.expr().location().array_id().ID()
                                posi = 0
                                if ctx.expr().location().array_id().int_literal():
                                    posi = ctx.expr().location().array_id().int_literal().getText()
                                else:
                                    self.error.append(f'200ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                if self.tablas.arrayExists(var, self.scopeActual):
                                    variableIgual = self.tablas.getArray(var, self.scopeActual)
                                    tipoIgual = variableIgual[1]
                                    if not returnType == tipoIgual:
                                        self.error.append(f'205ERROR: El tipo de la variable "{variableIgual[0]}" no es igual al tipo del metodo "{metodo[0]}", linea: {ctx.start.line}')
                                    if int(posi) <= 0 or int(posi) > variableIgual[4]:
                                        self.error.append(f'207ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                    elif ctx.expr().literal():
                        tipo = ''
                        if ctx.expr().literal().int_literal():
                            tipo = 'int'
                        elif ctx.expr().literal().bool_literal():
                            tipo = 'boolean'
                        elif ctx.expr().literal().char_literal():
                            tipo = 'char'
                        else:
                            self.error.append(f'217ERROR: El tipo de lo que retorna el método "{metodo[0]}" no es valido, linea: {ctx.start.line}')

                        if returnType != tipo and "if" not in metodo[0]:
                            self.error.append(f'220ERROR: Lo que retorna el método "{metodo[0]}" no igual al tipo del método, linea: {ctx.start.line}')
                    elif ctx.expr().method_call():
                        methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                        if self.tablas.metodoExists(methodName):
                            params = ctx.expr().method_call().method_call_inter().expr()
                            metodoDer = self.tablas.getMetodo(methodName)
                            metodoType = metodoDer[1]
                            metodoParams = metodoDer[2]
                            if metodoDer[4]:
                                if returnType != metodoType:
                                    self.error.append(f'230ERROR: El tipo del método "{metodo[0]} ({returnType})" es diferente del tipo del método "{methodName} ({metodoType})",linea: {ctx.start.line}')
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
                                                elif i.literal().char_literal():
                                                    tipo = 'char'
                                            elif i.location():
                                                if i.location().var_id():
                                                    var = i.location().var_id().getText()
                                                    if self.tablas.varExists(var, self.scopeActual):
                                                        tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                    else:
                                                        self.error.append(f'250ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                elif i.location().array_id():
                                                    var = i.location().array_id().ID().getText()
                                                    cantLocal = ''
                                                    if i.location().array_id().int_literal():
                                                        cantLocal = i.location().array_id().int_literal().getText()
                                                    else:
                                                        self.error.append(f'257ERROR: La posición del array no es valida, linea: {ctx.start.line}')

                                                    if self.tablas.arrayExists(var, self.scopeActual):
                                                        arrayVar = self.tablas.getArray(var, self.scopeActual)
                                                        tipo = arrayVar[1]
                                                        cant = arrayVar[4]
                                                        if int(cantLocal) < 0 or int(cantLocal) > cant:
                                                            self.error.append(f'264ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                                    else:
                                                        self.error.append(f'266ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                            if metodoParams[cont][0] != tipo:
                                                self.error.append(f'268ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                            cont += 1
                                    else:
                                        self.error.append(f'271ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'273ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                        else:
                            self.error.append(f'175ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
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
                                if i != '':
                                    if self.tablas.varExists(i, self.scopeActual):
                                        varInfo = self.tablas.getVariable(i, self.scopeActual)
                                        arrayTypes.append(varInfo[1])
                                    elif self.tablas.metodoExists(i):
                                        varInfo = self.tablas.getMetodo(i)
                                        arrayTypes.append(varInfo[1])
                                    elif i == 'True' or i == 'False':
                                        arrayTypes.append('boolean')
                                    elif "'" in i:
                                        arrayTypes.append('char')
                                    else:
                                        try:
                                            int(i)
                                            arrayTypes.append('int')
                                        except:
                                            self.error.append(f'309ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                            setArrayTypes = set(arrayTypes)
                            if len(setArrayTypes) > 1:
                                self.error.append(f'312ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
                            else:
                                arrayTypes2 = list(setArrayTypes)
                                if arrayTypes2[0] != returnType:
                                    self.error.append(f'316ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
            else:
                self.tablas.metodoSetReturn(metodo[3])
        elif ctx.location():
            if ctx.location().var_id():
                if ctx.location().var_id().POINT():
                    exp = ctx.location().var_id().getText()
                    arrayExp = []
                    if "." in exp:
                        arrayExp = exp.split(".")
                        tam = len(arrayExp)
                        cont = 1
                        structName = self.scopeActual
                        tipoIzq = ''
                        var = ''
                        for i in arrayExp:
                            if "[" in i and "]" in i:
                                index = i.find("[")
                                value = i[0:index]
                                if self.tablas.arrayExists(value, structName):
                                    struct = self.tablas.getArray(value, structName)
                                    structName = struct[1]
                                else:
                                    self.error.append(f'337ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                            else:
                                if cont == tam:
                                    if self.tablas.varExists(i, structName):
                                        var = self.tablas.getVariable(i, structName)
                                        tipoIzq = var[1]
                                    else:
                                        self.error.append(f'344ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                else:
                                    if self.tablas.structVarExists(i, structName):
                                        struct = self.tablas.getStructVar(i, structName)
                                        structName = struct[1]
                                    else:
                                        self.error.append(f'350ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                            cont += 1

                        entro = False
                        tipoDer = ''
                        expDer =''
                        if ctx.expr().literal():
                            if ctx.expr().literal().int_literal():
                                tipoDer = 'int'
                            elif ctx.expr().literal().bool_literal():
                                tipoDer = 'boolean'
                            elif ctx.expr().literal().char_literal():
                                tipoDer = 'char'
                        elif ctx.expr().location():
                            varDer = ctx.expr().location().getText()
                            if ctx.expr().location().array_id():
                                if ctx.expr().location().array_id().POINT():
                                    arrayExpDer = []
                                    if "." in varDer:
                                        arrayExpDer = varDer.split(".")
                                        tamNuevo = len(arrayExpDer)
                                        contNuevo = 1
                                        structNameDer = self.scopeActual
                                        for i in arrayExpDer:
                                            if "[" in i and "]" in i:
                                                index = i.find("[")
                                                value = i[0:index]
                                                if self.tablas.arrayExists(value, structNameDer):
                                                    struct = self.tablas.getArray(value, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'381ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if contNuevo == tamNuevo:
                                                    if self.tablas.varExists(i, structNameDer):
                                                        entro = True
                                                        varDer = self.tablas.getVariable(i, structNameDer)
                                                        tipoDer = varDer[1]
                                                    else:
                                                        self.error.append(f'389ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                                else:
                                                    if self.tablas.structVarExists(i, structNameDer):
                                                        struct = self.tablas.getStructVar(i, structNameDer)
                                                        structNameDer = struct[1]
                                                    else:
                                                        self.error.append(f'395ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                            contNuevo += 1
                                else:
                                    varDer = ctx.expr().location().array_id().ID()
                                    posi = 0
                                    if ctx.expr().location().array_id().int_literal():
                                        posi = ctx.expr().location().array_id().int_literal().getText()
                                    else:
                                        self.error.append(f'403ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                    if self.tablas.arrayExists(varDer, self.scopeActual):
                                        tama = self.tablas.getArray(varDer, self.scopeActual)[4]
                                        if str(tama) < posi or str(tama) == 0:
                                            self.error.append(f'407ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                            elif ctx.expr().location().var_id().POINT():
                                varDer = ctx.expr().location().var_id().getText()
                                arrayExpDer = []
                                if "." in varDer:
                                    arrayExpDer = varDer.split(".")
                                    tam = len(arrayExpDer)
                                    contNuevo = 1
                                    structNameDer = self.scopeActual
                                    for j in arrayExpDer:
                                        if "[" in j and "]" in j:
                                            index = j.find("[")
                                            value = j[0:index]
                                            if self.tablas.arrayExists(value, structNameDer):
                                                struct = self.tablas.getArray(value, structNameDer)
                                                structNameDer = struct[1]
                                            else:
                                                self.error.append(f'424ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                        else:
                                            if contNuevo == tam:
                                                if self.tablas.varExists(j, structNameDer):
                                                    varDer2 = self.tablas.getVariable(j, structNameDer)
                                                    entro = True
                                                    tipoDer = varDer2[1]
                                                    varDer = varDer2[0]
                                                else:
                                                    self.error.append(f'433ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if self.tablas.structVarExists(j, structNameDer):
                                                    struct = self.tablas.getStructVar(j, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'439ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                        contNuevo += 1
                            if self.tablas.varExists(varDer, self.scopeActual):
                                variableIgual = self.tablas.getVariable(varDer, self.scopeActual)
                                tipoDer = variableIgual[1]
                            elif self.tablas.arrayExists(varDer, self.scopeActual):
                                variableIgual = self.tablas.getArray(varDer, self.scopeActual)
                                tipoDer = variableIgual[1]
                            elif entro:
                                pass
                            else:
                                self.error.append(f'450ERROR: La variable "{varDer}" no existe, linea: {ctx.start.line}')
                        elif ctx.expr().method_call():
                            methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                            if self.tablas.metodoExists(methodName):
                                params = ctx.expr().method_call().method_call_inter().expr()
                                metodo = self.tablas.getMetodo(methodName)
                                metodoType = metodo[1]
                                metodoParams = metodo[2]
                                if metodo[4]:
                                    if tipoIzq != metodoType:
                                        self.error.append(f'460ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{var[0]} ({tipoIzq})",linea: {ctx.start.line}')
                                    else:
                                        tipoDer = metodoType
                                        if len(params) == len(metodoParams):
                                            cont = 0
                                            for i in params:
                                                if i.literal():
                                                    if i.literal().int_literal():
                                                        tipo = 'int'
                                                    elif i.literal().bool_literal():
                                                        tipo = 'boolean'
                                                    elif i.literal().char_literal():
                                                        tipo = 'char'
                                                elif i.location():
                                                    tipo = ''
                                                    varDer = i.location().getText()
                                                    if i.location().array_id():
                                                        varDer = i.location().array_id().ID()
                                                        posi = 0
                                                        if i.location().array_id().int_literal():
                                                            posi = i.location().array_id().int_literal().getText()
                                                        else:
                                                            self.error.append(f'482ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                                    elif i.location().var_id().POINT():
                                                        expDer = i.location().var_id().getText()
                                                        arrayExpDer = []
                                                        if "." in expDer:
                                                            arrayExpDer = expDer.split(".")
                                                            tam = len(arrayExpDer)
                                                            contNuevo = 1
                                                            structNameDer = self.scopeActual
                                                            for j in arrayExpDer:
                                                                if contNuevo == tam:
                                                                    if self.tablas.varExists(j, structNameDer):
                                                                        varDer2 = self.tablas.getVariable(j, structNameDer)
                                                                        entro = True
                                                                        tipoDer = varDer2[1]
                                                                        varDer = varDer2[0]
                                                                        tipo = tipoDer
                                                                    else:
                                                                        self.error.append(f'500ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                else:
                                                                    if self.tablas.structVarExists(j, structNameDer):
                                                                        struct = self.tablas.getStructVar(j, structNameDer)
                                                                        structNameDer = struct[1]
                                                                    else:
                                                                        self.error.append(f'506ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                contNuevo += 1
                                                    if self.tablas.varExists(varDer, self.scopeActual):
                                                        tipo = self.tablas.getVariable(varDer, self.scopeActual)[1]
                                                    elif self.tablas.arrayExists(varDer, self.scopeActual):
                                                        tipo = self.tablas.getArray(varDer, self.scopeActual)[1]
                                                    elif entro:
                                                        pass
                                                    else:
                                                        self.error.append(f'515ERROR: La variable "{varDer}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                if metodoParams[cont][0] != tipo:
                                                    self.error.append(f'517ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                                cont += 1
                                        else:
                                            self.error.append(f'520ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                                else:
                                    self.error.append(f'522ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'524ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
                        else:
                            self.error.append(f'526ERROR: Se debe igualar a algo valido,linea: {ctx.start.line}')

                        if tipoIzq != tipoDer:
                            self.error.append(f'529ERROR: La variable "{exp}" se debe igualar a algo del mismo tipo, linea: {ctx.start.line}')
                    else:
                        self.error.append(f'531ERROR: Struct invalida, linea: {ctx.start.line}')
                else:
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
                            elif ctx.expr().literal().char_literal():
                                valor = ctx.expr().literal().char_literal().getText()

                            if tipo == "char":
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
                                self.error.append(f'573ERROR: Hay un error en el valor de la variable "{name}", linea: {ctx.start.line}')
                        # Si se iguala a una variable
                        elif ctx.expr().location():
                            var = ctx.expr().location().getText()
                            if ctx.expr().location().array_id():
                                var = ctx.expr().location().array_id().ID()
                                posi = 0
                                if  ctx.expr().location().array_id().int_literal():
                                    posi = ctx.expr().location().array_id().int_literal().getText()
                                elif ctx.expr().location().array_id().var_id():
                                   pass
                                else:
                                    self.error.append(f'583ERROR: La posición del array no es valida, linea: {ctx.start.line}')

                            if self.tablas.varExists(var, self.scopeActual):
                                variableIgual = self.tablas.getVariable(var, self.scopeActual)
                                tipoIgual = variableIgual[1]
                                if not tipo == tipoIgual:
                                    self.error.append(f'589ERROR: El tipo de la variable "{variableIgual[0]}" no es igual que al de "{variable[0]}", linea: {ctx.start.line}')
                            elif self.tablas.arrayExists(var, self.scopeActual):
                                variableIgual = self.tablas.getArray(var, self.scopeActual)
                                tipoIgual = variableIgual[1]
                                if not tipo == tipoIgual:
                                    self.error.append(f'594ERROR: El tipo de la variable "{variableIgual[0]}" no es igual que al de "{variable[0]}", linea: {ctx.start.line}')
                                if int(posi) < 0 or int(posi) > variableIgual[4]:
                                    self.error.append(f'596ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'598ERROR: La variable "{var}" no existe, linea: {ctx.start.line}')
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
                                        self.error.append(f'610ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{name} ({varType})",linea: {ctx.start.line}')
                                    else:
                                        if len(params) == len(metodoParams):
                                            cont = 0
                                            for i in params:
                                                if i.literal():
                                                    if i.literal().int_literal():
                                                        tipo = 'int'
                                                    elif i.literal().bool_literal():
                                                        tipo = 'boolean'
                                                    elif i.literal().char_literal():
                                                        tipo = 'char'
                                                elif i.location():
                                                    var = i.location().getText()
                                                    entro = False
                                                    if i.location().array_id():
                                                        var = i.location().array_id().ID()
                                                        if i.location().array_id().POINT():
                                                            exp = i.location().array_id().getText()
                                                            arrayExpDer = []
                                                            varParam = ''
                                                            if "." in exp:
                                                                arrayExpDer = exp.split(".")
                                                                tam = len(arrayExpDer)
                                                                contNuevo = 1
                                                                structNameDer = self.scopeActual
                                                                tipo = ''
                                                                for j in arrayExpDer:
                                                                    if "[" in j and "]" in j:
                                                                        index = j.find("[")
                                                                        value = j[0:index]
                                                                        if self.tablas.arrayExists(value, structNameDer):
                                                                            varParam = self.tablas.getArray(value, structNameDer)
                                                                            structNameDer = varParam[1]
                                                                            tipo = varParam[1]
                                                                            if contNuevo == tam:
                                                                                entro = True
                                                                        else:
                                                                            self.error.append(f'647ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                                                    else:
                                                                        if contNuevo == tam:
                                                                            if self.tablas.varExists(j, structNameDer):
                                                                                varParam = self.tablas.getVariable(j, structNameDer)
                                                                                tipo = varParam[1]
                                                                                entro = True
                                                                            else:
                                                                                self.error.append(f'655ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                        else:
                                                                            if self.tablas.structVarExists(j, structNameDer):
                                                                                struct = self.tablas.getStructVar(j, structNameDer)
                                                                                structNameDer = struct[1]
                                                                            else:
                                                                                self.error.append(f'661ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                    contNuevo += 1
                                                    elif i.location().var_id():
                                                        if i.location().var_id().POINT():
                                                            exp = i.location().var_id().getText()
                                                            arrayExpDer = []
                                                            varParam = ''
                                                            if "." in exp:
                                                                arrayExpDer = exp.split(".")
                                                                tam = len(arrayExpDer)
                                                                contNuevo = 1
                                                                structNameDer = self.scopeActual
                                                                tipo = ''
                                                                for j in arrayExpDer:
                                                                    if "[" in j and "]" in j:
                                                                        index = j.find("[")
                                                                        value = j[0:index]
                                                                        if self.tablas.arrayExists(value, structNameDer):
                                                                            varParam = self.tablas.getArray(value, structNameDer)
                                                                            structNameDer = varParam[1]
                                                                            if contNuevo == tam:
                                                                                entro = True
                                                                        else:
                                                                            self.error.append(f'684ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                                                    else:
                                                                        if contNuevo == tam:
                                                                            if self.tablas.varExists(j, structNameDer):
                                                                                varParam = self.tablas.getVariable(j, structNameDer)
                                                                                tipo = varParam[1]
                                                                                entro = True
                                                                            else:
                                                                                self.error.append(f'692ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                        else:
                                                                            if self.tablas.structVarExists(j, structNameDer):
                                                                                struct = self.tablas.getStructVar(j, structNameDer)
                                                                                structNameDer = struct[1]
                                                                            else:
                                                                                self.error.append(f'698ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                    contNuevo += 1
                                                    if entro:
                                                        pass
                                                    elif self.tablas.varExists(var, self.scopeActual):
                                                        tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                    elif self.tablas.arrayExists(var, self.scopeActual):
                                                        tipo = self.tablas.getArray(var, self.scopeActual)[1]
                                                    else:
                                                        self.error.append(f'707ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                if metodoParams[cont][0] != tipo:
                                                    self.error.append(f'709ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                                cont += 1
                                        else:
                                            self.error.append(f'712ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                                else:
                                    self.error.append(f'714ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'716ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
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
                                    if len(i) > 0 and '!' not in i:
                                        if self.tablas.varExists(i, self.scopeActual):
                                            varInfo = self.tablas.getVariable(i, self.scopeActual)
                                            arrayTypes.append(varInfo[1])
                                        elif i == 'True' or i == 'False':
                                            arrayTypes.append('boolean')
                                        elif "'" in i:
                                            arrayTypes.append('char')
                                        else:
                                            try:
                                                int(i)
                                                arrayTypes.append('int')
                                            except:
                                                self.error.append(f'751ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                                setArrayTypes = set(arrayTypes)
                                if len(setArrayTypes) > 1:
                                    self.error.append(f'754ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                                else:
                                    arrayTypes2 = list(arrayTypes)
                                    if len(arrayTypes2) != 0:
                                        if arrayTypes2[0] != tipo:
                                            self.error.append(f'758ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                    else:
                        self.error.append(f'760ERROR: La variable "{name}" no esta definida, linea: {ctx.start.line}')
            elif ctx.location().array_id():
                if ctx.location().array_id().POINT():
                    exp = ctx.location().array_id().getText()
                    arrayExpDer = []
                    var = ''
                    if "." in exp:
                        arrayExpDer = exp.split(".")
                        tam = len(arrayExpDer)
                        cont = 1
                        structNameDer = self.scopeActual
                        tipoIzq = ''
                        for j in arrayExpDer:
                            if "[" in j and "]" in j:
                                index = j.find("[")
                                value = j[0:index]
                                existe = self.tablas.arrayExists(value, structNameDer)
                                if existe:
                                    var = self.tablas.getArray(value, structNameDer)
                                    structNameDer = var[1]
                                    if cont == tam:
                                        tipoIzq = var[1]
                                else:
                                    self.error.append(f'782ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                            else:
                                if cont == tam:
                                    if self.tablas.varExists(j, structNameDer):
                                        var = self.tablas.getVariable(j, structNameDer)
                                        tipoIzq = var[1]
                                    else:
                                        self.error.append(f'789ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                else:
                                    if self.tablas.structVarExists(j, structNameDer):
                                        struct = self.tablas.getStructVar(j, structNameDer)
                                        structNameDer = struct[1]
                                    else:
                                        self.error.append(f'795ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                            cont += 1

                        entro = False
                        tipoDer = ''
                        expDer =''
                        if ctx.expr().literal():
                            if ctx.expr().literal().int_literal():
                                tipoDer = 'int'
                            elif ctx.expr().literal().bool_literal():
                                tipoDer = 'boolean'
                            elif ctx.expr().literal().char_literal():
                                tipoDer = 'char'
                        elif ctx.expr().location():
                            varDer = ctx.expr().location().getText()
                            if ctx.expr().location().array_id():
                                if ctx.expr().location().array_id().POINT():
                                    arrayExpDer = []
                                    if "." in varDer:
                                        arrayExpDer = varDer.split(".")
                                        tamNuevo = len(arrayExpDer)
                                        contNuevo = 1
                                        structNameDer = self.scopeActual
                                        for i in arrayExpDer:
                                            if "[" in i and "]" in i:
                                                index = i.find("[")
                                                value = i[0:index]
                                                if self.tablas.arrayExists(value, structNameDer):
                                                    struct = self.tablas.getArray(value, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'826ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if contNuevo == tamNuevo:
                                                    if self.tablas.varExists(i, structNameDer):
                                                        entro = True
                                                        varDer = self.tablas.getVariable(i, structNameDer)
                                                        tipoDer = varDer[1]
                                                    else:
                                                        self.error.append(f'834ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                                else:
                                                    if self.tablas.structVarExists(i, structNameDer):
                                                        struct = self.tablas.getStructVar(i, structNameDer)
                                                        structNameDer = struct[1]
                                                    else:
                                                        self.error.append(f'840ERROR: La variable "{i}" no existe, linea: {ctx.start.line}')
                                            contNuevo += 1
                                else:
                                    varDer = ctx.expr().location().array_id().ID()
                                    posi = 0
                                    if ctx.expr().location().array_id().int_literal():
                                        posi = ctx.expr().location().array_id().int_literal().getText()
                                    else:
                                        self.error.append(f'848ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                    if self.tablas.arrayExists(varDer, self.scopeActual):
                                        tama = self.tablas.getArray(varDer, self.scopeActual)[4]
                                        if str(tama) < posi or str(tama) == 0:
                                            self.error.append(f'852ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                            elif ctx.expr().location().var_id().POINT():
                                varDer = ctx.expr().location().var_id().getText()
                                arrayExpDer = []
                                if "." in varDer:
                                    arrayExpDer = varDer.split(".")
                                    tam = len(arrayExpDer)
                                    contNuevo = 1
                                    structNameDer = self.scopeActual
                                    for j in arrayExpDer:
                                        if "[" in j and "]" in j:
                                            index = j.find("[")
                                            value = j[0:index]
                                            if self.tablas.arrayExists(value, structNameDer):
                                                struct = self.tablas.getArray(value, structNameDer)
                                                structNameDer = struct[1]
                                                if contNuevo == tam:
                                                    entro = True
                                                    tipoDer = var[1]
                                                    varDer = struct[0]
                                            else:
                                                self.error.append(f'869ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                        else:
                                            if contNuevo == tam:
                                                if self.tablas.varExists(j, structNameDer):
                                                    var = self.tablas.getVariable(j, structNameDer)
                                                    entro = True
                                                    tipoDer = var[1]
                                                    varDer = var[0]
                                                else:
                                                    self.error.append(f'878ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if self.tablas.structVarExists(j, structNameDer):
                                                    struct = self.tablas.getStructVar(j, structNameDer)
                                                    structNameDer = struct[1]
                                                else:
                                                    self.error.append(f'884ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                        contNuevo += 1
                            if self.tablas.varExists(varDer, self.scopeActual):
                                variableIgual = self.tablas.getVariable(varDer, self.scopeActual)
                                tipoDer = variableIgual[1]
                            elif self.tablas.arrayExists(varDer, self.scopeActual):
                                variableIgual = self.tablas.getArray(varDer, self.scopeActual)
                                tipoDer = variableIgual[1]
                            elif entro:
                                pass
                            else:
                                self.error.append(f'895ERROR: La variable "{varDer}" no existe, linea: {ctx.start.line}')
                        elif ctx.expr().method_call():
                            methodName = ctx.expr().method_call().method_call_inter().method_name().getText()
                            if self.tablas.metodoExists(methodName):
                                params = ctx.expr().method_call().method_call_inter().expr()
                                metodo = self.tablas.getMetodo(methodName)
                                metodoType = metodo[1]
                                metodoParams = metodo[2]
                                tipoDer = metodoType
                                if metodo[4]:
                                    if tipoIzq != metodoType:
                                        self.error.append(f'905ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{var[0]} ({tipoIzq})",linea: {ctx.start.line}')
                                    else:
                                        if len(params) == len(metodoParams):
                                            cont = 0
                                            for i in params:
                                                if i.literal():
                                                    if i.literal().int_literal():
                                                        tipo = 'int'
                                                    elif i.literal().bool_literal():
                                                        tipo = 'boolean'
                                                    elif i.literal().char_literal():
                                                        tipo = 'char'
                                                elif i.location():
                                                    tipo = ''
                                                    varDer = i.location().getText()
                                                    if i.location().array_id():
                                                        if i.location().array_id().POINT():
                                                            arrayExpDer = []
                                                            if "." in varDer:
                                                                arrayExpDer = varDer.split(".")
                                                                tam = len(arrayExpDer)
                                                                contNuevo = 1
                                                                structNameDer = self.scopeActual
                                                                for j in arrayExpDer:
                                                                    if "[" in j and "]" in j:
                                                                        index = j.find("[")
                                                                        value = j[0:index]
                                                                        if self.tablas.arrayExists(value, structNameDer):
                                                                            struct = self.tablas.getArray(value, structNameDer)
                                                                            structNameDer = struct[1]
                                                                            if contNuevo == tam:
                                                                                entro = True
                                                                                tipoDer = var[1]
                                                                                varDer = struct[0]
                                                                                tipo = tipoDer
                                                                        else:
                                                                            self.error.append(f'869ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                                                    else:
                                                                        if contNuevo == tam:
                                                                            if self.tablas.varExists(j, structNameDer):
                                                                                varDer2 = self.tablas.getVariable(j, structNameDer)
                                                                                entro = True
                                                                                tipoDer = varDer2[1]
                                                                                varDer = varDer2[0]
                                                                                tipo = tipoDer
                                                                            else:
                                                                                self.error.append(f'945ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                        else:
                                                                            if self.tablas.structVarExists(j, structNameDer):
                                                                                struct = self.tablas.getStructVar(j, structNameDer)
                                                                                structNameDer = struct[1]
                                                                            else:
                                                                                self.error.append(f'951ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                    contNuevo += 1
                                                        else:
                                                            varDer = i.location().array_id().ID()
                                                            posi = 0
                                                            if i.location().array_id().int_literal():
                                                                posi = i.location().array_id().int_literal().getText()
                                                            elif i.location().array_id().var_id():
                                                                varPosi = i.location().array_id().var_id().getText()
                                                                if self.tablas.varExists(varPosi, self.scopeActual):
                                                                    varPosiInfo = self.tablas.getVariable(varPosi, self.scopeActual)
                                                                    if varPosiInfo[1] != 'int':
                                                                        self.error.append(f'927ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                                            else:
                                                                self.error.append(f'927ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                                                    elif i.location().var_id().POINT():
                                                        expDer = i.location().var_id().getText()
                                                        arrayExpDer = []
                                                        if "." in expDer:
                                                            arrayExpDer = expDer.split(".")
                                                            tam = len(arrayExpDer)
                                                            contNuevo = 1
                                                            structNameDer = self.scopeActual
                                                            for j in arrayExpDer:
                                                                if "[" in j and "]" in j:
                                                                    index = j.find("[")
                                                                    value = j[0:index]
                                                                    if self.tablas.arrayExists(value, structNameDer):
                                                                        struct = self.tablas.getArray(value, structNameDer)
                                                                        structNameDer = struct[1]
                                                                        if contNuevo == tam:
                                                                            entro = True
                                                                            tipoDer = var[1]
                                                                            varDer = struct[0]
                                                                    else:
                                                                        self.error.append(f'869ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                                                else:
                                                                    if contNuevo == tam:
                                                                        if self.tablas.varExists(j, structNameDer):
                                                                            varDer2 = self.tablas.getVariable(j, structNameDer)
                                                                            entro = True
                                                                            tipoDer = varDer2[1]
                                                                            varDer = varDer2[0]
                                                                            tipo = tipoDer
                                                                        else:
                                                                            self.error.append(f'945ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                    else:
                                                                        if self.tablas.structVarExists(j, structNameDer):
                                                                            struct = self.tablas.getStructVar(j, structNameDer)
                                                                            structNameDer = struct[1]
                                                                        else:
                                                                            self.error.append(f'951ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                                contNuevo += 1
                                                    if self.tablas.varExists(varDer, self.scopeActual):
                                                        tipo = self.tablas.getVariable(varDer, self.scopeActual)[1]
                                                    elif self.tablas.arrayExists(varDer, self.scopeActual):
                                                        tipo = self.tablas.getArray(varDer, self.scopeActual)[1]
                                                    elif entro:
                                                        pass
                                                    else:
                                                        self.error.append(f'960ERROR: La variable "{varDer}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                if metodoParams[cont][0] != tipo:
                                                    self.error.append(f'962ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                                cont += 1
                                        else:
                                            self.error.append(f'965ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                                else:
                                    self.error.append(f'967ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                            else:
                                self.error.append(f'969ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
                        else:
                            self.error.append(f'971ERROR: Se debe igualar a algo valido,linea: {ctx.start.line}')

                        if tipoIzq != tipoDer:
                            self.error.append(f'974ERROR: La variable "{var[0]}" se debe igualar a algo del mismo tipo, linea: {ctx.start.line}')
                else:
                    varName = ctx.location().array_id().ID().getText()
                    if self.tablas.arrayExists(varName, self.scopeActual):
                        variable = self.tablas.getArray(varName, self.scopeActual)
                        tipo = variable[1]
                        if ctx.location().array_id().int_literal():
                            posi = ctx.location().array_id().int_literal().getText()
                            if int(posi) <= int(variable[4]):
                                if ctx.expr().location():
                                    if ctx.expr().location().var_id():
                                        varDerName = ctx.expr().location().var_id().getText()
                                        if self.tablas.varExists(varDerName, self.scopeActual):
                                            variableDer = self.tablas.getVariable(varDerName, self.scopeActual)
                                            if variableDer[1] != tipo:
                                                self.error.append(f'988ERROR: El tipo de la variable "{variable[0]}" no es igual que al de "{variableDer[0]}", linea: {ctx.start.line}')
                                # Validar caso por si se iguala a una literal
                                elif ctx.expr().literal():
                                    tipoDer = ''
                                    if ctx.expr().literal().int_literal():
                                        tipoDer = 'int'
                                    elif ctx.expr().literal().char_literal():
                                        tipoDer = 'char'
                                    elif ctx.expr().literal().bool_literal():
                                        tipoDer = 'boolean'

                                    if tipoDer != tipo:
                                        self.error.append(f'1000ERROR: El tipo de la variable "{variable[0]}" no es igual al tipo al que se esta igualando", linea: {ctx.start.line}')
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
                                                self.error.append(f'1012ERROR: El tipo del método "{methodName} ({metodoType})" es diferente del tipo de la variable "{variable[0]} ({varType})",linea: {ctx.start.line}')
                                            else:
                                                if len(params) == len(metodoParams):
                                                    cont = 0
                                                    for i in params:
                                                        if i.literal():
                                                            if i.literal().int_literal():
                                                                tipo = 'int'
                                                            elif i.literal().bool_literal():
                                                                tipo = 'boolean'
                                                            elif i.literal().char_literal():
                                                                tipo = 'char'
                                                        elif i.location():
                                                            var = i.location().getText()
                                                            if self.tablas.varExists(var, self.scopeActual):
                                                                tipo = self.tablas.getVariable(var, self.scopeActual)[1]
                                                            else:
                                                                self.error.append(f'1029ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe, linea: {ctx.start.line}')
                                                        if metodoParams[cont][0] != tipo:
                                                            self.error.append(f'1031ERROR: El parametro "{cont + 1}" es de tipo "{tipo}", se espera "{metodoParams[cont][0]}", linea: {ctx.start.line}')
                                                        cont += 1
                                                else:
                                                    self.error.append(f'1034ERROR: La cantidad de parametros a enviar en el método "{methodName}" no es la correcta, linea: {ctx.start.line}')
                                        else:
                                            self.error.append(f'1036ERROR: Se espera que el método "{methodName}" tenga un return, linea: {ctx.start.line}')
                                    else:
                                        self.error.append(f'1038ERROR: El método "{methodName}" no existe,linea: {ctx.start.line}')
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
                                                arrayTypes.append('char')
                                            else:
                                                try:
                                                    int(i)
                                                    arrayTypes.append('int')
                                                except:
                                                    self.error.append(f'1073ERROR: El parametro "{i}" no es un tipo valido, linea: {ctx.start.line}')
                                        setArrayTypes = set(arrayTypes)
                                        if len(setArrayTypes) > 1:
                                            self.error.append(f'1076ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                                        else:
                                            arrayTypes2 = list(setArrayTypes)
                                            if arrayTypes2[0] != tipo:
                                                self.error.append(f'1080ERROR: La variable "{variable[0]}" debe ser igual a algo del mismo tipo ({tipo}), linea: {ctx.start.line}')
                            else:
                                self.error.append(f'1082ERROR: La posición del array no es valida, linea: {ctx.start.line}')
                        elif ctx.location().array_id().var_id():
                            pass
                        else:
                            self.error.append(f'1084ERROR: La posición del array no es valida, linea: {ctx.start.line}')
        elif ctx.method_call():
            name = ctx.method_call().method_call_inter().method_name().getText()
            actualParams = ctx.method_call().method_call_inter().expr()
            if self.tablas.metodoExists(name):
                methodParams = self.tablas.getMetodo(name)[2]
                if len(actualParams) == len(methodParams):
                    cont = 0
                    for i in actualParams:
                        var = i.getText()
                        tipo = ''
                        entro = False
                        if i.location():
                            if i.location().array_id():
                                var = i.location().array_id().ID()
                                if i.location().array_id().POINT():
                                    exp = i.location().array_id().getText()
                                    arrayExpDer = []
                                    varParam = ''
                                    if "." in exp:
                                        arrayExpDer = exp.split(".")
                                        tam = len(arrayExpDer)
                                        contNuevo = 1
                                        structNameDer = self.scopeActual
                                        tipo = ''
                                        for j in arrayExpDer:
                                            if "[" in j and "]" in j:
                                                index = j.find("[")
                                                value = j[0:index]
                                                if self.tablas.arrayExists(value, structNameDer):
                                                    varParam = self.tablas.getArray(value, structNameDer)
                                                    structNameDer = varParam[1]
                                                    tipo = varParam[1]
                                                    if contNuevo == tam:
                                                        entro = True
                                                else:
                                                    self.error.append(f'1119ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if contNuevo == tam:
                                                    if self.tablas.varExists(j, structNameDer):
                                                        varParam = self.tablas.getVariable(j, structNameDer)
                                                        tipo = varParam[1]
                                                        entro = True
                                                    else:
                                                        self.error.append(f'1127ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                else:
                                                    if self.tablas.structVarExists(j, structNameDer):
                                                        struct = self.tablas.getStructVar(j, structNameDer)
                                                        structNameDer = struct[1]
                                                    else:
                                                        self.error.append(f'1133ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                            contNuevo += 1
                            elif i.location().var_id():
                                if i.location().var_id().POINT():
                                    exp = i.location().var_id().getText()
                                    arrayExpDer = []
                                    varParam = ''
                                    if "." in exp:
                                        arrayExpDer = exp.split(".")
                                        tam = len(arrayExpDer)
                                        contNuevo = 1
                                        structNameDer = self.scopeActual
                                        tipo = ''
                                        for j in arrayExpDer:
                                            if "[" in j and "]" in j:
                                                index = j.find("[")
                                                value = j[0:index]
                                                if self.tablas.arrayExists(value, structNameDer):
                                                    varParam = self.tablas.getArray(value, structNameDer)
                                                    structNameDer = varParam[1]
                                                    if contNuevo == tam:
                                                        entro = True
                                                else:
                                                    self.error.append(f'1156ERROR: La variable "{value}" no existe, linea: {ctx.start.line}')
                                            else:
                                                if contNuevo == tam:
                                                    if self.tablas.varExists(j, structNameDer):
                                                        varParam = self.tablas.getVariable(j, structNameDer)
                                                        tipo = varParam[1]
                                                        entro = True
                                                    else:
                                                        self.error.append(f'1164ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                                else:
                                                    if self.tablas.structVarExists(j, structNameDer):
                                                        struct = self.tablas.getStructVar(j, structNameDer)
                                                        structNameDer = struct[1]
                                                    else:
                                                        self.error.append(f'1170ERROR: La variable "{j}" no existe, linea: {ctx.start.line}')
                                            contNuevo += 1
                        if entro:
                            pass
                        elif self.tablas.varExists(var, self.scopeActual):
                            varInfo = self.tablas.getVariable(var, self.scopeActual)
                            tipo = varInfo[1]
                        elif self.tablas.arrayExists(var, self.scopeActual):
                            varInfo = self.tablas.getArray(var, self.scopeActual)
                            tipo = varInfo[1]
                        elif var == 'True' or var == 'False':
                            tipo = 'boolean'
                        elif "'" in var:
                            tipo = 'char'
                        else:
                            try:
                                int(var)
                                tipo = 'int'
                            except:
                                self.error.append(f'1189ERROR: El parametro "{var}" no es una variable existente ni un tipo valido, linea: {ctx.start.line}')
                        if tipo != '':
                            param = methodParams[cont]
                            if param[0] != tipo:
                                self.error.append(f'1193ERROR: El tipo del parametro "{cont + 1}" no es el esperado en la funcion "{name}", se espera "{param[0]}" y se envio "{tipo}", linea: {ctx.start.line}')
                        cont += 1
                else:
                    self.error.append(f'1196ERROR: La cantidad de parametros enviados al método "{name}" no es la correcta, linea: {ctx.start.line}')
            else:
                self.error.append(f'1198ERROR: El método "{name}" no es esta definido, linea: {ctx.start.line}')
        elif "[" in ctx.getText() and "]" in ctx.getText():
            name = ctx.location().array_id().ID()
            if self.tablas.arrayExists(name, self.scopeActual):
                var = self.tablas.getArray(name, self.scopeActual)
                if isinstance(var, list):
                    if var[2] != 'array':
                        self.error.append(f'1205ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
                else:
                    self.error.append(f'1207ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
            else:
                self.error.append(f'1209ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')

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
            if ctx.var_type()[i].STRUCT():
                type = ctx.var_type()[i].ID().getText()
                if ctx.field_var()[i].var_id():
                    name = ctx.field_var()[i].var_id().getText()
                    if not self.tablas.varExistsOnce(name, self.scopeActual):
                        if self.scopeActual in self.offsetDicc:
                            off = self.offsetDicc[self.scopeActual]
                        else:
                            self.offsetDicc[self.scopeActual] = 0
                            off = self.offsetDicc[self.scopeActual]
                        self.contVariables += 1
                        sizeVar = self.tablas.getSizeStruct(type)
                        self.tablas.setVariable(self.contVariables, name, type, self.scopeActual, 0, sizeVar, True, off)
                        self.offsetDicc[self.scopeActual] += sizeVar
                    else:
                        self.error.append(f'1232ERROR: La variable "{name}" ya existe, linea: {ctx.start.line}')
                elif ctx.field_var()[i].array_id():
                    name = ctx.field_var()[i].array_id().ID().getText()
                    if ctx.field_var()[i].array_id().int_literal():
                        tam = int(ctx.field_var()[i].array_id().int_literal().getText())
                        if tam <= 0 or tam == None:
                            self.error.append(f'1238ERROR: El tamaño del array "{name}" debe de ser un número mayor a 0, linea: {ctx.start.line}')
                        else:
                            if not self.tablas.varExistsOnce(name, self.scopeActual):
                                if self.scopeActual in self.offsetDicc:
                                    off = self.offsetDicc[self.scopeActual]
                                else:
                                    self.offsetDicc[self.scopeActual] = 0
                                    off = self.offsetDicc[self.scopeActual]
                                self.contEstructuras += 1
                                sizeVar = self.tablas.getSizeStruct(type)
                                self.tablas.setEstructura(self.contEstructuras, name, type, 'array', self.scopeActual, tam, True, sizeVar, off)
                                self.offsetDicc[self.scopeActual] += sizeVar
                            else:
                                self.error.append(f'1244ERROR: La variable "{name}" ya existe, linea: {ctx.start.line}')
                    else:
                        self.error.append(f'1246ERROR: El tamaño del array "{name}" debe de ser un numero mayor a 0, linea: {ctx.start.line}')
            else:
                fieldVar = ctx.field_var()[i]
                type = ctx.var_type()[i].getText()
                size = 0
                if ctx.var_type()[i].INT():
                    size = 4
                elif ctx.var_type()[i].CHAR():
                    size = 2
                elif ctx.var_type()[i].BOOLEAN():
                    size = 1
                if fieldVar.var_id():
                    name = fieldVar.var_id().getText()
                    if not self.tablas.varExistsOnce(name, self.scopeActual):
                        if self.scopeActual in self.offsetDicc:
                            off = self.offsetDicc[self.scopeActual]
                        else:
                            self.offsetDicc[self.scopeActual] = 0
                            off = self.offsetDicc[self.scopeActual]
                        self.contVariables += 1
                        self.tablas.setVariable(self.contVariables, name, type, self.scopeActual, 0, size, False, off)
                        self.offsetDicc[self.scopeActual] += size
                    else:
                        self.error.append(f'1256ERROR: La variable "{name}" ya existe, linea: {ctx.start.line}')
                elif fieldVar.array_id():
                    name = fieldVar.array_id().ID().getText()
                    if fieldVar.array_id().int_literal():
                        tam = int(fieldVar.array_id().int_literal().getText())
                        if tam <= 0 or tam == None:
                            self.error.append(f'1262ERROR: El tamaño del array "{name}" debe de ser un número mayor a 0, linea: {ctx.start.line}')
                        else:
                            if not self.tablas.varExistsOnce(name, self.scopeActual):
                                if self.scopeActual in self.offsetDicc:
                                    off = self.offsetDicc[self.scopeActual]
                                else:
                                    self.offsetDicc[self.scopeActual] = 0
                                    off = self.offsetDicc[self.scopeActual]
                                self.contEstructuras += 1
                                size = size * tam
                                self.tablas.setEstructura(self.contEstructuras, name, type, 'array', self.scopeActual, tam, False, size, off)
                                self.offsetDicc[self.scopeActual] += size
                            else:
                                self.error.append(f'1268ERROR: La variable "{name}" ya existe, linea: {ctx.start.line}')
                    else:
                        self.error.append(f'1270ERROR: El tamaño del array "{name}" debe de ser un numero mayor a 0, linea: {ctx.start.line}')

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
                elif "return" in i.getText():
                    retorna = True
            if retorna == False and returnName != 'void':
                self.error.append(f'1391ERROR: El método "{name}" no tiene un return, linea: {ctx.start.line}')
            if name == "main":
                self.notMainFunction = False
            arrayParams = []
            # Si viene 'void' como parametro
            if ctx.VOID():
                pass
            else:
                for i in range(len(ctx.var_id())):
                    param1 = ctx.var_type()[i].getText()
                    param2 = ctx.var_id()[i].getText()
                    if not self.tablas.varExistsOnce(param2, self.scopeActual):
                        if ctx.var_type()[i].INT():
                            size = 4
                        elif ctx.var_type()[i].CHAR():
                            size = 2
                        elif ctx.var_type()[i].BOOLEAN():
                            size = 1
                        if self.scopeActual in self.offsetDicc:
                            off = self.offsetDicc[self.scopeActual]
                        else:
                            self.offsetDicc[self.scopeActual] = 0
                            off = self.offsetDicc[self.scopeActual]
                        self.contVariables += 1
                        self.tablas.setVariable(self.contVariables, param2, param1, self.scopeActual, 0, size, False, off)
                        arrayParams.append([param1, param2])
                        self.offsetDicc[self.scopeActual] += size
                    else:
                        self.error.append(f'1297ERROR: La variable "{param2}" ya existe en el método "{self.scopeActual}", linea: {ctx.start.line}')

            self.tablas.setMetodo(self.contFunciones, name, returnName, arrayParams, self.scopes[len(self.scopes)-2], retorna)
        else:
            self.error.append(f'1301ERROR: El método "{name}" ya existe, linea: {ctx.start.line}')

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
        self.tablas.setSizeEstruct(self.scopeActual)
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

def mainProy1():
    data = open('./pruebas/simpleTest.txt').read()
    # data = open('./pruebas/multiple_tests.txt').read()
    lexer = DecafLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()

    proy1 = Proyecto1()
    walker = ParseTreeWalker()
    walker.walk(proy1, tree)

    print()
    proy1.tablas.showFullDicc()

    if proy1.notMainFunction:
        proy1.error.append("ERROR: El metodo main no esta defindo")
    file = open("errores", "wb")
    f = open("errores.txt", "w", encoding="utf8")
    f.write(f'Han ocurrido {str(len(proy1.getErrors()))} errores!')
    if len(proy1.getErrors()) > 0:
        f.write('\n')
        f.write('\n')
        for i in proy1.getErrors():
            print(i)
            f.write(i)
            f.write('\n')
        pickle.dump(proy1.error, file, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        pickle.dump([], file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()

    # else:
    print('Guardando tablas....')
    file = open("estructuras", "wb")
    pickle.dump(proy1.tablas.estructuras, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()

    file = open("variables", "wb")
    pickle.dump(proy1.tablas.variables, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()

    file = open("metodos", "wb")
    pickle.dump(proy1.tablas.metodos, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()

mainProy1()