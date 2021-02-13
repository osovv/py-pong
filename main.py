# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPropertyAnimation, QPoint
from random import randint
from Player import Player
import math

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.STEP_SIZE = 5
        self.PLAYER_WIDTH = 10
        self.PLAYER_HEIGHT = 60
        self.BORDER_THICKNESS = 20
        self.WINDOW_HEIGHT = 1024
        self.WINDOW_WIDTH = 768
        self.TICK_SPEED = 10
        self.BORDER_COLOR = 'gray'
        self.PLAYER_POS = self.BORDER_THICKNESS
        self.BALL_POSX = int(self.WINDOW_WIDTH / 2)
        self.BALL_POSY = int(self.WINDOW_HEIGHT / 2)
        phi = randint(0, 25132) / 10000 - 1.256636
        self.BALL_SPEEDX = int(self.STEP_SIZE * 1.5 * math.cos(phi))
        self.BALL_SPEEDY = int(self.STEP_SIZE *  1.5 * math.sin(phi))
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
        self.setStyleSheet('background-color:black;')
        self.setWindowTitle("Drawing example")
        self.initPlayer()
        self.initBall()
        self.show()

    def initPlayer(self):
        self.player = QWidget(self)
        self.player.setStyleSheet('background-color: red;')
        self.player.resize(self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.player.move(self.BORDER_THICKNESS, int(self.WINDOW_HEIGHT/2))
        self.PLAYER_POS = self.player.y() / self.height()
        
    def moveball(self):
        new_posx = int(self.BALL_POSX * self.WINDOW_WIDTH) - self.BALL_SPEEDX
        new_posy = int(self.BALL_POSY * self.WINDOW_HEIGHT) - self.BALL_SPEEDY
        self.BALL_POSX = self.ball.x() / self.WINDOW_WIDTH
        self.BALL_POSY = self.ball.y() / self.WINDOW_HEIGHT
        if new_posy < self.BORDER_THICKNESS or new_posy + self.PLAYER_WIDTH >= self.WINDOW_HEIGHT - self.BORDER_THICKNESS:
            print('border hit')
            self.BALL_SPEEDY = -self.BALL_SPEEDY
        elif self.player.y() <= new_posy <=self.player.y() + self.PLAYER_HEIGHT and new_posx <= self.BORDER_THICKNESS + self.PLAYER_WIDTH:
            print('player hit')
            self.BALL_SPEEDX = -self.BALL_SPEEDX * 1.5
        else:
            self.ball.move(new_posx, new_posy)

    def initBall(self):
        self.ball = QWidget(self)
        self.ball.setStyleSheet('background-color: lightblue;')
        self.ball.resize(self.PLAYER_WIDTH, self.PLAYER_WIDTH)
        self.ball.move(int(self.WINDOW_WIDTH / 2 - self.BORDER_THICKNESS / 2), int(self.WINDOW_HEIGHT / 2))
        self.BALL_POSX = self.ball.x() / self.WINDOW_WIDTH
        self.BALL_POSY = self.ball.y() / self.WINDOW_HEIGHT
        timer = QTimer(self)
        timer.timeout.connect(self.moveball)
        timer.start(self.TICK_SPEED)

    def drawField(self, qp):
        qp.setPen(QPen(QColor(self.BORDER_COLOR), self.WINDOW_WIDTH/100, Qt.DashLine))
        qp.drawLine(int(self.WINDOW_WIDTH/2), 0, int(self.WINDOW_WIDTH/2), self.WINDOW_HEIGHT)
        qp.setPen(QPen(QColor(self.BORDER_COLOR), self.WINDOW_WIDTH/100, Qt.SolidLine))
        qp.fillRect(0, 0, self.WINDOW_WIDTH, self.BORDER_THICKNESS, QColor(self.BORDER_COLOR))
        qp.fillRect(0, self.WINDOW_HEIGHT-self.BORDER_THICKNESS, self.WINDOW_WIDTH, self.BORDER_THICKNESS, QColor(self.BORDER_COLOR))

    def redraw(self):
        self.SCALEX = self.WINDOW_WIDTH / self.width()
        self.SCALEY = self.WINDOW_HEIGHT / self.height()
        self.WINDOW_WIDTH = self.width()
        self.WINDOW_HEIGHT = self.height()
        self.BORDER_THICKNESS = int(self.height() / 40)
        self.STEP_SIZE = int(self.height() / 40)
        self.PLAYER_WIDTH = int(self.width() / 80)
        self.PLAYER_HEIGHT = int(self.height() / 8)
        phi = randint(0, 25132) / 10000 - 1.256636
        self.BALL_SPEEDX = int(self.BALL_SPEEDX * self.SCALEX)
        self.BALL_SPEEDY = int(self.BALL_SPEEDY * self.SCALEY)
        self.player.resize(self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.player.move(self.BORDER_THICKNESS, int(self.WINDOW_HEIGHT * self.PLAYER_POS))
        self.ball.resize(self.PLAYER_WIDTH, self.PLAYER_WIDTH)
        self.ball.move(int(self.BALL_POSX * self.WINDOW_WIDTH), int(self.BALL_POSY*self.WINDOW_HEIGHT))
        # timer = QTimer(self)
        # timer.timeout.connect(self.moveball)
        # timer.start(250)

    def resizeEvent(self, event):
        # print("Window was resized.")
        print(f'Current resolution: {self.width()} x {self.height()}')
        self.redraw()

    def paintEvent(self, event):
        qp = QPainter(self)
        self.drawField(qp)

    def drawPoints(self, qp):
        qp.setPen(QColor(255, 0, 0))
        size = self.size()
        if size.height() <= 1 or size.height() <= 1:
            return

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Q:
            print('Stop')
            self.close()
        if e.key() == Qt.Key_Up:
            if (self.player.y() >= self.BORDER_THICKNESS+self.STEP_SIZE):
                self.player.move(self.player.x(), self.player.y()-self.STEP_SIZE)
                self.PLAYER_POS = self.player.y() / self.WINDOW_HEIGHT
            else:
                self.player.move(self.player.x(), self.BORDER_THICKNESS)
                self.PLAYER_POS = self.player.y() / self.WINDOW_HEIGHT
        if e.key() == Qt.Key_Down:
            if (self.player.y()+self.PLAYER_HEIGHT+self.STEP_SIZE <= self.height()-self.BORDER_THICKNESS):
                self.player.move(self.player.x(), self.player.y()+self.STEP_SIZE)
                self.PLAYER_POS = self.player.y() / self.WINDOW_HEIGHT
            else:
                self.player.move(self.player.x(), self.height()-self.BORDER_THICKNESS-self.PLAYER_HEIGHT)
                self.PLAYER_POS = self.player.y() / self.WINDOW_HEIGHT
        

if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
