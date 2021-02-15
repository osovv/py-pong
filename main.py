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

def rand_angle(angle):
    rad = int((angle * math.pi / 180) * 1000)
    return randint(-rad, rad) / 1000


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
        self.BALL_SPEED = 5
        self.BORDER_COLOR = 'gray'
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
        self.setStyleSheet('background-color:black;')
        self.setWindowTitle("Drawing example")
        self.init_players()
        self.init_ball()
        self.show()

    def init_players(self):
        self.player1 = QWidget(self)
        self.player1.setStyleSheet('background-color: red;')
        self.player1.resize(self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.player1.move(self.BORDER_THICKNESS, int(self.WINDOW_HEIGHT/2))
        self.player2 = QWidget(self)
        self.player2.setStyleSheet('background-color: blue;')
        self.player2.resize(self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.player2.move(self.WINDOW_WIDTH - self.BORDER_THICKNESS - self.PLAYER_WIDTH, int(self.WINDOW_HEIGHT/2))
        self.PLAYER_POS = self.player1.y() / self.height()
        
    def move_ball(self):
        new_posx = int(self.BALL_POSX * self.WINDOW_WIDTH - self.BALL_SPEEDX)
        new_posy = int(self.BALL_POSY * self.WINDOW_HEIGHT- self.BALL_SPEEDY)
        self.BALL_POSX = self.ball.x() / self.WINDOW_WIDTH
        self.BALL_POSY = self.ball.y() / self.WINDOW_HEIGHT
        if new_posy < self.BORDER_THICKNESS or new_posy + self.PLAYER_WIDTH >= self.WINDOW_HEIGHT - self.BORDER_THICKNESS:
            print('border hit')
            self.BALL_SPEEDY = -self.BALL_SPEEDY
        elif self.player1.y() <= new_posy <=self.player1.y() + self.PLAYER_HEIGHT and new_posx <= self.BORDER_THICKNESS + self.PLAYER_WIDTH:
            print('player hit')
            self.BALL_SPEEDX = -self.BALL_SPEEDX * 1.5
        else:
            self.ball.move(new_posx, new_posy)

    def init_ball(self):
        self.ball = QWidget(self)
        self.ball.setStyleSheet('background-color: lightblue;')
        self.ball.resize(self.PLAYER_WIDTH, self.PLAYER_WIDTH)
        self.ball.move(int(self.WINDOW_WIDTH / 2 - self.BORDER_THICKNESS / 2), int(self.WINDOW_HEIGHT / 2))
        self.BALL_POSX = self.ball.x() / self.WINDOW_WIDTH
        self.BALL_POSY = self.ball.y() / self.WINDOW_HEIGHT
        phi = rand_angle(60)
        self.BALL_SPEEDX = int((self.BALL_SPEED-1) * math.cos(phi)) + 1
        self.BALL_SPEEDY = int((self.BALL_SPEED-1) * math.sin(phi)) + 1
        timer = QTimer(self)
        timer.timeout.connect(self.move_ball)
        timer.start(self.TICK_SPEED)

    def respawn_ball(self):
        self.ball.move(int(self.WINDOW_WIDTH / 2 - self.BORDER_THICKNESS / 2), int(self.WINDOW_HEIGHT / 2))
        self.BALL_POSX = self.ball.x() / self.WINDOW_WIDTH
        self.BALL_POSY = self.ball.y() / self.WINDOW_HEIGHT
        phi = rand_angle(60)
        print('old speed:', self.BALL_SPEEDX)
        self.BALL_SPEEDX = int((self.BALL_SPEED-1) * math.cos(phi)) + 1
        self.BALL_SPEEDY = int((self.BALL_SPEED-1) * math.sin(phi)) + 1
        print('new speed:', self.BALL_SPEEDX)

    def player_move_up(self, player):
        if (player.y() >= self.BORDER_THICKNESS+self.STEP_SIZE):
                player.move(player.x(), player.y()-self.STEP_SIZE)
                self.PLAYER_POS = player.y() / self.WINDOW_HEIGHT
        else:
                player.move(player.x(), self.BORDER_THICKNESS)
                self.PLAYER_POS =player.y() / self.WINDOW_HEIGHT

    def player_move_down(self, player):
        if (player.y()+self.PLAYER_HEIGHT+self.STEP_SIZE <= self.height()-self.BORDER_THICKNESS):
                player.move(player.x(), player.y()+self.STEP_SIZE)
                self.PLAYER_POS = player.y() / self.WINDOW_HEIGHT
        else:
            player.move(player.x(), self.height()-self.BORDER_THICKNESS-self.PLAYER_HEIGHT)
            self.PLAYER_POS = player.y() / self.WINDOW_HEIGHT

    def draw_field(self, qp):
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
        self.BORDER_THICKNESS = int(self.WINDOW_HEIGHT / 40)
        self.STEP_SIZE = int(self.height() / 40)
        self.BALL_SPEED = int(self. BALL_SPEED * (self.SCALEX + self.SCALEY) / 2)
        self.PLAYER_WIDTH = int( self.WINDOW_WIDTH / 80)
        self.PLAYER_HEIGHT = int(self.WINDOW_HEIGHT / 8)
        phi = rand_angle(60)
        # self.BALL_SPEEDX = int(self.BALL_SPEEDX * self.SCALEX)
        # self.BALL_SPEEDY = int(self.BALL_SPEEDY * self.SCALEY)
        self.player1.resize(self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.player1.move(self.BORDER_THICKNESS, int(self.WINDOW_HEIGHT * self.PLAYER_POS))
        self.ball.resize(self.PLAYER_WIDTH, self.PLAYER_WIDTH)
        self.ball.move(int(self.BALL_POSX * self.WINDOW_WIDTH), int(self.BALL_POSY*self.WINDOW_HEIGHT))

    def resizeEvent(self, event):
        self.redraw()

    def paintEvent(self, event):
        qp = QPainter(self)
        self.draw_field(qp)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Q:
            print('Stop')
            self.close()
        elif e.key() == Qt.Key_Up:
            self.player_move_up(self.player1)
        elif e.key() == Qt.Key_Down:
            self.player_move_down(self.player1)
        elif e.key() == Qt.Key_W:
            self.player_move_up(self.player2)
        elif e.key() == Qt.Key_Down:
            self.player_move_down(self.player2)
        elif e.key() == Qt.Key_R:
                self.respawn_ball()

        

if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
