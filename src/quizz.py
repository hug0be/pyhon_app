# -*- coding: utf-8 -*-
import json
import random

class InvalidQuestionException(Exception): pass
class InvalidNbToDisplayException(Exception): pass
class Question:
    def __init__(self, title:str, rightAnswer:str, wrongAnswers:[str]):
        self.title = title
        self.wrongAnswers = wrongAnswers
        self.rightAnswer = rightAnswer

    def is_right_answer(self, answer)->bool:
        """Retourne si la réponse est vraie ou fausse"""
        return answer == self.rightAnswer

    def all_answers(self)->[str]:
        """Renvoi la liste de question dans un ordre aléatoire (pour l'affichage)"""
        return random.shuffle(self.wrongAnswers + [self.rightAnswer])

    def to_json(self)->dict:
        return {
            'title': self.title,
            'rightAnswer': self.rightAnswer,
            'wrongAnswers': [answer for answer in self.wrongAnswers]
        }

    @staticmethod
    def valid_inputs(title:str, answers:[str], indexRightAnswer:int):
        """Methode qui vérifie si les données renseignées pour créer une question sont valides
        Lance une exception InvalidQuestionException en cas d'invalidité"""
        # Pour éviter les erreurs d'adresse (ne pas modifier le paramètre appelant)
        _answers = answers.copy()

        # Validation de l'intitule
        if not title:
            raise InvalidQuestionException("Saisissez l'intitule de la question")

        # Check si au moins une réponse est écrite
        if not any(_answers):
            raise InvalidQuestionException("Écrivez au moins une réponse")

        # Check si une bonne réponse est choisie
        if indexRightAnswer == -1:
            raise InvalidQuestionException("Sélectionnez une bonne réponse")

        # Check si la bonne réponse choisie est vide
        indexRightAnswer = abs(indexRightAnswer + 2)  # Permets d'obtenir l'index de la réponse dans la liste de réponse
        if indexRightAnswer > len(_answers) or not _answers[indexRightAnswer]:
            raise InvalidQuestionException("La bonne réponse choisie est vide")

        # Check s'il existe au moins une mauvaise réponse
        _answers.pop(indexRightAnswer)
        wrongAnswers = [answer for answer in _answers if answer != '']
        if len(wrongAnswers) < 1:
            raise InvalidQuestionException("Il faut au moins une mauvaise réponse")

        return True

    def __str__(self):
        res = f"\"{self.title}\"\n" \
              f"✔ {self.rightAnswer}\n"
        res += "\n".join([f"❌ {wrongAnswer}\n" for wrongAnswer in self.wrongAnswers])
        return res


class Quizz:
    def __init__(self, title:str):
        self.title = title
        self.questions = []
        self.useRandomOrder = False
        self.nbQuestionsToDisplay = 1
    def save(self):
        """Sauvegarde un quizz"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            quizzes.append({
                'title': self.title,
                'questions': [question.to_json() for question in self.questions],
                'userRandomOrder': self.useRandomOrder,
                'nbQuestionsToDisplay': self.nbQuestionsToDisplay
            })
            quizzes_file.seek(0)
            json.dump(quizzes, quizzes_file, indent=4)
    def nb_questions(self)->int:
        return len(self.questions)
    def __str__(self):
        res = f"Quizz \"{self.title}\"\n" \
               f"Ordre aléatoire: {self.useRandomOrder}\n" \
               f"Nombre de questions affichés: {self.nbQuestionsToDisplay}/{self.nb_questions()}\n\n"
        res += '\n'.join(question.__str__() for question in self.questions)
        return res

    def valid_nb_to_display(self, nbToDisplay:str):
        """Methode qui vérifie si le nombre de questions à afficher pour créer une question est valide"""
        if nbToDisplay == "":
            raise InvalidNbToDisplayException("Saisissez un nombre de questions à afficher")

        nbQuestionsMax = self.nb_questions()
        try:
            nbToDisplay = int(nbToDisplay)
        except ValueError:
            raise InvalidNbToDisplayException(f"Saisissez un nombre valide entre 1 et {nbQuestionsMax}")

        if nbToDisplay <= 0 or nbToDisplay > nbQuestionsMax:
            raise InvalidNbToDisplayException(f"Saisissez un nombre entre 1 et {nbQuestionsMax}")

        # All good !
        return True

    @staticmethod
    def exists(title:str):
        """Teste si un quizz existe"""
        with open('data/quizzes.json', 'r') as file:
            for quizz in json.load(file):
                if title == quizz['title']: return True
            return False

    @staticmethod
    def get_list_quizzes():
        """Récupérer la liste de tous les quizzes"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            list_quizzes = []

            for idQuizz, aQuizz in enumerate(quizzes):
                list_quizzes.append({
                    "idQuizz": idQuizz,
                    "title": aQuizz["title"]
                })

        return list_quizzes