
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QDirIterator, QEvent, Qt, QTimer
from os.path import expanduser
from PyQt5.QtWidgets import QHBoxLayout, QHeaderView, QMainWindow, QMenu, QVBoxLayout, QWidget, QFileSystemModel, QTreeView,  QFileDialog, QGroupBox, QFrame, QToolTip, QDialog, QPlainTextEdit, QProgressBar, QApplication, QLabel, QPushButton, QLineEdit, QTextEdit, QPlainTextEdit
from PyQt5 import QtGui
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QIntValidator, QMovie, QFont, QColor, QPixmap
import os, sys, walls, resource, time
from cryptography.fernet import Fernet
from datetime import datetime


# import pywhatkit as kit
import tkinter
import socket


class LoadScreen(QWidget):
    def __init__(self):

        super().__init__()
        self.setFixedSize(128, 150)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie('Loader.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer()
        self.startAnimation()
        timer.singleShot(8000)

        self.show()


    def startAnimation(self):
        self.movie.start()
    def stopAnimation(self):
        self.movie.stop()
        self.close()



class Ui_MainWindow(QWidget):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1380, 730)
        MainWindow.setStyleSheet("*{\n"
                                # "background:  rgb(211, 215, 207);\n"
                                # 17, 98, 27
                                # "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(218, 218, 218, 255), stop:1 rgba(212, 212, 212, 255));\n"
                                "background: #034f84;\n"
                                "color: #eee;\n"
                                "font-family: bold;\n"
                                "font-size: 14px;\n"
                                "}\n"
                                "\n"
                                "#frame{\n"
                                # "background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.353211 rgba(234, 234, 234, 255), stop:0.366972 rgba(238, 238, 238, 255), stop:0.646789 rgba(215, 217, 218, 255));\n"
                                # "background: rgb(17, 98, 27);\n"
                                "background: #034f84;\n"
                                # "border-radius: 2px;\n"
                                "border-right: 2px solid  #ccc;\n"
                                "}\n"
                                "\n"
                                "#frame_3{\n"
                                # "background: rgb(46, 52, 54);\n"
                                "border-radius: 4px;\n"
                                "}\n"

                               
                                "\n"
                                "#plainTextEdit{\n"
                                "background: #f5f5f5;\n"
                                "border-radius: 4px;\n"
                                "color: #333;\n"
                                "border-bottom: 5px solid  #949e8b;\n"
                                "}\n"
                                "\n"
                                "")
         
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 80, 1361, 661))
        font = QtGui.QFont()
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.comboBox.setGeometry(QtCore.QRect(255, 5, 790, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet('color: #eee')

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(1050, 40, 320, 100))
        self.plainTextEdit.setObjectName("plainTextEdit")
        # self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        # self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setReadOnly(True)


        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.frame_3)
        self.plainTextEdit2.setGeometry(QtCore.QRect(1050, 145, 320, 475))
        self.plainTextEdit2.setObjectName("plainTextEdit")
        # self.plainTextEdit2.setFrameShape(QtWidgets.QFrame.Box)
        # self.plainTextEdit2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit2.setReadOnly(True)


        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(r'C\\')
        self.treeView = QtWidgets.QTreeView(self.frame_3)
        self.treeView.setModel(self.model)
        self.treeView.setGeometry(QtCore.QRect(255, 40, 790, 580))
        # self.listView.setHeaderHidden(True)

        self.treeView.doubleClicked.connect(self.listItemsView)
        # self.treeView.clicked.connect(self.qmenu)
        self.treeView.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        # self.treeView.setFrameShape(QtWidgets.QFrame.Box)
        # self.treeView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.treeView.setObjectName("treetView")
        self.treeView.setAlternatingRowColors(True)
        
        self.treeView.setAnimated(False)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setColumnWidth(0, 400)
        self.treeView.setStyleSheet('QTreeView'
                                    '{ '
                                        'alternate-background-color: #b5dffd;'
                                        'background: #f3f3f3;'
                                        'color: #333;'
                                        "border-bottom: 2px solid  #ccc;"
                                        '}'
                                            )
        # self.treeView.setRootIndex(self.model.index())
        

        
        self.frame = QtWidgets.QFrame(self.frame_3)

        # self.frame.setGeometry(QtCore.QRect(0, 0, 250, 699))
        # self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.taskbar = QtWidgets.QFrame(self.centralwidget)
        self.taskbar.setGeometry(QtCore.QRect(0, 0, 1385, 80))
        # self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.taskbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskbar.setObjectName("taskbar")
        self.taskbar.setStyleSheet('background: #012641; border-radius: 4px; ')

        
        self.sidebar = QtWidgets.QPushButton(self.taskbar)
        self.sidebar.setGeometry(QtCore.QRect(20, 20, 80, 40))
        self.sidebar.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.sidebar.setText("shrink")
        self.sidebar.setStyleSheet('background: #0479cc; border-radius: 4px; ')
        self.sidebar.clicked.connect(self.shrink)
        self.sidebar.setObjectName("Shrink")


        

        self.openfile = QtWidgets.QPushButton(self.frame)
        self.openfile.setGeometry(QtCore.QRect(50, 96, 150, 40))
        # self.openfile.setStyleSheet( 'QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.openfile.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.openfile.setText("Open File")

        self.openfile.clicked.connect(self.browse)
        self.openfile.setObjectName("openfile")



        self.openfolder = QtWidgets.QPushButton(self.frame)
        self.openfolder.setGeometry(QtCore.QRect(50, 144, 150, 40))
        # self.openfolder.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )

        self.openfolder.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.openfolder.setText("Open Folder")
        self.openfolder.clicked.connect(self.addFiles)
        self.openfolder.setObjectName("openfolder")




        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 192, 150, 40))
        # self.pushButton_3.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.pushButton_3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setText("Creat key")

        self.pushButton_3.clicked.connect(self.dialogCreateKey)
        self.pushButton_3.setObjectName("pushButton_3")
     
        


        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 245, 150, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_4.clicked.connect(self.dataBaseQuery)
        self.pushButton_4.setText("DataBase")
        # self.pushButton_4.setStyleSheet( 'QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )




        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 300, 150, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_5.clicked.connect(self.ChatApps)
        # self.pushButton_5.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.pushButton_5.setText("Chat/Message")

        self.pushButton_5.setObjectName("pushButton_5")
        

      

        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(1060, 5, 291, 35))
        self.frame_7.setStyleSheet("#frame_7{\n"
                                   "\n"
                                   "background: #949e8b;\n"
                                   "font-size: 12px;\n"
                                   "font-weight: bold;\n"
                                   "text-align: center;\n"
                                   "color: #fff;\n"
                                   "border-top-left-radius: 25px;\n"
                                   "border-bottom-left-radius: 10px;\n"
                                   "border-top-right-radius: 25px;\n"
                                   "border-bottom-right-radius: 10px;\n"
                                   "}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 121, 21))
        self.label_3.setStyleSheet("font-size: 14px;\n"
                                   "font-weight: bold;\n"
                                   "text-align: center;\n"
                                   "background: none;\n"
                                   "color: #fff;")
        self.label_3.setObjectName("label_3")

        

        self.frame_13 = QtWidgets.QFrame(self.frame_7)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 41, 35))
        self.frame_13.setStyleSheet("border-image: url(:/image/org.libreoffice.LibreOffice-writer.ico);\n"
                                    "background:  #008;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        
        

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(250, 20, 1090, 21))
        self.label_19.setStyleSheet("font-size: 25px;\n"
                                   "font-weight: bold;\n"
                                   "text-align: center;\n"
                                   "background: none;\n"
                                   "color: #eee;")
        self.label_19.setObjectName("label_3")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(255, 55, 481, 18))
        self.label_10.setStyleSheet("background: none; font-size: 18px; font-weight: bold;  color: #00cc00;")
        self.label_10.setObjectName("label_10")

        self.frame_14 = QtWidgets.QFrame(self.centralwidget)
        self.frame_14.setGeometry(QtCore.QRect(500, 386, 120, 120))
        self.frame_14.setStyleSheet("background: none; border-image: url(:/image/PngItem_2666090.png);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")

        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(680, 400, 100, 100))
        self.frame_15.setStyleSheet("background: none; border-image: url(:/image/371-3715555_nasarawa-state-university-keffi-nsuk.png);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")

        


        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setStyleSheet('background: none; border-radius: 4px;')
        self.frame_6.setGeometry(QtCore.QRect(680, 45, 460, 31))
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(15, 5, 500, 41))
        self.label.setStyleSheet("font-size: 11px;\n"
                                 "font-weight: bold;\n"
                                 "font-family: Raleway;\n"
                                 "text-align: center;\n"
                                 "background: none;\n"
                                 "color: #fff;")
        self.label.setObjectName("label")


        # self.label_animation = QLabel(self.frame)
        # self.label_animation.setStyleSheet("background: none; color: #fff; border:none;")
        # self.movie = QMovie('64x64.gif')
        # self.label_animation.setGeometry(88, 0, 118, 100)
        # self.label_animation.setMovie(self.movie)

        # timer = QTimer()
        # self.startAnimation()
        # # timer.singleShot(8000)


   


        self.same = 'This is a Final year project for computer Science Nasarawa state University Keffi @ CHUNTAN LIVINUS JOSIAH'
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFiles = QtWidgets.QAction(MainWindow)
        self.actionOpenFiles.setObjectName("actionOpenFiles")
        
        self.actionOpenFiles.triggered.connect(self.browse)
        self.actionOpenFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenFolder.setObjectName("actionOpenFolder")
        self.actionOpenFolder.triggered.connect(self.addFiles)
        self.menuFile.addAction(self.actionOpenFiles)
        self.menuFile.addAction(self.actionOpenFolder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Decryption and Encryption Security System"))
        MainWindow.statusBar().showMessage(self.same)
        self.label_3.setText(_translate("MainWindow", "DISPLAY Result"))
        # self.label.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", "DATA ENCRYPTION AND DECRYPTION SECURITY SYSTEM"))
        self.label_10.setText(_translate("MainWindow", "Your files safety is very important"))
        # self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menu.setTitle(_translate("MainWindow", "View"))
        # self.menu_2.setTitle(_translate("MainWindow", "..."))
        self.actionOpenFiles.setText(_translate("MainWindow", "Open Files"))
        self.actionOpenFolder.setText(_translate("MainWindow", "Open Folder"))
        



    def generatekey(self):
        self.win = CreateForm()
        self.win.show()

    def shrink(self):
        b = 250
        print('you click')
        currenth = self.height()
        self.frame = QtWidgets.QFrame(self.frame_3)

        self.frame.setGeometry(QtCore.QRect(0, 0, 250, 699))
        # self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.openfile = QtWidgets.QPushButton(self.frame)
        self.openfile.setGeometry(QtCore.QRect(50, 96, 150, 40))
        # self.openfile.setStyleSheet( 'QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.openfile.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.openfile.setText("Open File")

        self.openfile.clicked.connect(self.browse)
        self.openfile.setObjectName("openfile")



        self.openfolder = QtWidgets.QPushButton(self.frame)
        self.openfolder.setGeometry(QtCore.QRect(50, 144, 150, 40))
        # self.openfolder.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )

        self.openfolder.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.openfolder.setText("Open Folder")
        self.openfolder.clicked.connect(self.addFiles)
        self.openfolder.setObjectName("openfolder")




        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 192, 150, 40))
        # self.pushButton_3.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.pushButton_3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setText("Creat key")

        self.pushButton_3.clicked.connect(self.dialogCreateKey)
        self.pushButton_3.setObjectName("pushButton_3")
     
        


        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 245, 150, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_4.clicked.connect(self.dataBaseQuery)
        self.pushButton_4.setText("DataBase")
        # self.pushButton_4.setStyleSheet( 'QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )




        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 300, 150, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pushButton_5.clicked.connect(self.ChatApps)
        # self.pushButton_5.setStyleSheet('QPushButton'
        #                                 '{'
        #                                 'background: ##4a5143;'
        #                                 'border-bottom: 2px solid lightgreen;'
        #                                 'border-radius: 4px;'
        #                                 'color: #eee;'
        #                                 '}'
        #                                 'QPushButton:hover'
        #                                 '{'
        #                                 'background: #0b2028;'
        #                                 'color: #fff;'
        #                                 'border-bottom: 5px solid lightgreen;'

        #                                 '}'
        #                                  "QPushButton#pushButton_3::pressed"
        #                                 "{"
        #                                 "background: red;"
        #                                 'padding-left: 10px;'
        #                                 'padding-top: 10px;'
        #                                 "}"
        #                                 )
        self.pushButton_5.setText("Chat/Message")

        self.pushButton_5.setObjectName("pushButton_5")





    # def settingsForm(self):
    #     self.theme = settingThemeForm()
    #     self.theme.show()

    def startAnimation(self):
        self.movie.start()


    def dataBaseQuery(self):
        self.theme = DatabaseForm()
        self.theme.show()

    def addFiles(self):
        try:
            # self.listView.clear()
            self.comboBox.clear()
            self.frame_15.close()
            self.frame_14.close()

            
            self.folderChoosen = QtWidgets.QFileDialog.getExistingDirectory(None ,'Open Music Folder', expanduser('~'))
            # self.basenamefile = os.path.basename(self.folderChoosen[0])
            self.basenm = os.path.dirname(self.folderChoosen)
            self.model.setRootPath(self.basenm)
            self.treeView.setModel(self.model)
            self.treeView.setRootIndex(self.model.index(self.basenm))


            self.plainTextEdit.clear()
            self.comboBox.addItem(self.basenm)
            
        except IndexError:
            pass



    def browse(self):
        try:
           
            self.file_path = QtWidgets.QFileDialog.getOpenFileName()
            self.basenm = os.path.dirname(self.file_path[0])
            self.comboBox.clear()
            self.comboBox.insertItem(0, self.basenm)
            self.basenamefile = os.path.basename(self.file_path[0])
            print(self.basenm)

            self.model.setRootPath("C:\\")
            self.treeView.setModel(self.model)
            # self.treeView.setRootIndex(self.model.index(self.basenm))
            # print(self.basenm)

            
            self.treeView.reset()
            # self.treeView.insertItem(0, self.basenamefile)
            self.plainTextEdit.clear()

        except FileNotFoundError:
                pass
    
  
    

    def listItemsView(self, signal):
        self.plainTextEdit.clear()
        self.plainTextEdit2.clear()
        self.file_path = self.model.filePath(signal)
        self.basenm = os.path.dirname(self.file_path)
        self.basenamefile = os.path.basename(self.file_path)
        

        self.bb = os.path.join(self.basenm, self.basenamefile)
        self.label.setText(self.basenamefile)
        # self.label.setStyleSheet('background: #004000; border-radius: 4px;')
        
        self.frame_6.setStyleSheet('background: none; border-radius: 4px;')
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        



        
        self.comboBox.insertItem(0, self.file_path)

        self.bb = f'{os.path.join(self.file_path)}'

        try:
            with open(f'{self.bb}', 'rt') as self.myfiles:
                self.myfiles_path = self.myfiles.read()
                self.plainTextEdit2.setPlainText(self.myfiles_path)
        except UnicodeDecodeError:

            self.plainTextEdit.setPlainText(self.basenamefile)
        
        except PermissionError:
            self.plainTextEdit.setPlainText('Files Needed not Folder')
        
        self.form = Encryption_Decrypt_Form(self)
        self.form.path_lineEdit.setText(self.file_path)

        self.form.show()
    
    def combo(self):
        self.comboBox.insertItem(0, self.file_path)
        
    


    def dialogCreateKey(self):
        
        self.key = CreateForm()
        self.key.show()

    def ChatApps(self):

        self.chat = ChatingApp()
        self.chat.show()

#     def dialogDecrypt(self):

#             self.decrypt = DecryptForm()
#             self.decrypt.show()




class CreateForm(QWidget):
    def __init__(self):
        super().__init__()

        self.left =200
        self.top =400
        self.width =500
        self.height =451
        self.WindowApp()
        # self.setStyleSheet("background: #eff1f6; color: #eee")
        # self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(self.width, self.height)
        
        self.setStyleSheet(" color: #f4faff; border: 1px solid #3477b6; border-radius: 4px;")


    def WindowApp(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(' App')

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(QtCore.QRect(-5, 0, 581, 180))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.frame2.setStyleSheet("background: #0479cc;")

        self.keygenerator = QLineEdit(self.frame2)
        self.keygenerator.setGeometry(98, 50, 300, 41)
        self.keygenerator.setFont(QtGui.QFont('consola', 10))
        self.keygenerator.setAlignment(Qt.AlignLeft)
        self.keygenerator.setPlaceholderText('Type the of the Key')
        self.keygenerator.setStyleSheet("background: #fff; color: #333; border-radius: 8px;")

        self.sidebar = QtWidgets.QPushButton(self)
        self.sidebar.setGeometry(QtCore.QRect(458, 0, 40, 40))
        self.sidebar.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.sidebar.setText("X")
        self.sidebar.setStyleSheet('background: #034f84; border-radius: 4px; ')
        self.sidebar.clicked.connect(self.exit)
        self.sidebar.setObjectName("X")

        self.btn_submit = QPushButton(self.frame2)
        self.btn_submit.setGeometry(200, 120, 111, 41)
        self.btn_submit.setFont(QtGui.QFont('consola', 12))
        self.btn_submit.setObjectName("pushButton")
        self.btn_submit.setText("Create")
        self.btn_submit.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet("background: #252525; color: #eee; border-radius: 8px;")
        self.btn_submit.clicked.connect(self.createEncryptkey1)

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(10, 230, 481, 10)


        self.plainText = QPlainTextEdit(self)
        self.plainText.setGeometry(20, 290, 461, 121)
        self.plainText.setStyleSheet("background: #fff; border: 1px solid #333; border: none; font-size: 15px; color: #333;")
        self.plainText.setReadOnly(True)
        

        # self.labelInit = QLabel(self)
        # self.labelInit.setGeometry(190, 200, 81, 21)
        # self.labelInit.setText('InitTializing')

        # self.labelComplete = QLabel(self)
        # self.labelComplete.setGeometry(300, 200, 71, 16)
        # self.labelComplete.setText('completed')

    def exit(self):
        print('hello')
        self.winclose = CreateForm()
        self.winclose.close()
        
        

    def createEncryptkey1(self):
        if self.keygenerator.text() != '':
            import shutil
            self.file_path = QtWidgets.QFileDialog.getExistingDirectory()
            print(self.file_path)

            for i in range(101):
                time.sleep(0.02)
                self.progressbar.setValue(i)
            # self.demo = LoadScreen()
            key = Fernet.generate_key()
            self.bb = self.keygenerator.text()

            with open(f'{self.bb}.key', 'wb') as mykey:
                mykey.write(key)
            
            # print(self.bb)

            success = 'complete... \n key is generated successfully'

            self.plainText.setPlainText(success)

            self.basenm = os.path.join(os.getcwd(), f'{self.bb}.key')

            shutil.move(self.basenm, self.file_path)
        else:
            self.keygenerator.setText('Need a file name...')

      

class LogForm(QWidget):
    def __init__(self):
        super().__init__()

        self.left =140
        self.top =200
        self.width =981
        self.height =500
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width, self.height)
        
        self.setStyleSheet("background:  rgb(17, 98, 27);")

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Login Form')

        

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(QtCore.QRect(500, 0, 481, 500))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.frame2.setStyleSheet("background: #eee;")

        self.image_frame = QtWidgets.QFrame(self.frame2)
        self.image_frame.setGeometry(QtCore.QRect(190, 20, 120, 130))
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("frame_10")
        self.image_frame.setStyleSheet("background: #fff;")

        
        self.label_user = QLabel(self.image_frame)
        self.label_user.setStyleSheet("border-image: url(:/image/user.ico); color: #000; border:none;")
        self.label_user.setGeometry(0, 0, 120, 130)

        self.label_user = QLabel(self)
        self.label_user.setStyleSheet("border-image: url(:/image/encrypted); color: #000; border:none;")
        self.label_user.setGeometry(110, 10, 250, 250)
        


        self.username = QLineEdit(self.frame2)
        self.username.setGeometry(98, 170, 300, 41)
        self.username.setFont(QtGui.QFont('consola', 10))
        self.username.setAlignment(Qt.AlignLeft)
        self.username.setPlaceholderText('Username')
        self.username.setToolTip('You are onusername Input')
        # self.username.textChanged[str].connect(self.login)
        self.username.setStyleSheet("background: #302D2D; color: #f8f7fe; border-radius: 4px;")

        # self.frame_10 = QtWidgets.QFrame(self.frame2)
        # self.frame_10.setGeometry(QtCore.QRect(380, 170, 41, 41))
        # self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_10.setObjectName("frame_10")

        self.password = QLineEdit(self.frame2)
        self.password.setGeometry(98, 220, 300, 41)
        self.password.setFont(QtGui.QFont('consola', 10))
        self.password.setAlignment(Qt.AlignLeft)
        self.password.setPlaceholderText('Password')
        self.password.setToolTip('You are password Input')
        # self.password.setValidator(QIntValidator())
        # self.password.textChanged[str].connect(self.login)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("background: #302D2D; color: #f8f7fe; border-radius: 4px;")

        # self.frame_1b = QtWidgets.QFrame(self.frame2)
        # self.frame_1b.setGeometry(QtCore.QRect(380, 220, 41, 41))
        # self.frame_1b.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_1b.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_1b.setObjectName("frame_10")

        self.btn_submit = QPushButton(self.frame2)
        self.btn_submit.setGeometry(200, 280, 111, 41)
        self.btn_submit.setFont(QtGui.QFont('consola', 12))
        self.btn_submit.setObjectName("pushButton")
        self.btn_submit.setText("Login")
        self.btn_submit.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet('QPushButton'
                                        '{'
                                        "background: #252525; color: #fff; border-radius: 4px;"
                                        '}'
                                        'QPushButton#pushButton:pressed'
                                        '{'
                                            'padding-left: 5px;'
                                            'padding-top: 5px;'
                                            '}'
                                                )
        
        self.btn_submit.clicked.connect(self.login)
        # self.btn_submit.clicked.connect(self.check)


        self.progressbar = QProgressBar(self.frame2)
        self.progressbar.setGeometry(40, 330, 401, 30)
        self.frame2.setStyleSheet("background: #eee; border: none;")


        


        self.plainText = QPlainTextEdit(self.frame2)
        self.plainText.setGeometry(20, 360, 441, 131)
        self.plainText.setStyleSheet("background: rgb(46, 52, 54); border: 1px solid #031520; border-radius: 4px; font-size: 15px; color: #eee;")
        self.plainText.setReadOnly(True)

        # self.frame_15 = QtWidgets.QFrame(self)
        # self.frame_15.setGeometry(QtCore.QRect(100, 20, 120, 120))
        # self.frame_15.setStyleSheet("border-image: url(:/image/371-3715555_nasarawa-state-university-keffi-nsuk.png);")
        # self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_15.setObjectName("frame_15")

        # self.frame_16 = QtWidgets.QFrame(self)
        # self.frame_16.setGeometry(QtCore.QRect(110, 10, 250, 250))
        # self.frame_16.setStyleSheet("border-image: url(:/image/PngItem_2666090.png);")
        # self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_16.setObjectName("frame_15")
        
        self.Logoname = QLabel(self)
        self.Logoname.setGeometry(35, 260, 430, 90)
        self.Logoname.setText('DATA ENCRYPTION AND DECRYPTION SECURITY SYSTEM')
        self.Logoname.setStyleSheet('background: none; border:none; color: #FFF; font-size: 15px;')

        self.Logoname2 = QLabel(self)
        self.Logoname2.setFont(QtGui.QFont('weight: 25'))
        self.Logoname2.setGeometry(50, 310, 420, 80)
        self.Logoname2.setText('SECURITY OF YOUR DATA THAT MATTERS')
        self.Logoname2.setStyleSheet('background: none; color: orange; border:none; font-size: 18px;')

        self.label_animation = QLabel(self)
        self.label_animation.setStyleSheet("background: none; color: #fff; border:none;")
        self.movie = QMovie('64x64.gif')
        self.label_animation.setGeometry(200, 380, 118, 100)
        self.label_animation.setMovie(self.movie)

        timer = QTimer()
        self.startAnimation()
        # timer.singleShot(8000)

        self.show()

    def startAnimation(self):
        self.movie.start()


    def login(self):
        if self.username.text() == 'joe' and self.password.text() == '12345':

            for i in range(101):
                time.sleep(0.03)
                self.progressbar.setValue(i)
                self.progressbar.setStyleSheet(
              '''QProgressBar {
            background-color: #0078c2;
            color: #333;
            border-style: none;
            border-radius: 4px;
            text-align: center;
            font-size: 30px;
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color: #24a8ff;
        }
    ''')
            
            self.close()

            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()

            
        else:
            name = socket.gethostname()
            self.plainText.setPlainText(f'{name}: trying to login \n Not correct')
            


class ChatingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.left =100
        self.top =400
        self.width =464
        self.height =578
        self.ChatApp()
        # self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width, self.height)
        # self.setStyleSheet(" color: ##f4faff; border: 1px solid #3477b6")


    def ChatApp(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Chat App')

        self.frame = QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-5, 0, 581, 180))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background: #21a0fa;")

        # self.labelPhone = QLabel(self.frame)
        # self.labelPhone.setGeometry(30, 10, 81, 21)
        # self.labelPhone.setText('Encryption Key')
        # self.labelPhone.setStyleSheet('color: #eee')

        self.phone_number = QLineEdit(self.frame)
        self.phone_number.setPlaceholderText('Your Phone Number')
        self.phone_number.setGeometry(30, 30, 281, 41)
        self.phone_number.setFont(QtGui.QFont('consola', 10))
        self.phone_number.setStyleSheet("background: #fff; border: none; color: #333; border-radius: 4px;")

        # self.labelInit = QLabel(self.frame)
        # self.labelInit.setGeometry(30, 75, 81, 21)
        # self.labelInit.setText('Encryption Key')
        # self.labelInit.setStyleSheet('color: #eee')

        self.key = QLineEdit(self.frame)
        self.key.setPlaceholderText('Your Encrypt/Decrypt Key Here')
        self.key.setGeometry(30, 100, 380, 41)
        self.key.setFont(QtGui.QFont('consola', 10))
        self.key.setStyleSheet("background: #fff; border: none; color: #333; border-radius: 4px;")


        self.btn_browse_key = QPushButton(self)
        self.btn_browse_key.setGeometry(410, 100, 41, 41)
        self.btn_browse_key.setFont(QtGui.QFont('consola', 12))
        self.btn_browse_key.setText('...')
        self.btn_browse_key.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_browse_key.setToolTip('Browse a File')
        self.btn_browse_key.clicked.connect(self.GetKeyBrowser)
        self.btn_browse_key.setStyleSheet("background: green; color: #eee; border-radius:4px")


        self.labelComplete = QLabel(self)
        self.labelComplete.setGeometry(10, 180, 71, 16)
        self.labelComplete.setText('Chat Now')
        self.labelComplete.setStyleSheet('color: #333;')

        self.messages = QPlainTextEdit(self)
        self.messages.setGeometry(10, 198, 446, 171)
        self.messages.setFont(QtGui.QFont('consola', 10))
        self.messages.setStyleSheet("background: #fff; color: #333; border-radius: 4px;")

        self.btn_encrypt = QPushButton(self)
        self.btn_encrypt.setGeometry(100, 420, 42, 42)
        self.btn_encrypt.setFont(QtGui.QFont('consola', 12))
        self.btn_encrypt.setObjectName("pushButton")
        # self.btn_encrypt.setText("Encrypt")
        self.btn_encrypt.setToolTip('Click to Encrypt')
        self.btn_encrypt.clicked.connect(self.chatEncrypt)
        # self.btn_encrypt.setStyleSheet('background: #002266; color: #eee; border-radius:8px')
        self.btn_encrypt.setStyleSheet('QPushButton'
            '{'
            'border-image: url(:/image/icons/lock_32x32.png);'
            'color: #333;'
             '}'
             'QPushButton::Hover'
            '{'
            'background: #ddd;'
            '}')

        self.btn_decrypt = QPushButton(self)
        self.btn_decrypt.setGeometry(300, 420, 42, 42)
        self.btn_decrypt.setFont(QtGui.QFont('consola', 13))
        self.btn_decrypt.setObjectName("pushButton")
        self.btn_decrypt.setToolTip('Click to Decrypt')
        self.btn_decrypt.clicked.connect(self.chatDecrypt)
        # self.btn_decrypt.setStyleSheet('background: #002266; color: #eee; border-radius:8px')
        self.btn_decrypt.setStyleSheet('QPushButton'
            '{'
            'border-image: url(:/image/icons/unlock_32x32.png);'
             '}'
             'QPushButton::Hover'
            '{'
            'background: #ddd;'
            '}')
        
        self.btn_send = QPushButton(self)
        self.btn_send.setGeometry(80, 490, 301, 41)
        self.btn_send.setFont(QtGui.QFont('consola', 13))
        self.btn_send.setObjectName("pushButton")
        self.btn_send.setText("Send")
        self.btn_send.setToolTip('send Text')
        self.btn_send.clicked.connect(self.sendMessage)
        self.btn_send.setStyleSheet('QPushButton'
                                    '{'
                                    'background: #00b33c;'
                                    'color: #eee; border-radius:4px'
                                    '}'
                                    'QPushButton::Hover'
                                    '{'
                                    'background: #333;'
                                    '}')


    def GetKeyBrowser(self):
        try:
                self.file_path = QtWidgets.QFileDialog.getOpenFileName()
                self.basenm = os.path.dirname(self.file_path[0])
                self.basenamefile = os.path.basename(self.file_path[0])
                self.bb = f'{os.path.join(self.basenm, self.basenamefile)}'
                # print(self.path_lineEdit.text(), 'hello')
                with open(f'{self.bb}', 'rt') as mykey2:
                        key2 = mykey2.read()
                        self.key.setText(str(key2))

                with open('text.txt', 'rt') as original_files:
                    original = original_files.read()
                    self.messages.setPlainText(str(original))

        except FileNotFoundError:
                pass


    def chatEncrypt(self):
        day = datetime.now()
        day2 = day.strftime("%A")
        #............................................
        now = datetime.now()
        mtime = now.strftime("%I: %M: %p")
        #................................................
        today = datetime.today()
        STAMP_DATE = today.strftime("%d/%m/%y")

        print(STAMP_DATE, mtime)

        self.ph = self.phone_number.text()
        self.readkey = self.key.text()


        f = Fernet(self.readkey)

        self.chat = self.messages.toPlainText()

        with open('mainMessage.txt', 'w') as kk:
            aa = kk.write(self.chat)

        with open('mainMessage.txt', 'rb') as bb:
            c = bb.read()

        encrypted = f.encrypt(c)
        
        with open('mainMessage.txt', 'wb') as bb2:
            c2 = bb2.write(encrypted)
        
        with open('mainMessage.txt', 'rt') as mm:
            mb = mm.read()
        self.messages.setPlainText(str(mb))


    def sendMessage(self):
        pass
        # kit.sendwhatmsg(self.phone_number.text(), self.messages.toPlainText(), 2, 10)

        # print('i have send message')

        
        

        ###########################################################
        # self.chat = self.messages.toPlainText()

        # self.encode_message = self.chat.encode("ascii")
        # self.base64_byte = base64.b64encode(self.encode_message)
        # self.encrypt = self.base64_byte.decode("ascii")
        # self.messages.setPlainText(str(self.encrypt))
        ###########################################################


            

    def chatDecrypt(self):

        day = datetime.now()
        day2 = day.strftime("%A")
        #............................................
        now = datetime.now()
        mtime = now.strftime("%I: %M: %p")
        #................................................
        today = datetime.today()
        STAMP_DATE = today.strftime("%d/%m/%y")

        print(STAMP_DATE, mtime)


        self.ph = self.phone_number.text()
        self.readkey = self.key.text()

        f = Fernet(self.readkey)

        with open('mainMessage.txt', 'rb') as bb:
            c = bb.read()

        decrypted = f.decrypt(c)
        
        with open('mainMessage.txt', 'wb') as bb2:
            c2 = bb2.write(decrypted)
        
        with open('mainMessage.txt', 'rt') as mm:
            mb = mm.read()
        self.messages.setPlainText(str(mb))
    

        #######################################################
        # self.chat = self.messages.toPlainText()

        # self.encode_message = self.chat.encode("ascii")
        # self.base64_byte = base64.b64decode(self.encode_message)
        # self.encrypt = self.base64_byte.decode("ascii")
        # self.messages.setPlainText(str(self.encrypt))
        ###########################################################


            
    # def Chat(self):

    #     pwt.sendwhatmsg(f'{self.phone_number}, {self.messages}, 20, 30')
        

class Encryption_Decrypt_Form(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet("background: rgb(22, 65, 82); color: #eee")
        # self.setStyleSheet(" color: ##f4faff; border: 1px solid #3477b6")
        # self.setWindowModality(Qt.ApplicationModal)
        self.resize(576, 451)

        self.frame3 = QFrame(self)
        self.frame3.setGeometry(QtCore.QRect(-5, 0, 581, 220))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame")
        self.frame3.setStyleSheet("background: rgb(17, 98, 27);")


        self.keygenerator = QLineEdit(self.frame3)
        self.keygenerator.setGeometry(40, 60, 481, 41)
        self.keygenerator.setFont(QtGui.QFont('consola', 10))
        self.keygenerator.setStyleSheet("background: #fff; border-radius:4px; color: #333;")

        self.btn_browse = QPushButton(self.frame3)
        self.btn_browse.setGeometry(525, 60, 41, 41)
        self.btn_browse.setFont(QtGui.QFont('consola', 12))
        self.btn_browse.setText('...')
        self.btn_browse.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_browse.setToolTip('Browse a File')
        self.btn_browse.clicked.connect(self.getBrowser)
        self.btn_browse.setStyleSheet("background: #456f93; color: #eee; border-radius:4px")


        self.path_lineEdit = QLineEdit(self.frame3)
        self.path_lineEdit.setGeometry(10, 10, 601, 41)
        self.path_lineEdit.setFont(QtGui.QFont('consola', 10))
        # self.path_lineEdit.setText(signal)
        self.path_lineEdit.setStyleSheet("background: rgb(36, 41, 43); border: none; color: #eee")


        self.btn_encrypt = QPushButton(self.frame3)
        self.btn_encrypt.setGeometry(165, 130, 42, 42)
        self.btn_encrypt.setFont(QtGui.QFont('consola', 13))
        self.btn_encrypt.setObjectName("pushButton")
        # self.btn_encrypt.setText("Encrypt")
        self.btn_encrypt.setToolTip('Click to Encrypt')
        self.btn_encrypt.clicked.connect(self.EncryptSource)
        # self.btn_encrypt.setStyleSheet('background: #002266; color: #eee; border-radius:8px')
        self.btn_encrypt.setStyleSheet('QPushButton'
            '{'
            'border-image: url(:/image/icons/lock_32x32.png);'
            'padding-left: 5px;'
            'padding-top: 5px;'
            # 'background: green;'
             '}'
             'QPushButton::Hover'
            '{'
            'background: #ddd;'
            '}')
            # 'QPushButton#pushButton:pressed'
            # '{'
            #     'padding-left: 5px;'
            #     'padding-top: 5px;'
            #     'background: green;'
            # '}')


        self.btn_decrypt = QPushButton(self.frame3)
        self.btn_decrypt.setGeometry(360, 132, 42, 42)
        self.btn_decrypt.setFont(QtGui.QFont('consola', 13))
        self.btn_decrypt.setObjectName("pushButton")
        # self.btn_decrypt.setText("Decrypt")
        self.btn_decrypt.setToolTip('Click to Decrypt')
        self.btn_decrypt.clicked.connect(self.DecryptSource)
        # self.btn_decrypt.setStyleSheet('background: #002266; color: #eee; border-radius:8px')
        self.btn_decrypt.setStyleSheet('QPushButton'
            '{'
            'border-image: url(:/image/icons/unlock_32x32.png);'
             '}'
             'QPushButton::Hover'
            '{'
            'background: #ddd;'
            '}')

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(10, 230, 561, 10)
        

        self.plainText = QPlainTextEdit(self)
        self.plainText.setGeometry(0, 245, 580, 210)
        self.plainText.setStyleSheet("background: #fff; font-size: 15px; color: #333;")

        self.labelEncrypt = QLabel(self.frame3)
        self.labelEncrypt.setGeometry(170, 190, 81, 21)
        self.labelEncrypt.setText('Encrypt')

        self.labelDecrypt = QLabel(self.frame3)
        self.labelDecrypt.setGeometry(360, 190, 71, 16)
        self.labelDecrypt.setText('Decrypt')

    def getBrowser(self):
        try:

                self.file_path = QtWidgets.QFileDialog.getOpenFileName()
                self.basenm = os.path.dirname(self.file_path[0])
                self.basenamefile = os.path.basename(self.file_path[0])

                self.bbkey = f'{os.path.join(self.basenm, self.basenamefile)}'
                with open(f'{self.bbkey}', 'rt') as mykey2:
                        key2 = mykey2.read()
                        self.keygenerator.setStyleSheet("background: #fff; color: #333")
                        self.keygenerator.setText(str(key2))
        except FileNotFoundError:
                pass
    

    def EncryptSource(self):
        day = datetime.now()
        day2 = day.strftime("%A")
        #............................................
        now = datetime.now()
        mtime = now.strftime("%I: %M: %p")
        #................................................
        today = datetime.today()
        STAMP_DATE = today.strftime("%d/%m/%y")

        conn = sqlite3.connect('encryption_decryption_storebase.db')
        # print(' database open successfully')
        
        try:
            for i in range(101):
                time.sleep(0.02)
                self.progressbar.setValue(i)

            self.dd = self.path_lineEdit.text()
            # self.basenamefile = os.path.basename(self.dd)
            self.encryptkeyread = self.keygenerator.text()
            if self.keygenerator.text() == '':
                self.keygenerator.setText('key is needed')
            
            else:

                f = Fernet(self.encryptkeyread)

                with open(self.dd, 'rb') as original_files:
                    original = original_files.read()

                    encrypted = f.encrypt(original)

                with open(self.dd, 'wb') as encrypted_files:
                    encrypted_files.write(encrypted)

                success = 'Encrypted SuccessFully'
                self.plainText.setPlainText(f'{success}')

                insert_data = "INSERT INTO encryption_decryption_storebase (key_name, key_value, filename, stamp_date, time, day) VALUES('"+self.basenamefile+"', '" + self.encryptkeyread + "', '"+self.path_lineEdit.text()+"', '" + STAMP_DATE+ "', '" +mtime+ "', '" +day2 + "') "
                conn.execute(insert_data)
                conn.commit()
                # print('Record created successfully')
                conn.close()
        except AttributeError:
            self.message = "Oops Key is needed...."
            self.keygenerator.setStyleSheet("color: red")
            self.keygenerator.setText(self.message)


    def DecryptSource(self):

        try:
            for i in range(101):
                time.sleep(0.03)
                self.progressbar.setValue(i)

            self.bb = self.path_lineEdit.text()
            self.readkey = self.keygenerator.text()


            fd = Fernet(self.readkey)

            with open(self.bb, 'rb') as encrypted_files:
                encryted = encrypted_files.read()

            decrypt = fd.decrypt(encryted)

            with open(self.bb, 'wb') as decrypted_files:
                decrypted_files.write(decrypt)

            # with open(self.bb, 'rt') as mykey3:
            #     key3 = mykey3.read()
            success = 'Decrypted SuccessFully'
            self.plainText.setPlainText(f'{success}')
        except AttributeError:
            self.message = "Oops Key is needed...."
            self.keygenerator.setStyleSheet("color: red")
            self.keygenerator.setText(self.message)




class DatabaseForm(QWidget):
    def __init__(self):
        super().__init__()

        self.left =60
        self.top =100
        self.width =1230
        self.height =500
        self.DatabaseWindow()
        # self.setStyleSheet("background: #eff1f6; color: #eee")
        self.setFixedSize(self.width, self.height)
        # self.setWindowModality(Qt.ApplicationModal)
        
        self.setStyleSheet("background: #21a0fa; color: #fff; border: 1px solid #3477b6;")
    

    def DatabaseWindow(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(' Database Table')

        self.btn_database = QPushButton(self)
        self.btn_database.setGeometry(1120, 5, 101, 31)
        self.btn_database.setFont(QtGui.QFont('consola', 12))
        self.btn_database.setObjectName("pushButton")
        self.btn_database.setText("Query")
        self.btn_database.setToolTip('Query the Database')
        self.btn_database.setStyleSheet("background: #eee; color: #333; border-radius: 2px;")
        self.btn_database.clicked.connect(self.loadTable)

      
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 45, 1230, 500))
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setFont(QtGui.QFont('consola', 10))
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)
        header = ['Id','KeyName', 'KeyValue', 'FileName', 'Date', 'Time', 'Day']
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 290)
        self.tableWidget.setColumnWidth(3, 290)
        self.tableWidget.setColumnWidth(4, 140)
        self.tableWidget.setColumnWidth(5, 140)
        self.tableWidget.setColumnWidth(6, 140)
        
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.setStyleSheet("background: #fff; color: #007300; border: 1px solid #007300; border: none; font-size: 15px;")


    def loadTable(self):
        self.conn = sqlite3.connect('encryption_decryption_storebase.db')
        self.cursor="SELECT * FROM encryption_decryption_storebase"
        self.result = self.conn.execute(self.cursor)
        self.tableWidget.setRowCount(0)

        for row_num, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        
        self.conn.commit()
        self.conn.rollback()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # win = LogForm()
    # win.show()
    sys.exit(app.exec_())