from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer


class GameField(QWidget):
	def __init__(self, parent, color, width, height, thickness):
		super(GameField, self).__init__(parent)
		self.set_color(color)
		self.set_geometry(width, height)
		self.border_thickness = thickness
	
	def set_title(self, title):
		self.setWindowTitle("Py-Pong")


	def set_geometry(self, height, width):
		self.setGeometry(0, 0, height, width)
		self.height = height
		self.width = width

	def set_color(self, color):
		self.setStyleSheet('background-color: ' + color + ';')
	
	def draw_field(self, qp, color, bcolor):
		qp.fillRect(0, 0, self.width, self.height, QColor(color))
		qp.setPen(QPen(QColor(bcolor), self.width/100, Qt.DashLine))
		qp.drawLine(int(self.width/2), 0, int(self.width/2), self.height)
		qp.setPen(QPen(QColor(bcolor), self.width/100, Qt.SolidLine))
		qp.fillRect(0, 0, self.width, self.border_thickness, QColor(bcolor))
		qp.fillRect(0, self.height-self.border_thickness, self.width, self.border_thickness, QColor(bcolor))


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
	def border_thickness(self):
		return self._border_thickness
	@border_thickness.setter
	def border_thickness(self, thickness):
		self._border_thickness = thickness
	
