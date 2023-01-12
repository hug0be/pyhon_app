# -*- coding: utf-8 -*-
import json
import random

class InvalidQuestionException(Exception): pass
class InvalidNbToDisplayException(Exception): pass
class ImportQuizzException(Exception): pass
class Question:
    nbAnswersMax = 4
    def __init__(self, title:str="", rightAnswer:str="", wrongAnswers:[str]=[]):
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
    def default_values():
        """Retourne les valeurs par défaut de title, wrongAnswers et rightAnswer"""
        return "", [], None

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
    def __init__(self, title:str="", nbQuestionsToDisplay:int|None=1):
        self.title = title
        self.questions = []
        self.useRandomOrder = False
        self.nbQuestionsToDisplay = nbQuestionsToDisplay
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
    def has_no_question(self)->bool:
        return self.nb_questions() == 0
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
    def default_values():
        """Retourne les valeurs par défaut de title, userRandomOrder et nbQuestionsToDisplay"""
        return None, False, 1

    @staticmethod
    def import_txt(filepath: str):
        with open(filepath, encoding='utf8') as f:
            iLine = 1
            keywords = ["quizz:","question:","reponse:","bonne_reponse:","ordre:","nombre_questions:"]

            questionTitle, questionWrongAnswers, questionRightAnswer = Question.default_values()
            nbAnswers = 0
            quizzTitle, questionOrder, nbQuestionsToDisplay  = Quizz.default_values()
            answersNeeded = False
            quizz = Quizz()

            while True:
                line = f.readline().strip().split()

                # Fin de fichier
                if not line:
                    # Si une question est en cours, on l'ajoute
                    if nbAnswers > 0:
                        question = Question(questionTitle, questionRightAnswer, questionWrongAnswers)
                        quizz.questions.append(question)

                    # Check si le titre est valide
                    if not quizzTitle:
                        raise ImportQuizzException("Le Quizz n'a pas de titre, ajoutez un titre dans le fichier (\"quizz: votre_titre\")")

                    # Check si le quizz a au moins une question
                    if quizz.has_no_question(): raise ImportQuizzException("Le Quizz n'a pas de question")

                    # Check si le nbToDisplay est valide
                    if quizz.nb_questions() > 1:
                        try:
                            quizz.valid_nb_to_display(nbQuestionsToDisplay)
                        except InvalidNbToDisplayException as ex:
                            raise ImportQuizzException(f"A la ligne {iLine}, {ex.__str__().lower()}")

                    if questionOrder:
                        # Check si l'ordre est valide
                        if questionOrder == "aléatoire": questionOrder = True
                        elif questionOrder == "normal": questionOrder = False
                        else: raise ImportQuizzException(f"A la ligne {iLine}, l'ordre \"{rest}\" n'existe pas")

                    # All good !
                    quizz.useRandomOrder = questionOrder
                    quizz.nbQuestionsToDisplay = nbQuestionsToDisplay
                    quizz.title = quizzTitle
                    quizz.save()
                    break

                # Récupération donnée
                keyword = line[0]
                rest = " ".join(line[1:])

                # Check si le mot clé existe
                if not keyword in keywords: raise ImportQuizzException(f"Le mot clé \"{keyword}\" n'existe pas")

                # TODO : On autorise que le ces valeurs soient affectés plusieurs fois ?
                if keyword == "quizz:": quizzTitle = rest
                if keyword == "nombre_questions:": nbQuestionsToDisplay = rest
                if keyword == "ordre:": questionOrder = rest

                if keyword == "question:":
                    # Check si les réponses sont valides
                    if answersNeeded:
                        raise ImportQuizzException(f"A la ligne {iLine-nbAnswers}, la question doit avoir au moins deux réponses")
                    if questionRightAnswer is None and nbAnswers > 0:
                        raise ImportQuizzException(f"A la ligne {iLine-nbAnswers}, la question n'a pas de bonne réponse")

                    # Si ce n'est pas la première question, on enregistre la précédente
                    if nbAnswers > 0:
                        question = Question(questionTitle, questionRightAnswer, questionWrongAnswers)
                        quizz.questions.append(question)
                        # Preparation pour la prochaine question
                        questionTitle, questionWrongAnswers, questionRightAnswer = Question.default_values()

                    questionTitle = rest
                    answersNeeded = True

                if keyword in ["reponse:", "bonne reponse:"]:
                    nbAnswers += 1
                    # Check si on a dépassé le nombre max de réponses
                    if nbAnswers > Question.nbAnswersMax: raise ImportQuizzException(f"A la ligne {iLine}, il y a {nbAnswers} réponses. Il ne peut pas y en avoir plus de {Question.nbAnswersMax}")
                    if nbAnswers >= 2: answersNeeded = False

                if keyword == "reponse:": questionWrongAnswers.append(rest)

                if keyword == "bonne_reponse:":
                    # Check s'il y a plusieurs bonnes réponses
                    if questionRightAnswer is not None: raise ImportQuizzException(f"A la ligne {iLine}, il y a plusieurs bonnes réponse. Il ne peut en rester qu'une !")
                    questionRightAnswer = rest

                iLine += 1
