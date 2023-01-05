import sys

from PySide6 import QtUiTools
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader


loader = QUiLoader()

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)


    def say_hello():
        print("Button clicked, Hello!")

    def clickclick():
        print("clickclick")

    window = loader.load("untitled.ui", None)
    loader = QtUiTools.QUiLoader()
    window.pushButton_5.clicked.connect(clickclick)

    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())