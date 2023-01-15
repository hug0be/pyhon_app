import json
import sys
import os
import time
from functools import partial

from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtUiTools import QUiLoader

from src import History, HistoryItem
from src.account import Account, WrongPasswordException, UnknownAccountException
from src.quizz import Quizz, Question, InvalidQuestionException, InvalidNbToDisplayException, ImportQuizzException
from src.ui import Ui_MainWindow, Ui_userMenu

class UserMenuAccessException(Exception): pass

def change_page(name: str, currentUser:Account = None):
    """Change de page selon le nom donné"""
    global window
    window.close()
    # Check si l'utilisateur est valide
    if name == "userMenu" and currentUser is None:
        raise UserMenuAccessException("Il faut au utilisateur valide pour accéder à cette page")
    if name == "userMenu":
        window = UserMenuWindow(currentUser)
    if name == "home":
        window = MainWindow()
    window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        # Setup
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))

        # Binding
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        self.ui.connectButton.clicked.connect(self.connect_attempt)
        self.ui.createAccountButton.clicked.connect(self.create_account_attempt)

        # Binding changements de page
        self.ui.chooseConnectButton.clicked.connect(self.show_connect_page)
        self.ui.chooseCreateAccountButton.clicked.connect(self.show_create_account_page)
        self.ui.backButton.clicked.connect(self.show_home)
        self.ui.backButton2.clicked.connect(self.show_home)

    def show_home(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        # Quand l'user reviendra les erreurs auront disparu.
        self.ui.createAccountErrorsLabel.clear()
        self.ui.connectErrorsLabel.clear()

    def show_create_account_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.createAccountPage)

    def show_connect_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.connectPage)

    def connect_attempt(self):
        """Méthode appeler pour une tentative de connexion"""
        # Obtention des identifiants
        username = self.ui.connectUsername.text()
        password = self.ui.connectPassword.text()

        # Validation des identifiants
        is_valid = username and password
        if not is_valid:
            text_error = ""
            if not username: text_error += "Saisissez votre nom d'utilisateur\n"
            if not password: text_error += "Saisissez votre mot de passe"
            self.ui.connectErrorsLabel.setText(text_error)
            self.ui.createAccountErrorsLabel.clear()
            return False

        # Lancement de la tentative
        try:
            user = Account.get(username, password)
        except WrongPasswordException:
            self.ui.connectErrorsLabel.setText("Mot de passe incorrect")
            return False
        except UnknownAccountException:
            self.ui.connectErrorsLabel.setText("Compte inexistant")
            return False

        # All good !
        change_page("userMenu", user)

    def create_account_attempt(self):
        """Méthode appeler pour une tentative de création de compte"""
        # Obtention des identifiants
        username = self.ui.accountUsername.text()
        password = self.ui.accountPassword.text()
        password_confirmation = self.ui.accountPasswordConfirmation.text()

        # Check si le compte existe
        if Account.exists(username):
            self.ui.createAccountErrorsLabel.setText("Ce compte existe déjà")
            return False

        # Validation des identifiants
        is_valid = username and password and password == password_confirmation
        if not is_valid:
            text_error = ""
            if not username: text_error += "Saisissez un nom d'utilisateur\n"
            if not password: text_error += "Saisissez un mot de passe\n"
            if password != password_confirmation and username: text_error += "Le mot de passe et la confirmation sont différent"
            self.ui.createAccountErrorsLabel.setText(text_error)
            self.ui.connectErrorsLabel.clear()
            return False

        # All good !
        user = Account(username, password)
        user.save()
        change_page("userMenu", user)

class UserMenuWindow(QMainWindow):
    def __init__(self, currentUser:Account):
        QMainWindow.__init__(self)
        self.currentUser = currentUser
        self.ui = Ui_userMenu()
        self.ui.setupUi(self)
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        self.ui.showQuizzListButton.clicked.connect(self.show_quizz_list_page)
        self.ui.toggleButton.clicked.connect(lambda: self.toggle_menu(200))

        # Variables utilisés pendant le quizz
        self.hasAnswered = False
        self.indexQuestion = 0
        self.pendingQuizz = None
        self.score = 0
        self.startTime = None

        # Binding changements de pages
        self.ui.showQuizzListButton.clicked.connect(self.show_quizz_list_page)
        self.ui.createQuizzButton.clicked.connect(self.show_quizz_creation_page)
        self.ui.importQuizzButton.clicked.connect(self.import_quizz)
        self.ui.logoutButton.clicked.connect(lambda: change_page("home"))
        self.ui.historyButton.clicked.connect(self.show_history)

        # Binding des quatre pages de création d'un quizz
        self.ui.addQuestionsButton.clicked.connect(self.create_quizz1)
        self.ui.nextQuestionButton.clicked.connect(self.create_quizz2)
        self.ui.endQuestionsButton.clicked.connect(self.end_questions)
        self.ui.doRandomOrderButton.clicked.connect(lambda: self.create_quizz3(True))
        self.ui.noRandomOrderButton.clicked.connect(lambda: self.create_quizz3(False))
        self.ui.saveQuizzButton.clicked.connect(self.create_quizz4)

        # Binding des back buttons
        backButtons = [self.ui.backButton1, self.ui.backButton2, self.ui.backButton3, self.ui.backButton4,
                       self.ui.backButton5, self.ui.backButton6]
        for backButton in backButtons:
            backButton.clicked.connect(self.show_home_page)

        # Binding bouton "Valider" le game quizz
        self.ui.validateButton.clicked.connect(self.choose_question_page)

        # Binding page de fin de quizz
        self.ui.homeButton.clicked.connect(self.show_home_page)
        self.ui.listButton.clicked.connect(self.show_quizz_list_page)
        self.ui.retryButton.clicked.connect(lambda: self.init_quizz( Quizz.get(self.pendingQuizz.title) ))

    def reset_game(self):
        # Réinitialisation des variables utilisés pendant le quizz
        self.hasAnswered = False
        self.indexQuestion = 0
        self.pendingQuizz = None
        self.score = 0
        self.startTime = time.time()

    def show_home_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)

    def show_history(self):
        self.create_buttons_page_history()
        self.ui.pagesList.setCurrentWidget(self.ui.history)

    def show_quizz_list_page(self):
        self.init_question_page()
        self.ui.pagesList.setCurrentWidget(self.ui.quizzListPage)

    def show_quizz_creation_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.createQuizzPage)

    def init_quizz(self, quizz:Quizz):
        self.reset_game()
        self.pendingQuizz = quizz
        self.update_question_page(quizz.title, self.next_question())
        self.ui.pagesList.setCurrentWidget(self.ui.questionsPage)
        self.ui.questionPages.setCurrentWidget(self.ui.questionPage)

    def update_question_page(self, titleQuizz:str, question:Question):
        """Initialise les champs (titre, titre question, ...) d'une page question"""
        # Affichage du titre du quizz
        self.ui.label_titre.setText(titleQuizz)

        # Affichage de l'intitulé de la question
        self.ui.questionLabel.setText(question.title)

        # Obtention des radios boutons pour les réponses
        radioButtons = self.ui.choiceRightAnswerQuizz.buttons()

        # On efface leur contenu et on les désélectionne
        for radioButton in radioButtons:
            radioButton.setText(None)
            radioButton.setChecked(False)
            radioButton.setStyleSheet("background: transparent")

        # Obtention des réponses
        answers = question.get_shuffled_answers()
        for i, answer in enumerate(answers):
            radioButtons[i].setText(answer)

        # Affichage de l'id de la current Question
        self.ui.nbQuestionLabel.setText(f"{self.indexQuestion} / {self.pendingQuizz.nb_questions()}")

    def init_question_page(self):
        """Créer les boutons sur la page Liste des Quizz"""
        # Tous les quizz
        quizzes = Quizz.all()
        # Conteneur des quizz
        quizzContainer = self.ui.page_list_quizz_container_bot
        # Créer le layout pour page
        layout = QVBoxLayout()

        for quizz in quizzes:
            # Créer un bouton
            button = QPushButton(quizz.title)
            # Binding du bouton avec sa page de quizz
            # On utilise partial() sinon les boutons renvoient toujours sur le dernier quizz
            button.clicked.connect(partial(self.init_quizz, quizz))
            # Ajout du bouton au layout
            layout.addWidget(button)

        # Ajout du layout dans le conteneur des quizz
        quizzContainer.setLayout(layout)

    def choose_question_page(self):
        self.hasAnswered = not self.hasAnswered
        if self.hasAnswered:

            # Validation du choix
            chosenAnswer = self.ui.choiceRightAnswerQuizz.checkedButton()
            if chosenAnswer is None or chosenAnswer.text() == "":
                self.hasAnswered = False
                self.ui.validateAnswerErrorsLabel.setText("Saisissez une réponse")
                raise Exception("Saisissez une réponse")

            # Augmentation du score
            if chosenAnswer.text() == self.pendingQuizz.questions[self.indexQuestion-1].rightAnswer:
                self.score += 1
                self.ui.nbPointsLabel.setText(str(self.score))

            self.ui.validateButton.setText("Question suivante")
            self.show_answer(self.pendingQuizz.questions[self.indexQuestion-1])
        else:
            self.ui.validateButton.setText("Valider")
            self.update_question_page(self.pendingQuizz.title, self.next_question())

    def next_question(self)->Question:
        if self.indexQuestion < self.pendingQuizz.nb_questions():
            self.indexQuestion += 1
            return self.pendingQuizz.questions[self.indexQuestion-1]
        else:
            # Affichage de la page de résultat
            timeTaken = time.time() - self.startTime
            self.ui.timerLabel.setText(f"{timeTaken:.2f}s")
            self.ui.quizzTitleEndLabel.setText(self.pendingQuizz.title)
            self.ui.finalScoreLabel.setText(f"{self.score} / {self.pendingQuizz.nb_questions()}")
            self.ui.questionPages.setCurrentWidget(self.ui.endQuizzPage)

            # Sauvegarde si le résultat est meilleur que le précédent
            result = HistoryItem(self.pendingQuizz, self.score, timeTaken)
            self.currentUser.update_best_score(self.pendingQuizz ,result)
            raise Exception("Plus de question")

    def show_answer(self, currentQuestion):
        """Affiche la bonne réponse et les mauvaises réponses"""

        # Check si un bouton est sélectionné
        checkedButton = self.ui.choiceRightAnswerQuizz.checkedButton()
        if checkedButton is None:
            return False

        # Coloration des réponses
        for button in self.ui.choiceRightAnswerQuizz.buttons():
            if currentQuestion.is_right_answer(button.text()):
                button.setStyleSheet("background-color: #1D8E36")
            elif button.text() != "":
                button.setStyleSheet("background-color: #B41010")

    def is_right_answer_selected(self, currentQuestion):
        """Check si la réponse sélectionnée est bonne"""
        selectedButtonText = self.ui.choiceRightAnswerQuizz.checkedButton().text()
        return currentQuestion.is_right_answer(selectedButtonText)

    def create_quizz1(self):
        """Méthode qui constitue la première étape de création d'un quizz : choisir un titre"""
        # Obtention des données
        title = self.ui.quizzTitle.text()

        # Validation du titre
        if not title:
            self.ui.nameQuizzErrorsLabel.setText("Saisissez un titre de Quizz")
            return False

        # Check si le quizz existe
        if Quizz.exists(title):
            self.ui.nameQuizzErrorsLabel.setText("Ce quizz existe déjà")
            return False

        # All good !
        self.pendingQuizz = Quizz([], title)
        self.ui.quizzCreationSteps.setCurrentWidget(self.ui.createQuestionsPage)

    def create_quizz2(self):
        """Méthode qui constitue la deuxième étape de création d'un quizz : l'ajout des questions"""
        # Récupération des données
        title = self.ui.titleQuestion.text()
        indexRightAnswer = self.ui.choiceRightAnswer.checkedId()
        answersWidget = [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]
        answers = [answerWidget.text() for answerWidget in answersWidget]

        # Validation des données
        try:
            Question.valid_inputs(title, answers, indexRightAnswer)
        except InvalidQuestionException as ex:
            self.ui.questionCreationErrorsLabel.setText(ex.__str__())
            return False

        # Permets d'obtenir l'index de la réponse dans la liste de réponse
        indexRightAnswer = abs(indexRightAnswer + 2)
        rightAnswer = answers.pop(indexRightAnswer)
        wrongAnswers = [answer for answer in answers if answer != '']
        # Ajout de la question
        question = Question(title, rightAnswer, wrongAnswers)
        self.pendingQuizz.questions.append(question)

        # On vide les inputs
        # TODO : Il y a surement un moyen de reset la page au lieu de faire tout ça
        # TODO : Le code commenté suivant ne fonctionne  pas : le button choisi ne se désélectionne pas
        # self.ui.choiceRightAnswer.checkedButton().setChecked(False)
        self.ui.titleQuestion.clear()
        for answer in answersWidget: answer.clear()
        # On incrémente le numéro de question affiché
        self.ui.questionNumberLabel.setText(f"Question {self.pendingQuizz.nb_questions() + 1}")
        return True

    def end_questions(self):
        """
        Méthode qui passe à la troisième étape si les questions ont bien été faites.
        Elle peut aussi skipper l'étape 3 et 4 s'il n'y a qu'une question.
        """
        # On tente d'enregistré la question en cours
        self.create_quizz2()

        # Nombre de questions enregistré après la tentative
        nbQuestions = self.pendingQuizz.nb_questions()

        # La question en cours est invalide
        # Un message d'erreur à déjà été écrit dans create_quizz2()
        if nbQuestions == 0: return False

        # On peut skip les étapes s'il n'y a qu'une question
        if nbQuestions == 1:
            self.save_quizz()
            return True

        # Il y a plus d'une question, on passe à la prochaine étape
        self.ui.quizzCreationSteps.setCurrentWidget(self.ui.chooseOrderPage)
        return True

    def toggle_menu(self, maxWidth):
        """Méthode qui ouvre et ferme le menu de gauche (sidebar)"""
        # GET WIDTH
        width = self.ui.leftMenu.width()
        maxExtend = maxWidth  # 300
        standard = 75

        # SET MAX WIDTH
        if width == 75:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        # -- TOGGLE
        self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def create_quizz3(self, useRandomOrder: bool):
        """Méthode qui constitue la troisième étape de création d'un quizz : l'ordre des questions"""
        self.pendingQuizz.useRandomOrder = useRandomOrder

        # Affichage du nombre de questions max pour la page suivante
        nbMaxToDisplay = self.pendingQuizz.nb_questions()
        self.ui.nbQuestionsLabel.setText(f"Vous avez écrit {nbMaxToDisplay} questions")
        self.ui.quizzCreationSteps.setCurrentWidget(self.ui.chooseNbToDisplayPage)

    def create_quizz4(self):
        """Méthode qui constitue la quatrième et dernière étape de création d'un quizz : le choix du nombre de questions à afficher"""
        nbToDisplay = self.ui.nbToDisplay.text()

        # Validation du nombre
        try:
            self.pendingQuizz.valid_nb_to_display(nbToDisplay)
        except InvalidNbToDisplayException as ex:
            self.ui.nbToDisplayErrorsLabel.setText(ex.__str__())
            return False

        # All good !
        self.pendingQuizz.nbQuestionsToDisplay = nbToDisplay
        self.save_quizz()

    def save_quizz(self):
        """Enregistre le quizz après toutes les étapes terminées"""
        self.pendingQuizz.save()
        self.show_quizz_list_page()

    def create_buttons_page_history(self):
        """Créer les boutons sur la page Historique"""
        # Historique de l'utilisateur
        history = History.load(self.currentUser.username)

        # Conteneur de l'historique
        historyContainer = self.ui.historyContainer

        # Créer les layout pour page
        layout = QVBoxLayout()

        # On crée les boutons et on les ajoute dans le conteneur
        for item in history.items:
            button = QPushButton(item.__str__())
            layout.addWidget(button)

        # Mettre la layout contenant les boutons dans le conteneur page_list_history_container_bot
        historyContainer.setLayout(layout)

    def import_quizz(self):
        # Tentative d'ouverture du fichier
        # Tentative d'ajout du quizz
        try:
            file = QFileDialog.getOpenFileName(self, 'Importer un quizz', "", "Text files (*.txt)")
            Quizz.import_txt(file[0]).save()
        except ImportQuizzException as ex:
            self.ui.importQuizzErrorsLabel.setText(ex.__str__())
            return False
        except FileNotFoundError:
            return False

        # All good !
        self.ui.importQuizzErrorsLabel.clear()
        self.show_quizz_list_page()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    # Check si le fichier accounts.json existe
    if not os.path.exists("data/accounts.json"):
        if not os.path.exists("data"):
            os.mkdir("data")
        with open('data/accounts.json', 'w') as accounts_file:
            accounts = [
                {"username": "admin", "password": "foobar2", "admin": True},
                {"username": "user", "password": "foobar2", "admin": False}
            ]
            accounts_file.write(json.dumps(accounts))
            print("Fichier accounts.json créé")

    # Check si le fichier quizzes.json existe
    if not os.path.exists("data/quizzes.json"):
        with open('data/quizzes.json', 'w') as quizzes_file:
            quizzes_file.write(json.dumps([]))
        print("Fichier quizzes.json créé")

    # Convert file .ui -> .py
    os.system("pyside6-uic views/MainWindow.ui -o src/ui/MainWindow.py")
    os.system("pyside6-uic views/UserMenuWindow.ui -o src/ui/UserMenuWindow.py")
    os.system("pyside6-rcc resources/resources.qrc -o resources_rc.py")

    # Page principale
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
