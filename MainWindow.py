import sys

from PySide6 import QtUiTools
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

from src.account import connect_attempt, create_account_attempt

loader = QUiLoader()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Page principale
    window = loader.load("untitled.ui", None)
    window.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))
    loader = QtUiTools.QUiLoader()

    #Bouton "Se connecter"
    window.connectButton.clicked.connect(lambda: connect_attempt(window))
    window.createAccountButton.clicked.connect(lambda: create_account_attempt(window))

    window.show()
    sys.exit(app.exec())
