# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alca0\Documents\Python_Scripts\dicom_ui\dicom_ui_design.ui'
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
        self.load_button = QtWidgets.QPushButton(Dialog)
        self.load_button.setGeometry(QtCore.QRect(20, 670, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.load_button.setFont(font)
        self.load_button.setObjectName("load_button")
        self.img_slider = QtWidgets.QSlider(Dialog)
        self.img_slider.setGeometry(QtCore.QRect(20, 620, 821, 20))
        self.img_slider.setMinimum(0)
        self.img_slider.setMaximum(10)
        self.img_slider.setPageStep(2)
        self.img_slider.setProperty("value", 0)
        self.img_slider.setOrientation(QtCore.Qt.Horizontal)
        self.img_slider.setObjectName("img_slider")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 931, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.slice = QtWidgets.QLabel(Dialog)
        self.slice.setGeometry(QtCore.QRect(870, 610, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.slice.setFont(font)
        self.slice.setText("")
        self.slice.setObjectName("slice")
        self.img_path = QtWidgets.QLabel(Dialog)
        self.img_path.setGeometry(QtCore.QRect(190, 675, 441, 41))
        self.img_path.setObjectName("img_path")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(270, 680, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dicom3D_viewer"))
        self.load_button.setText(_translate("Dialog", "Load"))
        self.img_path.setText(_translate("Dialog", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

