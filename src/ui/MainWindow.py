# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 512)
        MainWindow.setBaseSize(QSize(1024, 512))
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#centralwidget, #pagesList > QWidget {\n"
"	background-color: #5158BB;\n"
"}\n"
"\n"
".QLineEdit {\n"
"	background: transparent;\n"
"	margin: 15px 0px;\n"
"	border-bottom: 2px solid #F26DF9;\n"
"}\n"
".QPushButton {\n"
"	background-color: #F26DF9;\n"
"	padding: 2px 5px;\n"
"}\n"
"\n"
"#backButton, #backButton2 {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#createAccountSecondaryButton {\n"
"	border: 2px solid #F26DF9;\n"
"	background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pagesList = QStackedWidget(self.centralwidget)
        self.pagesList.setObjectName(u"pagesList")
        self.pagesList.setMinimumSize(QSize(470, 450))
        self.pagesList.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"")
        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 471, 191))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.chooseConnectButton = QPushButton(self.homePage)
        self.chooseConnectButton.setObjectName(u"chooseConnectButton")
        self.chooseConnectButton.setGeometry(QRect(159, 170, 152, 24))
        self.chooseConnectButton.setStyleSheet(u"*{\n"
"display: flex;\n"
"justify-content : center\n"
"}")
        self.chooseCreateAccountButton = QPushButton(self.homePage)
        self.chooseCreateAccountButton.setObjectName(u"chooseCreateAccountButton")
        self.chooseCreateAccountButton.setGeometry(QRect(159, 210, 151, 24))
        self.pagesList.addWidget(self.homePage)
        self.connectPage = QWidget()
        self.connectPage.setObjectName(u"connectPage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectPage.sizePolicy().hasHeightForWidth())
        self.connectPage.setSizePolicy(sizePolicy)
        self.widget_3 = QWidget(self.connectPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(109, 120, 252, 208))
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.connectUsername = QLineEdit(self.widget_3)
        self.connectUsername.setObjectName(u"connectUsername")
        self.connectUsername.setMinimumSize(QSize(0, 50))
        self.connectUsername.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_5.addWidget(self.connectUsername)

        self.connectPassword = QLineEdit(self.widget_3)
        self.connectPassword.setObjectName(u"connectPassword")
        self.connectPassword.setMinimumSize(QSize(0, 50))
        self.connectPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.connectPassword)

        self.connectButton = QPushButton(self.widget_3)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.connectButton)

        self.connectErrorsLabel = QLabel(self.widget_3)
        self.connectErrorsLabel.setObjectName(u"connectErrorsLabel")
        self.connectErrorsLabel.setStyleSheet(u"color: #F3A917")

        self.verticalLayout_5.addWidget(self.connectErrorsLabel)

        self.backButton2 = QPushButton(self.connectPage)
        self.backButton2.setObjectName(u"backButton2")
        self.backButton2.setGeometry(QRect(40, 50, 75, 24))
        icon = QIcon()
        icon.addFile(u":/icons/images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton2.setIcon(icon)
        self.backButton2.setAutoDefault(False)
        self.pagesList.addWidget(self.connectPage)
        self.createAccountPage = QWidget()
        self.createAccountPage.setObjectName(u"createAccountPage")
        self.widget_4 = QWidget(self.createAccountPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(109, 120, 252, 208))
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.accountUsername = QLineEdit(self.widget_4)
        self.accountUsername.setObjectName(u"accountUsername")
        self.accountUsername.setMinimumSize(QSize(0, 50))
        self.accountUsername.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_6.addWidget(self.accountUsername)

        self.accountPassword = QLineEdit(self.widget_4)
        self.accountPassword.setObjectName(u"accountPassword")
        self.accountPassword.setMinimumSize(QSize(0, 50))
        self.accountPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.accountPassword)

        self.accountPasswordConfirmation = QLineEdit(self.widget_4)
        self.accountPasswordConfirmation.setObjectName(u"accountPasswordConfirmation")
        self.accountPasswordConfirmation.setMinimumSize(QSize(0, 50))
        self.accountPasswordConfirmation.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.accountPasswordConfirmation)

        self.createAccountButton = QPushButton(self.widget_4)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.createAccountButton)

        self.createAccountErrorsLabel = QLabel(self.widget_4)
        self.createAccountErrorsLabel.setObjectName(u"createAccountErrorsLabel")
        self.createAccountErrorsLabel.setStyleSheet(u"color: #F3A917")

        self.verticalLayout_6.addWidget(self.createAccountErrorsLabel)

        self.backButton = QPushButton(self.createAccountPage)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(40, 50, 75, 24))
        self.backButton.setIcon(icon)
        self.backButton.setAutoDefault(False)
        self.pagesList.addWidget(self.createAccountPage)

        self.horizontalLayout.addWidget(self.pagesList, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pagesList.setCurrentIndex(0)
        self.backButton2.setDefault(False)
        self.backButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WinQuest", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenue sur WinQuest", None))
        self.chooseConnectButton.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.chooseCreateAccountButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er mon compte", None))
        self.connectUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.connectPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.connectErrorsLabel.setText("")
        self.backButton2.setText("")
        self.accountUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.accountPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.accountPasswordConfirmation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmer le mot de passe", None))
        self.createAccountButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er mon compte", None))
        self.createAccountErrorsLabel.setText("")
        self.backButton.setText("")
    # retranslateUi

