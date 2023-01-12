# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserMenuWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_userMenu(object):
    def setupUi(self, userMenu):
        if not userMenu.objectName():
            userMenu.setObjectName(u"userMenu")
        userMenu.resize(917, 600)
        font = QFont()
        userMenu.setFont(font)
        userMenu.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #FFF;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#centralwidget  {\n"
"	background-color: #5158BB;\n"
"}\n"
"\n"
"#leftMenu {\n"
"	background-color: #2B4790;\n"
"}\n"
"\n"
"#sidebar QPushButton {\n"
"	text-align: left;\n"
"}\n"
"\n"
"#pagesList QPushButton {\n"
"	background-color: #F26DF9;\n"
"	padding: 5px 10px;\n"
"}\n"
"#pagesList > QWidget  {\n"
"	background-color: #5158BB;\n"
"}\n"
"\n"
"#createQuizzPage QLineEdit {\n"
"	background: transparent;\n"
"	border-bottom: 2px solid #F26DF9;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height:20px;\n"
"	image: url(:/icons/images/radio-button.svg);\n"
"}\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/images/checked-radio-button.svg);\n"
"}")
        self.centralwidget = QWidget(userMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.sidebar)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(70, 0))
        self.leftMenu.setMaximumSize(QSize(75, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toggleButton = QPushButton(self.frame)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/images/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon)
        self.toggleButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.toggleButton)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftMenu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.historyButton = QPushButton(self.frame_2)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.historyButton.setIcon(icon1)
        self.historyButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.historyButton)

        self.logoutButton = QPushButton(self.frame_2)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy2)
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon2)
        self.logoutButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.logoutButton)

        self.importQuizzButton = QPushButton(self.frame_2)
        self.importQuizzButton.setObjectName(u"importQuizzButton")
        sizePolicy2.setHeightForWidth(self.importQuizzButton.sizePolicy().hasHeightForWidth())
        self.importQuizzButton.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importQuizzButton.setIcon(icon3)
        self.importQuizzButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.importQuizzButton)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.importQuizzErrorsLabel = QLabel(self.menu)
        self.importQuizzErrorsLabel.setObjectName(u"importQuizzErrorsLabel")
        self.importQuizzErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.importQuizzErrorsLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.importQuizzErrorsLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.leftMenu, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.sidebar)

        self.pagesList = QStackedWidget(self.centralwidget)
        self.pagesList.setObjectName(u"pagesList")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"")
        self.showQuizzListButton = QPushButton(self.homePage)
        self.showQuizzListButton.setObjectName(u"showQuizzListButton")
        self.showQuizzListButton.setGeometry(QRect(150, 250, 375, 31))
        self.showQuizzListButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 100, 401, 71))
        self.createQuizzButton = QPushButton(self.homePage)
        self.createQuizzButton.setObjectName(u"createQuizzButton")
        self.createQuizzButton.setGeometry(QRect(150, 290, 375, 31))
        self.createQuizzButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pagesList.addWidget(self.homePage)
        self.createQuizzPage = QWidget()
        self.createQuizzPage.setObjectName(u"createQuizzPage")
        self.quizzCreationSteps = QStackedWidget(self.createQuizzPage)
        self.quizzCreationSteps.setObjectName(u"quizzCreationSteps")
        self.quizzCreationSteps.setGeometry(QRect(-1, -1, 771, 601))
        self.nameQuizzPage = QWidget()
        self.nameQuizzPage.setObjectName(u"nameQuizzPage")
        self.nameQuizzErrorsLabel = QLabel(self.nameQuizzPage)
        self.nameQuizzErrorsLabel.setObjectName(u"nameQuizzErrorsLabel")
        self.nameQuizzErrorsLabel.setGeometry(QRect(180, 260, 306, 37))
        self.nameQuizzErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.quizzTitle = QLineEdit(self.nameQuizzPage)
        self.quizzTitle.setObjectName(u"quizzTitle")
        self.quizzTitle.setGeometry(QRect(180, 310, 306, 18))
        self.quizzTitle.setEchoMode(QLineEdit.Normal)
        self.addQuestionsButton = QPushButton(self.nameQuizzPage)
        self.addQuestionsButton.setObjectName(u"addQuestionsButton")
        self.addQuestionsButton.setGeometry(QRect(180, 340, 311, 24))
        self.quizzCreationSteps.addWidget(self.nameQuizzPage)
        self.createQuestionsPage = QWidget()
        self.createQuestionsPage.setObjectName(u"createQuestionsPage")
        self.titleQuestion = QLineEdit(self.createQuestionsPage)
        self.titleQuestion.setObjectName(u"titleQuestion")
        self.titleQuestion.setGeometry(QRect(160, 90, 391, 50))
        self.titleQuestion.setMinimumSize(QSize(0, 50))
        self.titleQuestion.setEchoMode(QLineEdit.Normal)
        self.radioButton0 = QRadioButton(self.createQuestionsPage)
        self.choiceRightAnswer = QButtonGroup(userMenu)
        self.choiceRightAnswer.setObjectName(u"choiceRightAnswer")
        self.choiceRightAnswer.setExclusive(True)
        self.choiceRightAnswer.addButton(self.radioButton0)
        self.radioButton0.setObjectName(u"radioButton0")
        self.radioButton0.setGeometry(QRect(340, 200, 21, 21))
        self.radioButton0.setMinimumSize(QSize(0, 0))
        self.radioButton0.setFont(font)
        self.radioButton0.setChecked(False)
        self.radioButton2 = QRadioButton(self.createQuestionsPage)
        self.choiceRightAnswer.addButton(self.radioButton2)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(340, 260, 21, 21))
        self.radioButton2.setMinimumSize(QSize(0, 0))
        self.radioButton2.setFont(font)
        self.radioButton2.setChecked(False)
        self.radioButton3 = QRadioButton(self.createQuestionsPage)
        self.choiceRightAnswer.addButton(self.radioButton3)
        self.radioButton3.setObjectName(u"radioButton3")
        self.radioButton3.setGeometry(QRect(340, 320, 21, 21))
        self.radioButton3.setMinimumSize(QSize(0, 0))
        self.radioButton3.setFont(font)
        self.radioButton3.setChecked(False)
        self.radioButton4 = QRadioButton(self.createQuestionsPage)
        self.choiceRightAnswer.addButton(self.radioButton4)
        self.radioButton4.setObjectName(u"radioButton4")
        self.radioButton4.setGeometry(QRect(340, 380, 21, 21))
        self.radioButton4.setMinimumSize(QSize(0, 0))
        self.radioButton4.setFont(font)
        self.radioButton4.setChecked(False)
        self.label_2 = QLabel(self.createQuestionsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 170, 101, 16))
        self.nextQuestionButton = QPushButton(self.createQuestionsPage)
        self.nextQuestionButton.setObjectName(u"nextQuestionButton")
        self.nextQuestionButton.setGeometry(QRect(160, 430, 251, 30))
        self.nextQuestionButton.setMinimumSize(QSize(0, 30))
        self.endQuestionsButton = QPushButton(self.createQuestionsPage)
        self.endQuestionsButton.setObjectName(u"endQuestionsButton")
        self.endQuestionsButton.setGeometry(QRect(430, 430, 121, 30))
        self.endQuestionsButton.setMinimumSize(QSize(0, 30))
        self.questionCreationErrorsLabel = QLabel(self.createQuestionsPage)
        self.questionCreationErrorsLabel.setObjectName(u"questionCreationErrorsLabel")
        self.questionCreationErrorsLabel.setGeometry(QRect(160, 480, 391, 41))
        self.questionCreationErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.verticalLayoutWidget = QWidget(self.createQuestionsPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(160, 190, 160, 232))
        self.answers = QVBoxLayout(self.verticalLayoutWidget)
        self.answers.setObjectName(u"answers")
        self.answers.setContentsMargins(0, 0, 0, 0)
        self.answer1 = QLineEdit(self.verticalLayoutWidget)
        self.answer1.setObjectName(u"answer1")
        self.answer1.setMinimumSize(QSize(0, 50))
        self.answer1.setEchoMode(QLineEdit.Normal)

        self.answers.addWidget(self.answer1)

        self.answer2 = QLineEdit(self.verticalLayoutWidget)
        self.answer2.setObjectName(u"answer2")
        self.answer2.setMinimumSize(QSize(0, 50))
        self.answer2.setEchoMode(QLineEdit.Normal)

        self.answers.addWidget(self.answer2)

        self.answer3 = QLineEdit(self.verticalLayoutWidget)
        self.answer3.setObjectName(u"answer3")
        self.answer3.setMinimumSize(QSize(0, 50))
        self.answer3.setEchoMode(QLineEdit.Normal)

        self.answers.addWidget(self.answer3)

        self.answer4 = QLineEdit(self.verticalLayoutWidget)
        self.answer4.setObjectName(u"answer4")
        self.answer4.setMinimumSize(QSize(0, 50))
        self.answer4.setEchoMode(QLineEdit.Normal)

        self.answers.addWidget(self.answer4)

        self.questionNumberLabel = QLabel(self.createQuestionsPage)
        self.questionNumberLabel.setObjectName(u"questionNumberLabel")
        self.questionNumberLabel.setGeometry(QRect(160, 80, 101, 16))
        self.quizzCreationSteps.addWidget(self.createQuestionsPage)
        self.chooseOrderPage = QWidget()
        self.chooseOrderPage.setObjectName(u"chooseOrderPage")
        self.questionNumberLabel_3 = QLabel(self.chooseOrderPage)
        self.questionNumberLabel_3.setObjectName(u"questionNumberLabel_3")
        self.questionNumberLabel_3.setGeometry(QRect(190, 113, 381, 61))
        self.questionNumberLabel_3.setAlignment(Qt.AlignCenter)
        self.doRandomOrderButton = QPushButton(self.chooseOrderPage)
        self.doRandomOrderButton.setObjectName(u"doRandomOrderButton")
        self.doRandomOrderButton.setGeometry(QRect(220, 190, 116, 30))
        self.doRandomOrderButton.setMinimumSize(QSize(0, 30))
        self.noRandomOrderButton = QPushButton(self.chooseOrderPage)
        self.noRandomOrderButton.setObjectName(u"noRandomOrderButton")
        self.noRandomOrderButton.setGeometry(QRect(420, 190, 116, 30))
        self.noRandomOrderButton.setMinimumSize(QSize(0, 30))
        self.quizzCreationSteps.addWidget(self.chooseOrderPage)
        self.chooseNbToDisplayPage = QWidget()
        self.chooseNbToDisplayPage.setObjectName(u"chooseNbToDisplayPage")
        self.saveQuizzButton = QPushButton(self.chooseNbToDisplayPage)
        self.saveQuizzButton.setObjectName(u"saveQuizzButton")
        self.saveQuizzButton.setGeometry(QRect(230, 320, 306, 31))
        self.label_5 = QLabel(self.chooseNbToDisplayPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(222, 140, 321, 20))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.nbQuestionsLabel = QLabel(self.chooseNbToDisplayPage)
        self.nbQuestionsLabel.setObjectName(u"nbQuestionsLabel")
        self.nbQuestionsLabel.setGeometry(QRect(220, 169, 321, 31))
        self.nbQuestionsLabel.setAlignment(Qt.AlignCenter)
        self.nbToDisplay = QLineEdit(self.chooseNbToDisplayPage)
        self.nbToDisplay.setObjectName(u"nbToDisplay")
        self.nbToDisplay.setGeometry(QRect(270, 230, 234, 50))
        self.nbToDisplay.setMinimumSize(QSize(0, 50))
        self.nbToDisplay.setEchoMode(QLineEdit.Normal)
        self.nbToDisplayErrorsLabel = QLabel(self.chooseNbToDisplayPage)
        self.nbToDisplayErrorsLabel.setObjectName(u"nbToDisplayErrorsLabel")
        self.nbToDisplayErrorsLabel.setGeometry(QRect(270, 370, 234, 13))
        self.nbToDisplayErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.quizzCreationSteps.addWidget(self.chooseNbToDisplayPage)
        self.pagesList.addWidget(self.createQuizzPage)
        self.quizzListPage = QWidget()
        self.quizzListPage.setObjectName(u"quizzListPage")
        self.quizzListPage.setEnabled(True)
        self.label_3 = QLabel(self.quizzListPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 110, 211, 39))
        self.pagesList.addWidget(self.quizzListPage)

        self.horizontalLayout_2.addWidget(self.pagesList)

        userMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(userMenu)

        self.pagesList.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(userMenu)
    # setupUi

    def retranslateUi(self, userMenu):
        userMenu.setWindowTitle(QCoreApplication.translate("userMenu", u"WinQuest", None))
#if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate("userMenu", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.toggleButton.setText("")
#if QT_CONFIG(tooltip)
        self.historyButton.setToolTip(QCoreApplication.translate("userMenu", u"Consulter votre historique", None))
#endif // QT_CONFIG(tooltip)
        self.historyButton.setText(QCoreApplication.translate("userMenu", u"     Historique", None))
#if QT_CONFIG(tooltip)
        self.logoutButton.setToolTip(QCoreApplication.translate("userMenu", u"Se d\u00e9connecter", None))
#endif // QT_CONFIG(tooltip)
        self.logoutButton.setText(QCoreApplication.translate("userMenu", u"     Se d\u00e9connecter", None))
#if QT_CONFIG(tooltip)
        self.importQuizzButton.setToolTip(QCoreApplication.translate("userMenu", u"Se d\u00e9connecter", None))
#endif // QT_CONFIG(tooltip)
        self.importQuizzButton.setText(QCoreApplication.translate("userMenu", u"Importer un Quizz", None))
        self.importQuizzErrorsLabel.setText("")
        self.showQuizzListButton.setText(QCoreApplication.translate("userMenu", u"Liste des quizz", None))
        self.label.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Bienvenue sur WinQuest !</span></p></body></html>", None))
        self.createQuizzButton.setText(QCoreApplication.translate("userMenu", u"Cr\u00e9er un quizz", None))
        self.nameQuizzErrorsLabel.setText("")
        self.quizzTitle.setPlaceholderText(QCoreApplication.translate("userMenu", u"Titre du Quizz", None))
        self.addQuestionsButton.setText(QCoreApplication.translate("userMenu", u"Ajouter les questions >", None))
        self.titleQuestion.setPlaceholderText(QCoreApplication.translate("userMenu", u"Intitul\u00e9 de la question", None))
        self.radioButton0.setText("")
        self.radioButton2.setText("")
        self.radioButton3.setText("")
        self.radioButton4.setText("")
        self.label_2.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-weight:600;\">Bonne r\u00e9ponse</span></p></body></html>", None))
        self.nextQuestionButton.setText(QCoreApplication.translate("userMenu", u"Prochaine question", None))
        self.endQuestionsButton.setText(QCoreApplication.translate("userMenu", u"Terminer", None))
        self.questionCreationErrorsLabel.setText("")
        self.answer1.setPlaceholderText(QCoreApplication.translate("userMenu", u"R\u00e9ponse 1", None))
        self.answer2.setPlaceholderText(QCoreApplication.translate("userMenu", u"R\u00e9ponse 2", None))
        self.answer3.setPlaceholderText(QCoreApplication.translate("userMenu", u"R\u00e9ponse 3", None))
        self.answer4.setPlaceholderText(QCoreApplication.translate("userMenu", u"R\u00e9ponse 4", None))
        self.questionNumberLabel.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-weight:600;\">Question 1</span></p></body></html>", None))
        self.questionNumberLabel_3.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:12pt;\">Afficher les questions dans un ordre al\u00e9atoire ?</span></p></body></html>", None))
        self.doRandomOrderButton.setText(QCoreApplication.translate("userMenu", u"Oui", None))
        self.noRandomOrderButton.setText(QCoreApplication.translate("userMenu", u"Non", None))
        self.saveQuizzButton.setText(QCoreApplication.translate("userMenu", u"Valider", None))
        self.label_5.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:12pt;\">Combien voulez-vous afficher de questions ?</span></p></body></html>", None))
        self.nbQuestionsLabel.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p>Vous avez \u00e9crit 1 questions<br/></p></body></html>", None))
        self.nbToDisplay.setPlaceholderText(QCoreApplication.translate("userMenu", u"Ins\u00e9rez un nombre", None))
        self.nbToDisplayErrorsLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt;\">Liste des quizz</span></p></body></html>", None))
    # retranslateUi

