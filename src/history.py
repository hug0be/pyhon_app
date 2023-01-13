# -*- coding: utf-8 -*-
import json

from src.quizz import Quizz

class UnknownHistoryItemException(Exception): pass

class HistoryItem:
    def __init__(self, quizz:Quizz, best_score:int = 0, time:float = 0):
        self.quizz = quizz
        self.best_score = best_score
        self.time = time
    def update_high_score(self, username:str, bestScore:int, time:float):
        with open('data/accounts.json', 'r+') as accounts_file:
            accounts = json.load(accounts_file)
            for account in accounts:
                if account["username"] == username:
                    for item in account["history"]:
                        if item["quizz"] == self.quizz.title:
                            item["time"] = time
                            item["best_score"] = bestScore
                            accounts_file.seek(0)
                            json.dump(accounts, accounts_file, indent=4)
                            return True
                    raise UnknownHistoryItemException

    def to_json(self):
        return {'quizz': self.quizz.title, 'best_score': self.best_score, 'time': self.time}

    def __str__(self):
        res = f"\"{self.quizz.title}\"\n" \
              f"Meilleur score: {self.best_score} / {self.quizz.nb_questions()}\n" \
              f"Temps: {self.time}"
        return res

    def __lt__(self, other):
        """Check si le résultat est meilleur que celui-ci"""
        if not isinstance(other, HistoryItem):
            raise Exception(f"Impossible de comparer HistoryItem et {type(other)}")
        return self.best_score < other.best_score or (self.best_score == other.best_score and self.time > other.time)

    @staticmethod
    def from_json(item:dict):
        return HistoryItem(
            Quizz.get(item["quizz"]),
            item["best_score"],
            item["time"],
        )

class History:
    def __init__(self, items:[HistoryItem]=[]):
        self.items = items

    def save(self, user):
        """Sauvegarde un historique"""
        # TODO : vérifier si le compte existe
        # if not Account.exists(user):
        #     raise UnknownAccountException(f"Le compte '{user}' n'existe pas")
        print("I was here 2")
        with open('data/accounts.json', 'r+') as account_file:
            accounts = json.load(account_file)
            for account in accounts:
                if account['username'] == user:
                    account['history'] = self.to_json()
                    break
            account_file.seek(0)
            json.dump(accounts, account_file, indent=4)

    def get_item(self, quizzTile:str):
        for item in self.items:
            if item.quizz.title == quizzTile:
                return item
        raise UnknownHistoryItemException

    @staticmethod
    def load(user:str):
        """Renvoie l'historique de l'utilisateur"""
        with open('data/accounts.json', 'r') as account_file:
            accounts = json.load(account_file)
            for account in accounts:
                if account['username'] == user:
                    return History.from_json(account['history'])
            return None

    @staticmethod
    def from_json(items:list):
        return History([HistoryItem.from_json(item) for item in items])

    def to_json(self):
        return [item.to_json() for item in self.items]

    def __str__(self):
        return "\n".join(item.__str__() for item in self.items)