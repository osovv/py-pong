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

def rand_angle(angle):
    rad = int((angle * math.pi / 180) * 1000)
    return randint(-rad, rad) / 1000


class Ball(QWidget):
    def __init__(self, parent, color, size, speed, field, angle):
        super(Ball, self).__init__(parent)
        self.speed = speed
        self.set_color(color)
        self.set_size(size)
        self.set_speedxy(angle)
        self.move(int(field.width / 2 - field.border_thickness / 2), int (field.height / 2 ))
        self.pos_x = int(field.width / 2 - field.border_thickness / 2)
        self.pos_y = int (field.height / 2 )
        self.rel_x = self.x() / field.width
        self.rel_y = self.y() / field.height
        self.direction = False
        self.show()
    
    def draw(self, qp):
        qp.fillRect(self.pos_x, self.pos_y, self.size, self.size, QColor(self.color))
        
    def set_speedxy(self, angle):
        self.speed_x = int((self.speed - 1)* math.cos(angle)) + 1
        self.speed_y = int((self.speed - 1) * math.sin(angle)) + 1

    def set_speed(self, speed):
        self.speed = speed

    def set_color(self, color):
        self.color = color
        self.setStyleSheet('background-color: ' + color + ';')

    def set_size(self, size):
        self.size = size
        self.resize(size, size)
    
    def change_angle(self, angle):
        self.speed_x = int((self.speed - 1) * math.cos(angle)) + 1
        self.speed_y = int((self.speed - 1) * math.sin(angle)) + 1

    def spawn(self, field):
        wwidth = field.width
        wheight = field.height
        bthickness = field.border_thickness
        self.move(int(wwidth / 2 - bthickness / 2), int(wheight / 2))
        self.pos_x = int(wwidth / 2 - bthickness / 2)
        self.pos_y = int(wheight / 2)
        self.rel_x = self.x() / wwidth
        self.rel_y = self.y() / wheight
        phi = rand_angle(60)
        self.change_angle(phi)
        if self.direction:
            self.speed_x = -self.speed_x
        self.direction = not self.direction
    
    def move_ball(self, field, p1, p2, s1, s2):
        wwidth = field.width
        wheight = field.height
        bthickness = field.border_thickness
        new_posx = int(self.rel_x * wwidth - self.speed_x)
        new_posy = int(self.rel_y * wheight - self.speed_y)
        self.rel_x = self.x() / wwidth
        self.rel_y = self.y() / wheight
        if new_posx <= 0:
            return 1
        elif new_posx >= wwidth:
            return 2
        elif new_posy < bthickness or new_posy + self.size >= wheight - bthickness:
            self.speed_y = -self.speed_y
        elif p1.y() <= new_posy <= p1.y() + p1.height and new_posx <= p1.x() + p1.width:
            self.speed_x = -self.speed_x * 1.15
        elif p2.y() <= new_posy <= p2.y() + p2.height and new_posx >= p2.x():
            self.speed_x = -self.speed_x * 1.15
        else:
            self.move(new_posx, new_posy)
            self.pos_x = new_posx
            self.pos_y = new_posy

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        self._speed = speed
