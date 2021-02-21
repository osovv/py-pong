import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPropertyAnimation, QPoint
from random import randint
from Player import Player
import math
import time
from main import rand_angle


class Ball(QWidget):
    def __init__(self):
        self.speed = 10
        self.pos_x = 0
        self.pos_y = 0
        self.speed_x = 10
        self.speed_y = 10
        self.size = 5
        self.setStyleSheet('background-color: lightblue;')

    def set_color(self, color):
        self.setStyleSheet('background-color: ' + color + ';')

    def set_size(self, size):
        self.size = size
        self.resize(size, size)
    
    def change_angle(self, angle):
        self.speed_x = int((self.speed - 1) * math.cos(angle)) + 1
        self.speed_y = int((self.speed - 1) * math.sin(angle)) + 1

    def spawn(self, wwidth, wheight, bthickness):
        self.move(int(wwidth / 2 - bthickness / 2), int(wheight / 2))
        self.pos_x = self.x() / wwidth
        self.pos_y = self.y() / wheight
        phi = rand_angle(60)
        self.change_angle(phi)
    
    def move_ball(self, wwidth, wheight, bthickness, p1, p2):
        new_posx = int(self.pos_x * wwidth - self.speed_x)
        new_posy = int(self.pos_y * wheight - self.speed_y)
        self.pos_x = self.ball.x() / wwidth
        self.pos_y = self.ball.y() / wheight
        if new_posx <= 0:
            print('goal to player1')
        elif new_posx >= self.WINDOW_WIDTH:
            print('goal to player2')
        elif new_posy < bthickness or new_posy + self.size >= wheight - bthickness:
            print('border hit')
            self.speed_y = -self.speed_y
        elif p1.y() <= new_posy <= p1.y() + p1.thickness and new_posx <= p1.x() + p1.thickness:
            print('player1 hit')
            self.speed_x = -self.speed_x * 1.5
        elif p2.y() <= new_posy <= p2.y() + p2.thickness and new_posx >= p2.x():
            print('player2 hit')
            self.speed_x = -self.speed_x * 1.5
        else:
            self.move(new_posx, new_posy)
