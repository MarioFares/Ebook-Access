# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import os.path
import sqlite3
from glob import glob
from math import floor
from pathlib import Path
from time import sleep

import PyPDF2 as pdf
from PyQt5 import QtCore, QtGui, QtWidgets

from feedback import FeedbackDialog
from info import InfoDialog
from manual import ManualDialog
from settings import SettingsDialog
from user_settings import UserSettingsDialog


# noinspection PyBroadException
# noinspection PyPep8Naming,PyShadowingNames,PyAttributeOutsideInit,PyArgumentList,PyUnresolvedReferences
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.SORT = 0
        self.splash = QtWidgets.QSplashScreen(self)
        self.splash.setFixedSize(691, 301)
        # center the splash screen
        qr = self.splash.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.splash.move(qr.topLeft())
        # center
        self.frame = QtWidgets.QFrame(self.splash)
        self.frame.setFixedSize(691, 301)
        self.frame.setStyleSheet("background-color: black;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 671, 101))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: black;\n"
                                 "color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 250, 395, 51))
        font = QtGui.QFont()
        font.setFamily("garamond")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: black;\n"
                                   "color: red;\n"
                                   "font-family: garamond;")
        self.label_2.setObjectName("label_2")
        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        self.progress_bar.setGeometry(QtCore.QRect(80, 180, 533, 23))
        self.progress_bar.setStyleSheet("QProgressBar{\n"
                                        "background-color: black;\n"
                                        "border: 1px solid black;\n"
                                        "color: black;\n"
                                        "text-align: right;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: white;\n"
                                        "}")
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progressBar")
        self.label.setText('Ebook Access')
        self.label_2.setText('MarioKnight Technologies')
        QtCore.QMetaObject.connectSlotsByName(self.splash)
        self.splash.show()
        counter = 0
        while counter < 3:
            # time.sleep(0.00001)
            self.progress_bar.setValue(int(floor((counter / 3) * 100)))
            counter += 0.000004
        sleep(2)
        self.splash.close()
        # ! Menu Begin
        self.main_menu = QtWidgets.QMainWindow.menuBar(MainWindow)
        self.file_menu = self.main_menu.addMenu('&File')
        self.edit_menu = self.main_menu.addMenu('Edit')
        self.search_menu = self.main_menu.addMenu('Search')
        self.tool_menu = self.main_menu.addMenu('Database')
        self.help_menu = self.main_menu.addMenu('Help')
        self.main_menu.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.open_act = QtWidgets.QAction(QtGui.QIcon('./Icons/open_file_icon.png'), '&Open File', self)
        self.open_act.setShortcut('Ctrl+O')
        self.open_act.setStatusTip('Open File')
        self.open_act.triggered.connect(lambda: self.open_file())
        self.file_menu.addAction(self.open_act)
        self.add_file_act = QtWidgets.QAction(QtGui.QIcon('./Icons/add_book_icon.png'), '&Add File', self)
        self.add_file_act.setShortcut('Ctrl+A')
        self.add_file_act.setStatusTip('Add File')
        self.add_file_act.triggered.connect(lambda: self.find_path())
        self.file_menu.addAction(self.add_file_act)
        self.search_file_act = QtWidgets.QAction(QtGui.QIcon('./Icons/search_icon.png'), '&Search Files', self)
        self.search_file_act.setShortcut('Ctrl+S')
        self.search_file_act.setStatusTip('Search Files')
        self.search_file_act.triggered.connect(lambda: self.show_books(''))
        self.search_menu.addAction(self.search_file_act)
        self.clear_search_act = QtWidgets.QAction(QtGui.QIcon('./Icons/clear_search icon.png'), '&Clear Search', self)
        self.clear_search_act.setShortcut('Ctrl+C')
        self.clear_search_act.setStatusTip('Clear Search')
        self.clear_search_act.triggered.connect(lambda: self.clear_books())
        self.search_menu.addAction(self.clear_search_act)
        self.add_folder_act = QtWidgets.QAction(QtGui.QIcon('./Icons/add_folder_icon.png'), '&Add Folder', self)
        self.add_folder_act.setShortcut('Ctrl+F')
        self.add_folder_act.setStatusTip('Add Folder')
        self.add_folder_act.triggered.connect(lambda: self.add_folder())
        self.edit_menu.addAction(self.add_folder_act)
        self.add_genre_act = QtWidgets.QAction(QtGui.QIcon('./Icons/add_new_icon.png'), '&Add Genre', self)
        self.add_genre_act.setShortcut('Ctrl+G')
        self.add_genre_act.setStatusTip('Add Genre')
        self.add_genre_act.triggered.connect(lambda: self.add_genre())
        self.edit_menu.addAction(self.add_genre_act)
        self.add_author_act = QtWidgets.QAction(QtGui.QIcon('./Icons/add_user_icon.png'), '&Add Author', self)
        self.add_author_act.setStatusTip('Add Author')
        self.add_author_act.triggered.connect(lambda: self.add_author())
        self.edit_menu.addAction(self.add_author_act)
        self.add_group_act = QtWidgets.QAction(QtGui.QIcon('./Icons/add_collection_icon.png'), '&Add Group', self)
        self.add_group_act.setStatusTip('Add Group')
        self.add_group_act.triggered.connect(lambda: self.add_group_dialog())
        self.edit_menu.addAction(self.add_group_act)
        self.edit_menu.addSeparator()
        self.clear_entries_act = QtWidgets.QAction(QtGui.QIcon('./Icons/clear_icon.png'), '&Clear Entries', self)
        self.clear_entries_act.setStatusTip('Clear Entries')
        self.clear_entries_act.setShortcut('Ctrl+E')
        self.clear_entries_act.triggered.connect(lambda: self.clear_entries())
        self.edit_menu.addAction(self.clear_entries_act)
        self.sqlite_browser_act = QtWidgets.QAction(QtGui.QIcon('./Icons/database_icon.png'), '&SQLite DB Browser',
                                                    self)
        self.sqlite_browser_act.setStatusTip(
            'Open SQLite Database Browser to manipulate database and tables. For developers '
            'only.')
        self.sqlite_browser_act.setShortcut('Ctrl+D')
        self.sqlite_browser_act.triggered.connect(lambda: self.open_sqlite())
        self.tool_menu.addAction(self.sqlite_browser_act)
        self.edit_menu.addSeparator()
        self.reset_ebooks_act = QtWidgets.QAction('&Reset Ebooks Table', self)
        self.reset_ebooks_act.setStatusTip('Reset the ebooks table completely. Your groups will not be touched.')
        self.reset_ebooks_act.triggered.connect(lambda: self.reset_ebooks_table())
        self.edit_menu.addAction(self.reset_ebooks_act)
        self.reset_groups_act = QtWidgets.QAction('&Reset Groups Table', self)
        self.reset_groups_act.setStatusTip('Reset the groups table completely. No ebooks will be deleted.')
        self.reset_groups_act.triggered.connect(lambda: self.reset_groups_table())
        self.edit_menu.addAction(self.reset_groups_act)
        self.reset_all_act = QtWidgets.QAction('&Reset Database', self)
        self.reset_all_act.setStatusTip("Reset everything including ebooks and tables.")
        self.reset_all_act.triggered.connect(lambda: self.reset_ebooks_table())
        self.reset_all_act.triggered.connect(lambda: self.reset_groups_table())
        self.reset_all_act.triggered.connect(lambda: self.clear_entries())
        self.reset_themes_act = QtWidgets.QAction('&Reset Themes', self)
        self.reset_themes_act.setStatusTip("Reset all themes")
        self.reset_themes_act.triggered.connect(lambda: self.reset_themes())
        self.clean_ebooks_act = QtWidgets.QAction('&Clean Ebooks', self)
        self.clean_ebooks_act.setStatusTip("Remove all ebooks which have broken path or do not exist.")
        self.clean_ebooks_act.triggered.connect(lambda: self.clean_ebooks_dialog())
        self.edit_menu.addAction(self.reset_themes_act)
        self.edit_menu.addAction(self.reset_all_act)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.clean_ebooks_act)
        self.user_manual_act = QtWidgets.QAction(QtGui.QIcon('./Icons/about_icon.png'), '&User Manual', self)
        self.user_manual_act.setStatusTip('User Manual')
        self.user_manual_act.triggered.connect(lambda: self.show_user_manual())
        self.help_menu.addAction(self.user_manual_act)
        self.user_settings_act = QtWidgets.QAction(QtGui.QIcon('./Icons/user_settings_icon.png'), '&User Settings',
                                                   self)
        self.user_settings_act.setStatusTip('User Settings')
        self.user_settings_act.triggered.connect(lambda: self.show_user_settings())
        self.help_menu.addAction(self.user_settings_act)
        self.application_settings_act = QtWidgets.QAction(QtGui.QIcon('./Icons/settings_icon.png'), '&Application '
                                                                                                    'Settings',
                                                          self)
        self.application_settings_act.setStatusTip('Application Settings')
        self.application_settings_act.triggered.connect(lambda: self.show_app_settings())
        self.help_menu.addAction(self.application_settings_act)
        self.application_information_act = QtWidgets.QAction(QtGui.QIcon('./Icons/info_icon.png'),
                                                             '&Application Information',
                                                             self)
        self.application_information_act.setStatusTip('Application Information')
        self.application_information_act.triggered.connect(lambda: self.app_info())
        self.help_menu.addAction(self.application_information_act)
        self.help_menu.addSeparator()
        self.feedback_act = QtWidgets.QAction(QtGui.QIcon('./Icons/feedback_icon.png'), '&Submit Feedback', self)
        self.feedback_act.setStatusTip('Submit Feedback')
        self.feedback_act.triggered.connect(lambda: self.show_feedback())
        self.help_menu.addAction(self.feedback_act)
        # ! Menu End
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 530))
        MainWindow.setMaximumSize(QtCore.QSize(850, 530))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/book_window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.titleHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.titleHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleHorizontalLayout.setObjectName("titleHorizontalLayout")
        self.window_title_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(23)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_title_label.sizePolicy().hasHeightForWidth())
        self.window_title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(True)
        self.window_title_label.setFont(font)
        self.window_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.window_title_label.setObjectName("window_title_label")
        self.titleHorizontalLayout.addWidget(self.window_title_label)
        self.classification_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.classification_groupBox.setGeometry(QtCore.QRect(40, 50, 292, 156))
        self.classification_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.classification_groupBox.setFlat(True)
        self.classification_groupBox.setObjectName("classification_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.classification_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.class_folder_horizontalLayout = QtWidgets.QHBoxLayout()
        self.class_folder_horizontalLayout.setObjectName("class_folder_horizontalLayout")
        self.class_folder_label = QtWidgets.QLabel(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_folder_label.sizePolicy().hasHeightForWidth())
        self.class_folder_label.setSizePolicy(sizePolicy)
        self.class_folder_label.setObjectName("class_folder_label")
        self.class_folder_horizontalLayout.addWidget(self.class_folder_label)
        self.class_folder_comboBox = QtWidgets.QComboBox(self.classification_groupBox)
        self.class_folder_comboBox.setObjectName("class_folder_comboBox")
        self.class_folder_horizontalLayout.addWidget(self.class_folder_comboBox)
        self.add_folder_pushButton = QtWidgets.QPushButton(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_folder_pushButton.sizePolicy().hasHeightForWidth())
        self.add_folder_pushButton.setSizePolicy(sizePolicy)
        self.add_folder_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_folder_pushButton.setText("")
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("Icons/add_folder_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_folder_pushButton.setIcon(self.icon1)
        self.add_folder_pushButton.setFlat(True)
        self.add_folder_pushButton.setObjectName("add_folder_pushButton")
        self.class_folder_horizontalLayout.addWidget(self.add_folder_pushButton)
        self.verticalLayout.addLayout(self.class_folder_horizontalLayout)
        self.class_genre_horizontalLayout = QtWidgets.QHBoxLayout()
        self.class_genre_horizontalLayout.setObjectName("class_genre_horizontalLayout")
        self.class_genre_label = QtWidgets.QLabel(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_genre_label.sizePolicy().hasHeightForWidth())
        self.class_genre_label.setSizePolicy(sizePolicy)
        self.class_genre_label.setObjectName("class_genre_label")
        self.class_genre_horizontalLayout.addWidget(self.class_genre_label)
        self.class_genre_comboBox = QtWidgets.QComboBox(self.classification_groupBox)
        # self.class_genre_comboBox.setMinimumSize(QtCore.QSize(196, 20))
        self.class_genre_comboBox.setObjectName("class_genre_comboBox")
        self.class_genre_horizontalLayout.addWidget(self.class_genre_comboBox)
        self.add_genre_pushButton = QtWidgets.QPushButton(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_genre_pushButton.sizePolicy().hasHeightForWidth())
        self.add_genre_pushButton.setSizePolicy(sizePolicy)
        self.add_genre_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_genre_pushButton.setText("")
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("Icons/add_new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_genre_pushButton.setIcon(self.icon2)
        self.add_genre_pushButton.setFlat(True)
        self.add_genre_pushButton.setObjectName("add_genre_pushButton")
        self.class_genre_horizontalLayout.addWidget(self.add_genre_pushButton)
        self.verticalLayout.addLayout(self.class_genre_horizontalLayout)
        self.class_author_horizontalLayout = QtWidgets.QHBoxLayout()
        self.class_author_horizontalLayout.setObjectName("class_author_horizontalLayout")
        self.class_author_label = QtWidgets.QLabel(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_author_label.sizePolicy().hasHeightForWidth())
        self.class_author_label.setSizePolicy(sizePolicy)
        self.class_author_label.setObjectName("class_author_label")
        self.class_author_horizontalLayout.addWidget(self.class_author_label)
        self.class_author_comboBox = QtWidgets.QComboBox(self.classification_groupBox)
        self.class_author_comboBox.setObjectName("class_author_comboBox")
        self.class_author_horizontalLayout.addWidget(self.class_author_comboBox)
        self.add_author_pushButton = QtWidgets.QPushButton(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_author_pushButton.sizePolicy().hasHeightForWidth())
        self.add_author_pushButton.setSizePolicy(sizePolicy)
        self.add_author_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_author_pushButton.setText("")
        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap("Icons/add_user_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_author_pushButton.setIcon(self.icon3)
        self.add_author_pushButton.setFlat(True)
        self.add_author_pushButton.setObjectName("add_author_pushButton")
        self.class_author_horizontalLayout.addWidget(self.add_author_pushButton)
        self.verticalLayout.addLayout(self.class_author_horizontalLayout)
        self.class_group_horizontalLayout = QtWidgets.QHBoxLayout()
        self.class_group_horizontalLayout.setObjectName("class_group_horizontalLayout")
        self.class_group_label = QtWidgets.QLabel(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_group_label.sizePolicy().hasHeightForWidth())
        self.class_group_label.setSizePolicy(sizePolicy)
        self.class_group_label.setObjectName("class_group_label")
        self.class_group_horizontalLayout.addWidget(self.class_group_label)
        self.class_group_comboBox = QtWidgets.QComboBox(self.classification_groupBox)
        self.class_group_comboBox.setObjectName("class_group_comboBox")
        self.class_group_horizontalLayout.addWidget(self.class_group_comboBox)
        self.add_group_pushButton = QtWidgets.QPushButton(self.classification_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_group_pushButton.sizePolicy().hasHeightForWidth())
        self.add_group_pushButton.setSizePolicy(sizePolicy)
        self.add_group_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_group_pushButton.setText("")
        self.icon4 = QtGui.QIcon()
        self.icon4.addPixmap(QtGui.QPixmap("Icons/add_collection_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_group_pushButton.setIcon(self.icon4)
        self.add_group_pushButton.setFlat(True)
        self.add_group_pushButton.setObjectName("add_group_pushButton")
        self.class_group_horizontalLayout.addWidget(self.add_group_pushButton)
        self.verticalLayout.addLayout(self.class_group_horizontalLayout)
        self.book_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.book_groupBox.setGeometry(QtCore.QRect(40, 200, 292, 151))
        self.book_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.book_groupBox.setFlat(True)
        self.book_groupBox.setObjectName("book_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.book_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.book_name_horizontalLayout = QtWidgets.QHBoxLayout()
        self.book_name_horizontalLayout.setObjectName("book_name_horizontalLayout")
        self.book_name_label = QtWidgets.QLabel(self.book_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_name_label.sizePolicy().hasHeightForWidth())
        self.book_name_label.setSizePolicy(sizePolicy)
        self.book_name_label.setObjectName("book_name_label")
        self.book_name_horizontalLayout.addWidget(self.book_name_label)
        self.book_name_lineEdit = QtWidgets.QLineEdit(self.book_groupBox)
        self.book_name_lineEdit.setObjectName("book_name_lineEdit")
        self.book_name_horizontalLayout.addWidget(self.book_name_lineEdit)
        self.verticalLayout_2.addLayout(self.book_name_horizontalLayout)
        self.book_author_horizontalLayout = QtWidgets.QHBoxLayout()
        self.book_author_horizontalLayout.setObjectName("book_author_horizontalLayout")
        self.book_author_label = QtWidgets.QLabel(self.book_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_author_label.sizePolicy().hasHeightForWidth())
        self.book_author_label.setSizePolicy(sizePolicy)
        self.book_author_label.setObjectName("book_author_label")
        self.book_author_horizontalLayout.addWidget(self.book_author_label)
        self.book_author_lineEdit = QtWidgets.QLineEdit(self.book_groupBox)
        self.book_author_lineEdit.setObjectName("book_author_lineEdit")
        self.book_author_horizontalLayout.addWidget(self.book_author_lineEdit)
        self.verticalLayout_2.addLayout(self.book_author_horizontalLayout)
        self.book_genre_horizontalLayout = QtWidgets.QHBoxLayout()
        self.book_genre_horizontalLayout.setObjectName("book_genre_horizontalLayout")
        self.book_genre_label = QtWidgets.QLabel(self.book_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_genre_label.sizePolicy().hasHeightForWidth())
        self.book_genre_label.setSizePolicy(sizePolicy)
        self.book_genre_label.setObjectName("book_genre_label")
        self.book_genre_horizontalLayout.addWidget(self.book_genre_label)
        self.book_genre_lineEdit = QtWidgets.QLineEdit(self.book_groupBox)
        self.book_genre_lineEdit.setObjectName("book_genre_lineEdit")
        self.book_genre_horizontalLayout.addWidget(self.book_genre_lineEdit)
        self.verticalLayout_2.addLayout(self.book_genre_horizontalLayout)
        self.book_path_horizontalLayout = QtWidgets.QHBoxLayout()
        self.book_path_horizontalLayout.setObjectName("book_path_horizontalLayout")
        self.book_path_label = QtWidgets.QLabel(self.book_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_path_label.sizePolicy().hasHeightForWidth())
        self.book_path_label.setSizePolicy(sizePolicy)
        self.book_path_label.setObjectName("book_path_label")
        self.book_path_horizontalLayout.addWidget(self.book_path_label)
        self.book_path_lineEdit = QtWidgets.QLineEdit(self.book_groupBox)
        self.book_path_lineEdit.setObjectName("book_path_lineEdit")
        self.book_path_horizontalLayout.addWidget(self.book_path_lineEdit)
        self.book_path_pushButton = QtWidgets.QPushButton(self.book_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_path_pushButton.sizePolicy().hasHeightForWidth())
        self.book_path_pushButton.setSizePolicy(sizePolicy)
        self.book_path_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.book_path_pushButton.setFont(font)
        self.book_path_pushButton.setObjectName("book_path_pushButton")
        self.book_path_horizontalLayout.addWidget(self.book_path_pushButton)
        self.verticalLayout_2.addLayout(self.book_path_horizontalLayout)
        self.add_book_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_book_pushButton.setGeometry(QtCore.QRect(330, 260, 41, 38))
        self.add_book_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_book_pushButton.setText("")
        self.add_books_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_books_pushButton.setGeometry(QtCore.QRect(330, 300, 41, 38))
        self.add_books_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_books_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/add_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_book_pushButton.setIcon(icon5)
        self.add_book_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.add_book_pushButton.setFlat(True)
        self.add_book_pushButton.setObjectName("add_book_pushButton")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("Icons/add_books_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_books_pushButton.setIcon(icon30)
        self.add_books_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.add_books_pushButton.setFlat(True)
        self.add_books_pushButton.setObjectName("add_books_pushButton")
        self.book_details_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.book_details_groupBox.setGeometry(QtCore.QRect(380, 380, 461, 110))
        self.book_details_groupBox.setTitle("")
        self.book_details_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.book_details_groupBox.setFlat(True)
        self.book_details_groupBox.setCheckable(False)
        self.book_details_groupBox.setObjectName("book_details_groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.book_details_groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 221, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.det_verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.det_verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.det_verticalLayout1.setObjectName("det_verticalLayout1")
        self.det_name_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_name_horizontalLayout.setObjectName("det_name_horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.det_name_horizontalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.det_name_horizontalLayout.addWidget(self.label_10)
        self.det_verticalLayout1.addLayout(self.det_name_horizontalLayout)
        self.det_author_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_author_horizontalLayout.setObjectName("det_author_horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.det_author_horizontalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.det_author_horizontalLayout.addWidget(self.label_12)
        self.det_verticalLayout1.addLayout(self.det_author_horizontalLayout)
        self.det_genre_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_genre_horizontalLayout.setObjectName("det_genre_horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.det_genre_horizontalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.det_genre_horizontalLayout.addWidget(self.label_14)
        self.det_verticalLayout1.addLayout(self.det_genre_horizontalLayout)
        self.det_path_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_path_horizontalLayout.setObjectName("det_path_horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.det_path_horizontalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.det_path_horizontalLayout.addWidget(self.label_16)
        self.det_verticalLayout1.addLayout(self.det_path_horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.book_details_groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 10, 221, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.det_verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.det_verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.det_verticalLayout2.setObjectName("det_verticalLayout2")
        self.det_pages_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_pages_horizontalLayout.setObjectName("det_pages_horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.det_pages_horizontalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.det_pages_horizontalLayout.addWidget(self.label_18)
        self.det_verticalLayout2.addLayout(self.det_pages_horizontalLayout)
        self.det_size_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_size_horizontalLayout.setObjectName("det_size_horizontalLayout")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.det_size_horizontalLayout.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.det_size_horizontalLayout.addWidget(self.label_20)
        self.det_verticalLayout2.addLayout(self.det_size_horizontalLayout)
        self.det_date_horizontalLayout = QtWidgets.QHBoxLayout()
        self.det_date_horizontalLayout.setObjectName("det_date_horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.det_verticalLayout2.addLayout(self.det_date_horizontalLayout)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.configuration_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.configuration_groupBox.setGeometry(QtCore.QRect(40, 370, 291, 111))
        self.configuration_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.configuration_groupBox.setFlat(True)
        self.configuration_groupBox.setObjectName("configuration_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.configuration_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.config_horizontalLayout = QtWidgets.QHBoxLayout()
        self.config_horizontalLayout.setObjectName("config_horizontalLayout")
        self.user_settings_pushButton = QtWidgets.QPushButton(self.configuration_groupBox)
        self.user_settings_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_settings_pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/user_settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_settings_pushButton.setIcon(icon6)
        self.user_settings_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.user_settings_pushButton.setFlat(True)
        self.user_settings_pushButton.setObjectName("user_settings_pushButton")
        self.config_horizontalLayout.addWidget(self.user_settings_pushButton)
        self.app_settings_pushButton = QtWidgets.QPushButton(self.configuration_groupBox)
        self.app_settings_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_settings_pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_settings_pushButton.setIcon(icon7)
        self.app_settings_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.app_settings_pushButton.setFlat(True)
        self.app_settings_pushButton.setObjectName("app_settings_pushButton")
        self.config_horizontalLayout.addWidget(self.app_settings_pushButton)
        self.info_pushButton = QtWidgets.QPushButton(self.configuration_groupBox)
        self.info_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_pushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_pushButton.setIcon(icon8)
        self.info_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.info_pushButton.setFlat(True)
        self.info_pushButton.setObjectName("info_pushButton")
        self.config_horizontalLayout.addWidget(self.info_pushButton)
        self.verticalLayout_3.addLayout(self.config_horizontalLayout)
        self.book_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.book_listWidget.setGeometry(QtCore.QRect(380, 81, 461, 281))  # 370, 60, 461, 301
        self.book_listWidget.setItemAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.book_listWidget.setObjectName("book_listWidget")
        # Search
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setGeometry(380, 57, 410, 20)
        self.search_bar.setObjectName("search_bar")

        self.search_string_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.search_string_pushButton.setGeometry(QtCore.QRect(796, 56, 25, 21))
        self.search_string_pushButton.setObjectName("search_string_pushButton")
        self.search_string_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_string_pushButton.setText("")
        self.search_string_pushButton.setFlat(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("Icons/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_string_pushButton.setIcon(icon25)
        self.search_string_pushButton.setIconSize(QtCore.QSize(15, 15))

        self.sort_search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sort_search_pushButton.setGeometry(QtCore.QRect(820, 56, 25, 21))
        self.sort_search_pushButton.setObjectName("sort_search_pushButton")
        self.sort_search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sort_search_pushButton.setText("")
        self.sort_search_pushButton.setFlat(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("Icons/sort_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sort_search_pushButton.setIcon(icon24)
        self.sort_search_pushButton.setIconSize(QtCore.QSize(15, 15))

        self.clear_search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clear_search_pushButton.setGeometry(QtCore.QRect(330, 140, 41, 38))
        self.clear_search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_search_pushButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/clear_search icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_search_pushButton.setIcon(icon9)
        self.clear_search_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.clear_search_pushButton.setFlat(True)
        self.clear_search_pushButton.setObjectName("clear_search_pushButton")
        self.search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.search_pushButton.setGeometry(QtCore.QRect(330, 90, 41, 38))
        self.search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_pushButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_pushButton.setIcon(icon10)
        self.search_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.search_pushButton.setFlat(True)
        self.search_pushButton.setObjectName("search_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.statusBar.setObjectName("statusBar")
        # ! Database Begin
        self.connect = sqlite3.connect('ebook.db')
        self.cursor = self.connect.cursor()
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS ebooks (
                                                                        name text,
                                                                        author text,
                                                                        genre text,
                                                                        path text,
                                                                        folder TEXT
                                                                        )
                                                                        """)
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS groups (
                                                                        group_name TEXT NOT null
          
                                                                        )""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS ebooks_dist (
                                                                        group_id INTEGER not null,
                                                                        ebook_id INTEGER not null,
                                                                        primary key (group_id, ebook_id)
                                                                        )""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS settings (
                                                                        name text not null PRIMARY KEY,
                                                                        label_font text not null,
                                                                        label_color text not null,
                                                                        label_font_color text not null,
                                                                        title_font text not null,
                                                                        title_color text not null,
                                                                        title_font_color text not null,
                                                                        menubar_font text not null,
                                                                        menubar_color text not null,
                                                                        menubar_font_color text not null,
                                                                        statusbar_font text not null,
                                                                        statusbar_color text not null,
                                                                        statusbar_font_color text not null,
                                                                        button_font text not null,
                                                                        button_color text not null,
                                                                        button_radius int not null,
                                                                        button_font_color text not null,
                                                                        inputbox_font text not null,
                                                                        inputbox_color text not null,
                                                                        inputbox_radius int not null,
                                                                        inputbox_font_color text not null,
                                                                        combobox_font text not null,
                                                                        combobox_color text not null,
                                                                        combobox_radius int not null,
                                                                        combobox_font_color text not null,
                                                                        bg_color text not null,
                                                                        active int not null
                                                                         )""")
        # ! Database End
        # ! ComboBoxes Setup Begin
        self.settings_dialog = SettingsDialog(MainWindow, self.main_menu, self.statusBar, self.window_title_label)
        self.settings_dialog.setupUi(QtWidgets.QDialog())
        self.refresh_authors()
        self.refresh_folders()
        self.refresh_genres()
        self.refresh_groups()
        self.settings_dialog.apply_active_theme()
        # ! ComboBoxes Setup End
        # ! Button Functions Begin
        self.book_path_pushButton.clicked.connect(lambda: self.find_path())
        self.search_pushButton.clicked.connect(lambda: self.show_books(""))
        self.clear_search_pushButton.clicked.connect(lambda: self.clear_books())
        self.search_string_pushButton.clicked.connect(
            lambda: self.show_books(name=("%" + self.search_bar.text() + "%")))
        self.add_folder_pushButton.clicked.connect(lambda: self.add_class_dialog("Folder"))
        self.add_genre_pushButton.clicked.connect(lambda: self.add_class_dialog("Genre"))
        self.add_author_pushButton.clicked.connect(lambda: self.add_class_dialog("Author"))
        self.add_group_pushButton.clicked.connect(lambda: self.add_class_dialog("Group"))
        self.add_books_pushButton.clicked.connect(lambda: self.add_class_dialog("Books"))
        self.add_book_pushButton.clicked.connect(lambda: self.add_book(name=self.book_name_lineEdit.text(),
                                                                       author=self.book_author_lineEdit.text(),
                                                                       path=self.book_path_lineEdit.text(),
                                                                       genre=self.book_genre_lineEdit.text()))
        self.book_listWidget.itemClicked.connect(lambda: self.show_book_details())
        self.info_pushButton.clicked.connect(lambda: self.app_info())
        self.sort_search_pushButton.clicked.connect(lambda: self.sort_search())
        self.app_settings_pushButton.clicked.connect(lambda: self.show_app_settings())
        self.user_settings_pushButton.clicked.connect(lambda: self.show_user_settings())
        # ! Button Functions END
        self.book_listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.book_listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.right_menu_show)
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ebook Access"))
        self.window_title_label.setText(_translate("MainWindow", "Ebook Access"))
        self.classification_groupBox.setStatusTip(_translate("MainWindow", "Choose your book based on certain "
                                                                           "criteria..."))
        self.classification_groupBox.setTitle(_translate("MainWindow", "Classification"))
        self.class_folder_label.setText(_translate("MainWindow", "Folder"))
        self.add_folder_pushButton.setToolTip(_translate("MainWindow", "Add Folder"))
        self.add_folder_pushButton.setStatusTip(_translate("MainWindow", "Add Folder"))
        self.class_genre_label.setText(_translate("MainWindow", "Genre "))
        self.add_genre_pushButton.setToolTip(_translate("MainWindow", "Add Genre"))
        self.add_genre_pushButton.setStatusTip(_translate("MainWindow", "Add Genre"))
        self.search_string_pushButton.setToolTip(_translate("MainWindow", "Search String"))
        self.search_string_pushButton.setStatusTip(_translate("MainWindow", "Search string..."))
        self.sort_search_pushButton.setToolTip(_translate("MainWindow", "Toggle Sort Ebooks"))
        self.sort_search_pushButton.setStatusTip(_translate("MainWindow", "Toggle Sort Ebooks"))
        self.class_author_label.setText(_translate("MainWindow", "Author"))
        self.add_author_pushButton.setToolTip(_translate("MainWindow", "Add Author"))
        self.add_author_pushButton.setStatusTip(_translate("MainWindow", "Add Author"))
        self.class_group_label.setText(_translate("MainWindow", "Group "))
        self.search_bar.setToolTip(_translate("MainWindow", "Input string to search..."))
        self.search_bar.setStatusTip(_translate("MainWindow", "Input string to search..."))
        self.add_group_pushButton.setToolTip(_translate("MainWindow", "Add Group"))
        self.add_group_pushButton.setStatusTip(_translate("MainWindow", "Add Group"))
        self.book_groupBox.setStatusTip(_translate("MainWindow", "Add book by specifying input fields..."))
        self.book_groupBox.setTitle(_translate("MainWindow", "Book"))
        self.book_name_label.setText(_translate("MainWindow", "Name  "))
        self.book_name_lineEdit.setStatusTip(_translate("MainWindow", "Name of new book..."))
        self.book_author_label.setText(_translate("MainWindow", "Author"))
        self.book_author_lineEdit.setStatusTip(_translate("MainWindow", "Author of new book..."))
        self.book_genre_label.setText(_translate("MainWindow", "Genre "))
        self.book_genre_lineEdit.setStatusTip(_translate("MainWindow", "Genre of new book..."))
        self.book_path_label.setText(_translate("MainWindow", "Path    "))
        self.book_path_lineEdit.setStatusTip(_translate("MainWindow", "Path to new book..."))
        self.book_path_pushButton.setToolTip(_translate("MainWindow", "Open file path..."))
        self.book_path_pushButton.setStatusTip(_translate("MainWindow", "Find file..."))
        self.book_path_pushButton.setText(_translate("MainWindow", "..."))
        self.add_book_pushButton.setToolTip(_translate("MainWindow", "Add Book"))
        self.add_book_pushButton.setStatusTip(_translate("MainWindow", "Add Book"))
        self.add_books_pushButton.setToolTip(_translate("MainWindow", "Add Books in a Folder"))
        self.add_books_pushButton.setStatusTip(_translate("MainWindow", "Add Books in a Folder"))
        self.book_details_groupBox.setStatusTip(_translate("MainWindow", "View selected book details..."))
        self.label_9.setText(_translate("MainWindow", "Name:"))
        self.label_11.setText(_translate("MainWindow", "Author:"))
        self.label_13.setText(_translate("MainWindow", "Genre:"))
        self.label_15.setText(_translate("MainWindow", "Path:"))
        self.label_17.setText(_translate("MainWindow", "Pages:"))
        self.label_19.setText(_translate("MainWindow", "Size:"))
        self.configuration_groupBox.setStatusTip(_translate("MainWindow", "Choose your book based on certain "
                                                                          "criteria..."))
        self.configuration_groupBox.setTitle(_translate("MainWindow", "Configuration"))
        self.user_settings_pushButton.setToolTip(_translate("MainWindow", "User Settings"))
        self.user_settings_pushButton.setStatusTip(_translate("MainWindow", "User Settings"))
        self.app_settings_pushButton.setToolTip(_translate("MainWindow", "Application Settings"))
        self.app_settings_pushButton.setStatusTip(_translate("MainWindow", "Application Settings"))
        self.info_pushButton.setToolTip(_translate("MainWindow", "Information"))
        self.info_pushButton.setStatusTip(_translate("MainWindow", "Application Information"))
        self.book_listWidget.setStatusTip(_translate("MainWindow", "View Books"))
        self.book_listWidget.setSortingEnabled(True)
        self.clear_search_pushButton.setToolTip(_translate("MainWindow", "Clear Search"))
        self.clear_search_pushButton.setStatusTip(_translate("MainWindow", "Clear Search"))
        self.search_pushButton.setToolTip(_translate("MainWindow", "Search"))
        self.search_pushButton.setStatusTip(_translate("MainWindow", "Search"))

    def show_feedback(self):
        dialog = QtWidgets.QDialog(self)
        FeedbackDialog().setupUi(dialog)
        dialog.exec_()

    def show_user_settings(self):
        dialog = QtWidgets.QDialog(self)
        UserSettingsDialog().setupUi(dialog)
        dialog.exec_()

    def show_user_manual(self):
        dialog = QtWidgets.QDialog(self)
        ManualDialog().setupUi(dialog)
        dialog.exec_()

    def reset_themes(self):
        with self.connect:
            self.cursor.execute("DELETE FROM settings")

    def show_app_settings(self):
        self.dialog = QtWidgets.QDialog(self)
        self.settings_dialog.setupUi(self.dialog)
        self.dialog.exec_()

    def right_menu_show(self):
        rightMenu = QtWidgets.QMenu(self.book_listWidget)
        openEbook = QtWidgets.QAction("&Open Ebook", parent=self, triggered=lambda: self.open_ebook_listItem())
        rightMenu.addAction(openEbook)
        deleteEbook = QtWidgets.QAction("&Delete Ebook", parent=self, triggered=lambda: self.delete_ebook_listItem())
        rightMenu.addAction(deleteEbook)
        updateAction = QtWidgets.QAction("&Update Ebook", parent=self, triggered=lambda: self.update_ebook_dialog())
        rightMenu.addAction(updateAction)
        addToGroupAction = QtWidgets.QAction("&Add to Group", parent=self,
                                             triggered=lambda: self.add_item_to_group_dialog())
        rightMenu.addAction(addToGroupAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    def refresh_folders(self):
        self.class_folder_comboBox.clear()
        self.class_folder_comboBox.addItem('')
        with self.connect:
            self.cursor.execute("SELECT DISTINCT folder from ebooks")
            folders = self.cursor.fetchall()
            for folder in folders:
                self.class_folder_comboBox.addItem(folder[0])

    def refresh_authors(self):
        self.class_author_comboBox.clear()
        self.class_author_comboBox.addItem('')
        with self.connect:
            self.cursor.execute("SELECT DISTINCT author from ebooks")
            authors = self.cursor.fetchall()
            for author in authors:
                self.class_author_comboBox.addItem(author[0])

    def refresh_genres(self):
        self.class_genre_comboBox.clear()
        self.class_genre_comboBox.addItem('')
        with self.connect:
            self.cursor.execute("SELECT DISTINCT genre from ebooks")
            genres = self.cursor.fetchall()
            for genre in genres:
                self.class_genre_comboBox.addItem(genre[0])

    def refresh_groups(self):
        self.class_group_comboBox.clear()
        self.class_group_comboBox.clear()
        self.class_group_comboBox.addItem('')
        with self.connect:
            self.cursor.execute("SELECT DISTINCT group_name from groups")
            groups = self.cursor.fetchall()
            for group in groups:
                self.class_group_comboBox.addItem(group[0])

    def clear_entries(self):
        self.book_author_lineEdit.clear()
        self.book_genre_lineEdit.clear()
        self.book_name_lineEdit.clear()
        self.book_path_lineEdit.clear()

    def update_ebook_dialog(self):
        old_name = self.book_listWidget.currentItem().text()
        dialog = QtWidgets.QDialog()
        dialog.setStyleSheet(MainWindow.styleSheet())
        dialog.setWindowTitle('Update Ebook')
        pushBtn = QtWidgets.QPushButton(dialog)
        pushBtn.setText('Update')
        pushBtn.setGeometry(20, 170, 60, 30)
        self.nameLineEdit = QtWidgets.QLineEdit(dialog)
        self.authorLineEdit = QtWidgets.QLineEdit(dialog)
        self.genreLineEdit = QtWidgets.QLineEdit(dialog)
        self.folderLineEdit = QtWidgets.QLineEdit(dialog)
        self.pathLineEdit = QtWidgets.QLineEdit(dialog)
        nameLabel = QtWidgets.QLabel(dialog)
        nameLabel.setText('New Name')
        authorLabel = QtWidgets.QLabel(dialog)
        authorLabel.setText('New Author')
        genreLabel = QtWidgets.QLabel(dialog)
        genreLabel.setText('New Genre')
        folderLabel = QtWidgets.QLabel(dialog)
        folderLabel.setText('New Folder')
        pathLabel = QtWidgets.QLabel(dialog)
        pathLabel.setText('New Path')
        dialog.setFixedSize(520, 210)
        # dialog.move(400, 400)
        nameLabel.setGeometry(20, 20, 60, 20)
        self.nameLineEdit.setGeometry(100, 20, 400, 20)
        authorLabel.setGeometry(20, 50, 60, 20)
        self.authorLineEdit.setGeometry(100, 50, 400, 20)
        genreLabel.setGeometry(20, 80, 60, 20)
        self.genreLineEdit.setGeometry(100, 80, 400, 20)
        folderLabel.setGeometry(20, 110, 60, 20)
        self.folderLineEdit.setGeometry(100, 110, 400, 20)
        pathLabel.setGeometry(20, 140, 60, 20)
        self.pathLineEdit.setGeometry(100, 140, 400, 20)
        pushBtn.clicked.connect(lambda: self.update_ebook(old_name))
        with self.connect:
            self.cursor.execute("SELECT * FROM ebooks WHERE name=?", (old_name,))
            info = self.cursor.fetchone()
            self.nameLineEdit.setText(info[0])
            self.authorLineEdit.setText(info[1])
            self.genreLineEdit.setText(info[2])
            self.pathLineEdit.setText(info[3])
            self.folderLineEdit.setText(info[4])
        dialog.exec_()

    def update_ebook(self, old_name):
        newName = self.nameLineEdit.text()
        newAuthor = self.authorLineEdit.text()
        newGenre = self.genreLineEdit.text()
        newPath = self.pathLineEdit.text()
        newFolder = self.folderLineEdit.text()
        with self.connect:
            self.cursor.execute("UPDATE ebooks SET name=?, author=?, genre=?, folder=?, path=? WHERE name=?",
                                (newName, newAuthor, newGenre, newFolder, newPath, old_name))
        self.refresh_authors()
        self.refresh_folders()
        self.refresh_genres()
        self.refresh_groups()

    def clean_ebooks_dialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setStyleSheet(MainWindow.styleSheet())
        dialog.setFixedSize(310, 75)
        dialog.setWindowTitle('Clean Ebooks')
        self.cleaning_progress_bar = QtWidgets.QProgressBar(dialog)
        self.cleaning_progress_bar.setGeometry(10, 10, 300, 30)
        start_button = QtWidgets.QPushButton(dialog)
        start_button.setGeometry(120, 50, 50, 20)
        start_button.setText("Start")
        start_button.clicked.connect(lambda: self.clean_ebooks())
        dialog.exec_()

    def clean_ebooks(self):
        with self.connect:
            self.cursor.execute("SELECT path FROM ebooks")
            paths = self.cursor.fetchall()
            value = 0
            for path in paths:
                value += 1
                self.cleaning_progress_bar.setValue(int(floor((value / len(paths) * 100))))
                if os.path.exists(path[0]):
                    continue
                else:
                    self.cursor.execute("DELETE FROM ebooks WHERE path=?", (path[0],))
        self.refresh_authors()
        self.refresh_folders()
        self.refresh_genres()
        self.clear_books()

    def open_file(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "All files (*)")[0]
            os.startfile(file)
        except (OSError, AttributeError):
            self.error_box('Ebook path may not be incorrect.')

    def open_ebook_listItem(self):
        try:
            name = self.book_listWidget.currentItem().text()
            with self.connect:
                self.cursor.execute("SELECT path FROM ebooks WHERE name=?", (name,))
                path = self.cursor.fetchone()[0]
                os.startfile(path)
        except (OSError, AttributeError, FileNotFoundError):
            self.error_box('Ebook path may not be incorrect or you have not selected the item properly.')

    def delete_ebook_listItem(self):
        try:
            name = self.book_listWidget.currentItem().text()
            with self.connect:
                self.cursor.execute("DELETE FROM ebooks WHERE name=?", (name,))
            self.clear_books()
            self.refresh_genres()
            self.refresh_folders()
            self.refresh_authors()
            self.refresh_groups()
        except (OSError, AttributeError, FileNotFoundError):
            self.error_box('Seems an error has occurred.')

    def reset_ebooks_table(self):
        with self.connect:
            self.cursor.execute("DELETE FROM ebooks")
            self.cursor.execute("DELETE FROM ebooks_dist")
        self.refresh_authors()
        self.refresh_folders()
        self.refresh_genres()
        self.clear_books()

    def reset_groups_table(self):
        with self.connect:
            self.cursor.execute("DELETE FROM groups")
            self.cursor.execute("DELETE FROM ebooks_dist")
        self.refresh_groups()
        self.clear_books()

    def find_path(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "All files (*)")[0]
        self.book_path_lineEdit.setText(file_path)
        self.book_name_lineEdit.setText(os.path.basename(file_path))

    def show_books(self, name):
        self.book_listWidget.clear()
        genre = str(self.class_genre_comboBox.currentText())
        author = str(self.class_author_comboBox.currentText())
        folder = str(self.class_folder_comboBox.currentText())
        group = str(self.class_group_comboBox.currentText())
        if name == '':
            name = '%'
        if genre == '':
            genre = '%'
        if author == '':
            author = '%'
        if folder == '':
            folder = '%'
        if group != '':
            self.cursor.execute("""SELECT e.name FROM ebooks e 
                            LEFT JOIN ebooks_dist ed ON ed.ebook_id=e.rowid 
                            LEFT JOIN groups g ON g.rowid=ed.group_id
                            WHERE g.group_name LIKE ? 
                            AND e.name LIKE ?
                            AND e.genre LIKE ?
                            AND e.author LIKE ?
                            AND e.folder LIKE ?""", (group, name, genre, author, folder))
        else:
            self.cursor.execute(
                "SELECT name FROM ebooks WHERE genre LIKE ? AND author LIKE ? AND folder LIKE ? AND name LIKE ?",
                (genre, author, folder, name))
        books = self.cursor.fetchall()
        for book in books:
            if book[0] == '':
                continue
            else:
                item = QtWidgets.QListWidgetItem(book[0])
                self.book_listWidget.addItem(item)

    def clear_books(self):
        self.book_listWidget.clear()
        self.class_folder_comboBox.setCurrentIndex(0)
        self.class_author_comboBox.setCurrentIndex(0)
        self.class_genre_comboBox.setCurrentIndex(0)
        self.class_group_comboBox.setCurrentIndex(0)
        self.label_10.setText('')
        self.label_12.setText('')
        self.label_14.setText('')
        self.label_16.setText('')
        self.label_18.setText('')
        self.label_20.setText('')

    def add_group(self, name):
        self.class_group_comboBox.addItem(name)
        group = name
        with self.connect:
            self.cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group,))

    def open_sqlite(self):
        try:
            os.startfile('.\\sqlite\\browser.exe')
        except FileNotFoundError:
            self.error_box('The file you are trying to open is not found.')
        except OSError:
            self.error_box('You are attempting to use a feature that works on Windows on another OS.')

    def add_item_to_group_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowIcon(self.icon4)
        dialog.setStyleSheet(MainWindow.styleSheet())
        self.group_comboBox = QtWidgets.QComboBox(dialog)
        with self.connect:
            self.cursor.execute("SELECT DISTINCT group_name from groups")
            groups = self.cursor.fetchall()
            for group in groups:
                self.group_comboBox.addItem(group[0])
        group_pushBtn = QtWidgets.QPushButton("OK", dialog)
        group_pushBtn.move(40, 100)
        self.group_comboBox.move(40, 50)
        group_pushBtn.clicked.connect(lambda: self.add_item_to_group())
        dialog.setWindowTitle("Add Group")
        dialog.exec_()

    def add_item_to_group(self):
        try:
            book_name = self.book_listWidget.currentItem().text()
            group_name = self.group_comboBox.currentText()
            with self.connect:
                self.cursor.execute("SELECT rowid FROM groups WHERE group_name=?", (group_name,))
                group_id = self.cursor.fetchone()[0]
                self.cursor.execute("SELECT rowid FROM ebooks WHERE name=?", (book_name,))
                ebook_id = self.cursor.fetchone()[0]
                self.cursor.execute("INSERT INTO ebooks_dist VALUES (?, ?)", (group_id, ebook_id))
        except (sqlite3.IntegrityError, AttributeError):
            self.error_box('Ebook already in group. Cannot add twice.')

    def show_book_details(self):
        name = self.book_listWidget.currentItem().text()
        with self.connect:
            self.cursor.execute("SELECT * FROM ebooks WHERE name=?", (name,))
            book = self.cursor.fetchone()
        try:
            self.label_10.setText(book[0])
            with open(book[3], 'rb') as ebook:
                if book[1] == '':
                    self.label_12.setText(str(pdf.PdfFileReader(ebook).getDocumentInfo().author))
                else:
                    self.label_12.setText(book[1])
                self.label_18.setText(str(pdf.PdfFileReader(ebook).getNumPages()))
        except (pdf.utils.PdfReadError, PermissionError, ValueError, AttributeError):
            self.label_12.setText('')
            self.label_18.setText('')
        except FileNotFoundError:
            self.error_box('It seems this ebook is not an actual file on your hard drive.')
        self.label_14.setText(book[2])
        self.label_16.setText(book[3])
        try:
            self.label_20.setText(str(floor(int(os.path.getsize(book[3])) / 1024 / 1024)) + "  MB")
        except FileNotFoundError:
            self.error_box('It seems this ebook is not an actual file on your hard drive.')

    def add_dir_files(self, path, rec):
        try:
            names = []
            if rec:
                files = glob(path + '/**/*.*', recursive=rec)
            else:
                files = glob(path + '/*.*', recursive=rec)
            for file in files:
                file = os.path.basename(file)
                name = os.path.splitext(file)[0]
                names.append(name)
            total = int(len(files))
            value = 0
            with self.connect:
                for name, path in zip(names, files):
                    value += 1
                    progressValue = floor((value / total) * 100)
                    self.dir_progress.setValue(progressValue)
                    self.add_book(name, "", path, "")
        except:
            pass

    def add_book(self, name, author, path, genre):
        """
        Adds book to the table.
        User must have already inputted the arguments above.
        """
        try:
            book_folder = path.split('/')[-2]
        except IndexError:
            try:
                book_folder = path.split('\\')[-2]
            except IndexError:
                book_folder = ''
        with self.connect:
            self.cursor.execute("INSERT INTO ebooks VALUES (?, ?, ?, ?, ?)", (name, author, genre, path, book_folder))
        self.refresh_authors()
        self.refresh_folders()
        self.refresh_genres()
        self.refresh_groups()

    def app_info(self):
        dialogClass = InfoDialog()
        dialog = QtWidgets.QDialog(self)
        dialogClass.setupUi(dialog)
        dialog.exec_()

    def sort_search(self):
        if self.SORT == 0:
            self.book_listWidget.sortItems(QtCore.Qt.DescendingOrder)
            self.SORT = 1
        else:
            self.book_listWidget.sortItems(QtCore.Qt.AscendingOrder)
            self.SORT = 0

    @staticmethod
    def error_box(text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_class_dialog(self, title):
        dialog = QtWidgets.QDialog()
        dialog.setStyleSheet(MainWindow.styleSheet())
        lineEdit = QtWidgets.QLineEdit(dialog)
        pushBtn = QtWidgets.QPushButton("OK", dialog)
        label = QtWidgets.QLabel(dialog)
        dialog.setFixedSize(400, 200)
        pushBtn.move(80, 100)
        lineEdit.move(60, 50)
        label.move(20, 52)
        label.setText(title)
        if title == "Folder":
            pushBtn.clicked.connect(lambda: self.class_folder_comboBox.addItem(lineEdit.text()))
            dialog.setWindowIcon(self.icon1)
        elif title == "Genre":
            pushBtn.clicked.connect(lambda: self.class_genre_comboBox.addItem(lineEdit.text()))
            dialog.setWindowIcon(self.icon2)
        elif title == "Author":
            pushBtn.clicked.connect(lambda: self.class_author_comboBox.addItem(lineEdit.text()))
            dialog.setWindowIcon(self.icon3)
        elif title == "Group":
            pushBtn.clicked.connect(lambda: self.add_group(lineEdit.text()))
            dialog.setWindowIcon(self.icon4)
        else:
            self.dir_progress = QtWidgets.QProgressBar(dialog)
            self.dir_progress.setGeometry(40, 150, 300, 20)
            pushBtn.clicked.connect(lambda: self.add_dir_files(lineEdit.text(), True))
        dialog.setWindowTitle("Add " + title)
        dialog.exec_()


# noinspection PyArgumentList
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    MainWindow = QtWidgets.QMainWindow()
    # noinspection PyArgumentList
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    icon10_path = Path('.')
    sys.exit(app.exec_())
