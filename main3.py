import pickle5 as pickle
from generador import *

class Proyecto3():
    def __init__(self):
        infile = open("codigo", 'rb')
        self.arrayCodigoInt = pickle.load(infile)
        self.header = False
        self.codigoFinal = ""
        self.sizeMetodo = 0
        self.descriptorDirecciones = {}
        self.descriptorRegistros = {
            'R0': [],
            'R1': [],
            'R2': [],
            'R3': [],
            'R4': [],
            'R5': [],
            'R6': [],
            'R7': [],
            'R8': [],
            'R9': [],
            'R10': [],
        }
        self.operadoresBoolContrarios = {
            'bge': 'bgt',
            'ble': 'blt',
            'beq': 'bne',
            'bne': 'beq',
            'bgt': 'bge',
            'blt': 'ble',
        }
        self.operadoresBool = {
            '<=': 'bge',
            '>=': 'ble',
            '!=': 'bne',
            '==': 'beq',
            '<': 'bgt',
            '>': 'blt',
        }
        self.condicionActual = ""
        self.limpiarCodigo()
        self.generarCodigo()

    def limpiarCodigo(self):
        array = []
        for tripleta in self.arrayCodigoInt:
            cont = 0
            for i in tripleta:
                if i != ' ':
                    tripLimpia = tripleta[cont:len(tripleta)]
                    array.append(tripLimpia)
                    break
                cont += 1
        arrayFinal = []
        for pos in array:
            if '\n' in pos:
                arraySplit = pos.split('\n')
                for posi in arraySplit:
                    if posi != '' and posi != ' ':
                        arrayFinal.append(posi)
            else:
                arrayFinal.append(pos)

        for i in range(len(arrayFinal)):
            valor = arrayFinal[i]
            cont = 0
            for j in valor:
                if j.isalpha():
                    arrayFinal[i] = valor[cont:len(valor)]
                    break
                cont += 1

        self.arrayCodigoInt = arrayFinal
        # Debug only
        # for i in self.arrayCodigoInt:
        #     print(i)

    def generarCodigo(self):
        generador = Generador()
        codigo = ""
        registros = ['', '']
        elementos = []
        inWhile = False
        for linea in self.arrayCodigoInt:
            # print(linea)
            if self.condicionActual == "":
                for i in self.operadoresBool.keys():
                    if i in linea:
                        print('')
                        self.condicionActual = i
                        break
            if 'IF' in linea and 'GOTO' in linea and 'IF_FALSE' not in linea:
                condSimbol = self.operadoresBool[self.condicionActual]
                tag = self.operadoresBoolContrarios[condSimbol]
                if inWhile:
                    self.codigoFinal += generador.whileCond()
                    self.codigoFinal += codigo
                    self.codigoFinal += generador.condicion(registros)
                    self.codigoFinal += generador.tagsInWhile(tag)
                else:
                    self.codigoFinal += codigo
                    self.codigoFinal += generador.condicion(registros)
                    self.codigoFinal += generador.tagsInIf(tag)
                self.condicionActual = ""
            elif 'GOTO IF_FALSE' in linea:
                pass
            elif 'IF_TRUE' in linea:
                pass
            elif 'CALL' in linea:
                pass
            elif '= R' in linea:
                pass
            elif 'WHILE_LOOP_' in linea:
                inWhile = True
            elif 'GOTO END_WHILE_0' in linea:
                pass
            elif 'RETURN' in linea:
                pass
            elif 'END_WHILE_' in linea:
                self.codigoFinal += generador.tagsOutWhile(self.sizeMetodo)
                inWhile = False
            elif 'IF_FALSE' in linea and 'GOTO' not in linea:
                self.codigoFinal += generador.tagsOutIf(self.sizeMetodo)
            elif self.condicionActual != "":
                codigo, registros, elementos = self.getRegCondicion(linea)
            elif ('DEF' in linea) and ('END DEF' not in linea):
                nombreMetodo = linea.replace('DEF ', '')
                indexSize1 = nombreMetodo.find(',')
                indexSize2 = nombreMetodo.find(':')
                self.sizeMetodo = nombreMetodo[indexSize1+1:indexSize2]
                nombreMetodo = nombreMetodo[:indexSize1]
                if self.header == False:
                    self.header = True
                    self.codigoFinal += generador.construirHeader(nombreMetodo)
                else:
                    self.codigoFinal += generador.nuevaFuncion(nombreMetodo)
                self.codigoFinal += generador.incioFuncion()
                self.codigoFinal += generador.setEspacioFuncion(self.sizeMetodo)
            elif('END DEF' in linea):
                self.codigoFinal += generador.finFuncion()
            else:
                codigo, registros, elementos = self.getReg(linea)
                self.codigoFinal += codigo
                if '+' in linea or '-' in linea or '*' in linea:
                    if '+' in linea:
                        self.codigoFinal += generador.suma(registros)
                    elif '-' in linea:
                        self.codigoFinal += generador.resta(registros)
                    elif '*' in linea:
                        self.codigoFinal += generador.multi(registros)
                    self.descriptorRegistros[registros[0]] = [elementos[0]]
                    self.descriptorDirecciones[elementos[0]] = [registros[0]]
                    for llave, valor in self.descriptorDirecciones.items():
                        if registros[0] in valor and llave != elementos[0]:
                            indice = valor.index(registros[0])
                            self.descriptorDirecciones[llave].pop(indice)
                else:
                    self.descriptorRegistros[registros[1]].append(elementos[0])
                    self.descriptorDirecciones[elementos[0]] = [registros[1]]

        self.guardarCodigo()

    def guardarCodigo(self):
        print("-------------CODIGO----------")
        print()
        filename = 'codigoARM'
        outfile = open(filename, 'wb')
        pickle.dump(self.codigoFinal, outfile)
        outfile.close()
        print(self.codigoFinal)

    def getRegCondicion(self, condicion):
        codigoReturn = ""
        registros = ['', '']
        elementos = []
        array = condicion.split('=', 1)
        array = array[1].split(self.condicionActual)
        x = array[0].replace(' ', '')
        y = array[1].replace(' ', '')

        llaves = self.descriptorDirecciones.keys()

        if x not in llaves:
            self.descriptorDirecciones[x] = [] if 't' in x else [x]
        if y not in llaves:
            self.descriptorDirecciones[y] = [] if 't' in y else [y]

        elementos = [y, x]

        cont = 0
        for elem in elementos:
            for llave, valor in self.descriptorRegistros.items():
                if elem in valor:
                    registros[cont] = llave
                    break
                elif elem not in valor:
                    if len(valor) == 0:
                        self.descriptorRegistros[llave] = [elem]
                        self.descriptorDirecciones[elem].append(llave)
                        esLiteral = False
                        try:
                            elem = int(elem)
                            esLiteral = True
                        except:
                            pass
                        if not esLiteral:
                            codigoReturn += f"\tldr {llave}, {self.getPos(elem)}\n"
                        else:
                            codigoReturn += f"\tmov {llave}, #{elem}\n"
                            codigoReturn += f"\tstr {llave}, [sp]\n"
                        registros[cont] = llave
                        break
            cont += 1

        return codigoReturn, registros, elementos

    def getReg(self, tripleta):
        if '=' in tripleta:
            esOperacion = False
            operacion = ""
            operadores = ['+', '-', '*', '%']
            codigoReturn = ""
            registros = ['', '', '']
            caso3 = False
            elementos = []
            # Verificar si es una operacion u asignacion
            for x in operadores:
                if x in tripleta:
                    esOperacion = True
                    operacion = x
                    break

            llaves = self.descriptorDirecciones.keys()

            if esOperacion:  # si la instruccion es tripleta
                pos_eq = tripleta.find("=")
                pos_op = tripleta.find(operacion)
                x = tripleta[:pos_eq].replace(' ', '')
                y = tripleta[pos_eq+1:pos_op].replace(' ', '')
                z = tripleta[pos_op+1:].replace(' ', '')
                if x not in llaves:
                    self.descriptorDirecciones[x] = [] if 't' in x else [x]
                if y not in llaves:
                    self.descriptorDirecciones[y] = [] if 't' in y else [y]
                if z not in llaves:
                    self.descriptorDirecciones[z] = [] if 't' in z else [z]
                # print("Val1 ", x)
                # print("Val2 ", y)
                # print("Val3 ", z)
                elementos = [x, y, z]
                caso3 = True
                # Revision de caso 1 y 2
                for llave, valor in self.descriptorRegistros.items():
                    if y in valor:
                        # print("Entro al caso 1, no se hace nada")
                        # print("Reg ", llave)
                        registros[1] = llave
                        caso3 = False
                        break
                    if y not in valor:
                        if len(valor) == 0:
                            # print("Reg ", llave)
                            self.descriptorRegistros[llave] = [
                                y]  # se ingresa al registro
                            self.descriptorDirecciones[y].append(llave)
                            esLiteral = False
                            try:
                                y = int(y)
                                esLiteral = True
                            except:
                                pass
                            if(esLiteral == False):
                                codigoReturn += f"\tldr {llave}, {self.getPos(y)}\n"
                            else:
                                codigoReturn += f"\tmov {llave}, #{y}\n"
                                codigoReturn += f"\tstr {llave}, [sp]\n"
                            registros[1] = llave
                            caso3 = False
                            break
                if caso3:  # No encontro primeros casos
                    for llave, valor in self.descriptorDirecciones.items():
                        # ingresar casos de caso 3
                        if len(valor) > 1:
                            index = 0
                            for val in valor:
                                if 'R' in val:
                                    break
                                index += 1
                            tempR = self.descriptorDirecciones[llave].pop(
                                index)  # se quita el registro
                            self.descriptorRegistros[tempR] = llave
                            esLiteral = False
                            try:
                                y = int(y)
                                esLiteral = True
                            except:
                                pass
                            if(esLiteral == False):
                                codigoReturn += f"\tldr {tempR}, {self.getPos(y)}\n"
                            else:
                                codigoReturn += f"\tmov {tempR}, #{y}\n"
                                codigoReturn += f"\tstr {tempR}, [sp]\n"
                            registros[1] = llave
                            break

                caso3 = True
                # valor z Revision de caso 1 y 2
                for llave, valor in self.descriptorRegistros.items():
                    if z in valor:
                        # print("Entro al caso 1, no se hace nada")
                        # print("Reg ", llave)
                        registros[2] = llave
                        caso3 = False
                        break
                    if z not in valor:
                        if len(valor) == 0:
                            # print("Reg ", llave)
                            self.descriptorRegistros[llave] = [
                                z]  # se ingresa al registro
                            self.descriptorDirecciones[z].append(llave)
                            esLiteral = False
                            try:
                                z = int(z)
                                esLiteral = True
                            except:
                                pass
                            if(esLiteral == False):
                                codigoReturn += f"\tldr {llave}, {self.getPos(z)}\n"
                            else:
                                codigoReturn += f"\tmov {llave}, #{z}\n"
                                codigoReturn += f"\tstr {llave}, [sp]\n"
                            registros[2] = llave
                            caso3 = False
                            break
                if caso3:  # no se encontro nada en los otros casos
                    for llave, valor in self.descriptorDirecciones.items():
                        # ingresar casos de caso 3
                        if len(valor) > 1:
                            index = 0
                            for val in valor:
                                if 'R' in val:
                                    break
                                index += 1
                            tempR = self.descriptorDirecciones[llave].pop(
                                index)  # se quita el registro
                            self.descriptorRegistros[tempR] = llave
                            esLiteral = False
                            try:
                                z = int(z)
                                esLiteral = True
                            except:
                                pass
                            if(esLiteral == False):
                                codigoReturn += f"\tldr {tempR}, {self.getPos(z)}\n"
                            else:
                                codigoReturn += f"\tmov {tempR}, #{z}\n"
                                codigoReturn += f"\tstr {tempR}, [sp]\n"
                            registros[2] = llave
                            break

                # valor x
                for llave, valor in self.descriptorRegistros.items():  # Caso 1
                    if x in valor:
                        registros[0] = llave
                        break

                if registros[0] == '':  # No se cumple el caso 1
                    registros[0] = registros[1]

                self.descriptorDirecciones[x].append(registros[0])
                self.descriptorRegistros[registros[0]] = [x]

            else:  # si la instruccion es una asignacion
                pos_eq = tripleta.find("=")
                x = tripleta[:pos_eq].replace(' ', '')
                y = tripleta[pos_eq+1:].replace(' ', '')
                elementos = [x, y]
                keysDir = self.descriptorDirecciones.keys()
                if x not in keysDir:
                    self.descriptorDirecciones[x] = [] if 't' in x else [x]
                if y not in keysDir:
                    self.descriptorDirecciones[y] = [] if 't' in y else [y]
                # print("Val1 ", x)
                # print("Val2 ", y)
                tempReg = self.descriptorDirecciones[y]
                regy = ""
                # Encontrar registro de Y
                for ele in tempReg:
                    if "R" == ele[0]:
                        regy = ele

                if regy == '':
                    caso3 = True
                    numeric = False
                    if y.isnumeric():
                        numeric = True

                    # Se itera los registros
                    for key, value in self.descriptorRegistros.items():
                        # Si 'y' esta en un registro
                        if y in value:
                            regy = key
                            caso3 = False
                            break
                        # Si 'y' no esta en ese registro y el registro esta vacio
                        elif y not in value and len(value) == 0:
                            # Se actualizan ambos diccionarios
                            self.descriptorRegistros[key] = [y]
                            self.descriptorDirecciones[y].append(key)
                            if not numeric:
                                if y[2] == 't':
                                    codigoReturn = f'\tldr {key}, {self.getPosRg(y)}\n'
                                else:
                                    codigoReturn = f'\tldr {key}, {self.getPos(y)}\n'
                            regy = key
                            caso3 = False
                            break
                    if caso3:
                        for key, value in self.descriptorRegistros.items():
                            if len(value) > 1:
                                index = 0
                                for j in value:
                                    if 'R' in j:
                                        break
                                    index += 1
                                tempR = self.descriptorDirecciones[key].pop(index)
                                self.descriptorRegistros[tempR] = key
                                if not numeric:
                                    if y[2] == 't':
                                        codigoReturn = f'\tldr {key}, {self.getPosRg(y)}\n'
                                    else:
                                        codigoReturn = f'\tldr {key}, {self.getPos(y)}\n'
                                regy = key
                                break

                    if numeric:
                        codigoReturn += f'{regy}, #{y}\n'
                        self.descriptorRegistros[regy].pop()
                        self.descriptorDirecciones[y].pop()

                # Agregar x al descriptor de registro Ry
                self.descriptorRegistros[regy].append(x)
                self.descriptorDirecciones[x] = [x]
                registros[0] = regy
                registros[1] = regy
                esLiteral = False
                try:
                    x = int(x)
                    esLiteral = True
                except:
                    pass
                if esLiteral == False:
                    codigoReturn = f"\tstr {regy}, {self.getPos(x)}\n"
                else:
                    codigoReturn += f"\tmov {regy}, #{x}\n"
                    codigoReturn += f"\tstr {regy}, [sp]\n"

        return codigoReturn, registros, elementos

    def getPos(self, variable):
        # print('----getPos----')
        # print(variable)
        if variable[0] == "f":  # es una variable Local
            val = str(variable[3:-1])
            if val.isnumeric():
                inst = f'[sp, #{val}]'
                return inst
            else:
                return variable
        else:
            return ""

    def getPosRg(self, variable):
        # print('----getPosRg----')
        # print(variable)
        regs = self.descriptorDirecciones[variable[2:-1]]
        reg = ""
        inst = ""
        for ele in regs:
            if ele[0] == 'R':
                reg = ele

        if variable[0] == 'f':
            inst = f'[sp, {reg}]'

        return inst



def main():
    print('''
---------------------------------------------------------
--------------------- MAIN 3 ----------------------------
---------------------------------------------------------
    ''')
    proy3 = Proyecto3()

main()