# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinner_trough_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
# import os
from qgis import gui
# from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtCore

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
# FORM_CLASS, _ = uic.loadUiType(os.path.join(
#     os.path.dirname(__file__), 'spinner_trough_dialog_base.ui'))


class spinnnerDialog(QtWidgets.QDialog):
    """Form constructor sis """

    def __init__(self, parent=None):
        """Constructor."""
        super(spinnnerDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def setupUi(self, spinnnerDialog):
        """Pylint ignore"""
        spinnnerDialog.setObjectName("spinnnerDialog")
        spinnnerDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(spinnnerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(spinnnerDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(spinnnerDialog)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(spinnnerDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(spinnnerDialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(spinnnerDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mQgsSpinBox = gui.QgsSpinBox(spinnnerDialog)
        self.mQgsSpinBox.setObjectName("mQgsSpinBox")
        self.verticalLayout.addWidget(self.mQgsSpinBox)
        self.button_box = QtWidgets.QDialogButtonBox(spinnnerDialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(spinnnerDialog)
        self.button_box.accepted.connect(spinnnerDialog.accept)
        self.button_box.rejected.connect(spinnnerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(spinnnerDialog)

    def retranslateUi(self, spinnnerDialog):
        _translate = QtCore.QCoreApplication.translate
        spinnnerDialog.setWindowTitle(
            _translate("spinnnerDialogBase", "spinner"))
        self.label.setText(_translate(
            "spinnnerDialogBase", "QSpinBox Count: "))
        self.label_2.setText(_translate(
            "spinnnerDialogBase", "QDoubleSpinBoxCount: "))
        self.label_3.setText(_translate(
            "spinnnerDialogBase", "QgsSPinBox COunt: "))
