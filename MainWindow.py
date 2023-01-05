import sys

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    pass

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    window.show()

    # On démarre la boucle de gestion des événements. coucou
    sys.exit(app.exec())