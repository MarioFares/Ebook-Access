# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# noinspection PyAttributeOutsideInit
class InfoDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(652, 477)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 561, 221))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 280, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 320, 481, 101))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 440, 151, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.linkActivated.connect(lambda: self.link())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome to Ebook Access"))
        self.label_2.setText(_translate("Dialog", "This application was primarily designed as a library to handle "
                                                  "one\'s ebooks, even though it may be used with regular files just "
                                                  "as easily. Built to have a simple and clean interface with a "
                                                  "simple but rich set of commands, you will quickly find that "
                                                  "working with this application is extremely easy.\n "
                                                  "\n"
                                                  "It will definitely be better than your native computer\'s own file "
                                                  "explorer.\n "
                                                  "\n"
                                                  "This application is also built with customization in mind as we "
                                                  "know that not everyone is the same and likes the "
                                                  "same thing.\n "
                                                  "\n"
                                                  "There is also an optional feedback section in the help menu so "
                                                  "that you may give the developer feedback or simply "
                                                  "send a complaint about the application."))
        self.label_3.setText(_translate("Dialog", "For Developers"))
        self.label_4.setText(_translate("Dialog", "This application was built using Python 3.8.4 with PyQt5 as the "
                                                  "GUI library and SQLite as the RDBMS. The application even ships "
                                                  "with SQLite DB Browser so that you may manipulate data easily with "
                                                  "SQL.Most of the modules used are from the Python Standard Library. "
                                                  "\n "
                                                  "This application is open source, and you may find the source code "
                                                  "on:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><a "
                                                  "href=\"https://github.com/MarioFares\"><span style=\" "
                                                  "text-decoration: underline; "
                                                  "color:#0000ff;\">https://github.com/MarioFares</span></a></p"
                                                  "></body></html>"))

    @staticmethod
    def link():
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/MarioFares"))
