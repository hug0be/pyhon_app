import json
import sys
import os

from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QGroupBox, QLabel
from PySide6.QtUiTools import QUiLoader

from src.account import Account, WrongPasswordException, UnknownAccountException
from src.quizz import Quizz, Question, InvalidQuestionException, InvalidNbToDisplayException, ImportQuizzException
from src.ui import Ui_MainWindow, Ui_userMenu

def change_page(name:str="userMenu"):
    """Change de page selon le nom donné"""
    global window
    window.close()
    if name == "userMenu":
        window = UserMenuWindow()
    if name == "home":
        window = MainWindow()
    window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        #Setup
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('resources/images/favicon_96x96.png'))

        #Binding
        self.ui.connectButton.clicked.connect(self.connect_attempt)
        self.ui.createAccountButton.clicked.connect(self.create_account_attempt)

        #Binding changements de page
        self.ui.chooseConnectButton.clicked.connect(self.show_connect_page)
        self.ui.chooseCreateAccountButton.clicked.connect(self.show_create_account_page)
        self.ui.backButton.clicked.connect(self.show_home)
        self.ui.backButton2.clicked.connect(self.show_home)

    def show_home(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
        #Quand l'user reviendra les erreurs auront disparu.
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
            Account.access(username, password)
        except WrongPasswordException:
            self.ui.connectErrorsLabel.setText("Mot de passe incorrect")
            return False
        except UnknownAccountException:
            self.ui.connectErrorsLabel.setText("Compte inexistant")
            return False

        # All good !
        change_page()
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
        Account(username, password).save()
        change_page()

class UserMenuWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_userMenu()
        self.ui.setupUi(self)
        self.ui.pagesList.setCurrentIndex(0)
        self.ui.showQuizzListButton.clicked.connect(self.show_quizz_list_page)
        self.ui.toggleButton.clicked.connect(lambda : self.toggleBtn(200))
        self.pendingQuizz = None


        #Binding changements de pages
        # TODO: Retour arrière pour les pages "quizzListPage" et "createQuizzPage"
        self.ui.showQuizzListButton.clicked.connect(self.show_quizz_list_page)
        self.ui.createQuizzButton.clicked.connect(self.show_quizz_creation_page)
        self.ui.importQuizzButton.clicked.connect(self.import_quizz)
        self.ui.logoutButton.clicked.connect(lambda: change_page("home"))

        #Les 3 étapes/pages de création d'un quizz
        self.ui.addQuestionsButton.clicked.connect(self.create_quizz1)
        self.ui.nextQuestionButton.clicked.connect(self.create_quizz2)
        self.ui.endQuestionsButton.clicked.connect(self.end_questions)
        self.ui.doRandomOrderButton.clicked.connect(lambda : self.create_quizz3(True))
        self.ui.noRandomOrderButton.clicked.connect(lambda : self.create_quizz3(False))
        self.ui.saveQuizzButton.clicked.connect(self.create_quizz4)

        # Binding des back buttons
        backButtons = [self.ui.backButton1, self.ui.backButton2, self.ui.backButton3, self.ui.backButton4, self.ui.backButton5]
        for backButton in backButtons:
            backButton.clicked.connect(self.show_home_page)

    def show_home_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.homePage)
    def show_quizz_list_page(self):
        self.create_btns_page_list_quizz()
        self.ui.pagesList.setCurrentWidget(self.ui.quizzListPage)
    def show_quizz_creation_page(self):
        self.ui.pagesList.setCurrentWidget(self.ui.createQuizzPage)
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
        self.pendingQuizz = Quizz(title)
        self.ui.quizzCreationSteps.setCurrentWidget(self.ui.createQuestionsPage)
    def create_quizz2(self):
        """Méthode qui constitue la deuxième étape de création d'un quizz : l'ajout des questions"""
        # TODO : Ajouter une validation pour voir s'il n'y a pas 2 fois la même réponse
        #Récupération des données
        title = self.ui.titleQuestion.text()
        indexRightAnswer = self.ui.choiceRightAnswer.checkedId()
        answersWidget = [self.ui.answer1,self.ui.answer2,self.ui.answer3,self.ui.answer4]
        answers = [answerWidget.text() for answerWidget in answersWidget]

        #Validation des données
        try:
            Question.valid_inputs(title, answers, indexRightAnswer)
        except InvalidQuestionException as ex:
            self.ui.questionCreationErrorsLabel.setText(ex.__str__())
            return False

        # Permets d'obtenir l'index de la réponse dans la liste de réponse
        indexRightAnswer = abs(indexRightAnswer + 2)
        rightAnswer = answers.pop(indexRightAnswer)
        wrongAnswers = [answer for answer in answers if answer != '']
        question = Question(title, rightAnswer, wrongAnswers) #On crée la question
        self.pendingQuizz.questions.append(question) #On ajoute la question au quizz

        #On vide les inputs
        # TODO : Il y a surement un moyen de reset la page au lieu de faire tout ça
        # TODO : La code commenté suivant ne fonctionne  pas : le button choisi ne se désélectionne pas
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

    def toggleBtn(self, maxWidth):

        # GET WIDTH
        width = self.ui.leftMenu.width()
        maxExtend = maxWidth # 300
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

    def create_quizz3(self, useRandomOrder:bool):
        """Méthode qui constitue la troisième étape de création d'un quizz : l'ordre des questions"""
        self.pendingQuizz.useRandomOrder = useRandomOrder

        #Affichage du nombre de questions max pour la page suivante
        nbMaxToDisplay = self.pendingQuizz.nb_questions()
        self.ui.nbQuestionsLabel.setText(f"Vous avez écrit {nbMaxToDisplay} questions")
        self.ui.quizzCreationSteps.setCurrentWidget(self.ui.chooseNbToDisplayPage)

    def create_quizz4(self):
        """Méthode qui constitue la quatrième et dernière étape de création d'un quizz : le choix du nombre de questions à afficher"""
        nbToDisplay = self.ui.nbToDisplay.text()

        #Validation du nombre
        try:
            self.pendingQuizz.valid_nb_to_display(nbToDisplay)
        except InvalidNbToDisplayException as ex:
            self.ui.nbToDisplayErrorsLabel.setText(ex.__str__())
            return False

        #All good !
        self.pendingQuizz.nbQuestionsToDisplay = nbToDisplay
        self.save_quizz()

    def save_quizz(self):
        """Enregistre le quizz après toutes les étapes terminées"""
        self.pendingQuizz.save()
        # Ajout dynamique des boutons
        self.create_btns_page_list_quizz()
        self.ui.pagesList.setCurrentWidget(self.ui.quizzListPage)

    def create_btns_page_list_quizz(self):
        """Créer les boutons sur la page Liste des Quizz"""
        # GET THE LIST OF ALL QUIZZES
        list_quizzes = Quizz.get_list_quizzes()

        # GET THE LIST QUIZZES PAGE
        page_list_quizz_container_bot = self.ui.page_list_quizz_container_bot

        # Créer les layout pour page
        layout = QVBoxLayout()

        for aQuizz in list_quizzes:
            # Créer un bouton
            button = QPushButton(aQuizz["title"])
            # TODO Add the link to go on the quizz avec la methode button.clicked.connect(display_quizz(aQuizz["idQuizz"]) )

            # Ajouter le bouton au layout
            layout.addWidget(button)

        # Mettre la layout contenant les boutons dans le container page_list_quizz_container_bot
        page_list_quizz_container_bot.setLayout(layout)


    def import_quizz(self):
        # Tentative d'ouverture du fichier
        try:
            file = QFileDialog.getOpenFileName(self, 'Importer un quizz', "", "Text files (*.txt)")
        except FileNotFoundError:
            return False

        # Tentative d'ajout du quizz
        try:
            Quizz.import_txt(file[0]).save()
        except ImportQuizzException as ex:
            self.ui.importQuizzErrorsLabel.setText(ex.__str__())
            return False

        #All good !
        self.ui.importQuizzErrorsLabel.clear()
        self.show_quizz_list_page()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = QUiLoader()

    #Check si le fichier accounts.json existe
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

    #Convert file .ui -> .py
    os.system("pyside6-uic views/MainWindow.ui -o src/ui/MainWindow.py")
    os.system("pyside6-uic views/UserMenuWindow.ui -o src/ui/UserMenuWindow.py")

    os.system("pyside6-rcc resources/resources.qrc -o resources_rc.py")

    #Page principale
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

