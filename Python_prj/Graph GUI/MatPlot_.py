import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt

class My_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        Vbox = QVBoxLayout()

        lbl = QLabel('Graph Option', self)
        Vbox.addWidget(lbl)

        Min_lb = QLabel('Min ', self)
        Hbox1 = QHBoxLayout()
        Hbox1.addWidget(Min_lb)

        Min_LText = QLineEdit(self)
        Hbox1.addWidget(Min_LText)
        Min_LText.textChanged[str].connect(self.Min_LText_text)
        Hbox1.addStretch(1)
        Vbox.addLayout(Hbox1)

        Max_lb = QLabel('Max ', self)
        Hbox2 = QHBoxLayout()
        Hbox2.addWidget(Max_lb)

        Max_LText = QLineEdit(self)
        Hbox2.addWidget(Max_LText)
        Max_LText.textChanged[str].connect(self.Max_LText_text)
        Hbox2.addStretch(1)
        Vbox.addLayout(Hbox2)

        add_lb = QLabel('Add ', self)
        Hbox3 = QHBoxLayout()
        Hbox3.addWidget(add_lb)

        add_LText = QLineEdit(self)
        Hbox3.addWidget(add_LText)
        add_LText.textChanged[str].connect(self.add_LText_text)
        Hbox3.addStretch(1)
        Vbox.addLayout(Hbox3)
        
        Graph_btn=QPushButton('&Graph', self)
        Vbox.addWidget(Graph_btn)
        Graph_btn.clicked.connect(self.Graph_Button)

        self.setLayout(Vbox)
        self.setWindowTitle('Graph-UI')
        self.setGeometry(200, 200, 218, 70)
        self.show()
        pass

    def Min_LText_text(self, text):
        self.min=text
        pass

    def Max_LText_text(self, text):
        self.max=text
        pass

    def add_LText_text(self, text):
        self.add=text
        pass

    def Graph_Button(self):
        self.min=float(self.min)
        self.max=float(self.max)
        self.add=float(self.add)
        x= np.arange(self.min, self.max, self.add)
        print(x)
        plt.plot(x)
        plt.title(str(self.add)+'x + '+str(self.min), loc="center", pad=18)
        plt.grid(True)
        plt.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    My_Ui = My_GUI()
    sys.exit(app.exec_())