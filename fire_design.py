# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alca0\Documents\Python_Scripts\fire\fire_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(995, 767)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        self.comecar_button = QtWidgets.QPushButton(Dialog)
        self.comecar_button.setGeometry(QtCore.QRect(240, 670, 151, 61))
        self.comecar_button.setObjectName("comecar_button")
        self.wind_slider = QtWidgets.QSlider(Dialog)
        self.wind_slider.setGeometry(QtCore.QRect(100, 620, 851, 20))
        self.wind_slider.setMinimum(0)
        self.wind_slider.setMaximum(10)
        self.wind_slider.setPageStep(2)
        self.wind_slider.setProperty("value", 0)
        self.wind_slider.setOrientation(QtCore.Qt.Horizontal)
        self.wind_slider.setObjectName("wind_slider")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 10, 851, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.parar_button = QtWidgets.QPushButton(Dialog)
        self.parar_button.setGeometry(QtCore.QRect(610, 670, 151, 61))
        self.parar_button.setObjectName("parar_button")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(820, 660, 120, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.esquerda_button = QtWidgets.QRadioButton(self.groupBox)
        self.esquerda_button.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.esquerda_button.setChecked(True)
        self.esquerda_button.setObjectName("esquerda_button")
        self.direita_button = QtWidgets.QRadioButton(self.groupBox)
        self.direita_button.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.direita_button.setObjectName("direita_button")
        self.fire_slider = QtWidgets.QSlider(Dialog)
        self.fire_slider.setGeometry(QtCore.QRect(42, 20, 20, 571))
        self.fire_slider.setMinimum(15)
        self.fire_slider.setMaximum(100)
        self.fire_slider.setPageStep(10)
        self.fire_slider.setOrientation(QtCore.Qt.Vertical)
        self.fire_slider.setInvertedAppearance(False)
        self.fire_slider.setInvertedControls(True)
        self.fire_slider.setObjectName("fire_slider")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fire_Doom"))
        self.comecar_button.setText(_translate("Dialog", "Começar"))
        self.parar_button.setText(_translate("Dialog", "Parar"))
        self.esquerda_button.setText(_translate("Dialog", "Esquerda"))
        self.direita_button.setText(_translate("Dialog", "Direita"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

