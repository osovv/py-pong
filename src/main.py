# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPropertyAnimation, QPoint
from random import randint
from Player import Player
from GameField import GameField
from Ball import Ball
import math
import time

def rand_angle(angle):
    rad = int((angle * math.pi / 180) * 1000)
    return randint(-rad, rad) / 1000


class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.STEP_SIZE = 5
        self.PLAYER_WIDTH = 10
        self.PLAYER_HEIGHT = 60
        self.BORDER_THICKNESS = 20
        self.WINDOW_HEIGHT = 1024
        self.WINDOW_WIDTH = 768
        self.TICK_SPEED = 10
        self.BALL_SPEED = 10
        self.BACKGROUND_COLOR = 'black'
        self.BORDER_COLOR = 'gray'
        self.SLEEP_TIME = 1
        self.isPlayable = True
        self.initUI()

    def initUI(self):
        self.init_field()
        self.init_players()
        self.init_ball()
        self.init_scores()
        self.show()

    def init_scores(self):
        self.score1 = QLabel(self)
        self.score2 = QLabel(self)
        self.win_text = QLabel(self)
        self.score1.setStyleSheet('color: red; font-size: 18pt;')
        self.score2.setStyleSheet('color: blue; font-size: 18pt;')
        self.score1.setText("11")
        self.score2.setText("0")
        self.score1.resize(self.field.border_thickness * 3, self.field.border_thickness * 3)
        self.score2.resize(self.field.border_thickness * 3, self.field.border_thickness * 3)
        self.win_text.resize(self.field.border_thickness * 8, self.field.border_thickness * 6)
        self.score1.move(int(self.field.border_thickness * 2), int(self.field.border_thickness * 2))
        self.score2.move(int(self.field.width - self.field.border_thickness * 3), int(self.field.border_thickness * 2))
        self.win_text.move(int(self.field.width / 2 - self.field.border_thickness * 3), int(self.field.height / 2 - self.field.border_thickness * 2))

    def reset_scores(self):
        self.timer.stop()
        self.win_text.hide()
        self.ball.spawn(self.field)
        self.score1.setText("0")
        self.score2.setText("0")
        self.isPlayable = True
        self.timer.start(self.TICK_SPEED)

    def init_field(self):
        self.field = GameField(self, 'black', self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.BORDER_THICKNESS)
        self.field.show()

    def init_players(self):
        self.player1 = Player(self, "red", self.STEP_SIZE, self.PLAYER_WIDTH, self.PLAYER_HEIGHT, self.field.border_thickness, int(self.field.height / 2), self.field)
        self.player2 = Player(self, "blue", self.STEP_SIZE, self.PLAYER_WIDTH, self.PLAYER_HEIGHT, self.field.width - self.field.border_thickness - self.PLAYER_WIDTH, int(self.field.height / 2), self.field)
        
    def move_ball(self):
        status = 0
        status = self.ball.move_ball(self.field, self.player1, self.player2, self.score1, self.score2)
        if status == 1:
            self.score2.setText(str(int(self.score2.text()) + 1))
            time.sleep(self.SLEEP_TIME)
            self.ball.spawn(self.field)
        if status == 2:
            self.score1.setText(str(int(self.score1.text()) + 1))
            time.sleep(self.SLEEP_TIME)
            self.ball.spawn(self.field)
        if int(self.score1.text()) == 11:
            self.timer.stop()
            self.isPlayable = False
            self.win_text.setStyleSheet('color: red; font-size: 25pt;')
            self.win_text.setText('Player 1 \nWon')
            self.win_text.show()
        if int(self.score2.text()) == 11:
            self.timer.stop()
            self.isPlayable = False
            self.win_text.setStyleSheet('color: blue; font-size: 25pt;')
            self.win_text.setText('Player 2 \nWon')
            self.win_text.show()

    def init_ball(self):
        self.ball = Ball(self, "lightblue", self.PLAYER_WIDTH, self.BALL_SPEED, self.field, rand_angle(60))   
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_ball)
        self.timer.start(self.TICK_SPEED)

    def redraw(self):
        self.SCALEX = self.field.width / self.width()
        self.SCALEY = self.field.height / self.height()
        self.ball.speed = int(self.ball.speed * (self.SCALEX + self.SCALEY) / 2)
        self.field.width = self.width()
        self.field.height = self.height()
        self.field.border_thickness = int(self.field.height / 40)
        self.player1.step_size = int(self.height() / 40)
        self.player2.step_size = int(self.height() / 40)
        self.ball.speed = int(self.ball.speed * (self.SCALEX + self.SCALEY) / 2)
        self.player1.width = int( self.field.width / 80)
        self.player1.height = int(self.field.height / 8)
        self.player2.width = int( self.field.width / 80)
        self.player2.height = int(self.field.height / 8)
        phi = rand_angle(60)

        self.ball.speed_x = int(self.ball.speed_x * self.SCALEX)
        self.ball.speed_y = int(self.ball.speed_y * self.SCALEY)
        
        self.player1.pos_x = self.field.border_thickness
        self.player1.pos_y = int(self.player1.rel_y * self.field.height)
        self.player2.pos_x = int(self.field.width - self.field.border_thickness - self.player2.width)
        self.player2.pos_y = int(self.player2.rel_y * self.field.height)
        self.player1.resize(self.player1.width, self.player1.height)
        self.player1.move(self.field.border_thickness, int(self.field.height * self.player1.rel_y))
        self.player2.resize(self.player2.width, self.player2.height)
        self.player2.move(self.field.width - self.field.border_thickness - self.player2.width, int(self.field.height * self.player2.rel_y))
        
        self.ball.set_size(int((self.player1.width + self.player2.width) / 2))
        self.ball.move(int(self.ball.rel_x * self.field.width), int(self.ball.rel_y*self.field.height))
        self.ball.pos_x = int(self.ball.rel_x * self.field.width)
        self.ball.pos_y = int(self.ball.rel_y*self.field.height)

        self.score1.move(int(self.field.border_thickness * 2), int(self.field.border_thickness * 2))
        self.score2.move(int(self.field.width - self.field.border_thickness * 3), int(self.field.border_thickness * 2))
        self.win_text.move(int(self.field.width / 2 - self.field.border_thickness * 3), int(self.field.height / 2 - self.field.border_thickness * 3))
   
    def resizeEvent(self, event):
        self.redraw()

    def paintEvent(self, event):
        qp = QPainter(self)
        self.field.draw_field(qp, self.BACKGROUND_COLOR, self.BORDER_COLOR)
        self.player1.draw(qp)
        self.player2.draw(qp)
        self.ball.draw(qp)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_T:
                self.reset_scores()
        if e.key() == Qt.Key_Q:
            print('Stop')
            self.close()
        if not self.isPlayable:
            return
        elif e.key() == Qt.Key_Up:
            self.player2.move_up(self.field)
        elif e.key() == Qt.Key_Down:
            self.player2.move_down(self.field)
        elif e.key() == Qt.Key_W:
            self.player1.move_up(self.field)
        elif e.key() == Qt.Key_S:
            self.player1.move_down(self.field)
        elif e.key() == Qt.Key_R:
                self.ball.spawn(self.field)
        

if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
