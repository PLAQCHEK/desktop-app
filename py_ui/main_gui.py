from raw_ui.raw_main_gui import *

from PyQt5.QtWidgets import QMainWindow

class MainWindow(Ui_MainWindow, QMainWindow):

	def __init__(self, parent=None):
		# Setup Parent
		super().__init__(parent)

		# Init UI
		self.setupUi(self)