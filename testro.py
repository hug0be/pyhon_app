import sys
from PySide6 import QtWidgets, QtUiTools
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
def clickclick():
    print("clickclick")
def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")

app = QtWidgets.QApplication(sys.argv)

window = loader.load("untitled.ui", None)
loader = QtUiTools.QUiLoader()

window.pushButton_5.clicked.connect(clickclick)

mainwindow_setup(window)
window.show()
app.exec()