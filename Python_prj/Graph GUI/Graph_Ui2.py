import sys
import numpy as np
from PyQt5.QtWidgets import *

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.sc = MplCanvas()
        self.draw_graph()
        toolbar = NavigationToolbar(self.sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        self.setLayout(layout)
        self.show()

    def draw_graph(self):
        xs = np.linspace(0, 1, 101)
        ys = xs**2.0
        self.sc.axes.cla()
        self.sc.axes.plot(xs, ys, color = 'blue', lw = 1)
        self.sc.axes.set_xlabel("x")
        self.sc.axes.set_ylabel("y")
        self.sc.axes.grid()
        self.sc.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())