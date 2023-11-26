import sys

import random

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coord = [i for i in range(500)]
        self.do_paint = False
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        qp.setPen(QColor(r, g, b))
        qp.setBrush((QColor(r, g, b)))
        x, y = random.choice(self.coord), random.choice(self.coord)
        size = random.randint(5, 300)
        qp.drawEllipse(x, y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())