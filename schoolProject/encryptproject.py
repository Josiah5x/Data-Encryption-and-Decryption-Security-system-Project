# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RVS223.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 629)
        MainWindow.setStyleSheet("*{\n"
"\n"
"color: #000;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: balck;\n"
"font-size: 14px;\n"
"background: none;\n"
"}\n"
"\n"
"#frame{\n"
"background: rgb(0, 0, 76);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#frame_3{\n"
"background: #f8f8f8 ;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#listView{\n"
"border: 1px solid #008;\n"
"background: #fff;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#plainTextEdit{\n"
"background: #fff;\n"
"border-radius: 4px;\n"
"border: 1px solid #008;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: none;\n"
"border-radius: 4px;\n"
"color: #fff;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTextEdit{\n"
"background: ghostwhite;\n"
"border: 2px solid rgb(46, 140, 140);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #f0f0f0;\n"
"border: 2px solid rgb(46, 140, 140);\n"
"border-radius: 4px;\n"
"color: #fff;\n"
"font-size: 15px;\n"
"\n"
"}\n"
"\n"
"#frame_2{\n"
"background: #191966;\n"
"\n"
"}\n"
"\n"
"#frame_2:hover{\n"
"background: #050514;\n"
"\n"
"}\n"
"\n"
"#frame_4{\n"
"background: #191966;\n"
"\n"
"}\n"
"\n"
"#frame_4:hover{\n"
"background: #050514;\n"
"\n"
"}\n"
"\n"
"#frame_5{\n"
"background: #191966;\n"
"\n"
"}\n"
"\n"
"#frame_5:hover{\n"
"background: #050514;\n"
"\n"
"}\n"
"\n"
"#frame_9{\n"
"background: #191966;\n"
"\n"
"}\n"
"\n"
"#frame_9:hover{\n"
"background: #050514;\n"
"\n"
"}\n"
"\n"
"#frame_10{\n"
"background: #191966;\n"
"\n"
"}\n"
"\n"
"#frame_10:hover{\n"
"background: #050514;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 30, 981, 621))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(660, 70, 321, 441))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listView = QtWidgets.QListView(self.frame_3)
        self.listView.setGeometry(QtCore.QRect(90, 70, 561, 441))
        self.listView.setObjectName("listView")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(0, 0, 81, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 81, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.pushButton_3.setStyleSheet("border-image: url(:/image/key.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_7.setObjectName("label_7")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 110, 81, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.pushButton.setStyleSheet("border-image: url(:/image/lock.ico);\n"
" background-repeat: no-repeat;\n"
" background-position: center;\n"
" background-attachment: fixed;\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.label_8.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_8.setObjectName("label_8")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 200, 81, 91))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.pushButton_2.setStyleSheet("border-image: url(:/image/images/keys_open.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_9.setObjectName("label_9")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(0, 290, 81, 91))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.pushButton_5.setStyleSheet("border-image: url(:/image/user.ico);\n"
" background-repeat: no-repeat;\n"
" background-position: center;\n"
" background-attachment: fixed;\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.frame_9)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_12.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_12.setObjectName("label_12")
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setGeometry(QtCore.QRect(0, 380, 81, 91))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.pushButton_8.setStyleSheet("border-image: url(:/image/control-center.ico);\n"
" background-repeat: no-repeat;\n"
" background-position: center;\n"
" background-attachment: fixed;\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_14 = QtWidgets.QLabel(self.frame_10)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_14.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_14.setObjectName("label_14")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(710, 30, 211, 41))
        self.frame_7.setStyleSheet("#frame_7{\n"
"\n"
"background:  #0a0a29;\n"
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
        self.label_3.setGeometry(QtCore.QRect(70, 10, 111, 21))
        self.label_3.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"background: none;\n"
"color: #fff;")
        self.label_3.setObjectName("label_3")
        self.frame_13 = QtWidgets.QFrame(self.frame_7)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.frame_13.setStyleSheet("border-image: url(:/image/org.libreoffice.LibreOffice-writer.ico);\n"
"background:  #008;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setGeometry(QtCore.QRect(80, 520, 931, 31))
        self.frame_12.setStyleSheet("background: rgb(0, 0, 127)")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setGeometry(QtCore.QRect(6, 10, 441, 21))
        self.label_5.setStyleSheet("font-size: 13px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"background: none;\n"
"color: #fff;")
        self.label_5.setObjectName("label_5")
        self.label_16 = QtWidgets.QLabel(self.frame_12)
        self.label_16.setGeometry(QtCore.QRect(590, 10, 231, 21))
        self.label_16.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"background: none;\n"
"color: #fff;")
        self.label_16.setObjectName("label_16")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 561, 31))
        self.comboBox.setObjectName("comboBox")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.frame_6.setStyleSheet("background: rgb(85, 170, 255);\n"
"box-shadow: 10px 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_6.setStyleSheet("font-size: 15px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"background: none;\n"
"color: #f1f1f1;")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(160, 0, 211, 41))
        self.label.setStyleSheet("font-size: 15px;\n"
"font-weight: bold;\n"
"font-family: Raleway;\n"
"text-align: center;\n"
"background: none;\n"
"color: #f1f1f1;")
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(140, 10, 16, 21))
        self.label_15.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"\n"
"color: #f1f1f1;")
        self.label_15.setObjectName("label_15")
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setGeometry(QtCore.QRect(880, 0, 51, 51))
        self.frame_14.setStyleSheet("border-image: url(:/image/PngItem_2666090.png);\n"
"border-radius: 80px")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_6)
        self.frame_15.setGeometry(QtCore.QRect(930, 0, 51, 51))
        self.frame_15.setStyleSheet("border-image: url(:/image/371-3715555_nasarawa-state-university-keffi-nsuk.png);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(550, -10, 331, 51))
        self.label_11.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"background: none;\n"
"color: #006;")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(610, 20, 191, 41))
        self.label_2.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"font-family: Raleway;\n"
"background: none;\n"
"color: #006;")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(60, 30, 221, 16))
        self.label_10.setStyleSheet(" color: rgb(79, 79, 79)")
        self.label_10.setObjectName("label_10")
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
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Create Key"))
        self.label_8.setText(_translate("MainWindow", "Encrypt"))
        self.label_9.setText(_translate("MainWindow", "Decrypt"))
        self.label_12.setText(_translate("MainWindow", "Register"))
        self.label_14.setText(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "DISPLAY Result"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Data Encryption"))
        self.label.setText(_translate("MainWindow", " Decryption security System"))
        self.label_15.setText(_translate("MainWindow", "&"))
        self.label_11.setText(_translate("MainWindow", "NASARAWA STATE UNIVERSITY KEFFI"))
        self.label_2.setText(_translate("MainWindow", "COMPUTER SCIENCE"))
        self.label_10.setText(_translate("MainWindow", "Your files safety is very importance"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", ".."))
        self.menu_2.setTitle(_translate("MainWindow", "..."))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
