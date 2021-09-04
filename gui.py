from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.editor = QPlainTextEdit()

        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        self.path = None

        layout.addWidget(self.editor)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        file_toolbar = QToolBar("File")

        self.addToolBar(file_toolbar)

        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction("Open file", self)

        open_file_action.setStatusTip("Open file")

        open_file_action.triggered.connect(self.file_open)

        file_menu.addAction(open_file_action)

        file_toolbar.addAction(open_file_action)

        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        compilar_action = QAction("Compilar", self)
        compilar_action.triggered.connect(self.compilar)
        file_menu.addAction(compilar_action)
        file_toolbar.addAction(compilar_action)

        recargar_action = QAction("Recargar errores", self)
        recargar_action.triggered.connect(self.open_errors)
        file_menu.addAction(recargar_action)
        file_toolbar.addAction(recargar_action)

        borrar_action = QAction("Limpiar errores", self)
        borrar_action.triggered.connect(self.erase_errors)
        file_menu.addAction(borrar_action)
        file_toolbar.addAction(borrar_action)

        edit_toolbar = QToolBar("Edit")

        self.addToolBar(edit_toolbar)

        edit_menu = self.menuBar().addMenu("&Edit")

        copy_action = QAction("Copy", self)
        copy_action.setStatusTip("Copy selected text")

        copy_action.triggered.connect(self.editor.copy)

        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setStatusTip("Paste from clipboard")

        paste_action.triggered.connect(self.editor.paste)

        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        select_action = QAction("Select all", self)
        select_action.setStatusTip("Select all text")

        select_action.triggered.connect(self.editor.selectAll)

        edit_toolbar.addAction(select_action)
        edit_menu.addAction(select_action)

        wrap_action = QAction("Wrap text to window", self)
        wrap_action.setStatusTip("Check to wrap text to window")

        wrap_action.setCheckable(True)

        wrap_action.setChecked(True)

        wrap_action.triggered.connect(self.edit_toggle_wrap)

        edit_menu.addAction(wrap_action)

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
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:

                self.dialog_critical(str(e))
            else:
                self.path = path

                self.editor.setPlainText(text)

                self.update_title()

    def open_errors(self):

        try:
            with open("/Users/rsam/OneDrive/Documents/U/5Quinto/Semestre2/Compis/errores.txt", 'rU') as f:
                text = f.read()

        except Exception as e:

            self.dialog_critical(str(e))
        else:
            self.path = "/Users/rsam/OneDrive/Documents/U/5Quinto/Semestre2/Compis/errores.txt"

            self.editor.setPlainText(text)

            self.update_title()

    def erase_errors(self):
        fileVariable = open('errores.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()
        self.open_errors()

    def compilar(self):
        try:
            os.popen('python3 main.py')
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

    window2 = MainWindow()

    app.exec_()