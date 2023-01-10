# -*- coding: utf-8 -*-
import json

class WrongPasswordException(Exception): pass
class UnknownAccountException(Exception): pass

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

