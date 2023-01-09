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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 661)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#centralwidget  {\n"
"	background-color: #5158BB;\n"
"}\n"
"\n"
".QLineEdit {\n"
"	background: transparent;\n"
"	border-bottom: 2px solid #F26DF9;\n"
"}\n"
".QPushButton {\n"
"	background-color: #F26DF9;\n"
"	padding: 2px 5px;\n"
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.connectUsername = QLineEdit(self.centralwidget)
        self.connectUsername.setObjectName(u"connectUsername")
        self.connectUsername.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.connectUsername)

        self.connectPassword = QLineEdit(self.centralwidget)
        self.connectPassword.setObjectName(u"connectPassword")
        self.connectPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.connectPassword)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")

        self.verticalLayout.addWidget(self.connectButton)

        self.connectErrorsLabel = QLabel(self.centralwidget)
        self.connectErrorsLabel.setObjectName(u"connectErrorsLabel")
        self.connectErrorsLabel.setStyleSheet(u"color: #F3A917")

        self.verticalLayout.addWidget(self.connectErrorsLabel)

        self.createAccountSecondaryButton = QPushButton(self.centralwidget)
        self.createAccountSecondaryButton.setObjectName(u"createAccountSecondaryButton")

        self.verticalLayout.addWidget(self.createAccountSecondaryButton)

        self.verticalSpacer_2 = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.accountUsername = QLineEdit(self.centralwidget)
        self.accountUsername.setObjectName(u"accountUsername")
        self.accountUsername.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_2.addWidget(self.accountUsername)

        self.accountPassword = QLineEdit(self.centralwidget)
        self.accountPassword.setObjectName(u"accountPassword")
        self.accountPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.accountPassword)

        self.createAccountButton = QPushButton(self.centralwidget)
        self.createAccountButton.setObjectName(u"createAccountButton")

        self.verticalLayout_2.addWidget(self.createAccountButton)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.createAccountErrorsLabel = QLabel(self.centralwidget)
        self.createAccountErrorsLabel.setObjectName(u"createAccountErrorsLabel")
        self.createAccountErrorsLabel.setStyleSheet(u"color: #F3A917")

        self.verticalLayout_2.addWidget(self.createAccountErrorsLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WinQuest", None))
        self.connectUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.connectPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.connectErrorsLabel.setText("")
        self.createAccountSecondaryButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un compte", None))
        self.accountUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.accountPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.createAccountButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un compte", None))
        self.createAccountErrorsLabel.setText("")
    # retranslateUi

