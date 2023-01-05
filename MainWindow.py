import sys

from PySide6 import QtUiTools
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader


loader = QUiLoader()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    def say_hello():
        print("Button clicked, Hello!")

    def clickclick():
        print("clickclick")

    window: QMainWindow = loader.load("untitled.ui", None)
    window.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))
    loader = QtUiTools.QUiLoader()
    window.pushButton_5.clicked.connect(clickclick)

    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())