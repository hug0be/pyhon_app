import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinQuest")
        self.setWindowIcon(QIcon("resources/images/favicon.png"))
        self.resize(800, 600)

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())