import sys, time
from PyQt5 import QtCore, QtWidgets, QtGui


class Worker(QtCore.QThread):
    def __init__(self):
        self.timeout = None
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            print(self.timeout)
            time.sleep(0.1)
            pass
        pass

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False


class MyWindow(object):
    def __init__(self, Dialog):
        super().__init__()

        Dialog.resize(300, 300)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.worker = Worker()
        self.worker.start()

        btn1 = QtWidgets.QPushButton(Dialog)
        btn1.setGeometry(QtCore.QRect(50, 50, 100, 50))
        btn1.setWhatsThis("resume")
        btn1.clicked.connect(self.resume)

        btn2 = QtWidgets.QPushButton(Dialog)
        btn2.setGeometry(QtCore.QRect(50, 150, 100, 50))
        btn2.setWhatsThis("pause")
        btn2.clicked.connect(self.pause)

        btn3 = QtWidgets.QPushButton(Dialog)
        btn3.setGeometry(QtCore.QRect(50, 200, 100, 50))
        btn3.setWhatsThis("pause")
        btn3.clicked.connect(self.Btn_edit)

        self.edit = QtWidgets.QLineEdit(Dialog)
        self.edit.setGeometry(QtCore.QRect(200, 50, 70, 25))

    def Btn_edit(self):
        self.worker.timeout = int(self.edit.text())
        edit_num = int(self.edit.text())
        for i in range(edit_num):
            print('i:', i)
            time.sleep(0.1)

    def resume(self):
        self.worker.resume()
        self.worker.start()

    def pause(self):
        self.worker.pause()


app = QtWidgets.QApplication(sys.argv)
mywindow = QtWidgets.QDialog()
Ui = MyWindow(mywindow)
mywindow.show()
app.exec_()