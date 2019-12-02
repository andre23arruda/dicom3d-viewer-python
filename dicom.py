from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import time
import pydicom
import os
from skimage import exposure, future, io
from scipy.ndimage import median_filter

import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


def imNormalize(img):
    img_norm = (img - np.min(img)) / (np.max(img) - np.min(img))
    return img_norm

def filterWarning():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)

    msg.setText("Please, wait the image processing")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

    answer = msg.exec()
    if answer == QtWidgets.QMessageBox.Ok:
        return True
    return False

def finishWarning():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)

    msg.setText("Image filtering finished!")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1017, 868)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        self.load_button = QtWidgets.QPushButton(Dialog)
        self.load_button.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.load_button.setFont(font)
        self.load_button.setObjectName("load_button")
        self.img_slider = QtWidgets.QSlider(Dialog)
        self.img_slider.setEnabled(False)
        self.img_slider.setGeometry(QtCore.QRect(20, 800, 771, 20))
        self.img_slider.setMinimum(0)
        self.img_slider.setMaximum(10)
        self.img_slider.setPageStep(2)
        self.img_slider.setProperty("value", 0)
        self.img_slider.setOrientation(QtCore.Qt.Horizontal)
        self.img_slider.setObjectName("img_slider")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 831, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.slice = QtWidgets.QLabel(Dialog)
        self.slice.setGeometry(QtCore.QRect(800, 780, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.slice.setFont(font)
        self.slice.setText("")
        self.slice.setObjectName("slice")
        self.warning_label = QtWidgets.QLabel(Dialog)
        self.warning_label.setGeometry(QtCore.QRect(860, 760, 161, 41))
        self.warning_label.setText("")
        self.warning_label.setObjectName("warning_label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 830, 831, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gamma_slider = QtWidgets.QSlider(Dialog)
        self.gamma_slider.setEnabled(False)
        self.gamma_slider.setGeometry(QtCore.QRect(880, 90, 22, 681))
        self.gamma_slider.setMinimum(1)
        self.gamma_slider.setMaximum(100)
        self.gamma_slider.setProperty("value", 10)
        self.gamma_slider.setOrientation(QtCore.Qt.Vertical)
        self.gamma_slider.setObjectName("gamma_slider")
        self.gamma_label = QtWidgets.QLabel(Dialog)
        self.gamma_label.setGeometry(QtCore.QRect(870, 50, 51, 31))
        self.gamma_label.setObjectName("gamma_label")
        self.gain_slider = QtWidgets.QSlider(Dialog)
        self.gain_slider.setEnabled(False)
        self.gain_slider.setGeometry(QtCore.QRect(920, 90, 22, 681))
        self.gain_slider.setMinimum(1)
        self.gain_slider.setMaximum(100)
        self.gain_slider.setProperty("value", 10)
        self.gain_slider.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider.setObjectName("gain_slider")
        self.gain_label = QtWidgets.QLabel(Dialog)
        self.gain_label.setGeometry(QtCore.QRect(920, 50, 31, 31))
        self.gain_label.setObjectName("gain_label")
        self.filter_slider = QtWidgets.QSlider(Dialog)
        self.filter_slider.setEnabled(False)
        self.filter_slider.setGeometry(QtCore.QRect(960, 90, 22, 681))
        self.filter_slider.setMinimum(1)
        self.filter_slider.setMaximum(10)
        self.filter_slider.setPageStep(3)
        self.filter_slider.setProperty("value", 1)
        self.filter_slider.setOrientation(QtCore.Qt.Vertical)
        self.filter_slider.setObjectName("filter_slider")
        self.filter_label = QtWidgets.QLabel(Dialog)
        self.filter_label.setGeometry(QtCore.QRect(960, 50, 31, 31))
        self.filter_label.setObjectName("filter_label")

        self.progressBar.hide()
        # Dialog.showMaximized()

        self.slice_img = 0
        self.img_volume = None
        self.gamma = 1
        self.gain = 1

        img_arr = 255 * np.ones([100, 100],dtype = 'uint8')
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('k')
        self.img_canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.img_canvas)
        self.img_ax = self.img_canvas.figure.subplots()
        plt.subplots_adjust(left = 0.001, bottom = 0.001, right = 0.998, top = 0.999)
        self.img_ax.imshow(img_arr, cmap = 'gray', vmin = 0, vmax = 1, aspect = 'auto')
        self.img_ax.axis('off')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dicom3D_viewer"))

        self.load_button.setText(_translate("Dialog", "Load"))
        self.gamma_label.setText(_translate("Dialog", "Gamma"))
        self.gain_label.setText(_translate("Dialog", "Gain"))
        self.filter_label.setText(_translate("Dialog", "Filter"))

        self.img_slider.valueChanged.connect(self.getSlice)
        self.gamma_slider.sliderReleased.connect(self.adjustGamma)
        self.gain_slider.sliderReleased.connect(self.adjustGain)
        self.filter_slider.sliderReleased.connect(self.adjustFilter)

        self.load_button.clicked.connect(self.readExam)


    def getSlice(self):
        self.slice_img = self.img_slider.value()
        if self.img_volume is None:
            pass
        else:
            self.slice.setText(str(self.slice_img + 1))
            self.refreshAxes()


    def adjustGamma(self):
        self.gamma = 0.1 * self.gamma_slider.value()
        if self.img_volume is None:
            pass
        else:
            self.img_volume_showed = exposure.adjust_gamma(self.img_volume_filter, self.gamma, self.gain)
            self.refreshAxes()


    def adjustGain(self):
        self.gain = 0.1 * self.gain_slider.value()
        if self.img_volume is None:
            pass
        else:
            self.img_volume_showed = exposure.adjust_gamma(self.img_volume_filter, self.gamma, self.gain)
            self.refreshAxes()


    def adjustFilter(self):
        self.filter_kernel = self.filter_slider.value()
        # print(self.filter_kernel)
        if self.img_volume is None:
            pass
        else:
            if filterWarning():
                self.img_volume_filter = median_filter(self.img_volume,(self.filter_kernel, self.filter_kernel, 3))
                self.img_volume_showed = exposure.adjust_gamma(self.img_volume_filter, self.gamma, self.gain)
                self.refreshAxes()
                finishWarning()


    def refreshAxes(self):
        self.img_ax.clear()
        self.img_ax.imshow(self.img_volume_showed[:, :, self.slice_img], cmap = 'gray',
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

            self.gain_slider.setEnabled(True)
            self.gamma_slider.setEnabled(True)
            self.filter_slider.setEnabled(True)
            self.img_slider.setEnabled(True)

            self.img_slider.setMaximum(len(dicom_list) - 1)
            self.slice.setText(str(1))


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
            time.sleep(0.001)
        self.img_volume = img_volume.copy()
        self.img_volume_filter = img_volume.copy()
        self.img_volume_mask =  0 * img_volume
        self.img_volume_showed = exposure.adjust_gamma(img_volume, gamma = 1)
        self.gamma_slider.setProperty("value", 10)
        self.progressBar.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
