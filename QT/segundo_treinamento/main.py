#import Modules
import sys
import os

#import QT Core
from qt_core import *

#import Main Window
from gui.windows.main_window.ui_main_window import *

#Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Setup Main Window
        self.ui = UI_MainWindow
        self.ui.setup_ui(self)
        
        #Exibe a aplicação
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
