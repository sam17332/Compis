import pickle5 as pickle

class Proyecto3():
    def __init__(self):
        infile = open("codigo", 'rb')
        self.arrayCodigoInt = pickle.load(infile)
        self.limpiarCodigo()

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

        for i in range(len(arrayFinal)):
            valor = arrayFinal[i]
            cont = 0
            for j in valor:
                if j.isalpha():
                    arrayFinal[i] = valor[cont:len(valor)]
                    break
                cont += 1

        self.arrayCodigoInt = arrayFinal
        # for i in self.arrayCodigoInt:
        #     print(i)


def main():
    proy3 = Proyecto3()

main()