import ctypes, sys

from multiprocessing import freeze_support 

from constants import APPID

from PyQt5.QtWidgets import QApplication

from py_ui.main_gui import MainWindow

if __name__ == "__main__":
    # Freeze Support
    freeze_support()
    
    # Update App ID if Windows
    if sys.platform.startswith("win"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APPID)

    # Prep App Launch
    app = QApplication(sys.argv)

    win = MainWindow()

    # Show
    win.show()

    # End
    sys.exit(app.exec())
