# -*- coding: utf-8 -*-
import json
import random

class Answers:
    #TODO : Utiliser cette classe
    def __init__(self, rightAnswer:str, wrongAnswers:[str]):
        self.rightAnswer = rightAnswer
        self.wrongAnswer = wrongAnswers

    def is_answer(self, answer):
        """Retourne si la réponse est vraie ou fausse"""
        return answer == self.rightAnswer
    def answers_to_list(self):
        """Renvoi la liste de question dans un ordre aléatoire (pour l'affichage)"""
        shuffledAnswer = self.wrongAnswer + [self.rightAnswer]
        random.shuffle(shuffledAnswer)
        return shuffledAnswer

class Quizz:
    def __init__(self, title:str):
        self.title = title
    def save(self):
        """Sauvegarde un quizz"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            quizzes.append({'title': self.title})
            quizzes_file.seek(0)
            json.dump(quizzes, quizzes_file)
    @staticmethod
    def exists(title:str):
        """Teste si un quizz existe"""
        with open('data/quizzes.json', 'r') as file:
            for quizz in json.load(file):
                if title == quizz['title']: return True
            return False