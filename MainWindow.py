import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    pass

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)


    def say_hello():
        print("Button clicked, Hello!")



        # TODO : Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    button = QPushButton("Click me", window)
    button.clicked.connect(say_hello)
    button.show()
    window.show()

    # On démarre la boucle de gestion des événements. coucou
    sys.exit(app.exec())