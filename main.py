import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from src.account import Account, WrongPasswordException, UnknownAccountException
from src.ui import Ui_MainWindow, Ui_userMenu

def create_account_attempt():
    """Méthode appeler pour une tentative de création de compte"""
    #Obtention des identifiants
    username = window.ui.accountUsername.text()
    password = window.ui.accountPassword.text()

    # Check si le compte existe
    if Account.exists(username):
        window.ui.createAccountErrorsLabel.setText("Ce compte existe déjà")
        return False

    #Validation des identifiants
    is_valid = username and password
    if not is_valid:
        text_error = ""
        if not username: text_error += "Saisissez un nom d'utilisateur\n"
        if not password: text_error += "Saisissez un mot de passe"
        window.ui.createAccountErrorsLabel.setText(text_error)
        window.ui.connectErrorsLabel.clear()
        return False

    #All good !
    Account(username, password).save()
    change_page("userMenuWindow")

def connect_attempt():
    """Méthode appeler pour une tentative de connexion"""
    #Obtention des identifiants
    username = window.ui.connectUsername.text()
    password = window.ui.connectPassword.text()

    # Validation des identifiants
    is_valid = username and password
    if not is_valid:
        text_error = ""
        if not username: text_error += "Saisissez votre nom d'utilisateur\n"
        if not password: text_error += "Saisissez votre mot de passe"
        window.ui.connectErrorsLabel.setText(text_error)
        window.ui.createAccountErrorsLabel.clear()
        return False

    # Lancement de la tentative
    try:
        Account.access(username, password)
    except WrongPasswordException:
        window.ui.connectErrorsLabel.setText("Mot de passe incorrect")
        return False
    except UnknownAccountException:
        window.ui.connectErrorsLabel.setText("Compte inexistant")
        return False

    # All good !
    print("Authentification terminé")
    change_page("userMenuWindow")


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
        self.ui.connectButton.clicked.connect(connect_attempt)
        self.ui.createAccountButton.clicked.connect(create_account_attempt)
        self.show()

class UserMenuWindow(QMainWindow):
    def __init__(self):
        #Setup
        QMainWindow.__init__(self)
        self.ui = Ui_userMenu()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    #Page principale
    window = MainWindow()
    sys.exit(app.exec())
