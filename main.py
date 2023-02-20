import json
import sys
import os

from src.account import Account, WrongPasswordException, UnknownAccountException
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from src.ui import Ui_MainWindow

class UserMenuAccessException(Exception): pass

def change_window(name: str):
    """Change de page selon le nom donné"""
    global window
    window.close()
    if name == "home":
        window = MainWindow()
    window.show()

class MainWindow(QMainWindow):
    """Page principale"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Binding
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        self.ui.connectButton.clicked.connect(self.connect_attempt)
        self.ui.createAccountButton.clicked.connect(self.create_account_attempt)

        # Binding changements de page
        self.ui.chooseConnectButton.clicked.connect(self.show_connect_page)
        self.ui.chooseCreateAccountButton.clicked.connect(self.show_create_account_page)
        self.ui.backButton.clicked.connect(self.show_home)
        self.ui.backButton2.clicked.connect(self.show_home)

    def show_home(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        # Quand l'user reviendra les erreurs auront disparu.
        self.ui.createAccountErrorsLabel.clear()
        self.ui.connectErrorsLabel.clear()

    def show_create_account_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.createAccountPage)

    def show_connect_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.connectPage)

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
            user = Account.get(username, password)
        except WrongPasswordException:
            self.ui.connectErrorsLabel.setText("Mot de passe incorrect")
            return False
        except UnknownAccountException:
            self.ui.connectErrorsLabel.setText("Compte inexistant")
            return False

        # All good !
        print("Connexion réussie")

    def create_account_attempt(self):
        """Méthode appeler pour une tentative de création de compte"""
        # Obtention des identifiants
        username = self.ui.accountUsername.text()
        password = self.ui.accountPassword.text()
        password_confirmation = self.ui.accountPasswordConfirmation.text()

        # Check si le compte existe
        if Account.exists(username):
            self.ui.createAccountErrorsLabel.setText("Ce compte existe déjà")
            return False

        # Validation des identifiants
        is_valid = username and password and password == password_confirmation
        if not is_valid:
            text_error = ""
            if not username: text_error += "Saisissez un nom d'utilisateur\n"
            if not password: text_error += "Saisissez un mot de passe\n"
            if password != password_confirmation and username: text_error += "Le mot de passe et la confirmation sont différent"
            self.ui.createAccountErrorsLabel.setText(text_error)
            self.ui.connectErrorsLabel.clear()
            return False

        # All good !
        user = Account(username, password)
        user.save()
        print("Compte créé !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    # Convert file .ui -> .py
    os.system("pyside6-uic views/MainWindow.ui -o src/ui/MainWindow.py")
    os.system("pyside6-rcc resources/resources.qrc -o resources_rc.py")


    # Check si le fichier accounts.json existe
    if not os.path.exists("data/accounts.json"):
        if not os.path.exists("data"):
            os.mkdir("data")
        with open('data/accounts.json', 'w') as accounts_file:
            accounts = [
                Account("admin","foobar2",True).to_json(),
                Account("user","foobar2",False).to_json()
            ]
            accounts_file.write(json.dumps(accounts))
            print("Fichier accounts.json créé")

    # Page principale
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
