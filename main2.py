from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from DecafGramLexer import DecafGramLexer
from DecafGramListener import DecafGramListener
from DecafGramParser import DecafGramParser
import pickle5 as pickle
from tablas import *
from nodo import *
from nodoState import *
import pprint
import sys

class Proyecto2(DecafGramListener):
    def __init__(self):
        self.contNodos = 0
        self.contTemps = 0
        self.contCond = 0
        self.contWhile = 0
        self.diccVariables = {}
        self.diccEstructuras = {}
        self.diccMetodos = {}
        self.diccContext = {}
        self.arrayProd =[]
        self.scopes = ["global"]
        self.scopeActual = "global"
        self.tablas = Tablas()
        self.print = pprint.PrettyPrinter()
        self.lecturaArchivos()

    def lecturaArchivos(self):
        print('Cargando tablas....')
        file = open("variables", "rb")
        self.diccVariables = pickle.load(file)
        file.close()

        file = open("estructuras", "rb")
        self.diccEstructuras = pickle.load(file)
        file.close()

        file = open("metodos", "rb")
        self.diccMetodos = pickle.load(file)
        file.close()

        self.tablas.variables = self.diccVariables
        self.tablas.estructuras = self.diccEstructuras
        self.tablas.metodos = self.diccMetodos

        print('Variables')
        self.print.pprint(self.diccVariables)
        print()
        print('estructuras')
        self.print.pprint(self.diccEstructuras)
        print()
        print('Metodos')
        self.print.pprint(self.diccMetodos)
        print()

    def genTemp(self):
        value = f't{self.contTemps}'
        self.contTemps += 1
        return value

    def generateDir(self, var, temp = ''):
        value = ''
        if temp != '':
            if len(var) > 0:
                if var[3] == 'global':
                    value = f'gp[{temp}]'
                else:
                    value = f'fp[{temp}]'
        else:
            if len(var) > 0:
                if var[3] == 'global':
                    value = f'gp[{(var[6])}]'
                else:
                    value = f'fp[{(var[6])}]'
        return value

    def generateDirArray(self, var, temp):
        value = ''
        if len(var) > 0:
            if var[3] == 'global':
                value = f'gp[{(temp)}]'
            else:
                value = f'fp[{(temp)}]'
        return value

    def generateTopeGet(self, var):
        value = ''
        if len(var) > 0:
            if var[3] == 'global':
                value = f'gp[{(var[6])}]'
            else:
                value = f'fp[{(var[6])}]'
        return value

    def visitar(self, params):
        arrayNodos = []
        for param in params:
            nodoParam = Nodo(self.contNodos)
            self.contNodos += 1
            paramName = param.getText()
            if isinstance(param, DecafGramParser.Expr_methodCallContext):
                paramName = param.method_call().method_name().getText()
            elif isinstance(param, DecafGramParser.Expr_locationContext):
                if param.location().array_id() is not None:
                    paramName = param.location().array_id().ID().getText()

            if isinstance(param, DecafGramParser.Expr_presedencia1Context) or isinstance(param, DecafGramParser.Expr_presedencia2Context):
                hijo = self.diccContext[param]
                nodoParam.setCodigo(hijo.getCodigo())
                nodoParam.setDir(hijo.getDir())
            else:
                if self.tablas.varExists(paramName, self.scopeActual):
                    variable = self.tablas.getVariable(paramName, self.scopeActual)
                    nodoParam.setDir(self.generateTopeGet(variable))
                elif self.tablas.metodoExists(paramName):
                    funcion = self.tablas.getMetodo(paramName)
                    codigoConcat = ' CALL ' + paramName + ', ' + str(len(funcion[2])) + '\n'
                    nodoParam.setCodigo(codigoConcat)
                    nodoParam.setDir("R")
                elif self.tablas.arrayExists(paramName, self.scopeActual):
                    array = self.tablas.getArray(paramName, self.scopeActual)
                    if param.location().array_id().int_literal():
                        exp = self.diccContext[param.location().array_id().int_literal()]
                    elif param.location().array_id().var_id():
                        exp = self.diccContext[param.location().array_id().var_id()]
                    cantTipo = 0
                    if array[1] == 'int':
                        cantTipo = 4
                    elif array[1] == 'char':
                        cantTipo = 2
                    elif array[1] == 'boolean':
                        cantTipo = 1
                    temp1 = self.genTemp()
                    temp2 = self.genTemp()
                    offset = array[7]
                    nodoParam.setDir(self.generateDirArray(array, temp2))

                    codigoConcat = ' ' + exp.getCodigo() + \
                        (str(temp1) + ' = ' + str(cantTipo) + ' * ' + exp.getDir()) + '\n ' + \
                        (str(temp2) + ' = ' + str(offset) + ' + ' + str(temp1)) + '\n'

                    nodoParam.setCodigo(codigoConcat)

                else:
                    nodoParam.setDir(paramName)

            arrayNodos.append(nodoParam)

        return arrayNodos

    def nuevaEtiquetaIf(self, value):
        etiqueta = ''
        if value == 'true':
            etiqueta = f'IF_TRUE_{self.contCond}'
        elif value == 'false':
            etiqueta = f'IF_FALSE_{self.contCond}'
            self.contCond += 1
        elif value == 'endIf':
            etiqueta = f'END_IF_{self.contCond}'
        else:
            etiqueta = f'{value}:'

        return etiqueta

    def nuevaEtiquetaWhile(self, value):
        etiqueta = ''
        if value == 'startwhile':
            etiqueta = f'WHILE_LOOP_{self.contWhile}'
        elif value == 'endwhile':
            etiqueta = f'END_WHILE_{self.contWhile}'
            self.contWhile += 1
        elif value == 'true':
            etiqueta = f'IF_TRUE_{self.contCond}'
        elif value == 'false':
            etiqueta = f'IF_FALSE_{self.contCond}'
            self.contCond += 1
        else:
            etiqueta = f'{value}:'

        return etiqueta

    def iterateArrayProd(self):
        print()
        print("----CODIGO INTERMEDIO----")
        print()
        print()
        f = open("codigoIntermedio.txt", "w", encoding="utf8")
        f.write('----CODIGO INTERMEDIO----')
        f.write('\n')
        f.write('\n')
            # print(i)
            # f.write(i)
            # f.write('\n')
        for prod in self.arrayProd:
            if isinstance(prod, Nodo) or isinstance(prod, NodoState):
                f.write(prod.getCodigo())
                print(prod.getCodigo())
            else:
                f.write(prod)
                print(prod)

    def enterLocation(self, ctx: DecafGramParser.LocationContext):
        if ctx not in self.diccContext:
            self.diccContext[ctx] = ctx

    def exitLocation(self, ctx: DecafGramParser.LocationContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitVar_id_struct(self, ctx: DecafGramParser.Var_id_structContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setCodigo("")
        var = self.tablas.getVariable(ctx.ID(), self.scopeActual)
        if ctx.location()[0].var_id():
            var2 = self.tablas.getVariable(ctx.location()[0].getText(), var[1])
        # elif ctx.location()[0].array_id():
        #     var2 = self.tablas.getArray(ctx.location().array_id().ID()[0].getText(), var[1])
        temp1 = self.genTemp()

        codigoConcat = ' ' + temp1 + ' = ' + str(var[6]) + ' + ' + str(var2[6]) + ' \n'
        nodo.setCodigo(codigoConcat)
        nodo.setDir(self.generateDir(var2, temp1))

        self.diccContext[ctx] = nodo

    def exitVar_id_var(self, ctx: DecafGramParser.Var_id_varContext):
        nombre = ctx.getText()
        variable = self.tablas.getVariable(nombre, self.scopeActual)

        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setCodigo("")
        nodo.setDir(self.generateDir(variable))

        self.diccContext[ctx] = nodo

    # def exitVar_id(self, ctx: DecafGramParser.Var_idContext):
        # nombre = ctx.getText()
        # variable = self.tablas.getVariable(nombre, self.scopeActual)

        # nodo = Nodo(self.contNodos)
        # self.contNodos += 1
        # nodo.setCodigo("")
        # nodo.setDir(self.generateDir(variable))

        # self.diccContext[ctx] = nodo

    def exitArray_id_struct(self, ctx: DecafGramParser.Array_id_structContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        var = self.tablas.getArray(ctx.ID(), self.scopeActual)
        if ctx.location()[0].var_id():
            var2 = self.tablas.getVariable(ctx.location()[0].getText(), var[1])
        print('array', var)
        print('var', var2)
        if ctx.int_literal():
            posi = ctx.int_literal().getText()
        elif ctx.var_id():
            posi = 'a'
        # elif ctx.location()[0].array_id():
        #     var2 = self.tablas.getArray(ctx.location().array_id().ID()[0].getText(), var[1])
        temp1 = self.genTemp()
        temp2 = self.genTemp()
        temp3 = self.genTemp()

        codigoConcat = ' ' + temp1 + ' = ' + str(var[6]) + ' * ' + str(posi) + ' \n' +\
            ' ' + temp2 + ' = ' + str(var[7]) + ' + ' + temp1 + '\n ' + temp3 + ' = ' + temp2 + ' + ' + str(var2[6]) + '\n'

        print(codigoConcat)
        nodo.setCodigo(codigoConcat)
        nodo.setDir(self.generateDir(var2, temp3))

        self.diccContext[ctx] = nodo

    def exitArray_id_var(self, ctx: DecafGramParser.Array_id_varContext):
        parent = ctx.parentCtx
        if not isinstance(parent, DecafGramParser.Field_varContext):
            nombre = ctx.ID().getText()
            variable = self.tablas.getArray(nombre, self.scopeActual)

            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            exp = 0
            if ctx.int_literal():
                exp = self.diccContext[ctx.int_literal()]
            elif ctx.var_id():
                exp = self.diccContext[ctx.var_id()]
            cantTipo = 0
            if variable[1] == 'int':
                cantTipo = 4
            elif variable[1] == 'char':
                cantTipo = 2
            elif variable[1] == 'boolean':
                cantTipo = 1
            temp1 = self.genTemp()
            temp2 = self.genTemp()
            offset = variable[7]
            nodo.setDir(self.generateDirArray(variable, temp2))

            codigoConcat = ' ' +exp.getCodigo() + \
                (str(temp1) + ' = ' + str(cantTipo) + ' * ' + exp.getDir()) + '\n ' + \
                (str(temp2) + ' = ' + str(offset) + ' + ' + str(temp1)) + '\n'

            nodo.setCodigo(codigoConcat)
        else:
            nodo = Nodo(self.contNodos)
            self.contNodos += 1

        self.diccContext[ctx] = nodo

    # def exitArray_id(self, ctx: DecafGramParser.Array_idContext):
        # parent = ctx.parentCtx
        # if not isinstance(parent, DecafGramParser.Field_varContext):
        #     nombre = ctx.ID().getText()
        #     variable = self.tablas.getArray(nombre, self.scopeActual)

        #     nodo = Nodo(self.contNodos)
        #     self.contNodos += 1
        #     exp = 0
        #     if ctx.int_literal():
        #         exp = self.diccContext[ctx.int_literal()]
        #     elif ctx.var_id():
        #         exp = self.diccContext[ctx.var_id()]
        #     cantTipo = 0
        #     if variable[1] == 'int':
        #         cantTipo = 4
        #     elif variable[1] == 'char':
        #         cantTipo = 2
        #     elif variable[1] == 'boolean':
        #         cantTipo = 1
        #     temp1 = self.genTemp()
        #     temp2 = self.genTemp()
        #     offset = variable[7]
        #     nodo.setDir(self.generateDirArray(variable, temp2))

        #     codigoConcat = ' ' +exp.getCodigo() + \
        #         (str(temp1) + ' = ' + str(cantTipo) + ' * ' + exp.getDir()) + '\n ' + \
        #         (str(temp2) + ' = ' + str(offset) + ' + ' + str(temp1)) + '\n'

        #     nodo.setCodigo(codigoConcat)
        # else:
        #     nodo = Nodo(self.contNodos)
        #     self.contNodos += 1

        # self.diccContext[ctx] = nodo

    def exitMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        return super().exitMethod_declr(ctx)

    def exitVardeclr(self, ctx: DecafGramParser.VardeclrContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(1)]

    def exitField_var(self, ctx: DecafGramParser.Field_varContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitStatement_methodcall(self, ctx: DecafGramParser.Statement_methodcallContext):
        hijo = self.diccContext[ctx.getChild(0)]
        if hijo.getCodigo() != "":
            self.arrayProd.append(hijo)
        self.diccContext[ctx] = hijo

        abuelo = ctx.parentCtx.parentCtx
        if not isinstance(abuelo, DecafGramParser.Statement_whileContext) and not isinstance(abuelo, DecafGramParser.Statement_ifContext):
            self.arrayProd.append(hijo)

    def exitBlock(self, ctx: DecafGramParser.BlockContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        codigoConcat = ''
        for i in ctx.statement():
            codigoConcat += self.diccContext[i].getCodigo() + "\n "
        nodo.setCodigo(codigoConcat)

        self.diccContext[ctx] = nodo

    def exitExpr_presedencia1(self, ctx: DecafGramParser.Expr_presedencia1Context):
        nodo1 = self.diccContext[ctx.getChild(0)]
        nodo2 = self.diccContext[ctx.getChild(2)]

        if ctx.MULTIPLY():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = ' ' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + " * " + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.DIVIDE():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = ' ' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' / ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.REMINDER():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = ' ' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' % ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

    def exitExpr_presedencia2(self, ctx: DecafGramParser.Expr_presedencia2Context):
        nodo1 = self.diccContext[ctx.getChild(0)]
        nodo2 = self.diccContext[ctx.getChild(2)]

        if ctx.ADD():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = ' ' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' + ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.SUB():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = ' ' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' - ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

    def exitExpr_methodCall(self, ctx: DecafGramParser.Expr_methodCallContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitExpr_location(self, ctx: DecafGramParser.Expr_locationContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitExpr_menos(self, ctx: DecafGramParser.Expr_menosContext):
        nodo1 = self.diccContext[ctx.getChild(1)]
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        temp = self.genTemp()
        nodo.setDir(temp)
        codigoConcat = ' ' + nodo1.getCodigo() + (nodo.getDir() + ' = MENOS ' + nodo1.getDir()) + '\n'
        nodo.setCodigo(codigoConcat)
        self.diccContext[ctx] = nodo

    def exitExpr_negacion(self, ctx: DecafGramParser.Expr_negacionContext):
        nodo1 = self.diccContext[ctx.getChild(1)]
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        temp = self.genTemp()
        nodo.setDir(temp)
        codigoConcat = ' ' + nodo1.getCodigo() + (nodo.getDir() + ' = NEGADO ' + nodo1.getDir()) + '\n'
        nodo.setCodigo(codigoConcat)
        self.diccContext[ctx] = nodo

    def exitExpr_parentesis(self, ctx: DecafGramParser.Expr_parentesisContext):
        nodo1 = self.diccContext[ctx.getChild(1)]
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setDir(nodo1.getDir())
        nodo.setCodigo(nodo1.getCodigo())
        self.diccContext[ctx] = nodo

    def exitStatement_if(self, ctx: DecafGramParser.Statement_ifContext):
        if len(ctx.block()) == 1:
            nodoState = NodoState()
            nodoB = self.diccContext[ctx.expr()]
            nodoS1 = self.diccContext[ctx.getChild(4)]

            nodoB.setValorTrue(self.nuevaEtiquetaIf('true'))
            endIf = self.nuevaEtiquetaIf('false')

            if(len(nodoB.getCodigo().split("\n")) >= 2):
                temp = nodoB.getCodigo().split(
                    "\n")[2].split("=")[0].strip()
            else:
                if(len(nodoB.getCodigo().split("=")) != 0):
                    temp = nodoB.getCodigo().split("=")[0].strip()
                else:
                    temp = f't{self.contadorTemporales-1}'

            codigConcat = nodoB.getCodigo() + ('\n IF ' + f'{temp} > 0 '  f' GOTO {nodoB.getValorTrue()}') + '\n' +\
                (' GOTO ' + endIf) + '\n' + ' ' + self.nuevaEtiquetaIf(nodoB.getValorTrue()) + '\n' + ' ' + nodoS1.getCodigo() + '\n' + ' ' + self.nuevaEtiquetaIf(endIf)
        else:
            nodoState = NodoState()
            nodoB = self.diccContext[ctx.expr()]
            S1 = self.diccContext[ctx.block()[0]]
            S2 = self.diccContext[ctx.block()[1]]

            endIf = self.nuevaEtiquetaIf('endIf')
            nodoB.setValorTrue(self.nuevaEtiquetaIf('true'))
            nodoB.setValorFalse(self.nuevaEtiquetaIf('false'))

            if(len(nodoB.getCodigo().split("\n")) >= 2):
                temp = nodoB.getCodigo().split(
                    "\n")[2].split("=")[0].strip()
            else:
                if(len(nodoB.getCodigo().split("=")) != 0):
                    temp = nodoB.getCodigo().split("=")[0].strip()
                else:
                    temp = f't{self.contadorTemporales-1}'

            codigConcat = nodoB.getCodigo() + ('\n IF ' + f'{temp} > 0 GOTO {nodoB.getValorTrue()} \n ') + \
                (f'GOTO {nodoB.getValorFalse()} \n ') + self.nuevaEtiquetaIf(nodoB.getValorTrue()) + '\n ' + S1.getCodigo() + '\n ' + \
                (f' GOTO {endIf}') + '\n ' + self.nuevaEtiquetaIf(nodoB.getValorFalse()) + '\n ' + S2.getCodigo() + '\n ' + self.nuevaEtiquetaIf(endIf)

        abuelo = ctx.parentCtx.parentCtx
        nodoState.setCodigo(codigConcat)
        self.diccContext[ctx] = nodoState
        if not isinstance(abuelo, DecafGramParser.Statement_whileContext):
            self.arrayProd.append(nodoState)

    def exitStatement_while(self, ctx: DecafGramParser.Statement_whileContext):
        nodoState = NodoState()
        nodoB = self.diccContext[ctx.expr()]
        nodoS1 = self.diccContext[ctx.getChild(4)]

        inicio = self.nuevaEtiquetaWhile('startwhile')
        nodoB.setValorTrue(self.nuevaEtiquetaWhile('true'))
        nodoB.setValorFalse(self.nuevaEtiquetaWhile('endwhile'))

        if(len(nodoB.getCodigo().split("\n")) >= 2):
            temp = nodoB.getCodigo().split(
                "\n")[2].split("=")[0].strip()
        else:
            if(len(nodoB.getCodigo().split("=")) != 0):
                temp = nodoB.getCodigo().split("=")[0].strip()
            else:
                temp = f't{self.contadorTemporales-1}'

        codigConcat = ' ' + inicio + '\n ' + nodoB.getCodigo() + \
            ('\n  IF ' + f't{temp} > 0 ' + f'GOTO {nodoB.getValorTrue()}') + '\n ' + \
            (f' GOTO {nodoB.getValorFalse()}') + '\n  ' + self.nuevaEtiquetaWhile(nodoB.getValorTrue()) + '\n' + '  ' + nodoS1.getCodigo() + ' ' +\
            (f' GOTO {inicio}') + '\n ' + self.nuevaEtiquetaWhile(nodoB.getValorFalse())

        nodoState.setCodigo(codigConcat)

        self.diccContext[ctx] = nodoState
        abuelo = ctx.parentCtx.parentCtx
        if not isinstance(abuelo, DecafGramParser.Statement_ifContext):
            self.arrayProd.append(nodoState)

    def exitExpr_normal(self, ctx: DecafGramParser.Expr_normalContext):
        if ctx.eq_op() is not None:
            temp = self.genTemp()
            nodoState = NodoState()
            nodo = self.diccContext[ctx.getChild(0)]
            nodo2 = self.diccContext[ctx.getChild(2)]
            # print(ctx.getText())
            codigoConcat = nodo.getCodigo() + ' ' + nodo2.getCodigo() + ' ' + temp + ' = ' + nodo.getDir() + ' ' + ctx.eq_op().getText() + ' ' + nodo2.getDir()
            nodoState.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodoState
        elif ctx.rel_op() is not None:
            temp = self.genTemp()
            nodoState = NodoState()
            nodo = self.diccContext[ctx.getChild(0)]
            nodo2 = self.diccContext[ctx.getChild(2)]
            codigoConcat = nodo.getCodigo() + ' ' + nodo2.getCodigo() + ' ' + temp + ' = ' + nodo.getDir() + ' ' + ctx.rel_op().getText() + ' ' + nodo2.getDir()
            nodoState.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodoState
        elif ctx.cond_op() is not None:
            temp = self.genTemp()
            nodoState = NodoState()
            nodo1 = self.diccContext[ctx.getChild(0)]
            nodo2 = self.diccContext[ctx.getChild(2)]
            tempValue1 = ''
            tempValue2 = ''
            if(ctx.cond_op().getText() == "&&" or ctx.cond_op().getText() == "||"):
                if(len(nodo1.getCodigo().split("\n")) >= 2):
                    tempValue1 = nodo1.getCodigo().split(
                        "\n")[2].split("=")[0].strip()
                else:
                    if(len(nodo1.getCodigo().split("=")) != 0):
                        tempValue1 = nodo1.getCodigo().split("=")[
                            0].strip()
                    else:
                        tempValue1 = nodo1.getCodigo().split("=")[0]

                if(len(nodo2.getCodigo().split("\n")) >= 2):
                    tempValue2 = nodo2.getCodigo().split(
                        "\n")[2].split("=")[0].strip()
                else:
                    if(len(nodo2.getCodigo().split("=")) != 0):
                        tempValue2 = nodo2.getCodigo().split("=")[
                            0].strip()
                    else:
                        tempValue2 = nodo2.getCodigo().split("=")[0]

                codigoConcat = nodo1.getCodigo() + '\n' + nodo2.getCodigo() + '\n ' + temp + " = " + \
                    f'{tempValue1}' + " " + \
                    ctx.cond_op().getText() + \
                    f' {tempValue2}'
            else:
                codigoConcat = nodo1.getCodigo() + ' ' + nodo2.getCodigo() + ' ' + temp + " = " + nodo1.getDir() + " " + ctx.cond_op().getText() + " " + \
                    nodo2.getDir()
            nodoState.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodoState
        else:
            self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitExpr_literal(self, ctx: DecafGramParser.Expr_literalContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitLiteral(self, ctx: DecafGramParser.LiteralContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitInt_literal(self, ctx: DecafGramParser.Int_literalContext):
        nodo = Nodo(self.contNodos)
        nodo.setDir(ctx.getText())
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitChar_literal(self, ctx: DecafGramParser.Char_literalContext):
        nodo = Nodo(self.contNodos)
        nodo.setDir(ctx.getText())
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitBool_literal(self, ctx: DecafGramParser.Bool_literalContext):
        nodo = Nodo(self.contNodos)
        nodo.setDir(ctx.getText())
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitStatement_assign(self, ctx: DecafGramParser.Statement_assignContext):
        nodoL = self.diccContext[ctx.location()]
        nodoE = self.diccContext[ctx.expr()]

        nodo = Nodo(self.contNodos)
        self.contNodos += 1

        nombre = ''
        if ctx.location().var_id():
            nombre = ctx.location().var_id().getText()
            variable = self.tablas.getVariable(nombre, self.scopeActual)
        elif ctx.location().array_id():
            nombre = ctx.location().array_id().ID().getText()
            variable = self.tablas.getArray(nombre, self.scopeActual)

        if nodoL.getCodigo() != '' and nodoE.getCodigo() == '':
            codigoConcat = nodoL.getCodigo() + (' ' + nodoL.getDir() + ' = ' + nodoE.getDir())
        elif nodoL.getCodigo() != '' and nodoE.getCodigo() != '':
            codigoConcat = nodoL.getCodigo() + nodoE.getCodigo() + (' ' + nodoL.getDir() + ' = ' + nodoE.getDir())
        else:
            codigoConcat = nodoE.getCodigo() + (' ' + self.generateTopeGet(variable) + " = " + nodoE.getDir())
        nodo.setCodigo(codigoConcat)

        self.diccContext[ctx] = nodo
        abuelo = ctx.parentCtx.parentCtx
        if not isinstance(abuelo, DecafGramParser.Statement_ifContext) and not isinstance(abuelo, DecafGramParser.Statement_whileContext):
            self.arrayProd.append(nodo)

    def exitStatement_return(self, ctx: DecafGramParser.Statement_returnContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodoE = self.diccContext[ctx.expr()]
        codigoConcat = nodoE.getCodigo() + (' RETURN ' + nodoE.getDir())
        nodo.setCodigo(codigoConcat)

        abuelo = ctx.parentCtx.parentCtx
        if not isinstance(abuelo, DecafGramParser.Statement_ifContext):
            self.arrayProd.append(nodo)
        self.diccContext[ctx] = nodo

    def enterMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        name = ctx.method_name().getText()
        self.arrayProd.append('DEF ' + name.upper() + ':' '\n')
        self.scopes.append(name)
        self.scopeActual = name

    def exitMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        name = ctx.method_name().getText()
        self.contTemps = 0
        self.arrayProd.append('\nEND DEF ' + name.upper() + '\n')
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    def enterStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        name = ctx.ID().getText()
        self.scopes.append(name)
        self.scopeActual = name

    def exitStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    def exitMethod_call(self, ctx: DecafGramParser.Method_callContext):
        nombre = ctx.method_name().getText()
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        # print(ctx.expr())
        args = self.visitar(ctx.expr())

        for arg in args:
            print('arg', arg.getDir())
            codigo = nodo.getCodigo()
            codigo += arg.getCodigo() + (' PARAM ' + arg.getDir() + '\n')
            nodo.setCodigo(codigo)

        codigo = nodo.getCodigo()
        codigo += ' CALL ' + nombre + ', ' + str(len(args)) + '\n'
        nodo.setCodigo(codigo)
        nodo.setDir('R')
        self.diccContext[ctx] = nodo

def mainProy2():
    data = open('./pruebas/simpleTest.txt').read()
    lexer = DecafGramLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = DecafGramParser(stream)
    tree = parser.program()

    proy2 = Proyecto2()
    walker = ParseTreeWalker()
    walker.walk(proy2, tree)

    proy2.iterateArrayProd()

mainProy2()