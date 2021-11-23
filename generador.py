class Generador:
    def __init__(self):
        self.contEtiquetas = 0

    def construirHeader(self, nombre):
        return(f'''
.section .text
.global {nombre}
{nombre}:
''')

    def setEspacioFuncion(self, tam):
        return f"\tsub sp, sp, #{tam}\n"

    def nuevaFuncion(self, nombre):
        return(f'''
{nombre}:
''')

    def incioFuncion(self):
        return('''\tpush {r11, lr}
\tadd r11, sp, #0
''')

    def finFuncion(self):
        return('''\tsub sp, r11, #0
\tpop {r11, pc}
\tbx  lr
''')

    def condicion(self, registros):
        return f"\tcmp {registros[0]}, {registros[1]}"

    def tagsInIf(self, tag):
        self.genEtiquetasIf()
        return(f'''
\t{tag} .LBB0_{self.contEtiquetas}
\tb   .LBB0_{self.contEtiquetas-1}

.LBB0_{self.contEtiquetas-1}:
''')

    def tagsOutIf(self, size):
        return(f'''\tb   .LBB0_{self.contEtiquetas}

.LBB0_{self.contEtiquetas}:
\tadd sp, sp, #{size}
''')

    def tagsInWhile(self, tag):
        return(f'''
\t{tag} .LBB0_{self.contEtiquetas}
\tb   .LBB0_{self.contEtiquetas-1}

.LBB0_{self.contEtiquetas-1}:
''')

    def tagsOutWhile(self, size):
        return(f'''\tb   .LBB0_{self.contEtiquetas-2}

.LBB0_{self.contEtiquetas}:
\tadd sp, sp, #{size}
''')

    def whileCond(self):
        self.genEtiquetasWhile()
        return(f'''\tb .LBB0_{self.contEtiquetas-2}

.LBB0_{self.contEtiquetas-2}:
''')

    def suma(self, registros):
        return f"\tadd {registros[0]}, {registros[1]}, {registros[2]}\n"

    def resta(self, registros):
        return f"\tsub {registros[0]}, {registros[1]}, {registros[2]}\n"

    def multi(self, registros):
        return f"\tmul {registros[0]}, {registros[1]}, {registros[2]}\n"

    def genEtiquetasIf(self):
        self.contEtiquetas += 2

    def genEtiquetasWhile(self):
        self.contEtiquetas += 3