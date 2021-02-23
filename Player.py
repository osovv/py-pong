# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Player(QWidget):
    def __init__(self, parent, color, step_size, width, height, pos_x, pos_y, field):
        super(Player, self).__init__(parent)
        self.step_size = step_size
        self.set_size(width, height)
        self.set_color(color)
        self.move(pos_x, pos_y)
        self.pos_y = pos_y / field.height
        
    def set_color(self, color):
        self.setStyleSheet('background-color: ' + color + ';')
    
    def set_size(self, height, width):
        self.height = height
        self.width = width
        self.resize(height, width)

    def move_up(self, field):
        if self.y() >= field.border_thickness + self.step_size:
            self.move(self.x(), self.y() - self.step_size)
            self.pos_y = self.y() / field.height
        else:
            self.move(self.x(), field.border_thickness)
            self.pos_y = self.y() / field.height

    def move_down(self, field):
        if self.y() + self.height + self.step_size <= field.height - field.border_thickness:
            self.move(self.x(), self.y() + self.step_size)
            self.pos_y = self.y() / field.height
        else:
            self.move(self.x(), field.height - field.border_thickness - self.height)
            self.pos_y = self.y() / field.height

    @property
    def step_size(self):
        return self._step_size
    @step_size.setter
    def step_size(self, step_size):
        self._step_size = step_size
    @property
    def thickness(self):
        return self._thickness
    @thickness.setter
    def thickness(self, thicnkess):
        self._thickness = thicnkess
    @property
    def position(self):
         return self._position
    @position.setter
    def position(self, position):
        self._position = position
