import sys
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from src.account import Account, WrongPasswordException, UnknownAccountException
from src.ui import Ui_MainWindow, Ui_userMenu

def change_page(name):
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
        print("Authentification terminé")
        change_page("userMenuWindow")

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
            if not password == passwordConfirmation: text_error += "Le mot de passe et la confirmation sont différent"
            self.ui.createAccountErrorsLabel.setText(text_error)
            self.ui.connectErrorsLabel.clear()
            return False

        # All good !
        Account(username, password).save()
        change_page("userMenuWindow")

class UserMenuWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_userMenu()
        self.ui.setupUi(self)
        self.ui.showQuizzListButton.clicked.connect(self.showQuizzList)

    def showQuizzList(self):
        self.ui.pagesList.setCurrentWidget(self.ui.quizzListPage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    #Convert file .ui -> .py
    os.system("pyside6-uic views/MainWindow.ui -o src/ui/MainWindow.py")
    os.system("pyside6-uic views/UserMenuWindow.ui -o src/ui/UserMenuWindow.py")

    os.system("pyside6-rcc resources/resources.qrc -o resources_rc.py")

    #Page principale
    window = MainWindow()
    sys.exit(app.exec())

