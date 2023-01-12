import json

from src.quizz import Quizz


class HistoryCase:

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
        return {'quizz': self.quizz.to_json(), 'best_score': self.best_score, 'time': self.time}


class History:
    def __init__(self, cases:[HistoryCase]):
        self.cases = cases

    def to_json(self):
        return {'cases': [case.to_json() for case in self.cases]}

    def save(self, user):
        """Sauvegarde un historique"""
        with open('data/accounts.json', 'r+') as account_file:
            # history = json.load(history_file)
            # history.append(self.to_json()) # bof bof (pas le bon fichier)
            accounts = json.load(account_file)
            for account in accounts:
                if account['username'] == user:
                    account['history'] = self.to_json()
                    break
            account_file.seek(0)
            json.dump(accounts, account_file, indent=4)
