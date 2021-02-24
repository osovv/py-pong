from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import  QColor, QPalette, QFont

from Label import Label
from settings import *

class Score(Label):
	def __init__(self, color, width, height, pos_x, pos_y, font, parent = None):
		super(Score, self).__init__(color, width, height, pos_x, pos_y, font, parent)
		
	def resizeEvent(self, e):
		if self.flag:
			super(Score, self).resizeEvent(e)

	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, score):
		self.txt = str(score)
		self._score = score