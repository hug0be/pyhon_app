import json
import sys
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from src.account import Account, WrongPasswordException, UnknownAccountException
from src.quizz import Quizz
from src.ui import Ui_MainWindow, Ui_userMenu

def change_page():
    """Change de page selon le nom donné"""
    global window
    window = UserMenuWindow()
    window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        #Setup
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))

        #Binding
        self.ui.connectButton.clicked.connect(self.connect_attempt)
        self.ui.createAccountButton.clicked.connect(self.create_account_attempt)
        self.show()

    def connect_attempt(self):
        """Méthode appeler pour une tentative de connexion"""
        # Obtention des identifiants
        username = self.ui.connectUsername.text()
        password = self.ui.connectPassword.text()

        # Validation des identifiants
        is_valid = username and password
        if not is_valid:
            text_error = ""
            if not username: text_error += "Saisissez votre nom d'utilisateur\n"
            if not password: text_error += "Saisissez votre mot de passe"
            self.ui.connectErrorsLabel.setText(text_error)
            self.ui.createAccountErrorsLabel.clear()
            return False

        # Lancement de la tentative
        try:
            Account.access(username, password)
        except WrongPasswordException:
            self.ui.connectErrorsLabel.setText("Mot de passe incorrect")
            return False
        except UnknownAccountException:
            self.ui.connectErrorsLabel.setText("Compte inexistant")
            return False

        # All good !
        change_page()

    def create_account_attempt(self):
        """Méthode appeler pour une tentative de création de compte"""
        # Obtention des identifiants
        username = self.ui.accountUsername.text()
        password = self.ui.accountPassword.text()
        passwordConfirmation = self.ui.accountPasswordConfirmation.text()

        # Check si le compte existe
        if Account.exists(username):
            self.ui.createAccountErrorsLabel.setText("Ce compte existe déjà")
            return False

        # Validation des identifiants
        is_valid = username and password and password == passwordConfirmation
        if not is_valid:
            text_error = ""
            if not username: text_error += "Saisissez un nom d'utilisateur\n"
            if not password: text_error += "Saisissez un mot de passe\n"
            if password != passwordConfirmation and username: text_error += "Le mot de passe et la confirmation sont différent"
            self.ui.createAccountErrorsLabel.setText(text_error)
            self.ui.connectErrorsLabel.clear()
            return False

        # All good !
        Account(username, password).save()
        change_page()

class UserMenuWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_userMenu()
        self.ui.setupUi(self)

        #Binding changements de pages
        # TODO: Retour arrière pour les pages "quizzListPage" et "createQuizzPage"
        self.ui.showQuizzListButton.clicked.connect(self.show_quizz_list_page)
        self.ui.createQuizzButton.clicked.connect(self.show_quizz_creation_page)
        self.ui.saveQuizzButton.clicked.connect(self.create_quizz_attempt)

    def show_home_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
    def show_quizz_list_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.quizzListPage)
    def show_quizz_creation_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.createQuizzPage)
    def create_quizz_attempt(self):
        """Méthode appeler pour une tentative de création de quizz"""
        # Obtention des données
        title = self.ui.quizzTitle.text()

        # Validation des données
        if not title:
            self.ui.createQuizzErrorsLabel.setText("Saisissez un titre de quizz")
            return False

        # Check si le quizz existe
        if Quizz.exists(title):
            self.ui.createQuizzErrorsLabel.setText("Ce quizz existe déjà")
            return False

        # All good !
        Quizz(title).save()
        self.show_quizz_list_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    # Check si le fichier quizzes.json existe
    if not os.path.exists("data/quizzes.json"):
        with open('data/quizzes.json', 'w') as quizzes_file:
            quizzes_file.write(json.dumps([]))
        print("Fichier quizzes.json créé")

    #Convert file .ui -> .py
    os.system("pyside6-uic views/MainWindow.ui -o src/ui/MainWindow.py")
    os.system("pyside6-uic views/UserMenuWindow.ui -o src/ui/UserMenuWindow.py")
    os.system("pyside6-rcc resources/resources.qrc -o resources_rc.py")

    #Page principale
    window = MainWindow()
    sys.exit(app.exec())

