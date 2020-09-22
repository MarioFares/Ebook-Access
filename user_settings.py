# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


# noinspection PyAttributeOutsideInit
class UserSettingsDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(865, 639)
        self.ebooks_list = QtWidgets.QListWidget(Dialog)
        self.ebooks_list.setGeometry(QtCore.QRect(24, 209, 256, 192))
        self.ebooks_list.setObjectName("ebooks_list")
        self.folders_list = QtWidgets.QListWidget(Dialog)
        self.folders_list.setGeometry(QtCore.QRect(24, 436, 256, 192))
        self.folders_list.setObjectName("folders_list")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 871, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.authors_list = QtWidgets.QListWidget(Dialog)
        self.authors_list.setGeometry(QtCore.QRect(304, 209, 256, 192))
        self.authors_list.setObjectName("authors_list")
        self.ebooks_num_label = QtWidgets.QLabel(Dialog)
        self.ebooks_num_label.setGeometry(QtCore.QRect(24, 80, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.ebooks_num_label.setFont(font)
        self.ebooks_num_label.setObjectName("ebooks_num_label")
        self.folders_num_label = QtWidgets.QLabel(Dialog)
        self.folders_num_label.setGeometry(QtCore.QRect(24, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.folders_num_label.setFont(font)
        self.folders_num_label.setObjectName("folders_num_label")
        self.authors_num_label = QtWidgets.QLabel(Dialog)
        self.authors_num_label.setGeometry(QtCore.QRect(24, 121, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.authors_num_label.setFont(font)
        self.authors_num_label.setObjectName("authors_num_label")
        self.genres_num_label = QtWidgets.QLabel(Dialog)
        self.genres_num_label.setGeometry(QtCore.QRect(24, 140, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.genres_num_label.setFont(font)
        self.genres_num_label.setObjectName("genres_num_label")
        self.genres_list = QtWidgets.QListWidget(Dialog)
        self.genres_list.setGeometry(QtCore.QRect(304, 436, 256, 192))
        self.genres_list.setObjectName("genres_list")
        self.themes_list = QtWidgets.QListWidget(Dialog)
        self.themes_list.setGeometry(QtCore.QRect(584, 209, 256, 192))
        self.themes_list.setObjectName("themes_list")
        self.themes_num_label = QtWidgets.QLabel(Dialog)
        self.themes_num_label.setGeometry(QtCore.QRect(584, 81, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.themes_num_label.setFont(font)
        self.themes_num_label.setObjectName("themes_num_label")
        self.groups_num_label = QtWidgets.QLabel(Dialog)
        self.groups_num_label.setGeometry(QtCore.QRect(24, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.groups_num_label.setFont(font)
        self.groups_num_label.setObjectName("groups_num_label")
        self.groups_list = QtWidgets.QListWidget(Dialog)
        self.groups_list.setGeometry(QtCore.QRect(584, 436, 256, 192))
        self.groups_list.setObjectName("groups_list")
        self.active_theme_label = QtWidgets.QLabel(Dialog)
        self.active_theme_label.setGeometry(QtCore.QRect(584, 102, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.active_theme_label.setFont(font)
        self.active_theme_label.setObjectName("active_theme_label")
        self.ebooks_label = QtWidgets.QLabel(Dialog)
        self.ebooks_label.setGeometry(QtCore.QRect(131, 190, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.ebooks_label.setFont(font)
        self.ebooks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ebooks_label.setObjectName("ebooks_label")
        self.folders_label = QtWidgets.QLabel(Dialog)
        self.folders_label.setGeometry(QtCore.QRect(100, 410, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.folders_label.setFont(font)
        self.folders_label.setAlignment(QtCore.Qt.AlignCenter)
        self.folders_label.setObjectName("folders_label")
        self.authors_label = QtWidgets.QLabel(Dialog)
        self.authors_label.setGeometry(QtCore.QRect(380, 180, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.authors_label.setFont(font)
        self.authors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.authors_label.setObjectName("authors_label")
        self.genres_label = QtWidgets.QLabel(Dialog)
        self.genres_label.setGeometry(QtCore.QRect(380, 410, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.genres_label.setFont(font)
        self.genres_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genres_label.setObjectName("genres_label")
        self.groups_label = QtWidgets.QLabel(Dialog)
        self.groups_label.setGeometry(QtCore.QRect(660, 410, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.groups_label.setFont(font)
        self.groups_label.setAlignment(QtCore.Qt.AlignCenter)
        self.groups_label.setObjectName("groups_label")
        self.themes_label = QtWidgets.QLabel(Dialog)
        self.themes_label.setGeometry(QtCore.QRect(660, 180, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.themes_label.setFont(font)
        self.themes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.themes_label.setObjectName("themes_label")
        self.ebooks_num = QtWidgets.QLabel(Dialog)
        self.ebooks_num.setGeometry(QtCore.QRect(146, 80, 131, 21))
        self.ebooks_num.setText("")
        self.ebooks_num.setObjectName("ebooks_num")
        self.folders_num = QtWidgets.QLabel(Dialog)
        self.folders_num.setGeometry(QtCore.QRect(146, 100, 131, 21))
        self.folders_num.setText("")
        self.folders_num.setObjectName("folders_num")
        self.authors_num = QtWidgets.QLabel(Dialog)
        self.authors_num.setGeometry(QtCore.QRect(146, 120, 131, 21))
        self.authors_num.setText("")
        self.authors_num.setObjectName("authors_num")
        self.genres_num = QtWidgets.QLabel(Dialog)
        self.genres_num.setGeometry(QtCore.QRect(146, 140, 131, 21))
        self.genres_num.setText("")
        self.genres_num.setObjectName("genres_num")
        self.groups_num = QtWidgets.QLabel(Dialog)
        self.groups_num.setGeometry(QtCore.QRect(146, 160, 131, 21))
        self.groups_num.setText("")
        self.groups_num.setObjectName("groups_num")
        self.themes_num = QtWidgets.QLabel(Dialog)
        self.themes_num.setGeometry(QtCore.QRect(701, 82, 131, 21))
        self.themes_num.setText("")
        self.themes_num.setObjectName("themes_num")
        self.active_theme = QtWidgets.QLabel(Dialog)
        self.active_theme.setGeometry(QtCore.QRect(701, 103, 131, 21))
        self.active_theme.setText("")
        self.active_theme.setObjectName("active_theme")

        self.connect = sqlite3.connect('ebook.db')
        self.cursor = self.connect.cursor()
        with self.connect:
            self.cursor.execute("SELECT name FROM ebooks")
            ebooks = self.cursor.fetchall()
            self.cursor.execute("SELECT DISTINCT folder FROM ebooks")
            folders = self.cursor.fetchall()
            self.cursor.execute("SELECT DISTINCT author FROM ebooks")
            authors = self.cursor.fetchall()
            self.cursor.execute("SELECT DISTINCT genre FROM ebooks")
            genres = self.cursor.fetchall()
            self.cursor.execute("SELECT group_name FROM groups")
            groups = self.cursor.fetchall()
            self.cursor.execute("SELECT name FROM settings")
            themes = self.cursor.fetchall()
            self.cursor.execute("SELECT name FROM settings WHERE active=1")
            active_theme = self.cursor.fetchone()

        if ebooks is not None:
            for ebook in ebooks:
                if ebook[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(ebook[0])
                    self.ebooks_list.addItem(item)
            self.ebooks_num.setText(str(len(ebooks)))
        if authors is not None:
            for author in authors:
                if author[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(author[0])
                    self.authors_list.addItem(item)
            self.authors_num.setText(str(len(authors)))
        if folders is not None:
            for folder in folders:
                if folder[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(folder[0])
                    self.folders_list.addItem(item)
            self.folders_num.setText(str(len(folders)))
        if genres is not None:
            for genre in genres:
                if genre[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(genre[0])
                    self.genres_list.addItem(item)
            self.genres_num.setText(str(len(genres)))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        if groups is not None:
            for group in groups:
                if group[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(group[0])
                    self.groups_list.addItem(item)
            self.groups_num.setText(str(len(groups)))
        if themes is not None:
            for theme in themes:
                if theme[0] == '':
                    continue
                else:
                    item = QtWidgets.QListWidgetItem(theme[0])
                    self.themes_list.addItem(item)
            self.themes_num.setText(str(len(themes)))
        if active_theme is not None:
            self.active_theme.setText(active_theme[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.ebooks_num_label.setText(_translate("Dialog", "Number of Ebooks"))
        self.folders_num_label.setText(_translate("Dialog", "Number of Folders"))
        self.authors_num_label.setText(_translate("Dialog", "Number of Authors"))
        self.genres_num_label.setText(_translate("Dialog", "Number of Genres"))
        self.themes_num_label.setText(_translate("Dialog", "Number of Themes"))
        self.groups_num_label.setText(_translate("Dialog", "Number of Groups"))
        self.active_theme_label.setText(_translate("Dialog", "Active Theme"))
        self.ebooks_label.setText(_translate("Dialog", "Ebooks"))
        self.folders_label.setText(_translate("Dialog", "Folders"))
        self.authors_label.setText(_translate("Dialog", "Authors"))
        self.genres_label.setText(_translate("Dialog", "Genres"))
        self.groups_label.setText(_translate("Dialog", "Groups"))
        self.themes_label.setText(_translate("Dialog", "Themes"))
