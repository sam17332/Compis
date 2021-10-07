from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from DecafGramLexer import DecafGramLexer
from DecafGramListener import DecafGramListener
from DecafGramParser import DecafGramParser
import pickle5 as pickle
from tablas import *
from nodo import *
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
        if var[3] == 'global':
            value = f'gp[{(var[6])}]'
        else:
            value = f'fp[{(var[6])}]'
        return value

    def generateTopeGet(self, var):
        value = ''
        if var[3] == 'global':
            value = f'gp[{(var[6])}]'
        else:
            value = f'fp[{(var[6])}]'
        return value

    def iterateArrayProd(self):
        print()
        print("CODIGO INTERMEDIO")
        for prod in self.arrayProd:
            print(prod.getCodigo())

    # def enterVardeclr(self, ctx: DecafGramParser.VardeclrContext):
    #     self.diccContext[ctx] = ctx

    # def exitVardeclr(self, ctx: DecafGramParser.VardeclrContext):
    #     self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    # def enterField_var(self, ctx: DecafGramParser.Field_varContext):
    #     self.diccContext[ctx] = ctx

    # def exitField_var(self, ctx: DecafGramParser.Field_varContext):
    #     self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def enterLocation(self, ctx: DecafGramParser.LocationContext):
        if ctx not in self.diccContext:
            self.diccContext[ctx] = ctx

    def exitLocation(self, ctx: DecafGramParser.LocationContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    # def enterVar_id(self, ctx: DecafGramParser.Var_idContext):
    #     parent = ctx.parentCtx
    #     if parent not in self.diccContext:
    #         self.diccContext[ctx] = self.diccContext[parent]

    def exitVar_id(self, ctx: DecafGramParser.Var_idContext):
        nombre = ctx.getText()
        variable = self.tablas.getVariable(nombre, self.scopeActual)

        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setCodigo("")
        nodo.setDir(self.generateDir(variable))

        self.diccContext[ctx] = nodo

    def exitExpr_presedencia1(self, ctx: DecafGramParser.Expr_presedencia1Context):
        nodo1 = self.diccContext[ctx.getChild(0)]
        nodo2 = self.diccContext[ctx.getChild(2)]

        if ctx.MULTIPLY():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + " * " + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.DIVIDE():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' / ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.REMINDER():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' % ' + nodo2.getDir() + '\n'
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
            codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' + ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

        elif ctx.SUB():
            nodo = Nodo(self.contNodos)
            self.contNodos += 1
            temp = self.genTemp()
            nodo.setDir(temp)
            codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + ' = ' + nodo1.getDir() + ' - ' + nodo2.getDir() + '\n'
            nodo.setCodigo(codigoConcat)
            self.diccContext[ctx] = nodo

    def exitExpr_location(self, ctx: DecafGramParser.Expr_locationContext):
        self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]

    def exitExpr_menos(self, ctx: DecafGramParser.Expr_menosContext):
        nodo1 = self.diccContext[ctx.getChild(1)]
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        temp = self.genTemp()
        nodo.setDir(temp)
        codigoConcat = '\n' + nodo1.getCodigo() + (nodo.getDir() + ' = MENOS ' + nodo1.getDir()) + '\n'
        nodo.setCodigo(codigoConcat)
        self.diccContext[ctx] = nodo

    def exitExpr_parentesis(self, ctx: DecafGramParser.Expr_parentesisContext):
        nodo1 = self.diccContext[ctx.getChild(1)]
        nodo = Nodo(self.contNodos)
        self.contNodos += 1
        nodo.setDir(nodo1.getDir())
        nodo.setCodigo(nodo1.getCodigo())
        self.diccContext[ctx] = nodo

    # def exitExpr_literal(self, ctx: DecafGramParser.Expr_literalContext):
    #     return super().exitExpr_literal(ctx)

    # def exitExpr(self, ctx: DecafGramParser.ExprContext):
    #     if len(ctx.children) == 1:
    #         self.diccContext[ctx] = self.diccContext[ctx.getChild(0)]
    #     else:
    #         if ctx.arith_op() is not None or ctx.rel_op() is not None:
    #             nodo1 = self.diccContext[ctx.getChild(0)]
    #             nodo2 = self.diccContext[ctx.getChild(2)]

    #             if ctx.ADD():
    #                 nodo = Nodo(self.contNodos)
    #                 self.contNodos += 1
    #                 temp = self.genTemp()
    #                 nodo.setDir(temp)
    #                 codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + '=' + nodo1.getDir() + "+" + nodo2.getDir() + '\n'
    #                 nodo.setCodigo(codigoConcat)
    #                 self.diccContext[ctx] = nodo

    #             elif ctx.SUB():
    #                 nodo = Nodo(self.contNodos)
    #                 self.contNodos += 1
    #                 temp = self.genTemp()
    #                 nodo.setDir(temp)
    #                 codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + '=' + nodo1.getDir() + "-" + nodo2.getDir() + '\n'
    #                 nodo.setCodigo(codigoConcat)
    #                 self.diccContext[ctx] = nodo

    #             elif ctx.MULTIPLY():
    #                 nodo = Nodo(self.contNodos)
    #                 self.contNodos += 1
    #                 temp = self.genTemp()
    #                 nodo.setDir(temp)
    #                 codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + '=' + nodo1.getDir() + "*" + nodo2.getDir() + '\n'
    #                 nodo.setCodigo(codigoConcat)
    #                 self.diccContext[ctx] = nodo

    #             elif ctx.DIVIDE():
    #                 nodo = Nodo(self.contNodos)
    #                 self.contNodos += 1
    #                 temp = self.genTemp()
    #                 nodo.setDir(temp)
    #                 codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + '=' + nodo1.getDir() + "/" + nodo2.getDir() + '\n'
    #                 nodo.setCodigo(codigoConcat)
    #                 self.diccContext[ctx] = nodo

    #             elif ctx.REMINDER():
    #                 nodo = Nodo(self.contNodos)
    #                 self.contNodos += 1
    #                 temp = self.genTemp()
    #                 nodo.setDir(temp)
    #                 codigoConcat = '\n' + nodo1.getCodigo() + nodo2.getCodigo() + nodo.getDir() + '=' + nodo1.getDir() + "%" + nodo2.getDir() + '\n'
    #                 nodo.setCodigo(codigoConcat)
    #                 self.diccContext[ctx] = nodo

    def exitStatement_assign(self, ctx: DecafGramParser.Statement_assignContext):
        nodoL = self.diccContext[ctx.location()]
        nodoE = self.diccContext[ctx.expr()]

        nodo = Nodo(self.contNodos)
        self.contNodos += 1

        nombre = ctx.location().var_id().getText()
        variable = self.tablas.getVariable(nombre, self.scopeActual)

        codigoConcat = nodoE.getCodigo() + (self.generateTopeGet(variable) + "=" + nodoE.getDir())

        nodo.setCodigo(codigoConcat)

        self.diccContext[ctx] = nodo
        self.arrayProd.append(nodo)

    def enterMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        name = ctx.method_name().getText()
        self.scopes.append(name)
        self.scopeActual = name

    def exitMethod_declr(self, ctx: DecafGramParser.Method_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

    def enterStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        name = ctx.ID().getText()
        self.scopes.append(name)
        self.scopeActual = name

    def exitStruct_declr(self, ctx: DecafGramParser.Struct_declrContext):
        self.scopes.pop()
        self.scopeActual = self.scopes[len(self.scopes)-1]

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