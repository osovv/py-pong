# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen

class Player(QWidget):
    def __init__(self, parent, color, step_size, width, height, pos_x, pos_y, field):
        super(Player, self).__init__(parent)
        self.step_size = step_size
        self.set_size(width, height)
        self.set_color(color)
        self.move(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rel_y = pos_y / field.height
        self.show()
        
    def set_color(self, color):
        self.color = color
        self.setStyleSheet('background-color: ' + color + ';')
    
    def set_size(self, width, height):
        self.height = height
        self.thickness = width
        self.width = width
        self.resize(height, width)
    
    def draw(self, qp):
        qp.fillRect(self.pos_x, self.pos_y, self.width, self.height, QColor(self.color))

    def move_up(self, field):
        if self.y() >= field.border_thickness + self.step_size:
            self.move(self.x(), self.y() - self.step_size)
            self.pos_y -= self.step_size
            self.rel_y = self.y() / field.height
        else:
            self.move(self.x(), field.border_thickness)
            self.pos_y = field.border_thickness
            self.rel_y = self.y() / field.height

    def move_down(self, field):
        if self.y() + self.height + self.step_size <= field.height - field.border_thickness:
            self.move(self.x(), self.y() + self.step_size)
            self.pos_y += self.step_size
            self.rel_y = self.y() / field.height
        else:
            self.move(self.x(), field.height - field.border_thickness - self.height)
            self.pos_y = field.height - field.border_thickness - self.height
            self.rel_y = self.y() / field.height

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width
    @property
    def step_size(self):
        return self._step_size
    @step_size.setter
    def step_size(self, step_size):
        self._step_size = step_size
    @property
    def rel_y(self):
         return self._rel_y
    @rel_y.setter
    def rel_y(self, rel_y):
        self._rel_y = rel_y
    @property
    def pos_x(self):
        return self._pos_x
    @pos_x.setter
    def pos_x(self, pos_x):
        self._pos_x = pos_x
    @property
    def pos_y(self):
        return self._pos_y
    @pos_y.setter
    def pos_y(self, pos_y):
        self._pos_y = pos_y
