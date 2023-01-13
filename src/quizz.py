# -*- coding: utf-8 -*-
import json
import random

class InvalidQuizzException(Exception): pass
class UnknownQuizzException(Exception): pass
class InvalidQuestionException(Exception): pass
class InvalidNbToDisplayException(Exception): pass
class InvalidNbAnswersException(Exception): pass
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

    def nb_answers(self):
        return len(self.wrongAnswers) + bool(self.rightAnswer)

    def is_valid(self):
        # Check de l'intitule
        if not self.title:
            raise InvalidQuestionException("Saisissez l'intitule de la question")
        # Check le nombre de réponses
        try: Question.valid_nb_answers(self.nb_answers())
        except InvalidNbAnswersException as e:
            raise InvalidQuestionException(f"Pour la question {self.title}, {e.__str__().lower()}")
        # Check s'il y a une bonne réponse
        if self.rightAnswer == "": raise InvalidQuestionException(f"La question n'a pas de bonne réponse")
        return True

    def to_json(self)->dict:
        return {
            'title': self.title,
            'rightAnswer': self.rightAnswer,
            'wrongAnswers': [answer for answer in self.wrongAnswers]
        }
    @staticmethod
    def from_json(question_json:dict):
        return Question(
            question_json["title"],
            question_json["rightAnswer"],
            question_json["wrongAnswers"]
        )

    @staticmethod
    def default_values():
        """Retourne les valeurs par défaut de title, wrongAnswers et rightAnswer"""
        return "", [], ""

    @staticmethod
    @staticmethod
    def valid_inputs(title:str, answers:[str], indexRightAnswer:int):
        """Check si les données de cette question sont valides"""
        # Pour éviter les erreurs d'adresse (ne pas modifier le paramètre appelant)
        _answers = answers.copy()

        # Check title
        if not title:
            raise InvalidQuestionException("Saisissez l'intitulé de la question")

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

    @staticmethod
    def valid_nb_answers(nbAnswers:int):
        """Check si le nombre de réponses est valide"""
        if nbAnswers < 2:
            raise InvalidNbAnswersException(f"La question doit avoir au moins deux réponses")
        if nbAnswers > Question.nbAnswersMax:
            raise InvalidNbAnswersException(f"La question ne peux pas avoir plus de {Question.nbAnswersMax} réponses")
        return True

    def get_shuffled_answers(self):
        answers = [self.rightAnswer] + self.wrongAnswers
        random.shuffle(answers)
        return answers

    def __str__(self):
        res = f"\"{self.title}\"\n" \
              f"✔ {self.rightAnswer}"
        res += "\n".join([f"❌ {wrongAnswer}" for wrongAnswer in self.wrongAnswers])
        return res

class Quizz:
    def __init__(self, questions:[Question], title:str="", nbQuestionsToDisplay:int|None=1, useRandomOrder:bool=False):
        self.title = title
        self.questions = questions
        self.useRandomOrder = useRandomOrder
        self.nbQuestionsToDisplay = nbQuestionsToDisplay

    def to_json(self):
        # TODO POURQUOI IL Y A ÉCRIT "useRRRRRandomOrder" ??
        return {
            'title': self.title,
            'questions': [
                question.to_json() for question in self.questions
            ],
            'userRandomOrder': self.useRandomOrder,
            'nbQuestionsToDisplay': self.nbQuestionsToDisplay
        }

    def save(self):
        """Sauvegarde un quizz"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            quizzes.append(self.to_json())
            quizzes_file.seek(0)
            json.dump(quizzes, quizzes_file, indent=4)

    def nb_questions(self)->int:
        return len(self.questions)

    def has_no_question(self)->bool:
        return self.nb_questions() == 0

    def valid_inputs(self, title:str, nbToDisplay:str):
        """Méthode qui check si un titre et un nombre de questions à afficher sont valides"""
        Quizz.valid_title(title)

        # Check si le quizz a au moins une question
        if self.has_no_question(): raise InvalidQuizzException("le Quizz n'a pas de question")
        if self.nb_questions() > Question.nbAnswersMax: raise InvalidQuizzException(f"le Quizz ne peux pas avoir plus de {Question.nbAnswersMax}")

        # Check si le nbToDisplay est valide
        if self.nb_questions() > 1:
            try:
                self.valid_nb_to_display(nbToDisplay)
            except InvalidNbToDisplayException as ex:
                raise InvalidQuizzException(f"{ex.__str__().lower()}")
        return True

    def is_valid(self):
        """Check si le quizz en cours est valide"""
        # Check le titre
        Quizz.valid_title(self.title)

        # Check le nombre de questions
        if self.nb_questions() == 0:
            raise InvalidQuizzException(f"Il n'y a aucune question")

        # Check les questions
        for question in self.questions:
            try: question.is_valid()
            except InvalidQuestionException as ex:
                raise InvalidQuizzException(ex.__str__())

        # Check le nbQuestionsToDisplay
        try: self.valid_nb_to_display(self.nbQuestionsToDisplay)
        except InvalidNbToDisplayException as ex:
            raise InvalidQuizzException(f"Le nombre de questions à affiché est invalide, {ex.__str__().lower()}")

        return True
    def __str__(self):
        res = f"Quizz \"{self.title}\"\n" \
               f"Ordre aléatoire: {self.useRandomOrder}\n" \
               f"Nombre de questions affichés: {self.nbQuestionsToDisplay}/{self.nb_questions()}\n\n"
        res += '\n'.join(question.__str__() for question in self.questions)
        return res

    def valid_nb_to_display(self, nbToDisplay:str|int):
        """Methode qui vérifie si le nombre de questions à afficher pour créer une question est valide"""
        if nbToDisplay == "": raise InvalidNbToDisplayException("Saisissez un nombre de questions à afficher")
        nbQuestionsMax = self.nb_questions()
        try: nbToDisplay = int(nbToDisplay)
        except ValueError:
            raise InvalidNbToDisplayException(f"Saisissez un nombre valide")
        if nbToDisplay <= 0:
            raise InvalidNbToDisplayException(f"Saisissez un nombre supérieur à 0")
        if nbToDisplay > nbQuestionsMax:
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
    def valid_title(title:str):
        # Check si le titre est vide
        if not title: raise InvalidQuizzException("Le Quizz n'a pas de titre")
        # Check si le Quizz existe déjà
        if Quizz.exists(title): raise InvalidQuizzException(f"Le Quizz \"{title}\" existe déjà")

    @staticmethod
    def import_txt(filepath: str):
        with open(filepath, encoding='utf8') as f:
            iLine = 1
            keywords = ["quizz:","question:","reponse:","bonne_reponse:","ordre:","nombre_questions:"]

            questionTitle, questionWrongAnswers, questionRightAnswer = Question.default_values()
            nbAnswers = 0
            isFirstQuestion = True
            questionOrder, nbQuestionsToDisplay, questions, quizzTitle = False, 1, [], ""

            while True:
                line = f.readline().strip().split()

                # Fin de fichier et une question est en cours, on l'ajoute
                if not line and nbAnswers > 0:
                    question = Question(questionTitle, questionRightAnswer, questionWrongAnswers)
                    questions.append(question)

                # Fin de fichier, on sauvegarde le quizz
                if not line:
                    # Check si l'ordre est valide
                    if questionOrder:
                        if questionOrder == "aléatoire": questionOrder = True
                        elif questionOrder == "normal": questionOrder = False
                        else: raise ImportQuizzException(f"L'ordre \"{questionOrder}\" n'existe pas")


                    # Check du titre et du nombre de questions à afficher
                    try:
                        quizz = Quizz(questions, quizzTitle, nbQuestionsToDisplay, questionOrder)
                        if nbQuestionsToDisplay == "": quizz.nbQuestionsToDisplay = quizz.nb_questions()
                        elif quizz.nb_questions() == 1: quizz.nbQuestionsToDisplay = 1
                        quizz.is_valid()
                    except InvalidQuizzException as ex:
                        raise ImportQuizzException(f"{ex}")

                    # All good !
                    return quizz

                # Récupération des données
                keyword = line[0]
                rest = " ".join(line[1:])

                # Check si le mot clé existe
                if not keyword in keywords:
                    raise ImportQuizzException(f"A la ligne {iLine}, le mot clé \"{keyword}\" n'existe pas")

                # TODO : On autorise que le ces valeurs soient affectés plusieurs fois ?
                if keyword == "quizz:": quizzTitle = rest
                elif keyword == "ordre:": questionOrder = rest
                elif keyword == "nombre_questions:": nbQuestionsToDisplay = rest
                elif keyword == "reponse:":
                    nbAnswers += 1
                    questionWrongAnswers.append(rest)
                elif keyword == "bonne_reponse:":
                    nbAnswers += 1
                    # Check s'il y a déjà une bonne réponse
                    if questionRightAnswer != "": raise ImportQuizzException(f"A la ligne {iLine}, il y a plusieurs bonnes réponse. Il ne peut en rester qu'une !")
                    questionRightAnswer = rest

                # Première question
                if keyword == "question:" and isFirstQuestion:
                    questionTitle = rest
                    isFirstQuestion = False
                # Validation de la question en cours
                elif keyword == "question:" and not isFirstQuestion:
                    question = Question(questionTitle, questionRightAnswer, questionWrongAnswers)
                    questions.append(question)

                    # Préparation pour la prochaine question
                    _, questionWrongAnswers, questionRightAnswer = Question.default_values()
                    nbAnswers = 0
                    questionTitle = rest

                iLine += 1

    @staticmethod
    def get_list_quizzes():
        """Récupérer la liste de tous les Quizz"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            list_quizzes = []

            for idQuizz, aQuizz in enumerate(quizzes):
                list_quizzes.append({
                    "idQuizz": idQuizz,
                    "title": aQuizz["title"]
                })
        return list_quizzes

    @staticmethod
    def all():
        quizzes = []
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes_json = json.load(quizzes_file)
            for quizz_json in quizzes_json:
                quizzes.append(Quizz.from_json(quizz_json))
        return quizzes

    @staticmethod
    def get(title:str):
        """Récupère un Quizz avec son titre"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)
            for quizz in quizzes:
                if quizz["title"] == title:
                    return Quizz.from_json(quizz)
        raise UnknownQuizzException(f"Le quizz {title} n'existe pas")

    @staticmethod
    def from_json(quizz):
        return Quizz(
            [Question.from_json(question) for question in quizz["questions"]],
            quizz["title"],
            quizz["nbQuestionsToDisplay"],
            quizz["userRandomOrder"]
        )