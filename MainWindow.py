import sys

from PySide6 import QtUiTools
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

from src.account import Account, WrongPasswordException, UnknownAccountException

loader = QUiLoader()

def create_account_attempt():
    """Méthode appeler pour une tentative de création de compte"""
    #Obtention des identifiants
    username = window.accountUsername.text()
    password = window.accountPassword.text()

    # Check si le compte existe
    if Account.exists(username):
        window.createAccountErrorsLabel.setText("Ce compte existe déjà")
        return False

    #Validation des identifiants
    is_valid = username and password
    if not is_valid:
        text_error = ""
        if not username: text_error += "Saisissez un nom d'utilisateur\n"
        if not password: text_error += "Saisissez un mot de passe"
        window.createAccountErrorsLabel.setText(text_error)
        window.connectErrorsLabel.clear()
        return False

    #All good !
    Account(username, password).save()
    change_page("user_menu")

def connect_attempt():
    """Méthode appeler pour une tentative de connexion"""
    #Obtention des identifiants
    username = window.connectUsername.text()
    password = window.connectPassword.text()

    # Validation des identifiants
    is_valid = username and password
    if not is_valid:
        text_error = ""
        if not username: text_error += "Saisissez votre nom d'utilisateur\n"
        if not password: text_error += "Saisissez votre mot de passe"
        window.connectErrorsLabel.setText(text_error)
        window.createAccountErrorsLabel.clear()
        return False

    # Lancement de la tentative
    try:
        Account.access(username, password)
    except WrongPasswordException:
        window.connectErrorsLabel.setText("Mot de passe incorrect")
        return False
    except UnknownAccountException:
        window.connectErrorsLabel.setText("Compte inexistant")
        return False

    # All good !
    print("Authentification terminé")
    change_page("user_menu")


def change_page(name):
    """Change de page selon le nom donné"""
    global window
    if name == "user_menu":
        window = loader.load("userMenuWindow.ui", None)
    window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Page principale
    window = loader.load("untitled.ui", None)
    window.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))
    loader = QtUiTools.QUiLoader()

    #Bouton "Se connecter"
    window.connectButton.clicked.connect(connect_attempt)
    window.createAccountButton.clicked.connect(create_account_attempt)

    window.show()
    sys.exit(app.exec())
