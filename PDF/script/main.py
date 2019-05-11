#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license

# Title: PyQt5 lesson 14              Version: 1.0
# Date: 09-01-17                      Language: python3
# Description: pyqt5 gui and opening files
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################
# do something


import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

import matplotlib.pyplot as plt
import cv2

from load import *


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 120, 70)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))

        # extractAction = QAction('&Get to the choppah', self)
        # extractAction.setShortcut('Ctrl+Q')
        # extractAction.setStatusTip('leave the app')
        # extractAction.triggered.connect(self.close_application)

        # openEditor = QAction('&Editor', self)
        # openEditor.setShortcut('Ctrl+E')
        # openEditor.setStatusTip('Open Editor')
        # openEditor.triggered.connect(self.editor)

        openFile = QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        # self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        # fileMenu.addAction(extractAction)

        fileMenu.addAction(openFile)

        # cal.resize(200, 200)

        self.home()

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)



    def file_open(self):

        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        classify(detector, name)

    def upload(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        classify(detector, name)
        
        
    def home(self):
        self.btn = QPushButton('Upload', self)
        self.btn.move(10, 30)
        self.btn.clicked.connect(self.upload)


        self.show()



if __name__ == "__main__":  # had to add this otherwise app crashed
    global detector
    model_weight_path = "../../resnet50_v2.0.1.h5"

    # execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(model_weight_path)
    detector.loadModel()

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
