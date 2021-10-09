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

# t0 = fp[0] + fp[4]
# fp[8] = t0

# t1 = fp[0] + fp[4]
# gp[0] = t1

class Proyecto2(DecafGramListener):
    def __init__(self):
        self.contNodos = 0
        self.contTemps = 0
        self.contTrue = 0
        self.contFalse = 0
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

    def generateDir(self, var):
        value = ''
        if len(var) > 0:
            if var[3] == 'global':
                value = f'gp[{(var[6])}]'
            else:
                value = f'fp[{(var[6])}]'
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
            nodoParam.setCodigo('')
            if self.tablas.varExists(param.getText(), self.scopeActual):
                variable = self.tablas.getVariable(param.getText(), self.scopeActual)
                nodoParam.setDir(self.generateDir(variable))
            else:
                nodoParam.setDir(param.getText())
            arrayNodos.append(nodoParam)

        return arrayNodos

    def nuevaEtiqueta(self, cond):
        value = ''
        if cond == 'true':
            value = f'IF_TRUE_{self.contTrue}'
            self.contTrue += 1
        elif cond == 'false':
            value = f'IF_FALSE_{self.contFalse}'
            self.contFalse += 1
        else:
            value = f'{cond}:'

        return value

    def iterateArrayProd(self):
        print()
        print("----CODIGO INTERMEDIO----")
        print()
        print()
        for prod in self.arrayProd:
            if isinstance(prod, Nodo) or isinstance(prod, NodoState):
                print(prod.getCodigo())
            else:
                print(prod)

    def enterLocation(self, ctx: DecafGramParser.LocationContext):
        if ctx not in self.diccContext:
            self.diccContext[ctx] = ctx

    def exitLocation(self, ctx: DecafGramParser.LocationContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitVar_id(self, ctx: DecafGramParser.Var_idContext):
        nombre = ctx.getText()
        variable = self.tablas.getVariable(nombre, self.scopeActual)

        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setCodigo("")
        nodo.setDir(self.generateDir(variable))

        self.diccContext[ctx] = nodo

    def exitVardeclr(self, ctx: DecafGramParser.VardeclrContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(1)]

    def exitField_var(self, ctx: DecafGramParser.Field_varContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitBlock(self, ctx: DecafGramParser.BlockContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(1)]

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
        nodoState = NodoState()
        nodoB = self.diccContext[ctx.expr()]
        nodoS1 = self.diccContext[ctx.getChild(4)]

        nodoB.setValorTrue(self.nuevaEtiqueta('true'))
        endIf = self.nuevaEtiqueta('false')

        codigConcat = nodoB.getCodigo() + (' IF ' + f't{self.contTemps-1} > 0 '  f' GOTO {nodoB.getValorTrue()}') + '\n' +\
            (' GOTO ' + endIf) + '\n' + ' ' + self.nuevaEtiqueta(nodoB.getValorTrue()) + '\n' + ' ' + nodoS1.getCodigo() + '\n' + ' ' + self.nuevaEtiqueta(endIf)
        nodoState.setCodigo(codigConcat)

        self.diccContext[ctx] = nodoState
        self.arrayProd.append(nodoState)


    def exitExpr_normal(self, ctx: DecafGramParser.Expr_normalContext):
        if ctx.eq_op is not None:
            temp = self.genTemp()
            nodoState = NodoState()
            self.contNodos += 1
            nodo = self.diccContext[ctx.getChild(0)]
            codigoConcat = ' ' + temp + ' = ' + nodo.getDir() + ' ' + ctx.eq_op().getText() + ' ' + ctx.getChild(2).getText() + '\n'
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
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitChar_literal(self, ctx: DecafGramParser.Char_literalContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitBool_literal(self, ctx: DecafGramParser.Bool_literalContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        self.diccContext[ctx] = nodo

    def exitStatement_assign(self, ctx: DecafGramParser.Statement_assignContext):
        nodoL = self.diccContext[ctx.location()]
        nodoE = self.diccContext[ctx.expr()]

        nodo = Nodo(self.contNodos)
        self.contNodos += 1

        nombre = ctx.location().var_id().getText()
        variable = self.tablas.getVariable(nombre, self.scopeActual)

        codigoConcat = nodoE.getCodigo() + (' ' + self.generateTopeGet(variable) + " = " + nodoE.getDir())
        nodo.setCodigo(codigoConcat)

        self.diccContext[ctx] = nodo
        # TODO verificar cuando hay que hacer append y cuando no
        self.arrayProd.append(nodo)

    def exitStatement_return(self, ctx: DecafGramParser.Statement_returnContext):
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodoE = self.diccContext[ctx.expr()]
        codigoConcat = nodoE.getCodigo() + (' RETURN ' + nodoE.getDir())
        nodo.setCodigo(codigoConcat)
        self.arrayProd.append(codigoConcat)

        self.diccContext[ctx] = nodo

    def enterMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        name = ctx.method_name().getText()
        self.arrayProd.append('DEF ' + name.upper() + ':')
        self.scopes.append(name)
        self.scopeActual = name

    def exitMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        name = ctx.method_name().getText()
        self.arrayProd.append('END DEF ' + name.upper() + '\n')
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    def enterStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        name = ctx.ID().getText()
        self.scopes.append(name)
        self.scopeActual = name

    def exitStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    # def enterMethod_call(self, ctx: DecafGramParser.Method_callContext):
    #     return super().enterMethod_call(ctx)

    def exitMethod_call(self, ctx: DecafGramParser.Method_callContext):
        nombre = ctx.method_name().getText()
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        # print(ctx.expr())
        args = self.visitar(ctx.expr())

        for arg in args:
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