from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import time
import pydicom
import os

import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


def imNormalize(img):
    img_norm = (img - np.min(img)) / (np.max(img) - np.min(img))
    return img_norm

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
        self.progressBar.hide()


        self.img_arr = 255 * np.ones([100, 100],dtype = 'uint8')
        self.slice_img = 0
        self.img_volume = None

        self.figure = plt.figure()
        self.figure.patch.set_facecolor('k')
        self.img_canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.img_canvas)
        self.img_ax = self.img_canvas.figure.subplots()
        plt.subplots_adjust(left = 0.001, bottom = 0.001, right = 0.998, top = 0.999)
        self.img_ax.imshow(self.img_arr, cmap = 'gray', vmin = 0, vmax = 1, aspect = 'auto')
        self.img_ax.axis('off')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dicom3D_viewer"))
        self.load_button.setText(_translate("Dialog", "Load"))
        self.img_path.setText(_translate("Dialog", " "))
        
        self.img_slider.valueChanged.connect(self.getSlice)

        self.load_button.clicked.connect(self.readExam)


    def getSlice(self):
        self.slice_img = self.img_slider.value()
        self.slice.setText(str(self.slice_img))
        if self.img_volume is None:
            pass
        else:
            self.refreshAxes()

    def refreshAxes(self):
        self.img_ax.clear()        
        self.img_ax.imshow(self.img_volume[:, :, self.slice_img], cmap = 'gray', 
                           vmin = 0, vmax = 1, aspect = 'auto')
        self.img_ax.axis('off')
        self.img_ax.figure.canvas.draw()  

    def readExam(self):
        exam_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Image")
        dicom_list = None
        if exam_path:
            exam_path = os.path.join(exam_path,'DICOM')
            dicom_names = os.listdir(exam_path)
            dicom_list = [os.path.join(exam_path, dicom_name) for dicom_name in dicom_names]
            
            self.img_slider.setProperty("value", 0)
            self.slice_img = 0
            self.createExam3D(dicom_list)
            self.refreshAxes()
            self.img_slider.setMaximum(len(dicom_list) - 1)
            

    def createExam3D(self, dicom_list):

        dicom_obj = pydicom.dcmread(dicom_list[0])
        dicom_img = dicom_obj.pixel_array
        img_volume = np.zeros((dicom_img.shape[0], dicom_img.shape[1], len(dicom_list)), dtype = 'float')

        complete = 0
        self.progressBar.show()

        for dicom in dicom_list:
            dicom_obj = pydicom.dcmread(dicom)
            dicom_img = dicom_obj.pixel_array
            img_slice = dicom_obj.InstanceNumber - 1
            img_volume[:, :, img_slice] = imNormalize(dicom_img)

            complete += (100/len(dicom_list))
            self.progressBar.setValue(complete)
            time.sleep(0.01)
        self.img_volume = img_volume
        self.progressBar.hide()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

