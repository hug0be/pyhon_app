# -*- coding: utf-8 -*-
import json
import random

class Answers:
    def __init__(self, realAnswer:str, falseAnswers:[str]):
        self.realAnswer = realAnswer
        self.falseAnswer = falseAnswers

    def is_answer(self, answer):
        """Retourne si la réponse est vraie ou fausse"""
        return answer == self.realAnswer
    def answers_to_list(self):
        """Renvoi la liste de question dans un ordre aléatoire (pour l'affichage)"""
        shuffledAnswer = self.falseAnswer + [self.realAnswer]
        random.shuffle(shuffledAnswer)
        return shuffledAnswer

class Quizz:
    def __init__(self, title:str):
        self.title = title
    def save(self):
        """Sauvegarde un quiz"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            quizzes.append({'title': self.title})
            quizzes_file.seek(0)
            json.dump(quizzes, quizzes_file)
    @staticmethod
    def exists(title:str):
        """Teste si un quiz existe"""
        with open('data/quizzes.json', 'r') as file:
            for quizz in json.load(file):
                if title == quizz['title']: return True
            return False

