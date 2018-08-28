from PyQt4 import QtCore, QtGui
import winsound

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(418, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.labelFrequency = QtGui.QLabel(self.centralwidget)
        self.labelFrequency.setGeometry(QtCore.QRect(60, 70, 60, 20))
        self.labelFrequency.setText("Frequency")
        self.labelFrequency.setObjectName(_fromUtf8("labelFrequency"))

        self.frequencyDial = QtGui.QDial(self.centralwidget)
        self.frequencyDial.setGeometry(QtCore.QRect(60, 90, 50, 64))
        self.frequencyDial.setMaximum(15000)
        self.frequencyDial.setSingleStep(100)
        self.frequencyDial.setOrientation(QtCore.Qt.Horizontal)
        self.frequencyDial.setNotchesVisible(True)
        self.frequencyDial.setObjectName(_fromUtf8("frequencyDial"))

        self.labelVolume = QtGui.QLabel(self.centralwidget)
        self.labelVolume.setGeometry(QtCore.QRect(260, 70, 60, 20))
        self.labelVolume.setText("Volume")
        self.labelVolume.setObjectName(_fromUtf8("labelVolume"))

        self.Volume = QtGui.QDial(self.centralwidget)
        self.Volume.setGeometry(QtCore.QRect(260, 90, 50, 64))
        self.Volume.setMaximum(30000)
        self.Volume.setSingleStep(1000)
        self.Volume.setWrapping(False)
        self.Volume.setNotchesVisible(True)
        self.Volume.setObjectName(_fromUtf8("durationVolume"))

        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(50, 200, 100, 23))
        self.playButton.setAutoFillBackground(False)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.playButton.setText("Play")

        self.spinBoxFrequency = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxFrequency.setGeometry(QtCore.QRect(130, 110, 42, 22))
        self.spinBoxFrequency.setMaximum(10000)
        self.spinBoxFrequency.setSingleStep(100)
        self.spinBoxFrequency.setObjectName(_fromUtf8("spinBoxFrequency"))

        self.spinBoxVolume = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxVolume.setGeometry(QtCore.QRect(320, 110, 42, 22))
        self.spinBoxVolume.setMaximum(30000)
        self.spinBoxVolume.setSingleStep(1000)
        self.spinBoxVolume.setObjectName(_fromUtf8("spinBoxVolume"))

        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.exitButton.setText("Exit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.frequencyDial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxFrequency.setValue)
        QtCore.QObject.connect(self.Volume, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxVolume.setValue)
        QtCore.QObject.connect(self.spinBoxFrequency, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.frequencyDial.setValue)
        QtCore.QObject.connect(self.spinBoxVolume, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Volume.setValue)
        QtCore.QObject.connect(self.playButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.playSound)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

    def playSound(self):
        nFrequency = self.frequencyDial.value()
        winsound.Beep(nFrequency,1500)
        #set_volume(self.Volume.value())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


