# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinner_trough_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_spinnnerDialogBase(object):
    def setupUi(self, spinnnerDialogBase):
        spinnnerDialogBase.setObjectName("spinnnerDialogBase")
        spinnnerDialogBase.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(spinnnerDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(spinnnerDialogBase)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(spinnnerDialogBase)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(spinnnerDialogBase)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(spinnnerDialogBase)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(spinnnerDialogBase)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mQgsSpinBox = gui.QgsSpinBox(spinnnerDialogBase)
        self.mQgsSpinBox.setObjectName("mQgsSpinBox")
        self.verticalLayout.addWidget(self.mQgsSpinBox)
        self.button_box = QtWidgets.QDialogButtonBox(spinnnerDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(spinnnerDialogBase)
        self.button_box.accepted.connect(spinnnerDialogBase.accept)
        self.button_box.rejected.connect(spinnnerDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(spinnnerDialogBase)

    def retranslateUi(self, spinnnerDialogBase):
        _translate = QtCore.QCoreApplication.translate
        spinnnerDialogBase.setWindowTitle(_translate("spinnnerDialogBase", "spinner"))
        self.label.setText(_translate("spinnnerDialogBase", "QSpinBox Count: "))
        self.label_2.setText(_translate("spinnnerDialogBase", "QDoubleSpinBoxCount: "))
        self.label_3.setText(_translate("spinnnerDialogBase", "QgsSPinBox COunt: "))

from qgis import gui
