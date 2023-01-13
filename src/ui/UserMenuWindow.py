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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_userMenu(object):
    def setupUi(self, userMenu):
        if not userMenu.objectName():
            userMenu.setObjectName(u"userMenu")
        userMenu.resize(917, 600)
        userMenu.setMinimumSize(QSize(917, 600))
        userMenu.setMaximumSize(QSize(917, 600))
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
"#label_Nb_Points{\n"
"	font-size : 50px\n"
"}\n"
"\n"
"#label_Points{\n"
"	font-size : 20px\n"
"}\n"
"\n"
"#label_NB_Question{\n"
"	font-size : 20px\n"
"}\n"
"\n"
"#label_titre{\n"
"	font-size : 30px\n"
"}\n"
"\n"
"#label_titre_2{\n"
"	font-size : 20px\n"
"}\n"
"\n"
"#label_Fin_Quiz{\n"
"	font-size : 55px;\n"
"}\n"
"\n"
"#label_Fin_VotreScore{\n"
"	font-size : 30px;\n"
"}\n"
"\n"
"\n"
"#label_Fin_Score{\n"
"	font-size : 55px;\n"
"}\n"
"\n"
"#label_Fin_Temps{\n"
"	font-size : 20px;\n"
"}\n"
"\n"
"#label_Fin_VotreTemps{\n"
"	font-size : 30px;\n"
"}\n"
"\n"
"#centralwidget, QStackedWidget > QWidget  {\n"
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
""
                        "    qproperty-cursor: PointingHandCursor;\n"
"}\n"
"#pagesList > QWidget  {\n"
"	background-color: #5158BB;\n"
"}\n"
"\n"
"#createQuizzPage QLineEdit, #questionsPage QLineEdit{\n"
"	background: transparent;\n"
"	border-bottom: 2px solid #F26DF9;\n"
"}\n"
"\n"
"#radioButton1_Quiz, #radioButton2_Quiz, #radioButton3_Quiz, #label_Question{\n"
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
"}\n"
"\n"
"#FinQuestionPage QPushButton{\n"
"	height:30px;\n"
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

        self.importQuizzButton = QPushButton(self.frame_2)
        self.importQuizzButton.setObjectName(u"importQuizzButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.importQuizzButton.sizePolicy().hasHeightForWidth())
        self.importQuizzButton.setSizePolicy(sizePolicy2)
        self.importQuizzButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importQuizzButton.setIcon(icon2)
        self.importQuizzButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.importQuizzButton)

        self.logoutButton = QPushButton(self.frame_2)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy2.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy2)
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon3)
        self.logoutButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.logoutButton)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.importQuizzErrorsLabel = QLabel(self.leftMenu)
        self.importQuizzErrorsLabel.setObjectName(u"importQuizzErrorsLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.importQuizzErrorsLabel.sizePolicy().hasHeightForWidth())
        self.importQuizzErrorsLabel.setSizePolicy(sizePolicy3)
        self.importQuizzErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.importQuizzErrorsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.importQuizzErrorsLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.importQuizzErrorsLabel)


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
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.label_4 = QLabel(self.history)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 90, 841, 71))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4 = QGroupBox(self.history)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 163, 841, 421))
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.historyContainer = QWidget(self.groupBox_4)
        self.historyContainer.setObjectName(u"historyContainer")
        self.historyContainer.setGeometry(QRect(240, 10, 450, 241))
        self.backButton6 = QPushButton(self.history)
        self.backButton6.setObjectName(u"backButton6")
        self.backButton6.setGeometry(QRect(70, 50, 141, 31))
        self.backButton6.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton6.setStyleSheet(u"background: transparent")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton6.setIcon(icon4)
        self.backButton6.setAutoDefault(False)
        self.pagesList.addWidget(self.history)
        self.quizzListPage = QWidget()
        self.quizzListPage.setObjectName(u"quizzListPage")
        self.quizzListPage.setEnabled(True)
        self.label_3 = QLabel(self.quizzListPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 110, 841, 39))
        self.groupBox_3 = QGroupBox(self.quizzListPage)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 173, 841, 421))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.page_list_quizz_container_bot = QWidget(self.groupBox_3)
        self.page_list_quizz_container_bot.setObjectName(u"page_list_quizz_container_bot")
        self.page_list_quizz_container_bot.setGeometry(QRect(190, 30, 450, 241))
        self.backButton1 = QPushButton(self.quizzListPage)
        self.backButton1.setObjectName(u"backButton1")
        self.backButton1.setGeometry(QRect(70, 60, 141, 31))
        self.backButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton1.setStyleSheet(u"background: transparent")
        self.backButton1.setIcon(icon4)
        self.backButton1.setAutoDefault(False)
        self.pagesList.addWidget(self.quizzListPage)
        self.questionsPage = QWidget()
        self.questionsPage.setObjectName(u"questionsPage")
        self.questionPages = QStackedWidget(self.questionsPage)
        self.questionPages.setObjectName(u"questionPages")
        self.questionPages.setGeometry(QRect(0, -1, 801, 601))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.questionPages.sizePolicy().hasHeightForWidth())
        self.questionPages.setSizePolicy(sizePolicy4)
        self.questionPage = QWidget()
        self.questionPage.setObjectName(u"questionPage")
        self.verticalLayoutWidget_5 = QWidget(self.questionPage)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(220, 210, 421, 231))
        self.answers_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.answers_6.setObjectName(u"answers_6")
        self.answers_6.setContentsMargins(0, 0, 0, 0)
        self.radioButton1_Quiz = QRadioButton(self.verticalLayoutWidget_5)
        self.choiceRightAnswerQuizz = QButtonGroup(userMenu)
        self.choiceRightAnswerQuizz.setObjectName(u"choiceRightAnswerQuizz")
        self.choiceRightAnswerQuizz.addButton(self.radioButton1_Quiz)
        self.radioButton1_Quiz.setObjectName(u"radioButton1_Quiz")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radioButton1_Quiz.sizePolicy().hasHeightForWidth())
        self.radioButton1_Quiz.setSizePolicy(sizePolicy5)
        self.radioButton1_Quiz.setMinimumSize(QSize(0, 0))
        self.radioButton1_Quiz.setFont(font)
        self.radioButton1_Quiz.setIconSize(QSize(16, 16))
        self.radioButton1_Quiz.setChecked(False)

        self.answers_6.addWidget(self.radioButton1_Quiz)

        self.radioButton2_Quiz = QRadioButton(self.verticalLayoutWidget_5)
        self.choiceRightAnswerQuizz.addButton(self.radioButton2_Quiz)
        self.radioButton2_Quiz.setObjectName(u"radioButton2_Quiz")
        sizePolicy5.setHeightForWidth(self.radioButton2_Quiz.sizePolicy().hasHeightForWidth())
        self.radioButton2_Quiz.setSizePolicy(sizePolicy5)
        self.radioButton2_Quiz.setMinimumSize(QSize(0, 0))
        self.radioButton2_Quiz.setFont(font)
        self.radioButton2_Quiz.setChecked(False)

        self.answers_6.addWidget(self.radioButton2_Quiz)

        self.radioButton3_Quiz = QRadioButton(self.verticalLayoutWidget_5)
        self.choiceRightAnswerQuizz.addButton(self.radioButton3_Quiz)
        self.radioButton3_Quiz.setObjectName(u"radioButton3_Quiz")
        sizePolicy5.setHeightForWidth(self.radioButton3_Quiz.sizePolicy().hasHeightForWidth())
        self.radioButton3_Quiz.setSizePolicy(sizePolicy5)
        self.radioButton3_Quiz.setMinimumSize(QSize(0, 0))
        self.radioButton3_Quiz.setFont(font)
        self.radioButton3_Quiz.setChecked(False)

        self.answers_6.addWidget(self.radioButton3_Quiz)

        self.radioButton4_Quiz = QRadioButton(self.verticalLayoutWidget_5)
        self.choiceRightAnswerQuizz.addButton(self.radioButton4_Quiz)
        self.radioButton4_Quiz.setObjectName(u"radioButton4_Quiz")
        sizePolicy5.setHeightForWidth(self.radioButton4_Quiz.sizePolicy().hasHeightForWidth())
        self.radioButton4_Quiz.setSizePolicy(sizePolicy5)
        self.radioButton4_Quiz.setMinimumSize(QSize(0, 0))
        self.radioButton4_Quiz.setFont(font)
        self.radioButton4_Quiz.setChecked(False)

        self.answers_6.addWidget(self.radioButton4_Quiz)

        self.label_VotreReponse = QLabel(self.questionPage)
        self.label_VotreReponse.setObjectName(u"label_VotreReponse")
        self.label_VotreReponse.setGeometry(QRect(190, 190, 101, 16))
        self.questionErrorsLabel = QLabel(self.questionPage)
        self.questionErrorsLabel.setObjectName(u"questionErrorsLabel")
        self.questionErrorsLabel.setGeometry(QRect(150, 470, 391, 41))
        self.questionErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.label_Points = QLabel(self.questionPage)
        self.label_Points.setObjectName(u"label_Points")
        self.label_Points.setGeometry(QRect(690, 120, 61, 20))
        self.nbPointsLabel = QLabel(self.questionPage)
        self.nbPointsLabel.setObjectName(u"nbPointsLabel")
        self.nbPointsLabel.setGeometry(QRect(690, 70, 61, 51))
        self.nbPointsLabel.setFont(font)
        self.label_NB_Question = QLabel(self.questionPage)
        self.label_NB_Question.setObjectName(u"label_NB_Question")
        self.label_NB_Question.setGeometry(QRect(690, 480, 61, 16))
        self.validateButton = QPushButton(self.questionPage)
        self.validateButton.setObjectName(u"validateButton")
        self.validateButton.setGeometry(QRect(290, 460, 251, 30))
        self.validateButton.setMinimumSize(QSize(0, 30))
        self.label_Question = QLabel(self.questionPage)
        self.label_Question.setObjectName(u"label_Question")
        self.label_Question.setGeometry(QRect(220, 110, 391, 51))
        self.label_titre = QLabel(self.questionPage)
        self.label_titre.setObjectName(u"label_titre")
        self.label_titre.setGeometry(QRect(0, 10, 841, 51))
        self.label_titre.setFont(font)
        self.label_titre.setAlignment(Qt.AlignCenter)
        self.validateAnswerErrorsLabel = QLabel(self.questionPage)
        self.validateAnswerErrorsLabel.setObjectName(u"validateAnswerErrorsLabel")
        self.validateAnswerErrorsLabel.setGeometry(QRect(210, 60, 451, 51))
        sizePolicy1.setHeightForWidth(self.validateAnswerErrorsLabel.sizePolicy().hasHeightForWidth())
        self.validateAnswerErrorsLabel.setSizePolicy(sizePolicy1)
        self.validateAnswerErrorsLabel.setStyleSheet(u"color: #F3A917")
        self.validateAnswerErrorsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.validateAnswerErrorsLabel.setWordWrap(True)
        self.questionPages.addWidget(self.questionPage)
        self.endQuizzPage = QWidget()
        self.endQuizzPage.setObjectName(u"endQuizzPage")
        self.label_Fin_Quiz = QLabel(self.endQuizzPage)
        self.label_Fin_Quiz.setObjectName(u"label_Fin_Quiz")
        self.label_Fin_Quiz.setGeometry(QRect(-10, 40, 841, 71))
        self.label_Fin_Quiz.setAlignment(Qt.AlignCenter)
        self.label_Fin_VotreScore = QLabel(self.endQuizzPage)
        self.label_Fin_VotreScore.setObjectName(u"label_Fin_VotreScore")
        self.label_Fin_VotreScore.setGeometry(QRect(110, 180, 151, 51))
        self.label_Fin_Score = QLabel(self.endQuizzPage)
        self.label_Fin_Score.setObjectName(u"label_Fin_Score")
        self.label_Fin_Score.setGeometry(QRect(110, 210, 141, 121))
        self.gridLayoutWidget = QWidget(self.endQuizzPage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(310, 210, 461, 241))
        self.finQuestionLayout = QGridLayout(self.gridLayoutWidget)
        self.finQuestionLayout.setObjectName(u"finQuestionLayout")
        self.finQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.retryButton = QPushButton(self.gridLayoutWidget)
        self.retryButton.setObjectName(u"retryButton")

        self.finQuestionLayout.addWidget(self.retryButton, 0, 0, 1, 1)

        self.homeButton = QPushButton(self.gridLayoutWidget)
        self.homeButton.setObjectName(u"homeButton")

        self.finQuestionLayout.addWidget(self.homeButton, 0, 1, 1, 1)

        self.listButton = QPushButton(self.gridLayoutWidget)
        self.listButton.setObjectName(u"listButton")

        self.finQuestionLayout.addWidget(self.listButton, 1, 0, 1, 1)

        self.shareButton = QPushButton(self.gridLayoutWidget)
        self.shareButton.setObjectName(u"shareButton")

        self.finQuestionLayout.addWidget(self.shareButton, 1, 1, 1, 1)

        self.label_Fin_VotreTemps = QLabel(self.endQuizzPage)
        self.label_Fin_VotreTemps.setObjectName(u"label_Fin_VotreTemps")
        self.label_Fin_VotreTemps.setGeometry(QRect(100, 350, 171, 51))
        self.label_Fin_Temps = QLabel(self.endQuizzPage)
        self.label_Fin_Temps.setObjectName(u"label_Fin_Temps")
        self.label_Fin_Temps.setGeometry(QRect(130, 400, 111, 51))
        self.label_titre_2 = QLabel(self.endQuizzPage)
        self.label_titre_2.setObjectName(u"label_titre_2")
        self.label_titre_2.setGeometry(QRect(280, 150, 521, 51))
        self.label_titre_2.setFont(font)
        self.label_titre_2.setAlignment(Qt.AlignCenter)
        self.questionPages.addWidget(self.endQuizzPage)
        self.pagesList.addWidget(self.questionsPage)
        self.createQuizzPage = QWidget()
        self.createQuizzPage.setObjectName(u"createQuizzPage")
        self.quizzCreationSteps = QStackedWidget(self.createQuizzPage)
        self.quizzCreationSteps.setObjectName(u"quizzCreationSteps")
        self.quizzCreationSteps.setGeometry(QRect(-1, -1, 791, 601))
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
        self.backButton2 = QPushButton(self.nameQuizzPage)
        self.backButton2.setObjectName(u"backButton2")
        self.backButton2.setGeometry(QRect(70, 60, 121, 31))
        self.backButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton2.setStyleSheet(u"background: transparent")
        self.backButton2.setIcon(icon4)
        self.backButton2.setAutoDefault(False)
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
        self.backButton3 = QPushButton(self.createQuestionsPage)
        self.backButton3.setObjectName(u"backButton3")
        self.backButton3.setGeometry(QRect(70, 40, 121, 31))
        self.backButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton3.setStyleSheet(u"background: transparent")
        self.backButton3.setIcon(icon4)
        self.backButton3.setAutoDefault(False)
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
        self.backButton4 = QPushButton(self.chooseOrderPage)
        self.backButton4.setObjectName(u"backButton4")
        self.backButton4.setGeometry(QRect(60, 60, 121, 31))
        self.backButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton4.setStyleSheet(u"background: transparent")
        self.backButton4.setIcon(icon4)
        self.backButton4.setAutoDefault(False)
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
        self.backButton5 = QPushButton(self.chooseNbToDisplayPage)
        self.backButton5.setObjectName(u"backButton5")
        self.backButton5.setGeometry(QRect(70, 60, 121, 31))
        self.backButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton5.setStyleSheet(u"background: transparent")
        self.backButton5.setIcon(icon4)
        self.backButton5.setAutoDefault(False)
        self.quizzCreationSteps.addWidget(self.chooseNbToDisplayPage)
        self.pagesList.addWidget(self.createQuizzPage)

        self.horizontalLayout_2.addWidget(self.pagesList)

        userMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(userMenu)

        self.pagesList.setCurrentIndex(2)
        self.backButton6.setDefault(False)
        self.backButton1.setDefault(False)
        self.questionPages.setCurrentIndex(0)
        self.quizzCreationSteps.setCurrentIndex(0)
        self.backButton2.setDefault(False)
        self.backButton3.setDefault(False)
        self.backButton4.setDefault(False)
        self.backButton5.setDefault(False)


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
        self.importQuizzButton.setToolTip(QCoreApplication.translate("userMenu", u"Se d\u00e9connecter", None))
#endif // QT_CONFIG(tooltip)
        self.importQuizzButton.setText(QCoreApplication.translate("userMenu", u"     Importer un Quizz", None))
#if QT_CONFIG(tooltip)
        self.logoutButton.setToolTip(QCoreApplication.translate("userMenu", u"Se d\u00e9connecter", None))
#endif // QT_CONFIG(tooltip)
        self.logoutButton.setText(QCoreApplication.translate("userMenu", u"     Se d\u00e9connecter", None))
        self.importQuizzErrorsLabel.setText("")
        self.showQuizzListButton.setText(QCoreApplication.translate("userMenu", u"Liste des quizz", None))
        self.label.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Bienvenue sur WinQuest !</span></p></body></html>", None))
        self.createQuizzButton.setText(QCoreApplication.translate("userMenu", u"Cr\u00e9er un quizz", None))
        self.label_4.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:30pt;\">Historique</span></p></body></html>", None))
        self.groupBox_4.setTitle("")
        self.backButton6.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
        self.label_3.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt;\">Liste des quizz</span></p></body></html>", None))
        self.groupBox_3.setTitle("")
        self.backButton1.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
        self.radioButton1_Quiz.setText(QCoreApplication.translate("userMenu", u"          R\u00e9ponse 1", None))
        self.radioButton2_Quiz.setText(QCoreApplication.translate("userMenu", u"          R\u00e9ponse 2", None))
        self.radioButton3_Quiz.setText(QCoreApplication.translate("userMenu", u"          R\u00e9ponse 3", None))
        self.radioButton4_Quiz.setText(QCoreApplication.translate("userMenu", u"          R\u00e9ponse 4", None))
        self.label_VotreReponse.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-weight:600;\">Votre r\u00e9ponse</span></p></body></html>", None))
        self.questionErrorsLabel.setText("")
        self.label_Points.setText(QCoreApplication.translate("userMenu", u"Points", None))
        self.nbPointsLabel.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:36pt;\">0</span></p></body></html>", None))
        self.label_NB_Question.setText(QCoreApplication.translate("userMenu", u"23/30", None))
        self.validateButton.setText(QCoreApplication.translate("userMenu", u"Valider", None))
        self.label_Question.setText(QCoreApplication.translate("userMenu", u"Question", None))
        self.label_titre.setText(QCoreApplication.translate("userMenu", u"Nom du Quiz", None))
        self.validateAnswerErrorsLabel.setText("")
        self.label_Fin_Quiz.setText(QCoreApplication.translate("userMenu", u"Le Quiz est termin\u00e9e", None))
        self.label_Fin_VotreScore.setText(QCoreApplication.translate("userMenu", u"Votre score", None))
        self.label_Fin_Score.setText(QCoreApplication.translate("userMenu", u"28/30", None))
        self.retryButton.setText(QCoreApplication.translate("userMenu", u"Recommencer", None))
        self.homeButton.setText(QCoreApplication.translate("userMenu", u"Acceuil", None))
        self.listButton.setText(QCoreApplication.translate("userMenu", u"Liste des quizz", None))
        self.shareButton.setText(QCoreApplication.translate("userMenu", u"Partager", None))
        self.label_Fin_VotreTemps.setText(QCoreApplication.translate("userMenu", u"Votre temps", None))
        self.label_Fin_Temps.setText(QCoreApplication.translate("userMenu", u"9min10sec", None))
        self.label_titre_2.setText(QCoreApplication.translate("userMenu", u"Nom du Quiz", None))
        self.nameQuizzErrorsLabel.setText("")
        self.quizzTitle.setPlaceholderText(QCoreApplication.translate("userMenu", u"Titre du Quizz", None))
        self.addQuestionsButton.setText(QCoreApplication.translate("userMenu", u"Ajouter les questions >", None))
        self.backButton2.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
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
        self.backButton3.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
        self.questionNumberLabel_3.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:12pt;\">Afficher les questions dans un ordre al\u00e9atoire ?</span></p></body></html>", None))
        self.doRandomOrderButton.setText(QCoreApplication.translate("userMenu", u"Oui", None))
        self.noRandomOrderButton.setText(QCoreApplication.translate("userMenu", u"Non", None))
        self.backButton4.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
        self.saveQuizzButton.setText(QCoreApplication.translate("userMenu", u"Valider", None))
        self.label_5.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:12pt;\">Combien voulez-vous afficher de questions ?</span></p></body></html>", None))
        self.nbQuestionsLabel.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p>Vous avez \u00e9crit 1 questions<br/></p></body></html>", None))
        self.nbToDisplay.setPlaceholderText(QCoreApplication.translate("userMenu", u"Ins\u00e9rez un nombre", None))
        self.nbToDisplayErrorsLabel.setText("")
        self.backButton5.setText(QCoreApplication.translate("userMenu", u"Retour accueil", None))
    # retranslateUi

