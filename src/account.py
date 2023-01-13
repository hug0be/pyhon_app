# -*- coding: utf-8 -*-
import json

from src.history import History


class WrongPasswordException(Exception): pass


class UnknownAccountException(Exception): pass


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.history = History()

    def save(self):
        """Sauvegarde un compte"""
        with open('data/accounts.json', 'r+') as accounts_file:
            accounts = json.load(accounts_file)
            accounts.append(self.to_json())
            accounts_file.seek(0)
            json.dump(accounts, accounts_file)

    def to_json(self):
        """Renvoie le compte en format .json"""
        return {'username': self.username, 'password': self.password, 'admin': False, 'history': self.history.to_json()}

    @staticmethod
    def exists(username: str):
        """Teste si un compte existe"""
        with open('data/accounts.json', 'r') as file:
            for account in json.load(file):
                if username == account['username']: return True
            return False

    @staticmethod
    def access(username: str, password: str):
        """Check compte existe et si le mot de passe est correct"""
        with open('data/accounts.json', 'r') as file:
            accounts = json.load(file)
            for account in accounts:
                if username == account['username']:
                    if password == account['password']: return True
                    raise WrongPasswordException
            raise UnknownAccountException
