from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

import sys
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
