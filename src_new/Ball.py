from PyQt5.QtWidgets import QWidget
from random import randint
import math

from Object import Object
from settings import *



class Ball(Object):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(Ball, self).__init__(color, width, height, pos_x, pos_y, parent)
		self.spawn_pos_x = pos_x / parent.width()
		self.spawn_pos_y = pos_y / parent.height()
		self.new_spawn_pos_x = pos_x
		self.new_spawn_pos_y = pos_y
		self.direction = True
		
	def resizeEvent(self, e):
		self.newspeed *= (self.scale_x + self.scale_y) / 2
		if abs(self.newspeed - self.speed) >=1:
			self.speed = self.newspeed
		self.newspeed_x *= self.scale_x
		if abs(self.newspeed_x - self.speed_x) >=1:
			self.speed_x = self.newspeed_x
		self.newspeed_y *= self.scale_y
		if abs(self.newspeed_y - self.speed_y) >=1:
			self.speed_y = self.newspeed_y
		if self.flag:
			super(Ball, self).resizeEvent(e)

	def move_ball(self, field, p1, p2):
		new_posx = int(self.pos_x - self.speed_x)
		new_posy = int(self.pos_y - self.speed_y)
		if new_posx <= 0:
			return 1
		elif new_posx >= field.w:
			return 2
		elif new_posy < field.bthick or new_posy + self.h >= field.h - field.bthick:
			self.speed_y = -self.speed_y
		elif p1.y()  - self.h < new_posy < p1.y() + p1.h and new_posx <= p1.x() + p1.w:
			self.speed_x =  -self.speed_x * BALL_ACC
			if self.speed_x > self.w:
				self.speed_x = self.speed_x * self.w / abs(self.speed_x)
		elif p2.y() - self.h < new_posy < p2.y() + p2.h and new_posx + self.w >= p2.x():
			self.speed_x = -self.speed_x * BALL_ACC
			if self.speed_x > self.w:
				self.speed_x = self.speed_x * self.w / abs(self.speed_x)
		else:
			self.move(new_posx, new_posy)
			self.pos_x = new_posx
			self.pos_y = new_posy


	def spawn(self, field):
		self.pos_x = int(self.spawn_pos_x * field.width())
		self.pos_y = int(self.spawn_pos_x * field.height())
		self.direction = not self.direction
		angle = self.rand_angle(60)
		self.change_angle(angle)
		if self.direction:
			self.speed_x = -self.speed_x

	def change_angle(self, angle):
		self.speed_x = int((self.speed - 1) * math.cos(angle)) + 1
		self.speed_y = int((self.speed - 1) * math.sin(angle)) + 1

	@staticmethod
	def rand_angle(angle):
		rad = int((angle * math.pi / 180) * 1000)
		return randint(-rad, rad) / 1000

	@property
	def speed(self):
		return self._speed
	@speed.setter
	def speed(self, speed):
		self._speed = speed
		self.newspeed = speed

	@property
	def speed_x(self):
		return self._speed_x
	@speed_x.setter
	def speed_x(self, speed_x):
		self._speed_x = speed_x
		self.newspeed_x = speed_x

	@property
	def speed_y(self):
		return self._speed_y
	@speed_y.setter
	def speed_y(self, speed_y):
		self._speed_y = speed_y
		self.newspeed_y = speed_y
	