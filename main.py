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
        self.contIfs = 0
        self.scopes = ["global"]
        self.scopeActual = "global"

    def getErrors(self):
        return self.error

    def enterStatement(self, ctx: DecafParser.StatementContext):
        if ctx.location().array_id():
            name = ctx.location().array_id().ID()
            if self.tablas.arrayExists(name, self.scopeActual):
                var = self.tablas.getArray(name, self.scopeActual)
                print('var', var)
                if isinstance(var, list):
                    if var[2] != 'array':
                        self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
                else:
                    self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
            else:
                self.error.append(f'ERROR: La variable "{name}", no es un array, linea: {ctx.start.line}')
        elif 'struct' in ctx.getText():
            print('struct')
            print(ctx.location().array_id().ID())
        elif ctx.IF():
            self.contIfs += 1
            scope = 'if'+ str(self.contIfs)
            self.scopes.append(scope)
            self.scopeActual = scope
            self.contFunciones += 1
            self.tablas.setMetodo(self.contFunciones, scope, '', [], self.scopes[len(self.scopes)-2])
        elif ctx.FOR():
            print('forrrr')
        elif ctx.WHILE():
            print('whileeee')
        elif ctx.ELSE():
            print('elseeee')
        elif ctx.RETURN():
            value = ctx.expr().getText()
            # print(value)
            arrayVars = []
            metodo = self.tablas.getMetodo(self.scopeActual)
            returnType = metodo[1]
            if returnType == 'void':
                self.error.append(f'ERROR: Hay un error en el método "{self.scopeActual}", es de tipo void y tiene un return, linea: {ctx.start.line}')
            else:
                for i in range(len(value)):
                    if value[i] != '+' or value[i] != '-' or value[i] != '/' or value[i] != '*' or value[i] != ' ':
                        var = self.tablas.getVariable(value[i], self.scopeActual)
                        if isinstance(var, list):
                            arrayVars.append(var[1])
                        elif var == 'True' or var == 'False':
                            arrayVars.append('boolean')
                        elif "'" in var:
                            arrayVars.append('string')
                        else:
                            try:
                                int(var)
                                arrayVars.append('int')
                            except:
                                self.error.append(f'ERROR: El parametro "{value[i]}" no es una variable existente ni un tipo valido, linea: {ctx.start.line}')
                if len(arrayVars) > 0:
                    setArray = set(arrayVars)
                    if len(setArray) > 1:
                        self.error.append(f'ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
                    else:
                        if list(setArray)[0] != returnType:
                            self.error.append(f'ERROR: Hay un error en el valor de retorno en el método "{self.scopeActual}", linea: {ctx.start.line}')
        elif ctx.location():
            # print(ctx.getText())
            name = ctx.location().var_id().getText()
            error = False
            valor = ''
            # print(name)
            # print(self.scopeActual)
            if self.tablas.varExists(name, self.scopeActual):
                variable = self.tablas.getVariable(name, self.scopeActual)
                # print('variable', variable)
                # Condicion si se iguala a una variable
                if ctx.expr().literal():
                    if ctx.expr().literal().int_literal():
                        valor = ctx.expr().literal().int_literal().getText()
                    elif ctx.expr().literal().bool_literal():
                        valor = ctx.expr().literal().bool_literal().getText()
                    elif ctx.expr().literal().string_literal():
                        valor = ctx.expr().literal().string_literal().getText()

                    tipo = variable[1]
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
                        self.error.append(f'ERROR: Hay un error en el valor de la variable "{name}" en el método "{self.scopeActual}", linea: {ctx.start.line}')
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
                                                self.error.append(f'ERROR: La variable "{var}" a enviar como parametro al metodo "{methodName}" no existe en el método "{self.scopeActual}", linea: {ctx.start.line}')
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
                self.error.append(f'ERROR: La variable "{name}" no esta definida en el método "{self.scopeActual}", linea: {ctx.start.line}')
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
                        existe = self.tablas.varExists(var, self.scopeActual)
                        if existe:
                            varInfo = self.tablas.getVariable(var, self.scopeActual)
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
            # print(self.scopeActual)

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
            self.tablas.setEstructura(self.contEstructuras, name)

    def exitStruct_declr(self, ctx: DecafParser.Struct_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

def main():
    data = open('./pruebas/simpleTest.txt').read()
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