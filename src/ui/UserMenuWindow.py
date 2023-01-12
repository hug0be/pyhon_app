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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
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
"")
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.historyButton.setIcon(icon1)
        self.historyButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.historyButton)

        self.disconnectButton = QPushButton(self.frame_2)
        self.disconnectButton.setObjectName(u"disconnectButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnectButton.setIcon(icon2)
        self.disconnectButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.disconnectButton)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

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
        self.showQuizzListButton.setGeometry(QRect(130, 250, 375, 31))
        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 100, 371, 71))
        self.pagesList.addWidget(self.homePage)
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

        self.pagesList.setCurrentIndex(0)


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
        self.disconnectButton.setToolTip(QCoreApplication.translate("userMenu", u"Se d\u00e9connecter", None))
#endif // QT_CONFIG(tooltip)
        self.disconnectButton.setText(QCoreApplication.translate("userMenu", u"     Se d\u00e9connecter", None))
        self.showQuizzListButton.setText(QCoreApplication.translate("userMenu", u"Liste des quizz", None))
        self.label.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt;\">Bienvenue sur WinQuest !</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("userMenu", u"<html><head/><body><p><span style=\" font-size:24pt;\">Liste des quizz</span></p></body></html>", None))
    # retranslateUi

