from PyQt4 import QtCore , QtGui
import sys

class windowApplication(object):

    def init(self,mainWindowApp):
        mainWindowApp.setObjectName("MainScreen")
        mainWindowApp.resize(800,600)
        mainWindowApp.setWindowTitle("Observe the difference")

        self.centralwidget = QtGui.QWidget(mainWindowApp)
        self.centralwidget.setObjectName("central widget")


        
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(700,500,75,23))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Exit")

        self.sliderDist = QtGui.QSlider(self.centralwidget)
        self.sliderDist.setGeometry(QtCore.QRect(100,500,200,19))
        self.sliderDist.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDist.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderDist.setTickInterval(10)
        self.sliderDist.setMaximum(100)
        self.sliderDist.setObjectName("sliderDist")

        self.labelDist = QtGui.QLabel(self.centralwidget)
        self.labelDist.setGeometry(QtCore.QRect(100,530,60,20))
        self.labelDist.setText("Distance")
        self.labelDist.setObjectName("labelDist")

        self.sliderWidth = QtGui.QSlider(self.centralwidget)
        self.sliderWidth.setGeometry(QtCore.QRect(400,500,200,19))
        self.sliderWidth.setOrientation(QtCore.Qt.Horizontal)
        self.sliderWidth.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderWidth.setTickInterval(10)
        self.sliderWidth.setMaximum(100)
        self.sliderWidth.setObjectName("sliderWidth")

        self.labelDist = QtGui.QLabel(self.centralwidget)
        self.labelDist.setGeometry(QtCore.QRect(400,530,60,20))
        self.labelDist.setText("Width")
        self.labelDist.setObjectName("labelWidth")

        self.sliderDistLabel = QtGui.QLabel(self.centralwidget)
        self.sliderDistLabel.setGeometry(QtCore.QRect(400,540,30,40))
        self.sliderDistLabel.setObjectName("sliderDistLabel")
        self.sliderDistLabel.setText("0")

        self.sliderWidthLabel = QtGui.QLabel(self.centralwidget)
        self.sliderWidthLabel.setGeometry(QtCore.QRect(100,540,30,40))
        self.sliderWidthLabel.setObjectName("sliderWidthLabel")
        self.sliderWidthLabel.setText("0")

        self.firstLine = QtGui.QFrame(self.centralwidget)
        self.firstLine.setGeometry(QtCore.QRect(100,200,600,100))
        self.firstLine.setFrameShape(QtGui.QFrame.HLine)
        self.firstLine.setFrameShadow(QtGui.QFrame.Plain)
        self.firstLine.setObjectName("firstLine")

        self.secondLine = QtGui.QFrame(self.centralwidget)
        self.secondLine.setGeometry(QtCore.QRect(100,200,600,100))
        self.secondLine.setFrameShape(QtGui.QFrame.HLine)
        self.secondLine.setFrameShadow(QtGui.QFrame.Plain)
        self.secondLine.setObjectName("secondLine")

        mainWindowApp.setCentralWidget(self.centralwidget)

        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL("clicked()"), mainWindowApp.close)
        QtCore.QObject.connect(self.sliderWidth,QtCore.SIGNAL("valueChanged(int)"),self.changeWidth)
        QtCore.QObject.connect(self.sliderDist,QtCore.SIGNAL("valueChanged(int)"),self.changeDist)

        QtCore.QMetaObject.connectSlotsByName(mainWindowApp)

    def changeWidth(self,value):
        self.firstLine.setLineWidth(value)
        self.secondLine.setLineWidth(value)

        dist = int(self.secondLine.y()-self.firstLine.y())
        self.sliderDistLabel.setNum(dist - value)
        self.sliderWidthLabel.setNum(value)

    def changeDist(self,value):
        nwidth = int(self.secondLine.lineWidth())
        self.firstLine.setGeometry(QtCore.QRect(100,200-value,600,100))
        self.secondLine.setGeometry(QtCore.QRect(100,200+value,600,100))

        if nwidth == 1:
            self.sliderWidthLabel.setNum(2*value)

        else:
            self.sliderWidthLabel.setNum(2*value - nwidth)

if __name__ == "__main__":
    qtApp = QtGui.QApplication(sys.argv)
    mainWindowApp = QtGui.QMainWindow()

    userInterface = windowApplication()
    userInterface.init(mainWindowApp)

    mainWindowApp.show()
    sys.exit(qtApp.exec_())
