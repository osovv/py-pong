# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPropertyAnimation, QPoint
import random


class Player(QWidget):
    def __init__(self):
        QWidget.__init__.self()
        self.initUI()

    def initUI(self):
        self.setStyleSheet('background-color:red;')
        self.x = 0
        self.y = 0
        self.dimx = 50
        self.dimy = 25

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1024, 768)
        self.setStyleSheet('background-color:black;')
        self.setWindowTitle("Drawing example")
        self.initGameField()
        self.initPlayer()
        self.show()

    def initPlayer(self):
        self.player = QWidget(self)
        self.player.setStyleSheet('background-color: red;')
        self.player.resize(10, 60)
        self.player.move(100, int(self.height()/20 + 5))

    def drawPoints(self, qp):
        qp.setPen(QColor(255, 0, 0))
        size = self.size()
        if size.height() <= 1 or size.height() <= 1:
            return

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def initGameField(self):
        fieldTop = QWidget(self)
        fieldBot = QWidget(self)
#        fieldMid = QWidget(self)
        fieldTop.setStyleSheet('background-color:gray;')
        fieldBot.setStyleSheet('background-color:gray;')
#        fieldMid.setStyleSheet('background-color:gray;')
        fieldTop.resize(self.width(), int(self.height()/40))
        fieldTop.move(0, 0)
        fieldBot.resize(self.width(), int(self.height()/20))
        fieldBot.move(0, int(self.height()*19/20))



#    def drawAnimation(self):
#        self.child = QWidget(self)
#        self.child.setStyleSheet('background-color:red;border-radius:15px;')
#        self.child.resize(50, 25)
#        self.anim = QPropertyAnimation(self.child, b'pos')
#        self.anim.setStartValue(QPoint(100, 100))
#        self.anim.setEndValue(QPoint(100, 400))
#        self.anim.setDuration(1000)
#        self.anim.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            print('Stop')
            self.close()
        if e.key() == Qt.Key_Down:
            if (self.player.y() < self.height()*19/20-5):
                self.player.move(self.player.x(), self.player.y()+10)
        if e.key() == Qt.Key_Up:
            if (self.player.y() > self.height()*1/20+5):
                self.player.move(self.player.x(), self.player.y()-10)


if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
