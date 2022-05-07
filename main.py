# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ctypes import alignment
from msilib.schema import tables
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtTest import *

import random
from os import environ
from InputScheduling import start_scheduling


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.I_P_Label = []
        self.I_P_AT = []
        self.I_P_BT = []

        self.pCount = 15
        self.cCount = 4
        # self.cColor = ["rgb(21, 139, 230)","rgb(91, 172, 234)","rgb(40, 75, 102)","rgb(16, 108, 179)"]
        self.cColor = [(139, 71, 252), (77, 85, 230), (71, 155, 252), (68, 221, 242)]

        self.I_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.I_groupBox.setGeometry(QtCore.QRect(20, 10, 521, 421))
        self.I_groupBox.setObjectName("I_groupBox")

        self.I_RGroupBox = QtWidgets.QGroupBox(self.I_groupBox)
        self.I_RGroupBox.setGeometry(QtCore.QRect(10, 20, 501, 61))
        self.I_RGroupBox.setObjectName("I_RGroupBox")

        self.I_R_Button = QtWidgets.QPushButton(self.I_RGroupBox)
        self.I_R_Button.setGeometry(QtCore.QRect(290, 30, 51, 21))
        self.I_R_Button.setObjectName("I_R_Button")
        self.I_R_Button.clicked.connect(self.setPCCount)

        self.I_R_PCombo = QtWidgets.QComboBox(self.I_RGroupBox)
        self.I_R_PCombo.setGeometry(QtCore.QRect(10, 30, 131, 22))
        self.I_R_PCombo.setObjectName("I_R_PCombo")
        self.I_R_CCombo = QtWidgets.QComboBox(self.I_RGroupBox)
        self.I_R_CCombo.setGeometry(QtCore.QRect(150, 30, 131, 22))
        self.I_R_CCombo.setObjectName("I_R_CCombo")

        self.I_R_label1 = QtWidgets.QLabel(self.I_RGroupBox)
        self.I_R_label1.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.I_R_label1.setObjectName("I_R_label1")
        self.I_R_label2 = QtWidgets.QLabel(self.I_RGroupBox)
        self.I_R_label2.setGeometry(QtCore.QRect(150, 10, 111, 21))
        self.I_R_label2.setObjectName("I_R_label2")

        self.I_C_GroupBox = QtWidgets.QGroupBox(self.I_groupBox)
        self.I_C_GroupBox.setGeometry(QtCore.QRect(310, 80, 201, 181))
        self.I_C_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.I_C_GroupBox.setObjectName("CoreBox")
        self.I_C_GroupBox.raise_()

        self.I_C_Layout = QtWidgets.QWidget(self.I_C_GroupBox)
        self.I_C_Layout.setGeometry(QtCore.QRect(10, 20, 171, 151))
        self.I_C_Layout.setObjectName("I_C_Layout")

        self.I_C_Grid = QtWidgets.QGridLayout(self.I_C_Layout)
        self.I_C_Grid.setObjectName("I_C_Grid")

        self.I_C_PButton = []
        self.I_C_EButton = []
        self.I_C_C_GroupBox = []

        for i in range(4):
            groupBox = QtWidgets.QGroupBox(self.I_C_Layout)
            groupBox.setEnabled(True)
            groupBox.setObjectName("I_C_groupBox" + str(i))
            self.I_C_C_GroupBox.append(groupBox)

            PButton = QtWidgets.QRadioButton(groupBox)
            PButton.setGeometry(QtCore.QRect(10, 20, 71, 16))
            PButton.setChecked(True)
            PButton.setObjectName("I_C_PButton" + str(i))
            self.I_C_PButton.append(PButton)

            EButton = QtWidgets.QRadioButton(groupBox)
            EButton.setGeometry(QtCore.QRect(10, 40, 71, 16))
            EButton.setChecked(False)
            EButton.setObjectName("I_C_EButton" + str(i))
            self.I_C_EButton.append(EButton)

            # groupBox.toggled['bool'].connect(PButton.setEnabled)
            # groupBox.toggled['bool'].connect(EButton.setEnabled)

            # self.I_C_Grid.setContentsMargins(0, 0, 0, 0)
            self.I_C_Grid.addWidget(groupBox, int(i / 2), int(i % 2), 1, 1)

        self.I_ScheduleComboBox = QtWidgets.QComboBox(self.I_groupBox)
        self.I_ScheduleComboBox.setGeometry(QtCore.QRect(310, 270, 201, 21))
        self.I_ScheduleComboBox.setObjectName("I_ScheduleComboBox")
        self.I_ScheduleComboBox.addItem("FCFS")
        self.I_ScheduleComboBox.addItem("RR")
        self.I_ScheduleComboBox.addItem("SPN")
        self.I_ScheduleComboBox.addItem("SRTN")
        self.I_ScheduleComboBox.addItem("HRRN")
        self.I_ScheduleComboBox.addItem("P-HRRN")
        self.I_ScheduleComboBox.currentIndexChanged.connect(
            lambda index: self.I_RRTimeGroupBox.setEnabled(True if (index == 1 or index == 5) else False))
        self.I_ScheduleComboBox.raise_()

        self.I_RRTimeGroupBox = QtWidgets.QGroupBox(self.I_groupBox)
        self.I_RRTimeGroupBox.setEnabled(False)
        self.I_RRTimeGroupBox.setGeometry(QtCore.QRect(310, 300, 201, 41))
        self.I_RRTimeGroupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        # self.I_RRTimeGroupBox.setStyleSheet("")
        # self.I_RRTimeGroupBox.setTitle("")
        self.I_RRTimeGroupBox.setObjectName("I_RRTimeGroupBox")
        self.I_RRTimeGroupBox.raise_()

        self.I_RRTimeSpinBox = QtWidgets.QSpinBox(self.I_RRTimeGroupBox)
        self.I_RRTimeSpinBox.setGeometry(QtCore.QRect(100, 10, 41, 22))
        self.I_RRTimeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.I_RRTimeSpinBox.setAlignment(QtCore.Qt.AlignRight)

        self.I_RR_label1 = QtWidgets.QLabel(self.I_RRTimeGroupBox)
        self.I_RR_label1.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.I_RR_label1.setObjectName("I_RR_label1")
        self.I_RR_label2 = QtWidgets.QLabel(self.I_RRTimeGroupBox)
        self.I_RR_label2.setGeometry(QtCore.QRect(150, 10, 41, 21))
        self.I_RR_label2.setObjectName("I_RR_label2")

        self.I_StartButton = QtWidgets.QPushButton(self.I_groupBox)
        self.I_StartButton.setGeometry(QtCore.QRect(310, 350, 201, 61))
        self.I_StartButton.setObjectName("I_StartButton")
        self.I_StartButton.clicked.connect(self.doStart)
        self.I_StartButton.raise_()

        self.Consume_Group = QtWidgets.QGroupBox(self.centralwidget)
        self.Consume_Group.setGeometry(QtCore.QRect(550, 340, 131, 91))
        self.Consume_Group.setCheckable(False)
        self.Consume_Group.setObjectName("Consume_Group")

        self.Consume_SpinBox = []
        for i in range(4):
            spinBox = QtWidgets.QDoubleSpinBox(self.Consume_Group)
            spinBox.setGeometry(QtCore.QRect(10 + 55 * int(i % 2), 20 + 30 * int(i / 2), 56, 31))
            spinBox.setFrame(True)
            spinBox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinBox.setObjectName("Consume_spinBox" + str(i))
            spinBox.setReadOnly(True)
            spinBox.setSuffix(' W')
            spinBox.setStyleSheet("border: 1px solid rgb" + str(self.cColor[i]))
            spinBox.setMaximum(1000)
            spinBox.setDecimals(1)
            self.Consume_SpinBox.append(spinBox)

        self.RQ_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.RQ_GroupBox.setGeometry(QtCore.QRect(690, 340, 311, 91))
        self.RQ_GroupBox.setObjectName("RQ_GroupBox")

        self.RQ_HLWidget = QtWidgets.QWidget(self.RQ_GroupBox)
        self.RQ_HLWidget.setGeometry(QtCore.QRect(10, 20, 291, 61))
        self.RQ_HLWidget.setObjectName("RQ_HLWidget")

        self.RQ_HLayout = QtWidgets.QHBoxLayout(self.RQ_HLWidget)
        self.RQ_HLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.RQ_HLayout.setContentsMargins(0, 0, 0, 0)
        self.RQ_HLayout.setSpacing(6)
        self.RQ_HLayout.setObjectName("RQ_HLayout")

        for i in range(15):
            label = QtWidgets.QLabel(self.RQ_HLWidget)
            label.setFixedSize(QtCore.QSize(14, 59))
            label.setStyleSheet("background-color: rgb(255, 255, 255);")
            label.setObjectName("pQueueElement" + str(i + 1))
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.RQ_HLayout.addWidget(label)
            # label.setText(QtCore.QCoreApplication.translate("MainWindow", "P"+str(i+1)))

        self.I_P_GroupBox = QtWidgets.QGroupBox(self.I_groupBox)
        self.I_P_GroupBox.setGeometry(QtCore.QRect(10, 80, 291, 331))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.I_P_GroupBox.setFont(font)
        self.I_P_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.I_P_GroupBox.setObjectName("I_P_GroupBox")

        self.gridLayoutWidget = QtWidgets.QWidget(self.I_P_GroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.I_P_PLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.I_P_PLabel.setMaximumSize(QtCore.QSize(70, 16777215))
        self.I_P_PLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.I_P_PLabel.setObjectName("I_P_PLabel")
        self.gridLayout.addWidget(self.I_P_PLabel, 0, 0, 1, 1)

        self.I_P_ATLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.I_P_ATLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.I_P_ATLabel.setObjectName("I_P_ATLabel")
        self.gridLayout.addWidget(self.I_P_ATLabel, 0, 1, 1, 1)

        self.I_P_BTLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.I_P_BTLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.I_P_BTLabel.setObjectName("I_P_BTLabel")
        self.gridLayout.addWidget(self.I_P_BTLabel, 0, 2, 1, 1)

        self.I_P_PLabel.setFixedHeight(20)
        self.I_P_ATLabel.setFixedHeight(20)
        self.I_P_BTLabel.setFixedHeight(20)
        self.gridLayout.setRowStretch(16, 20)
        self.I_P_GroupBox.raise_()

        self.G_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.G_GroupBox.setGeometry(QtCore.QRect(20, 430, 981, 401))
        self.G_GroupBox.setObjectName("G_GroupBox")

        self.G_TableWidget = QtWidgets.QTableWidget(self.G_GroupBox)
        self.G_TableWidget.setGeometry(QtCore.QRect(10, 50, 951, 341))
        self.G_TableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.G_TableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.G_TableWidget.setAutoScroll(True)
        self.G_TableWidget.setRowCount(15)
        self.G_TableWidget.setColumnCount(40)
        self.G_TableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G_TableWidget.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        self.G_TableWidget.setObjectName("G_TableWidget")

        for i in range(15):
            item = QtWidgets.QTableWidgetItem()
            self.G_TableWidget.setVerticalHeaderItem(i, item)

        for r in range(self.G_TableWidget.rowCount()):
            for c in range(self.G_TableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.G_TableWidget.setItem(r, c, item)

        self.G_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.G_TableWidget.horizontalHeader().setMaximumSectionSize(23)
        self.G_TableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.G_TableWidget.horizontalHeader().setDefaultSectionSize(23)
        #self.G_TableWidget.verticalHeader().setMinimumSectionSize(20)
        self.G_TableWidget.verticalHeader().setMaximumSectionSize(20)
        self.G_TableWidget.verticalHeader().setDefaultSectionSize(20)
        self.G_TableWidget.verticalHeader().setFixedWidth(29)

        self.R_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.R_GroupBox.setGeometry(QtCore.QRect(550, 10, 451, 321))
        self.R_GroupBox.setObjectName("R_GroupBox")

        self.R_TableWidget = QtWidgets.QTableWidget(self.R_GroupBox)
        self.R_TableWidget.setGeometry(QtCore.QRect(10, 20, 431, 295))
        self.R_TableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.R_TableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.R_TableWidget.setAutoScroll(True)
        self.R_TableWidget.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        self.R_TableWidget.setRowCount(15)
        self.R_TableWidget.setColumnCount(5)
        self.R_TableWidget.setObjectName("R_TableWidget")
        self.R_TableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")

        for i in range(15):
            item = QtWidgets.QTableWidgetItem()
            self.R_TableWidget.setVerticalHeaderItem(i, item)
        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.R_TableWidget.setHorizontalHeaderItem(i, item)

        for r in range(self.R_TableWidget.rowCount()):
            for c in range(self.R_TableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.R_TableWidget.setItem(r, c, item)

        self.R_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.R_TableWidget.horizontalHeader().setMaximumSectionSize(80)
        self.R_TableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.R_TableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.R_TableWidget.verticalHeader().setMaximumSectionSize(18)
        self.R_TableWidget.verticalHeader().setDefaultSectionSize(18)
        self.R_TableWidget.verticalHeader().setFixedWidth(29)

        self.powerConsumeSpinBox = QtWidgets.QDoubleSpinBox(self.G_GroupBox)
        self.powerConsumeSpinBox.setGeometry(QtCore.QRect(730, 20, 81, 22))
        self.powerConsumeSpinBox.setFrame(True)
        self.powerConsumeSpinBox.setReadOnly(True)
        self.powerConsumeSpinBox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.powerConsumeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.powerConsumeSpinBox.setMaximum(10000)
        self.powerConsumeSpinBox.setDecimals(1)
        self.powerConsumeSpinBox.setObjectName("powerConsumeSpinBox")

        self.nowTimeSpinBox = QtWidgets.QSpinBox(self.G_GroupBox)
        self.nowTimeSpinBox.setGeometry(QtCore.QRect(880, 20, 81, 22))
        self.nowTimeSpinBox.setFrame(True)
        self.nowTimeSpinBox.setReadOnly(True)
        self.nowTimeSpinBox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.nowTimeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.nowTimeSpinBox.setMaximum(10000)
        self.nowTimeSpinBox.setObjectName("nowTimeSpinBox")

        self.powerConsume = QtWidgets.QLabel(self.G_GroupBox)
        self.powerConsume.setGeometry(QtCore.QRect(670, 20, 51, 21))
        self.powerConsume.setObjectName("powerConsume")
        self.nowTime = QtWidgets.QLabel(self.G_GroupBox)
        self.nowTime.setGeometry(QtCore.QRect(820, 20, 51, 21))
        self.nowTime.setObjectName("nowTime")

        MainWindow.setCentralWidget(self.centralwidget)
        for i in range(15):
            label = QtWidgets.QLabel(self.gridLayoutWidget)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setObjectName("I_P_Label" + str(i + 1))
            self.gridLayout.addWidget(label, i + 1, 0, 1, 1)
            self.I_P_Label.append(label)

            processAT = QtWidgets.QSpinBox(self.gridLayoutWidget)
            # processAT.setEnabled(False)
            processAT.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            processAT.setObjectName("processAT" + str(i + 1))
            processAT.setFixedHeight(17)
            self.gridLayout.addWidget(processAT, i + 1, 1, 1, 1)

            processBT = QtWidgets.QSpinBox(self.gridLayoutWidget)
            # processBT.setEnabled(False)
            processBT.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            processBT.setObjectName("processAT" + str(i + 1))
            processBT.setFixedHeight(17)
            self.gridLayout.addWidget(processBT, i + 1, 2, 1, 1)

            self.I_P_AT.append(processAT)
            self.I_P_BT.append(processBT)

            '''
            cbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            cbox.setMaximumSize(QtCore.QSize(70, 16777215))
            cbox.setObjectName("processCheckBox"+str(i))
            cbox.toggled['bool'].connect(self.I_P_AT[i].setEnabled)
            cbox.toggled['bool'].connect(self.I_P_BT[i].setEnabled)
            self.gridLayout.addWidget(cbox, i+1, 0, 1, 1, QtCore.Qt.AlignHCenter)
            self.I_P_Label.append(cbox)
            '''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "프로세스 스케줄링"))

        self.Consume_Group.setTitle(_translate("MainWindow", "코어 소모전력"))
        self.RQ_GroupBox.setTitle(_translate("MainWindow", "ReadyQueue"))
        self.G_GroupBox.setTitle(_translate("MainWindow", "GanttChart"))
        self.R_GroupBox.setTitle(_translate("MainWindow", "Result"))

        self.I_R_label1.setText(_translate("MainWindow", "프로세스 수(N):"))
        self.I_R_label2.setText(_translate("MainWindow", "프로세서 수(N):"))
        self.I_R_Button.setText(_translate("MainWindow", "설정"))

        for i in range(15):
            item = self.G_TableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", "P" + str(i + 1)))

        for i in range(15):
            item = self.R_TableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", "P" + str(i + 1)))

        item = self.R_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "AT"))
        item = self.R_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BT"))
        item = self.R_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "WT"))
        item = self.R_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TT"))
        item = self.R_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NTT"))

        self.I_groupBox.setTitle(_translate("MainWindow", "Input"))
        self.I_P_GroupBox.setTitle(_translate("MainWindow", "Process"))
        self.I_C_GroupBox.setTitle(_translate("MainWindow", "Core"))

        self.I_P_PLabel.setText(_translate("MainWindow", "Process"))
        self.I_P_ATLabel.setText(_translate("MainWindow", "ArrivalTime(AT)"))
        self.I_P_BTLabel.setText(_translate("MainWindow", "BurstTime(BT)"))

        for i in range(15):
            self.I_P_Label[i].setText(_translate("MainWindow", "P" + str(i + 1)))
            # if int(i / 5) == 0: rgb = "197, 12, 246, "
            # elif int(i / 5) == 1: rgb = "214, 18, 10, "
            self.I_P_Label[i].setStyleSheet("border: 1px solid white; background-color: " + self.getPColor(i + 1))

        for i in range(4):
            self.I_C_C_GroupBox[i].setStyleSheet("border: 3px solid rgb" + str(self.cColor[i]))

        for i in range(4):
            self.I_C_C_GroupBox[i].setTitle(_translate("MainWindow", "Core " + str(i + 1)))
            self.I_C_PButton[i].setText(_translate("MainWindow", "P Core"))
            self.I_C_EButton[i].setText(_translate("MainWindow", "E Core"))
            self.I_C_PButton[i].setStyleSheet("border: 0px")
            self.I_C_EButton[i].setStyleSheet("border: 0px")

        for i in range(15): self.I_R_PCombo.addItem(str(i + 1))
        for i in range(4):  self.I_R_CCombo.addItem(str(i + 1))
        self.I_R_PCombo.setCurrentIndex(14)
        self.I_R_CCombo.setCurrentIndex(3)

        self.I_RR_label1.setText(_translate("MainWindow", "TimeQuantum"))
        self.I_RR_label2.setText(_translate("MainWindow", "second(s)"))

        self.I_StartButton.setText(_translate("MainWindow", "시작"))

        self.nowTime.setText(_translate("MainWindow", "현재시간"))
        self.nowTimeSpinBox.setSuffix(_translate("MainWindow", " s"))
        self.powerConsume.setText(_translate("MainWindow", "소모전력"))
        self.powerConsumeSpinBox.setSuffix(_translate("MainWindow", " W"))

    def doStart(self):
        scheduling = self.I_ScheduleComboBox.currentText()
        process = self.pCount
        core = self.cCount
        pcore_id = []
        at_lst = []
        bt_lst = []
        tq = 0

        for pID in range(self.pCount):
            at_lst.append(self.I_P_AT[pID].value())
            bt_lst.append(self.I_P_BT[pID].value())
            print(pID + 1, self.I_P_AT[pID].value(), self.I_P_BT[pID].value())
        for cID in range(self.cCount):
            if self.I_C_PButton[cID].isChecked():
                pcore_id.append(cID + 1)
            print(cID + 1, \
                  "P Core" if self.I_C_PButton[cID].isChecked() else "E Core")

        if 0 in bt_lst:
            QtWidgets.QMessageBox.critical(self.main,'Error','잘못된 BT 값이 있습니다.')
            return

        print(self.I_ScheduleComboBox.currentText())
        if self.I_RRTimeSpinBox.isEnabled():
            tq = self.I_RRTimeSpinBox.value()
            print(self.I_RRTimeSpinBox.value())

        self.G_TableWidget.setRowCount(self.pCount)
        self.R_TableWidget.setRowCount(self.pCount)

        for i in range(self.pCount):
            item = QtWidgets.QTableWidgetItem()
            item.setText('P' + str(i + 1))
            self.G_TableWidget.setVerticalHeaderItem(i, item)

            item2 = QtWidgets.QTableWidgetItem()
            item2.setText('P' + str(i + 1))
            self.R_TableWidget.setVerticalHeaderItem(i, item2)

        # initialize
        for r in range(self.G_TableWidget.rowCount()):
            for c in range(self.G_TableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                item.setBackground(QtGui.QColor(255, 255, 255))
                self.G_TableWidget.setItem(r, c, item)

        for r in range(self.R_TableWidget.rowCount()):
            for c in range(self.R_TableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem('')
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.R_TableWidget.setItem(r, c, item)

        self.setReadyQueue([])
        self.setPowerConsume(0)
        self.setNowTime(0)
        for i in range(4): self.setCorePowerConsume(i, 0)
        self.G_TableWidget.setColumnCount(40)

        process_lst, processor_lst, queue_lst = \
            start_scheduling(self, scheduling, process, core, pcore_id, at_lst, bt_lst, tq)
        print("-----------")
        print(process_lst)  # 프로세스정보 출력
        print("-----------")
        print(processor_lst)  # 프로세서정보 출력
        print("-----------")
        print(queue_lst)  # 레디큐 정보 출력

    def setGTable(self, pID, time, cID):
        # self.G_TableWidget.setItem(pID-1, time-1, QtWidgets.QTableWidgetItem(str(time) + ' ' + str(pID)))
        if time > self.G_TableWidget.columnCount():
            for i in range(time - self.G_TableWidget.columnCount()):
                self.addGTableColumn()
        r, g, b = self.cColor[cID - 1]
        self.G_TableWidget.item(pID - 1, time - 1).setBackground(QtGui.QColor(r, g, b))

    def setReadyQueue(self, pList):
        pIndex = 0
        for i in range(15):
            if pIndex < len(pList):
                self.RQ_HLayout.itemAt(i).widget().setText(str(pList[pIndex]))
                self.RQ_HLayout.itemAt(i).widget().setStyleSheet("background-color: " + self.getPColor(pList[pIndex]))
                pIndex += 1
            else:
                self.RQ_HLayout.itemAt(i).widget().setText('')
                self.RQ_HLayout.itemAt(i).widget().setStyleSheet("background-color: rgb(255, 255, 255);")

    def setPowerConsume(self, power):
        self.powerConsumeSpinBox.setValue(power)

    def setCorePowerConsume(self, core, power):
        self.Consume_SpinBox[core - 1].setValue(power)

    def setNowTime(self, time):
        self.nowTimeSpinBox.setValue(time)

    def setResult(self, pID, col_code, value):
        self.R_TableWidget.setItem(pID - 1, col_code, QtWidgets.QTableWidgetItem(str(value)))

    def addGTableColumn(self):
        col = self.G_TableWidget.horizontalHeader().count() + 1
        self.G_TableWidget.setColumnCount(col)
        for r in range(self.G_TableWidget.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.G_TableWidget.setItem(r, col - 1, item)

    def setPCCount(self):
        self.pCount = int(self.I_R_PCombo.currentText())
        self.cCount = int(self.I_R_CCombo.currentText())

        for i in range(15):
            if i < self.pCount:
                self.I_P_Label[i].setHidden(False)
                self.I_P_AT[i].setHidden(False)
                self.I_P_BT[i].setHidden(False)
            else:
                self.I_P_Label[i].setHidden(True)
                self.I_P_AT[i].setHidden(True)
                self.I_P_BT[i].setHidden(True)

        for i in range(4):
            if i < self.cCount:
                self.I_C_C_GroupBox[i].setEnabled(True)
            else:
                self.I_C_C_GroupBox[i].setEnabled(False)

    def getPColor(self, p):
        return "rgba(235, 113, 34, " + str(255 - p * 16) + ')'

    def sleep(self):
        QTest.qWait(250)


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    import sys

    suppress_qt_warnings()

    app = QtWidgets.QApplication(sys.argv)
    # app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact Gi