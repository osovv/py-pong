# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Player(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setStyleSheet('background-color: red;')
        self.resize(10, 60)
        self.move(100, int(self.height()/20 + 5))
        self.position = 0
    @property
    def position(self):
         return self.position
    @position.setter
    def position(self, position):
        self.position = position
