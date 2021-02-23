from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt

from GameField import GameField
from Player import Player
from Ball import Ball
from Score import Score

class MainWindow(QMainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.init_UI()
		self.init_field()
		self.init_players()
		self.init_balls()
		self.init_scores()
		print(self.width(), self.height())
		self.show()
		print(self.width(), self.height())

	def init_UI(self):
		self.setGeometry(0, 0, 1024, 768)
		self.setWindowTitle('PyQT-Pong')

	def init_field(self):
		self.field = GameField('black', 1024, 768, 0, 0, self)
		pass

	def init_players(self):
		self.p1 = Player('blue', 100, 100, 0, 0, self)
		self.p2 = Player('red', 100, 100, 0, 100, self)
		pass

	def init_balls(self):
		self.b1 = Ball('lightblue', 50, 50, 0, 200, self)
		pass

	def init_scores(self):
		self.s1 = Score(self)
		self.s2 = Score(self)
		pass

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Q:
			self.close()

	def resizeEvent(self ,e):
		pass
		print(self.width(), self.height())