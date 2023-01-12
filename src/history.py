import json

from src import Quizz


class HistoryCase:

    def __init__(self, quizz:Quizz, best_score:int, time:float):
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
    def __init__(self, cases:[HistoryCase]):
        self.cases = cases
    def save(self):
        """Sauvegarde un historique"""
        with open('data/history.json', 'r+') as history_file:
            history = json.load(history_file)
            history.append({'cases': [case.to_json() for case in self.cases]})
            history_file.seek(0)
            json.dump(history, history_file)
