# -*- coding: utf-8 -*-
import json


class WrongPasswordException(Exception): pass

class UnknownAccountException(Exception): pass

class Account:
    """
    Classe qui représente un compte utilisateur
    Propriétés :
        username (nom d'utilisateur), password (mot de passe)
        isAdmin (vrai si l'utilisateur est un admin)
        history (l'historique des quizz joué par l'utilisateur)
    """
    def __init__(self, username: str, password: str, isAdmin: bool = False):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def save(self):
        """Sauvegarde un compte"""
        with open('data/accounts.json', 'r+') as accounts_file:
            accounts = json.load(accounts_file)
            accounts.append(self.to_json())
            accounts_file.seek(0)
            json.dump(accounts, accounts_file, indent=4)

    def to_json(self):
        """Renvoie le compte en format .json"""
        return {'username': self.username, 'password': self.password, 'admin': self.isAdmin }

    @staticmethod
    def from_json(accountJson:dict):
        """Renvoie le compte depuis un .json"""
        return Account(
            accountJson["username"],
            accountJson["password"],
            accountJson["admin"]
        )

    @staticmethod
    def exists(username: str):
        """Teste si un compte existe"""
        with open('data/accounts.json', 'r') as file:
            for account in json.load(file):
                if username == account['username']: return True
            return False

    @staticmethod
    def get(username: str, password: str):
        """Get un compte s'il existe et si le mot de passe est correct"""
        with open('data/accounts.json', 'r') as file:
            accounts = json.load(file)
            for account in accounts:
                if username == account['username']:
                    if password == account['password']:
                        return Account.from_json(account)
                    raise WrongPasswordException
            raise UnknownAccountException
