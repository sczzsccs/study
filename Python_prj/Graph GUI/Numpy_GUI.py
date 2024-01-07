import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass
        
    def initUI(self):
        cb = QComboBox()
        cb.addItem('0, 10, 0.5')
        cb.addItem('0, 5, 0.25')
        
        Vbox = QVBoxLayout()
        Vbox.addWidget(cb)

        cb.activated[str].connect(self.onComboBoxChanged)
        self.onComboBoxChanged(cb.currentText())

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        self.setLayout(Vbox)
        self.setWindowTitle('Grahp-UI')
        self.setGeometry(200, 200, 800, 600)
        pass

    def onComboBoxChanged(self, text):
        x = np.arange(int(text[0]), int(text[text.index(",",1)+2:text.index(",",2)]), float(text[text.index(",",2)+2:]))
        sin_x = np.sin(x)
        cos_x = np.cos(x)
    
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(x, sin_x, label="sin(x)")
        ax.plot(x, cos_x, label="cos(x)", linestyle="--")
        
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("sin & cos")
        ax.legend()
        ax.grid*True
        
        ax.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()