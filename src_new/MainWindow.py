from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
import time

from GameField import GameField
from Player import Player
from Ball import Ball
from Score import Score
from Label import Label
from settings import *

class MainWindow(QMainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.init_UI()
		self.init_field()
		self.init_players()
		self.init_balls()
		self.init_scores()
		self.init_win_label()
		self.show()

	def init_UI(self):
		self.setGeometry(0, 0, WIDTH, HEIGHT)
		self.setWindowTitle('PyQT-Pong')
		self.keys = dict()
		self.isPlayable = True

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
		self.b1.speed = BALL_SPEED
		self.b1.spawn(self.field)
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.move_balls)
		self.timer.start(TICK_SPEED)
	
	def init_scores(self):
		self.s1 = Score(S1_COLOR, S1_WIDTH, S1_HEIGHT, S1_POSX, S1_POSY, self, S1_FONT)
		self.s1.font_size = S1_FONT_SIZE * 100
		self.s1.score = 0
		self.s2 = Score(S2_COLOR, S2_WIDTH, S2_HEIGHT, S2_POSX, S2_POSY, self, S2_FONT)
		self.s2.font_size = S2_FONT_SIZE * 100
		self.s2.score = 0
	
	def init_win_label(self):
		pass
		self.win_label = Label(WIN_LABEL_COLOR, WIN_LABEL_WIDTH, WIN_LABEL_HEIGHT, WIN_LABEL_POSX, WIN_LABEL_POSY, self)
		self.win_label.font_size = WIN_LABEL_FONT_SIZE * 100
		self.win_label.setAlignment(Qt.AlignCenter)
		self.win_label.hide()

	def display_message(self, who, p1_name, p2_name):
		if who == 1:
			self.win_label.txt = f'{p1_name}\n Won!\n Press T to restart\nPress Q To Exit'
		if who == 2:
			self.win_label.txt = f'{p2_name}\n Won!\n Press T to restart\nPress Q To Exit'
		self.win_label.show()

	def check_goal(self, status):
		if status == 1:
			self.s2.score += 1
			time.sleep(SLEEP_TIME)
			self.b1.spawn(self.field)
			if self.s2.score == 11:
				self.timer.stop()
				self.isPlayable = False
				self.display_message(2, P1_NAME, P2_NAME)
		elif status == 2:
			self.s1.score += 1
			time.sleep(SLEEP_TIME)
			self.b1.spawn(self.field)
			if self.s1.score == 11:
				self.timer.stop()
				self.isPlayable = False
				self.display_message(1, P1_NAME, P2_NAME)
		else:
			pass

	def move_balls(self):
		status = self.b1.move_ball(self.field, self.p1, self.p2)
		self.check_goal(status)

	def restart(self):
		self.timer.stop()
		self.win_label.hide()
		self.b1.spawn(self.field)
		self.s1.score = 0
		self.s2.score = 0
		self.isPlayable = True
		self.timer.start(TICK_SPEED)


	def keyPressEvent(self, e):
		super(MainWindow, self).keyPressEvent(e)
		if not self.keys.get(e.key(), False):
			self.keys[e.key()] = True
		for key, value in self.keys.items():
			if value:
				if key == Qt.Key_Q:
					self.close()
				elif key == Qt.Key_T:
					self.restart()
				if self.isPlayable:
					if key == Qt.Key_Up:
						self.p2.move_up(self.field)
					elif key == Qt.Key_Down:
						self.p2.move_down(self.field)
					elif key == Qt.Key_W:
						self.p1.move_up(self.field)
					elif key == Qt.Key_S:
						self.p1.move_down(self.field)
					elif key == Qt.Key_R:
						self.b1.spawn(self.field)
				

	def keyReleaseEvent(self, e):
		super(MainWindow, self).keyPressEvent(e)
		if self.keys.get(e.key(), True):
			self.keys[e.key()] = False

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
		self.s1.scale_x = self.field.scale_x
		self.s1.scale_y = self.field.scale_y
		self.s2.scale_y = self.field.scale_y
		self.s2.scale_x = self.field.scale_x
		self.win_label.scale_x = self.field.scale_x
		self.win_label.scale_y = self.field.scale_y
		self.p1.resizeEvent(e)
		self.p2.resizeEvent(e)
		self.b1.resizeEvent(e)
		self.s1.resizeEvent(e)
		self.s2.resizeEvent(e)