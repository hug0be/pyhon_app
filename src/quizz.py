# -*- coding: utf-8 -*-
import json
import random

class InvalidQuizzException(Exception): pass
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
        """Check si les données (title, answers, indexRightAnswer) pour créer une question sont valides"""
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

    @staticmethod
    def valid_nb_answers(nbAnswers:int):
        """Check si le nombre de réponses est valide"""
        if nbAnswers < 2:
            raise InvalidNbAnswersException(f"la question doit avoir au moins deux réponses")
        if nbAnswers > Question.nbAnswersMax:
            raise InvalidNbAnswersException(f"la question ne peux pas avoir plus de {Question.nbAnswersMax} réponses")
        return True

    @staticmethod
    def get_shuffled_answers_question(aQuestion):
        listAnswers = [aQuestion["rightAnswer"]] + [ wrongAnswer for wrongAnswer in aQuestion["wrongAnswers"] ]
        random.shuffle(listAnswers)
        return listAnswers

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

    def valid_inputs(self, title:str, nbToDisplay:str):
        """Méthode qui check si un titre et un nombre de questions à afficher sont valides"""
        # Check si le titre est vide
        if not title: raise InvalidQuizzException("Le Quizz n'a pas de titre")
        # Check si le Quizz existe déjà
        if Quizz.exists(title): raise InvalidQuizzException(f"Le Quizz \"{title}\" existe déjà")

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
        def attempt_create_question(title, rightAnswer, wrongAnswers)->Question:
            """Check si la creation d'une question est possible, renvoie cette question si oui"""
            i
            # Check s'il y a une bonne réponse
            if rightAnswer is None: raise InvalidQuestionException(f"la question n'a pas de bonne réponse")
            # Check le nombre de réponses
            try:
                Question.valid_nb_answers(nbAnswers)
            except InvalidNbAnswersException as e:
                raise InvalidQuestionException(e.__str__())
            return Question(title, rightAnswer, wrongAnswers)

        with open(filepath, encoding='utf8') as f:
            iLine = 1
            keywords = ["quizz:","question:","reponse:","bonne_reponse:","ordre:","nombre_questions:"]

            questionTitle, questionWrongAnswers, questionRightAnswer = Question.default_values()
            nbAnswers = 0
            quizzTitle, questionOrder, nbQuestionsToDisplay  = Quizz.default_values()
            quizz = Quizz()

            while True:
                line = f.readline().strip().split()
                # Fin de fichier et une question est en cours, on l'ajoute
                if not line and nbAnswers > 0:
                    # Check les autres données
                    try:
                        question = attempt_create_question(questionTitle, questionRightAnswer, questionWrongAnswers)
                        quizz.questions.append(question)
                    except InvalidQuestionException as ex:
                        raise ImportQuizzException(f"A la ligne {iLine - nbAnswers}, {ex}")
                    return quizz

                # Fin de fichier, on sauvegarde le quizz
                if not line:
                    # Check du titre et du nombre de questions à afficher
                    try:
                        quizz.valid_inputs(quizzTitle, nbQuestionsToDisplay)
                    except InvalidQuizzException as ex:
                        raise ImportQuizzException(f"A la ligne {iLine}, {ex}")

                    # Check si l'ordre est valide
                    if questionOrder:
                        if questionOrder == "aléatoire": questionOrder = True
                        elif questionOrder == "normal": questionOrder = False
                        else: raise InvalidQuizzException(f"A la ligne {iLine}, l'ordre \"{questionOrder}\" n'existe pas")

                    # All good !
                    quizz.useRandomOrder = questionOrder
                    quizz.nbQuestionsToDisplay = nbQuestionsToDisplay
                    quizz.title = quizzTitle
                    return quizz

                # Récupération des données
                keyword = line[0]
                rest = " ".join(line[1:])

                # Check si le mot clé existe
                if not keyword in keywords: raise ImportQuizzException(f"Le mot clé \"{keyword}\" n'existe pas")

                # TODO : On autorise que le ces valeurs soient affectés plusieurs fois ?
                if keyword == "quizz:": quizzTitle = rest
                if keyword == "question": questionTitle = rest
                if keyword == "ordre:": questionOrder = rest
                if keyword == "nombre_questions:": nbQuestionsToDisplay = rest

                # Gestion des mots-clés reponse et bonne_reponse
                if keyword in ["reponse:", "bonne_reponse:"]:
                    if rest == "": raise ImportQuizzException(f"A la ligne {iLine - nbAnswers}, la réponse est vide")
                    nbAnswers += 1
                    if nbAnswers > Question.nbAnswersMax: raise ImportQuizzException(f"A la ligne {iLine - nbAnswers}, la question ne peux pas avoir plus de {Question.nbAnswersMax} réponses")
                    if keyword == "reponse:": questionWrongAnswers.append(rest)
                    if keyword == "bonne_reponse:":
                        # Check s'il y a plusieurs bonnes réponses
                        if questionRightAnswer is not None: raise ImportQuizzException(f"A la ligne {iLine}, il y a plusieurs bonnes réponse. Il ne peut en rester qu'une !")
                        questionRightAnswer = rest

                # Validation de la question en cours
                if keyword == "question:" and nbAnswers > 0:
                    try:
                        question = attempt_create_question(questionTitle, questionRightAnswer, questionWrongAnswers)
                        quizz.questions.append(question)
                    except InvalidQuestionException as ex:
                        raise ImportQuizzException(f"A la ligne {iLine - nbAnswers}, {ex}")

                    # Préparation pour la prochaine question
                    questionTitle, questionWrongAnswers, questionRightAnswer = Question.default_values()
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
    def get_quizz_by_id(id:int):
        """Récupérer un Quizz avec son id"""
        with open('data/quizzes.json', 'r+') as quizzes_file:
            quizzes = json.load(quizzes_file)

        # print(quizzes[id])
        return quizzes[id]
