from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt

from GameField import GameField
from Player import Player
from Ball import Ball
from Score import Score
from settings import *

class MainWindow(QMainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.init_UI()
		self.init_field()
		self.init_players()
		self.init_balls()
		self.init_scores()
		self.show()

	def init_UI(self):
		self.setGeometry(0, 0, WIDTH, HEIGHT)
		self.setWindowTitle('PyQT-Pong')

	def init_field(self):
		self.field = GameField(FIELD_COLOR, self.width(), self.height(), 0, 0, self)
		self.field.bcolor = BORDER_COLOR
		self.field.bthick = BORDER_THICKNESS

	def init_players(self):
		self.p1 = Player(P1_COLOR, P1_WIDTH, P1_HEIGHT, P1_POSX, P1_POSY, self)
		self.p1.step_size = P1_STEP_SIZE
		self.p2 = Player(P2_COLOR, P2_WIDTH, P2_HEIGHT, P2_POSX, P2_POSY, self)
		self.p2.step_size = P2_STEP_SIZE

	def init_balls(self):
		self.b1 = Ball(BALL_COLOR, BALL_WIDTH, BALL_HEIGHT, BALL_POSX, BALL_POSY, self)

	def init_scores(self):
		self.s1 = Score(self)
		self.s2 = Score(self)

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Q:
			self.close()

	def resizeEvent(self ,e):
		self.field.scale_x = self.width() / self.field.w 
		self.field.scale_y = self.height() / self.field.h
		self.field.resize(self.width(), self.height())
		self.p1.scale_x = self.field.scale_x
		self.p1.scale_y = self.field.scale_y
		self.p2.scale_x = self.field.scale_x
		self.p2.scale_y = self.field.scale_y
		self.b1.scale_x = self.field.scale_x
		self.b1.scale_y = self.field.scale_y
		self.p1.resizeEvent(e)
		self.p2.resizeEvent(e)
		self.b1.resizeEvent(e)