# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MapCreatorDlg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapCreatorDlg(object):
    def setupUi(self, MapCreatorDlg):
        MapCreatorDlg.setObjectName("MapCreatorDlg")
        MapCreatorDlg.resize(401, 181)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapCreatorDlg.sizePolicy().hasHeightForWidth())
        MapCreatorDlg.setSizePolicy(sizePolicy)
        MapCreatorDlg.setMinimumSize(QtCore.QSize(401, 181))
        MapCreatorDlg.setMaximumSize(QtCore.QSize(401, 181))
        self.verticalLayoutWidget = QtWidgets.QWidget(MapCreatorDlg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Label1.setMinimumSize(QtCore.QSize(379, 0))
        self.Label1.setObjectName("Label1")
        self.verticalLayout.addWidget(self.Label1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tbxInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tbxInput.setObjectName("tbxInput")
        self.horizontalLayout_5.addWidget(self.tbxInput)
        self.btnBrowse1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBrowse1.setObjectName("btnBrowse1")
        self.horizontalLayout_5.addWidget(self.btnBrowse1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(MapCreatorDlg)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ProgressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout_3.addWidget(self.ProgressBar)
        self.btnRun = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout_3.addWidget(self.btnRun)
        self.btnExit = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_3.addWidget(self.btnExit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(MapCreatorDlg)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 381, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Label3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Label3.setObjectName("Label3")
        self.verticalLayout_3.addWidget(self.Label3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbxOutput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.tbxOutput.setObjectName("tbxOutput")
        self.horizontalLayout_2.addWidget(self.tbxOutput)
        self.btnBrowse2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnBrowse2.setObjectName("btnBrowse2")
        self.horizontalLayout_2.addWidget(self.btnBrowse2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MapCreatorDlg)
        QtCore.QMetaObject.connectSlotsByName(MapCreatorDlg)

    def retranslateUi(self, MapCreatorDlg):
        _translate = QtCore.QCoreApplication.translate
        MapCreatorDlg.setWindowTitle(_translate("MapCreatorDlg", "Map Creator"))
        self.Label1.setText(_translate("MapCreatorDlg", "Select input coordinate file:"))
        self.tbxInput.setToolTip(_translate("MapCreatorDlg", "Give the filepath and filename of the output shapefile"))
        self.btnBrowse1.setToolTip(_translate("MapCreatorDlg", "Gives dialog box for selecting output filepath and filename."))
        self.btnBrowse1.setText(_translate("MapCreatorDlg", "Browse"))
        self.btnRun.setText(_translate("MapCreatorDlg", "Run"))
        self.btnExit.setText(_translate("MapCreatorDlg", "Exit"))
        self.Label3.setText(_translate("MapCreatorDlg", "Specify output shapefile:"))
        self.tbxOutput.setToolTip(_translate("MapCreatorDlg", "Give the filepath and filename of the output shapefile"))
        self.btnBrowse2.setToolTip(_translate("MapCreatorDlg", "Gives dialog box for selecting output filepath and filename."))
        self.btnBrowse2.setText(_translate("MapCreatorDlg", "Browse"))
