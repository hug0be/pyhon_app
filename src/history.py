import json
from src import Account, UnknownAccountException
from src.quizz import Quizz

class HistoryItem:

    def __init__(self, quizz:Quizz = None, best_score:int = None, time:float = None):
        self.quizz = quizz
        self.best_score = best_score
        self.time = time

    def __str__(self):
        res = f"Quizz \"{self.quizz.title}\"\n" \
              f"Meilleur Score: {self.best_score} / {self.quizz.nb_questions()}\n" \
              f"Temps: {self.time}\n"
        return res

    def to_json(self):
        return {'quizz': self.quizz.title, 'best_score': self.best_score, 'time': self.time}


class History:
    def __init__(self, items:[HistoryItem]):
        self.items = items

    def to_json(self):
        return {'items': [item.to_json() for item in self.items]}
    def compare_item(self, item, itemToEdit: HistoryItem)->HistoryItem:
        """Renvoie l'item avec les meilleurs stats"""
        mustBeReplaced = item.best_score < itemToEdit.best_score or (item.best_score == item.best_score and item.time > item.time)
        return itemToEdit if mustBeReplaced else item

    def add_item(self, itemToAdd: HistoryItem)->None:
        """
        Ajoute un item à la liste de l'historique, 4 cas :
            - le quizz n'a jamais été fait : on l'ajoute à la liste
            - le quizz a déjà été fait, mais on n'a pas battu le score : il ne se passe rien
            - le quizz a déjà été fait et on a battu le meilleur score : on remplace l'item
            - le quizz a déjà été réalisé au même score : si le temps est meilleur on remplace l'item, sinon on ne fait rien
        """
        itemsCopy = self.items.copy()
        for i_item, item in enumerate(self.items):
            if item.quizz.title == item.quizz.title:
                itemsCopy[i_item] = self.compare_item(itemToAdd, item)
            else:
                itemsCopy.append(item)
        self.items = itemsCopy
    def save(self, user):
        """Sauvegarde un historique"""
        if not Account.exists(user):
            raise UnknownAccountException(f"Le compte '{user}' n'existe pas")

        with open('data/accounts.json', 'r+') as account_file:
            accounts = json.load(account_file)
            for account in accounts:
                if account['username'] == user:
                    account['history'] = self.to_json()
                    break
            account_file.seek(0)
        with open('data/accounts.json', 'w') as account_file:
            json.dump(accounts, account_file, indent=4)
