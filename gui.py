from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import pickle
import os
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(200, 200, 1000, 500)

        self.editor = QPlainTextEdit()

        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(10)

        mainlayout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.windowEditor = QWidget()
        self.windowCodigo = QWidget()
        self.windowIntermedio = QWidget()

        self.tabs.addTab(self.windowEditor, "Editor")
        self.tabs.addTab(self.windowCodigo, "Análisis semántico")
        self.tabs.addTab(self.windowIntermedio, "Código intermedio")

        self.textForCode = QPlainTextEdit()
        self.textForCode.setFont(fixedfont)

        self.windowIntermedio.layout = QVBoxLayout()
        self.windowIntermedio.layout.addWidget(self.textForCode)
        self.windowIntermedio.setLayout(self.windowIntermedio.layout)

        self.editor = QPlainTextEdit()

        self.errorForLog = QLabel()
        self.errorForLog.setFont(fixedfont)
        self.errorForLog.setText("")
        self.windowCodigo.layout = QVBoxLayout()
        self.windowCodigo.layout.addWidget(self.errorForLog)
        self.windowCodigo.setLayout(self.windowCodigo.layout)

        self.editor.setFont(fixedfont)

        self.path = None

        mainlayout.addWidget(self.tabs)

        self.windowEditor.layout = QVBoxLayout()
        self.windowEditor.layout.addWidget(self.editor)
        self.windowEditor.setLayout(self.windowEditor.layout)

        container = QWidget()

        container.setLayout(mainlayout)

        self.setCentralWidget(container)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        file_toolbar = QToolBar("File")

        self.addToolBar(file_toolbar)

        open_file_action = QAction("Open file", self)

        open_file_action.setStatusTip("Open file")

        open_file_action.triggered.connect(self.file_open)

        file_toolbar.addAction(open_file_action)

        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_toolbar.addAction(save_file_action)

        compilar_action = QAction("Compilar", self)
        compilar_action.setStatusTip("Compilar programa")
        compilar_action.triggered.connect(self.compilar)
        file_toolbar.addAction(compilar_action)

        borrar_action = QAction("Limpiar errores", self)
        borrar_action.triggered.connect(self.erase_errors)
        file_toolbar.addAction(borrar_action)

        generar_action = QAction("Generar código", self)
        generar_action.setStatusTip("Generar código")
        generar_action.triggered.connect(self.codigoIntermedio)
        file_toolbar.addAction(generar_action)

        borrar_codigo_action = QAction("Limpiar codigo", self)
        borrar_codigo_action.triggered.connect(self.erase_code)
        file_toolbar.addAction(borrar_codigo_action)

        wrap_action = QAction("Wrap text to window", self)
        wrap_action.setStatusTip("Check to wrap text to window")

        wrap_action.setCheckable(True)

        wrap_action.setChecked(True)

        wrap_action.triggered.connect(self.edit_toggle_wrap)

        self.update_title()

        self.show()

    def dialog_critical(self, s):

        dlg = QMessageBox(self)

        dlg.setText(s)

        dlg.setIcon(QMessageBox.Critical)

        dlg.show()

    def file_open(self):

        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                             "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()

            except Exception as e:

                self.dialog_critical(str(e))
            else:
                self.path = path

                self.editor.setPlainText(text)

                self.update_title()

    def erase_errors(self):
        fileVariable = open('errores.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()
        self.errorForLog.setText('')

    def erase_code(self):
        self.textForCode.setText('')

    def compilar(self):
        try:
            os.popen('python3 main.py')
            infile = open("errores", 'rb')
            arrayErrores = pickle.load(infile)
            errores = ''
            if arrayErrores != None and len(arrayErrores) > 0:
                errores = '\n'.join(arrayErrores)
            else:
                errores = 'No hay errores'
            self.errorForLog.setText(errores)
        except:
            print('Ha ocurrido un error al compilar')

    def codigoIntermedio(self):
        try:
            os.popen('python3 main2.py')
            infile = open("codigo", 'rb')
            arrayCodigo = pickle.load(infile)
            # print(arrayCodigo)
            codigo = ''.join(arrayCodigo)
            self.textForCode.setPlainText(codigo)
        except:
            print('Ha ocurrido un error al compilar')

    def file_save(self):

        if self.path is None:

            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                             "Text documents (*.txt);All files (*.*)")

        if not path:
            return

        self._save_to_path(path)

    def _save_to_path(self, path):

        text = self.editor.toPlainText()

        try:

            with open(path, 'w') as f:

                f.write(text)

        except Exception as e:

            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def update_title(self):

        self.setWindowTitle("%s - PyQt5 Notepad" %(os.path.basename(self.path)
                                                  if self.path else "Untitled"))

    def edit_toggle_wrap(self):

        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )

if __name__ == '__main__':

    app = QApplication(sys.argv)

    app.setApplicationName("GUI")

    window = MainWindow()

    # window2 = MainWindow()

    app.exec_()