# -*- coding: utf-8 -*-
import json

class WrongPasswordException(Exception): pass
class UnknownAccountException(Exception): pass

class Account:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
    def save(self):
        """Sauvegarde un compte"""
        with open('data/accounts.json', 'r+') as accounts_file:
            accounts = json.load(accounts_file)
            accounts.append({'username': self.username, 'password': self.password})
            accounts_file.seek(0)
            json.dump(accounts, accounts_file)
    @staticmethod
    def exists(username:str):
        """Teste si un compte existe"""
        with open('data/accounts.json', 'r') as file:
            for account in json.load(file):
                if username == account['username']: return True
            return False

    @staticmethod
    def access(username:str, password:str):
        """
        Test si un compte existe et si le mot de passe est juste
        Renvoie une UnknownAccountException s'il n'existe pas
        Renvoie une WrongPasswordException si le mot de passe est incorrecte
        Renvoie True s'il existe
        """
        with open('data/accounts.json', 'r') as file:
            accounts = json.load(file)
            for account in accounts:
                if username == account['username']:
                    if password == account['password']: return True
                    raise WrongPasswordException
            raise UnknownAccountException

def create_account_attempt(window):
    """Méthode appeler pour une tentative de création de compte"""
    #Obtention des identifiants
    username = window.accountUsername.text()
    password = window.accountPassword.text()

    #Validation des identifiants
    is_valid = username and password
    if not is_valid:
        text_error = ""
        if not username: text_error += "Saisissez un nom d'utilisateur\n"
        if not password: text_error += "Saisissez un mot de passe"
        window.createAccountErrorsLabel.setText(text_error)
        window.connectErrorsLabel.clear()
        return False

    #Check si les identifiants existent
    if Account.exists(username):
        print("Ce compte existe déjà")
        return False

    #All good !
    Account(username, password).save()

def connect_attempt(window):
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
        print("Mot de passe incorrect")
        return False
    except UnknownAccountException:
        print("Compte inexistant")
        return False

    # All good !
    print("Authentification terminé")
